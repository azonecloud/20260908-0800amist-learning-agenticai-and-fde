################################################################################# 
# 01. LIST OF TOOLS TO BE INSTALLED
#################################################################################

1. Install Visual Studio Code (Editor)
   Action: Download and install Visual Studio Code from [Visual Studio Code Official Website](https://code.visualstudio.com/).

2. Install Git (Version Control System)
   Action: Download and install Git from [Git Official Website](https://git-scm.com/).
```bash
   git --version
```

3. Set up GitHub (For Git Repositories)
   Action: Create an account or log in to [GitHub](https://github.com/).

4. Install Java JDK
   Action: Download Java JDK 17 from [Oracle's Website](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html).
 
      Setup:
         Set environment variables:
         - `JAVA_HOME`: Path to the Java installation directory (e.g., `C:\Program Files\Java\jdk-17\` OR 'C:\Program Files\Java\jdk-21.0.11')
         - Add `%JAVA_HOME%\bin` to the `PATH` variable.

5. Install Python
   Action: Download and install Python from [Python Official Website](https://www.python.org/).
   Setup: Add Python to the `PATH` (e.g., `C:\python`).
```bash
   python --version
   pip --version
   which python #(use git bash)
```

6. Install Jupyter Lab
   Action: Open a terminal and run the following:

```bash
      pip install jupyterlab
      pip install notebook
```
Action: Open another terminal and run the following:
```bash
      jupyter --version
      jupyter lab #(Running the Jupyter lab, and extract the Token and submit to Password/Token)
```

7. Install Oracle VirtualBox - For Virtualization 
   - URL : https://www.virtualbox.org/
   - URL : https://docs.docker.com/desktop/troubleshoot-and-support/troubleshoot/topics/#virtualization
   - CheckPoint : Enable virtualization from BIOS - [Enabled]

8. Install Docker Desktop for Windows - For Containers
   - URL : https://docs.docker.com/desktop/troubleshoot-and-support/troubleshoot/topics/#virtualization

(For Windows)
https://www.docker.com/products/docker-desktop/

(For Linux)
```bash
apt-get update -y && apt-get install docker.io -y #(for Ubuntu)
yum update -y && yum install docker -y #(for Fedora/RedHat)
systemctl start docker #(for Fedora/RedHat)
docker --version

```
```bash
   $ docker --version
   $ docker images
   $ docker ps -a
   $ docker rmi <<CONTAINER_ID>>
   $ docker rmi $(docker ps -a)
   $ docker rm  <<IMAGE_ID>>
   $ docker rm $(docker images -a)
```

9. Setup Docker Container Registry
- URL: hub.docker.com

10. Install minikube
- URL: https://minikube.sigs.k8s.io/docs/

11. Install Kubectl
URL: https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/

```bash
kubectl version
```
