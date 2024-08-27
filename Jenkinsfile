pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('finalproj')
    }

    stages {
        stage('SCM Checkout') {
            steps {
                git branch: 'master', credentialsId: 'gitfinalproj', url: 'https://github.com/tzahidaniel/SpecialMenu.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'sudo docker build -t tzahidaniel/specialmenu:$BUILD_NUMBER .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push tzahidaniel/specialmenu:$BUILD_NUMBER'
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                docker stop webapp_ctr || true
                docker run --rm -d -p 5000:5000 --name webapp_ctr tzahidaniel/specialmenu:$BUILD_NUMBER
                '''
            }
        }
    }
}
