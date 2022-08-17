###############################################
# Base Image
###############################################
FROM python:3.9.0-slim  as base

#use as working directory
WORKDIR /temp
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.4

RUN pip install "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml .
RUN  poetry export -f  requirements.txt --without-hashes >requirements.txt
RUN pip install -r requirements.txt

FROM base as builder
WORKDIR /app

#copy files to container
COPY . /app

EXPOSE 80
#Run server on port 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
