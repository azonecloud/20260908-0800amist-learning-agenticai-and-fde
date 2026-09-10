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