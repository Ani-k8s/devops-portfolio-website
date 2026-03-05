pipeline {
    agent any

    environment {
        IMAGE_NAME = "anik8s/annappa-portfolio"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Ani-k8s/devops-portfolio-website.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:v3 .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $IMAGE_NAME:v3'
            }
        }

    }
}
