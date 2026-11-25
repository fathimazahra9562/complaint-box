pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'GitHub source code downloaded successfully'
            }
        }

        stage('Python Version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip --version'
            }
        }

        stage('Security Scan - Bandit') {
            steps {
                sh 'python3 -m pip install bandit'
                sh 'bandit -r project4 -f txt'
            }
        }

        stage('Security Scan - Safety') {
            steps {
                sh 'python3 -m pip install safety'
                sh 'safety scan'
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
