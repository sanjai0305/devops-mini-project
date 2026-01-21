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
                bat 'docker build -t flask-devops-app .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 flask-devops-app'
            }
        }
    }
}
