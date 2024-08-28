pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "tzahidaniel/specialmenu_app"
        DOCKERHUB_CREDENTIALS = credentials('finalproj')
        GIT_REPO_URL = 'https://github.com/tzahidaniel/SpecialMenu.git'
        GIT_CREDENTIALS_ID = 'gitfinalproj'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Checkout the repository
                    echo "Checking out the repository from branch: ${env.BRANCH_NAME}"
                    git branch: env.BRANCH_NAME, credentialsId: GIT_CREDENTIALS_ID, url: GIT_REPO_URL

                    // Clean up any previous images
                    echo 'Cleaning up old Docker images...'
                    sh "docker rmi ${DOCKER_IMAGE}:${BUILD_NUMBER} || true"

                    // Build the Docker image
                    echo 'Building the Docker image...'
                    sh "docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} ."
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Docker login to Docker Hub
                    echo 'Logging in to Docker Hub...'
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'

                    // Push Docker image to Docker Hub
                    echo 'Pushing the Docker image to Docker Hub...'
                    sh "docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}"
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'master'
            }
            steps {
                script {
                    // Clean up any running container with the same name
                    echo 'Stopping and removing old containers...'
                    sh '''
                    docker stop random-menu || true
                    docker rm random-menu || true
                    '''
                    // Deploy the application
                    echo 'Deploying the application...'
                    sh '''
                    docker run --rm -d -p 5000:5000 --name random-menu ${DOCKER_IMAGE}:${BUILD_NUMBER}
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
        success {
            echo "Build succeeded: ${env.JOB_NAME} for branch: ${env.BRANCH_NAME}"
        }
        failure {
            echo "Build failed: ${env.JOB_NAME} for branch: ${env.BRANCH_NAME}"
        }
    }
}

