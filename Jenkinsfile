pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                echo 'Cloning repository'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flask-devops-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat '''
                docker stop flask-devops || exit 0
                docker rm flask-devops || exit 0
                '''
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name flask-devops flask-devops-app'
            }
        }
    }
}
