import unittest
import os
import sys
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

class TestAppIntegration(unittest.TestCase):
    def setUp(self):
        # Configurer l'application Flask pour les tests
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home_page_loads(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Enter your details', response.data)

    def test_form_submission(self):
        response = self.app.post('/', data=dict(
            first_name="John",
            last_name="Doe"
        ), follow_redirects=True)
        
        # Vérifier le statut de la réponse
        self.assertEqual(response.status_code, 200)
        
        # Charger la réponse JSON
        response_data = json.loads(response.data)
        
        # Vérifier que le message et les données sont corrects
        self.assertEqual(response_data['message'], "Form Submitted")
        self.assertEqual(response_data['data']['first_name'], "John")
        self.assertEqual(response_data['data']['last_name'], "Doe")

if __name__ == '__main__':
    unittest.main()
