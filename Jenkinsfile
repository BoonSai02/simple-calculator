pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t calculator-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop calc-container || true'
                sh 'docker rm calc-container || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8000:8000 --name calc-container calculator-app'
            }
        }
    }
}