# ASSIGNMENT 2

## Section 1: 15 commands:

### 1. docker –version
This command is used to get the currently installed version of docker <br>
![1](https://github.com/siva24031990/FirstFasyApp/blob/main/Resources/Capture%201.JPG)

### 2. docker pull \<image name\>
command is used to pull images from the docker repository(hub.docker.com) <br>
![1](https://github.com/siva24031990/FirstFasyApp/blob/main/Resources/Capture%202.JPG)

### 3. docker run
docker run –dp \<image name\>
This command is used to create a container from an image <br>
![1](https://github.com/siva24031990/FirstFasyApp/blob/main/Resources/Capture%203.JPG)
 
### 4. docker ps
This command is used to list the running containers <br>
![1](https://github.com/siva24031990/FirstFasyApp/blob/main/Resources/Capture%204.JPG)
 
### 5. docker ps -a
This command is used to show all the running and exited containers <br>
![1](https://github.com/siva24031990/FirstFasyApp/blob/main/Resources/Capture%205.JPG)
 
### 6. docker exec
Usage: docker exec -it \<container id\> bash
This command is used to access the running container <br>
![1](https://github.com/siva24031990/FirstFasyApp/blob/main/Resources/Capture%206.JPG) 

### 7. docker stop
Usage: docker stop \<container id\>
This command stops a running container <br>
![1](https://github.com/siva24031990/FirstFasyApp/blob/main/Resources/Capture%207.JPG)
 
### 8. docker kill \<container id\>
This command kills the container by stopping its execution immediately. The difference between ‘docker kill’ and ‘docker stop’ is that ‘docker stop’ gives the container time to shutdown gracefully, in situations when it is taking too much time for getting the container to stop, one can opt to kill it <br>
 ![1](https://github.com/siva24031990/FirstFasyApp/blob/main/Resources/Capture%208.JPG)

### 9. docker commit
Usage: docker commit \<conatainer id\> \<username/imagename\>
This command creates a new image of an edited container on the local system <br>
![1](https://github.com/siva24031990/FirstFasyApp/blob/main/Resources/Capture%209.JPG)
 
### 10. docker login
This command is used to login to the docker hub repository <br>
![1](https://github.com/siva24031990/FirstFasyApp/blob/main/Resources/Capture%2010.JPG)

### 11. docker push \<username/image name\>
This command is used to push an image to the docker hub repository <br>
![1](https://github.com/siva24031990/FirstFasyApp/blob/main/Resources/Capture%2011.JPG)

### 12. docker images
This command lists all the locally stored docker images <br>
![1](https://github.com/siva24031990/FirstFasyApp/blob/main/Resources/Capture%2012.JPG)
 
### 13. docker rm \<container id\>
This command is used to delete a stopped container <br>
![1](https://github.com/siva24031990/FirstFasyApp/blob/main/Resources/Capture%2013.JPG)
 
### 14. docker rmi \<image-id\>
This command is used to delete an image from local storage <br>
![1](https://github.com/siva24031990/FirstFasyApp/blob/main/Resources/Capture%2014.JPG)
 
### 15. docker build
Usage: docker build \<path to docker file\>
This command is used to build an image from a specified docker file <br>
![1](https://github.com/siva24031990/FirstFasyApp/blob/main/Resources/Capture%2015.JPG)

## Section 2: Hello World Docker Image
Ran in play ground <br>
![1](https://github.com/siva24031990/FirstFasyApp/blob/main/Resources/Section%202.JPG)

## Section 3: 
created Fast Api app and uploaded in Github, could not create docker image due to system not support <br>
 ![1](https://github.com/siva24031990/FirstFasyApp/blob/main/Resources/Section%203.JPG)
