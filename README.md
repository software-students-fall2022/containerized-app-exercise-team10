# Containerized App Exercise

[![Machine Learning Client](https://github.com/software-students-fall2022/containerized-app-exercise-team10/actions/workflows/test-machine-learning.yaml/badge.svg)](https://github.com/software-students-fall2022/containerized-app-exercise-team10/actions/workflows/test-machine-learning.yaml)

[![Containerized App Server CI](https://github.com/software-students-fall2022/containerized-app-exercise-team10/actions/workflows/test-build-app.yaml/badge.svg)](https://github.com/software-students-fall2022/containerized-app-exercise-team10/actions/workflows/test-build-app.yaml)

# Handscribe

Handscribe is an online tool that uses the handprint package to extract text from png, jpg, and jpeg images.

## Installation

### 1. Docker
This application uses Docker to containerize its parts. You must have [Docker](https://docs.docker.com/get-docker/) installed on your machine to run this.

### 2. Download files
[https://github.com/software-students-fall2022/containerized-app-exercise-team10/archive/refs/heads/main.zip](Download the files from GitHub) Create a new directory on your machine where you want to run the app and extract the files there.

### 3. Run containers
Navigate to said directory and run the containers together using:
```bash
$ docker compose up
```
This should begin building the containers. Wait for this process to finish. 

### 4. Start app
When the console shows the app running on localhost, click the link that appears to open the app, or navigate to `https://localhost:3000`.
```bash
app  |  Server running on port https://localhost:3000
```

### 5. App is ready for use
From here, just interact with the form on the homepage, and extract your text from your images!


## Authors
[Danilo Montes](https://github.com/danilo-montes) \
[]() \
[]() \
[]() \
[]() \
[]() \