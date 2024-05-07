FROM python:3.10.5

RUN apt-get update && \
    apt-get install -y libpq-dev

RUN useradd --create-home dev

WORKDIR /home/dev/unb-connect-api

USER dev

COPY . .

RUN pip install -U --no-cache-dir -r requirements.txt