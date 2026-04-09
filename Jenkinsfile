pipeline {
    agent any

    stages {
        stage('Setup Python & UV') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install uv'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh './venv/bin/uv pip install -e backend'
            }
        }

        stage('Run Server') {
            steps {
                sh './venv/bin/uvicorn backend.app:app --host 0.0.0.0 --port 8000 &'
            }
        }
    }
}