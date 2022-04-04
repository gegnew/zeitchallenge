FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /root
COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install .
