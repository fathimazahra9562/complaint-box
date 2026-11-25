pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'GitHub source code downloaded successfully'
            }
        }

        stage('Python Setup') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/pip install bandit safety
                '''
            }
        }

        stage('Python Version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Bandit Security Scan') {
            steps {
                sh '.venv/bin/bandit -r project4 -f txt'
            }
        }

        stage('Safety Security Scan') {
            steps {
                sh '.venv/bin/safety scan'
            }
        }
    }

    post {
        success {
            echo 'DevSecOps pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
