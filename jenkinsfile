pipeline {
    agent any

    environment {
        // Retrieve AWS credentials from Jenkins and set them as environment variables
        AWS_ACCESS_KEY_ID = credentials('aws_credentials').username
        AWS_SECRET_ACCESS_KEY = credentials('aws_credentials').password
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout your repository
                git 'https://github.com/tzahidaniel/SpecialMenu.git'
            }
        }

        stage('Terraform Init') {
            steps {
                // Initialize Terraform
                sh 'terraform init'
            }
        }

        stage('Terraform Plan') {
            steps {
                // Plan Terraform changes
                sh 'terraform plan'
            }
        }

        stage('Terraform Apply') {
            steps {
                // Apply Terraform changes
                sh 'terraform apply -auto-approve'
            }
        }
    }

    post {
        always {
            // Clean up workspace after build
            cleanWs()
        }
    }
}
