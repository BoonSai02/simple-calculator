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

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t calculator-app .'
            }
        }

        stage('Stop Old Containers') {
            steps {
                // Remove all possible conflicting containers
                sh 'docker rm -f calculator-container || true'
                sh 'docker rm -f backend || true'
                sh 'docker rm -f frontend || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8000:8000 --name calculator-container calculator-app'
            }
        }

        stage('Show Logs') {
            steps {
                // wait for app to start
                sh 'sleep 5'
                
                // print logs in Jenkins console
                sh 'docker logs calculator-container'
            }
        }
    }
}