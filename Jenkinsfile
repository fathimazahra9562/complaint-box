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
                    .venv/bin/pip install bandit pip-audit
                '''
            }
        }

        stage('Install Project Dependencies') {
            steps {
                sh '.venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Python Version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Bandit Security Scan') {
            steps {
                sh '.venv/bin/bandit -r project4 -x project4/venv,.venv -f txt'
            }
        }

        stage('Dependency Security Scan') {
            steps {
                sh '.venv/bin/pip-audit -r requirements.txt'
            }
        }

        stage('Django Quality Checks') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'complaint-db-password',
                        usernameVariable: 'DB_USERNAME',
                        passwordVariable: 'DB_PASSWORD'
                    )
                ]) {
                    sh '''
                        .venv/bin/python project4/manage.py check
                        .venv/bin/python project4/manage.py makemigrations --check --dry-run
                        .venv/bin/python project4/manage.py test project4
                    '''
                }
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
