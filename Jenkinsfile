pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:/usr/bin:/bin"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Backend Image') {
            steps {
                sh 'docker build -t calculator-backend .'
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh 'docker build -t calculator-frontend ./frontend'
            }
        }

        stage('Stop Old Containers') {
            steps {
                sh 'docker rm -f backend || true'
                sh 'docker rm -f frontend || true'
                sh 'docker rm -f calculator-container || true'
            }
        }

        stage('Create Network') {
            steps {
                sh 'docker network create calculator-network || true'
            }
        }

        stage('Run Backend Container') {
            steps {
                sh 'docker run -d -p 8000:8000 --name backend --network calculator-network calculator-backend'
            }
        }

        stage('Run Frontend Container') {
            steps {
                sh 'docker run -d -p 3000:80 --name frontend --network calculator-network calculator-frontend'
            }
        }

        stage('Show Backend Logs') {
            steps {
                sh 'sleep 5'
                sh 'docker logs backend'
            }
        }

        stage('Show Frontend Logs') {
            steps {
                sh 'docker logs frontend'
            }
        }
    }
}