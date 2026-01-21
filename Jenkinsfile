pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/sanjai0305/devops-mini-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t devops-flask-app .'
            }
        }

        stage('Run Container') {
            steps {
                bat '''
                docker stop devops-container || exit 0
                docker rm devops-container || exit 0
                docker run -d -p 5000:5000 --name devops-container devops-flask-app
                '''
            }
        }
    }
}
