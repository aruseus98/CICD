pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '-u root'
        }
    }

    environment {
        SONAR_PROJECT_KEY_DEV = 'Projet-CICD-Dev'
    }
    
    stages {
        stage('Initialize') {
            steps {
                script{
                    // Déclaration variables
                    def currentBranch = env.BRANCH_NAME ?: 'dev'
                    echo "Current branch : ${currentBranch}"
                }
            }
        }

        stage('Build') {
            steps {
                echo "Building application on ${env.BRANCH_NAME} branch"
                sh 'python --version'
                sh 'pip --version'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running Python test on ${env.BRANCH_NAME} branch"
                sh 'pytest --maxfail=1 --disable-warnings'
            }
        }

        stage('Analyse SonarQube') {
            agent {
                docker {
                    image 'sonarsource/sonar-scanner-cli:latest'
                    args '-u root'
                }
            }
            steps {
                script {
                    withSonarQubeEnv('SonarQubeDev') {  // 'SonarQubeDev' est le serveur SonarQube
                        sh 'sonar-scanner -Dsonar.projectKey=${SONAR_PROJECT_KEY_DEV}'
                    }
                }
            }
        }

        stage('Deploy with Ansible') {
            agent {
                docker {
                    image 'willhallonline/ansible:latest'
                    args "-u root -v /var/jenkins_home/.ssh:/root/.ssh"
                }
            }
            steps{
                withCredentials([string(credentialsId: 'SUDO_PASS', variable: 'SUDO_PASS')]) {
                    sshagent(['projet-prod-id']) {
                        sh 'ls -la'
                        sh 'pwd'
                        ansiblePlaybook(
                            playbook: 'deploy-app-dev.yml',
                            inventory: 'hosts.ini',
                            extraVars: [
                                ansible_become_pass: "${SUDO_PASS}"
                            ]
                        )
                    }
                }
            }
        }

        stage('Succès') {
            steps {
                script {
                    echo "Succès !"
                }
            }
        }
    }
}
