provider "aws" {
  region = "eu-central-1"  # Replace with your desired region

  # Use environment variables, an AWS credentials file, or IAM roles for credentials
  access_key = var.access_key
  secret_key = var.secret_key
}

resource "aws_instance" "example" {
  ami           = "ami-00060fac2f8c42d30"  # Replace with your desired AMI ID
  instance_type = "t3.micro"               # Replace with your desired instance type

  # Use existing VPC and subnet
  subnet_id                   = "subnet-03d11a9f9e6f0ac77"  # Replace with your subnet ID
  associate_public_ip_address = true

  key_name        = "Jenkins_key"         # Replace with your key-pair name
  security_groups = ["sg-0b057cad7057723f3"]  # Replace with your security group ID

  tags = {
    Name = "project-jenkins"  # Replace with your desired tag
  }

  # User Data script to install Docker, Jenkins, and necessary dependencies
user_data = <<-EOF
              #!/bin/bash
              # Update package manager
              sudo yum update -y

              # Install Docker
              sudo amazon-linux-extras install docker -y
              sudo service docker start
              sudo usermod -a -G docker ec2-user

              # Install Python3
              sudo yum install python3 -y

              # Install Flask
              sudo pip3 install Flask

              # Install Git
              sudo yum install git -y
              EOF

  # Block device mapping (optional)
  root_block_device {
    volume_size = 8            # Size of the root volume in GiB
    volume_type = "gp3"        # Type of the root volume
  }

  # Enable monitoring (optional)
  monitoring = true
}

output "instance_id" {
  value = aws_instance.example.id
}

output "instance_public_ip" {
  value = aws_instance.example.public_ip
}

output "instance_public_dns" {
  value = aws_instance.example.public_dns
}

