# Deploying the mock API

 1. Spin up EC2 instance
 2. SSH to the instance
 3. Install docker on EC2 instance

 From: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html
 
 > **To install Docker on an Amazon EC2 instance**
> 
> Launch an instance with the Amazon Linux 2 AMI. For more information, see Launching an Instance in the Amazon EC2 User Guide for Linux Instances.
> 
> Connect to your instance. For more information, see Connect to Your Linux Instance in the Amazon EC2 User Guide for Linux Instances.
> 
> Update the installed packages and package cache on your instance.
> ```sudo yum update -y```
> 
> Install the most recent Docker Community Edition package.
> `sudo amazon-linux-extras install docker`
> 
> Start the Docker service.
> `sudo service docker start`
>
> Add the ec2-user to the docker group so you can execute Docker commands without using sudo.
> `sudo usermod -a -G docker ec2-user`
>
> Log out and log back in again to pick up the new docker group permissions. You can accomplish this by closing your current SSH terminal window > and reconnecting to your instance in a new one. Your new SSH session will have the appropriate docker group permissions.
> 
> Verify that the ec2-user can run Docker commands without sudo.
>  `docker info`
> 
> Note
> In some cases, you may need to reboot your instance to provide permissions for the ec2-user to access the Docker daemon. Try rebooting your > instance if you see the following error:
> 
> Cannot connect to the Docker daemon. Is the docker daemon running on this host?


 3. Install git and do git clone

    ~~~~
    sudo yum install git
    mkdir P1078-dummy-api
    cd P1078-dummy-api
    git clone https://github.com/FelixCarrierBNC/dummy-api.git
    ~~~~
    

 4. Build and run

    ~~~~
    cd dummy-api
    docker build -t dummy-api .
    docker images
    docker run -p 80:5000 dummy-api:latest
    ~~~~
