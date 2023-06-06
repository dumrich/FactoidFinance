FROM python:3.10.4-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN adduser --disabled-password --gecos '' myuser
RUN chown -R myuser:myuser /code

# Switch to the newly created user
USER myuser

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .