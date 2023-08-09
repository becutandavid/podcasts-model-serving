FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt
# RUN pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false && poetry install --only main