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

## Run Unit Tests

### 1. Activate virtual environment

If you are currently running the docker containers from your terminal, stop them with `CTRL+C`

Set up and activate a virtual environment in the root directory with:

```
python3 -m venv env

source env/bin/activate
```

### 2. Install testing dependencies

Once you have activated your virtual environment, install the requisite testing packages with:

```
pip install -r requirements.txt
```

### 3. Navigate to testing directory

If you want to test the machine learning client code, execute:

```
cd machine-learning-client
```

Or, if you want to test the web app code, execute:

```
cd web-app
```

### 3. Run tests

To run tests with coverage reports, execute in your terminal:

```
coverage run -m pytest

coverage report -m
```

Sample coverage report output:

```
Name                Stmts   Miss  Cover
---------------------------------------
app.py                 63     20    68%
tests/__init__.py       0      0   100%
tests/ml_test.py       72      0   100%
---------------------------------------
TOTAL                 135     20    85%
```

Machine learning client code coverage: **68%**

Web app code coverage: **add\_%_here**

## Authors

[Danilo Montes](https://github.com/danilo-montes) \
[Bhavig Pointi](https://github.com/bpointi) \
[]() \
[]() \
[Rachel Andoh](https://github.com/rachel0lehcar) \
[Misha Seo](https://github.com/mishaseo)
