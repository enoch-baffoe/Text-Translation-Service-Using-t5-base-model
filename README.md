
# Text Translation service using T5-base model

This is a text translation service using the [t5-base](https://huggingface.co/t5-base) model from huggingface
The api service is built using [Fastapi](https://fastapi.tiangolo.com/)





## Features

- Translate text among 4 languages namely
    - English
    - French
    - German
    - Romanian


## Documentation

After running the app, the documentation is available at the "/docs" endpoint

## Hardware Requirements
Minimum hardware requirements 
CPU: 4GB RAM
DISK: 2GB

## Run Locally
You need to have in order to successfully run the project.
  - [Python 3.9](https://www.python.org/downloads/release/python-390/)
  - [Poetry 1.1.14](https://github.com/python-poetry/install.python-poetry.org)

Clone the project

```bash
  git clone the-project
```

Go to the project directory

```bash
  cd Text-Translation-Service-Using-t5-base-model
```

Install dependencies

```bash
   poetry install
```

Start the server

```bash
  poetry run uvicorn main:app --host 0.0.0.0 --port 80
```

## Deployment

To deploy the project,
1. Build the image with
```bash
  $ docker build . -t t5-base-api-service
```

2. Then run it in a container
```bash
  $ docker run --publish 80:80 t5-base-api-service   
```
 
### Using dockerhub
Alternately, the image can be pulled from docker hub
1. Pull the image
```bash
  docker pull peprah/t5-base-api-service:latest   
```

2. Run in container
```bash
  $ docker run --publish 80:80 peprah/t5-base-api-service  
```
