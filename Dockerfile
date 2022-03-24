FROM python:slim
COPY . /app

WORKDIR /app

RUN ["pip", "install", "-r", "rubelBot.txt"]

ENTRYPOINT [ "python3", "main.py" ]
