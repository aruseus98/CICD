import os
from flask import Flask, render_template, request, jsonify
from forms import NameForm
import json

app = Flask(__name__)

# Charger la clé secrète depuis la variable d'environnement
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback_default_key')

# Définir le chemin du fichier où stocker les réponses JSON
JSON_FILE_PATH = 'form_data.json'

@app.route('/', methods=['GET', 'POST'])
def index():
    # Utiliser WTForms directement
    form = NameForm(request.form)
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data

        # Créer un dictionnaire avec les données du formulaire
        form_data = {
            "first_name": first_name,
            "last_name": last_name
        }

        # Sauvegarder les données dans un fichier JSON
        save_to_json_file(form_data)

        # Retourner un message confirmant la soumission avec les données
        return jsonify(message="Form Submitted", data=form_data)

    return render_template('form.html', form=form)

def save_to_json_file(data):
    """Sauvegarder les données du formulaire dans un fichier JSON"""
    if os.path.exists(JSON_FILE_PATH):
        # Si le fichier existe, charger les données existantes
        with open(JSON_FILE_PATH, 'r') as file:
            existing_data = json.load(file)
    else:
        existing_data = []

    # Ajouter les nouvelles données
    existing_data.append(data)

    # Écrire dans le fichier JSON
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(existing_data, file, indent=4)

if __name__ == '__main__':
    app.run(debug=True)
