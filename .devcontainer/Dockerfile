# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT=3.10
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

ARG DEBIAN_FRONTEND=noninteractive \
    USER_NAME=user \
    USER_UID=61000 \
    USER_GID=61000

ENV POETRY_VERSION=1.6.1 \
    POETRY_HOME=/opt/poetry \
    POETRY_VENV=/opt/poetry-venv \
    POETRY_CACHE_DIR=/opt/.cache \
    POETRY_VIRTUALENVS_CREATE=true \
    PATH="/opt/poetry-venv/bin:${PATH}"

COPY poetry.lock pyproject.toml ./

RUN apt-get update \
    && apt-get -y install --no-install-recommends sqlite3

RUN groupadd -g ${USER_GID} ${USER_NAME} \
    && useradd -r -s /bin/bash -m -u ${USER_UID} -g ${USER_GID} ${USER_NAME} \
    && pip install -U pip setuptools poetry==${POETRY_VERSION} \
    && poetry install --no-interaction --no-ansi \
    && ln -s $(poetry env info --path) ${POETRY_VENV} \
    && chown ${USER_NAME}: -R /opt

