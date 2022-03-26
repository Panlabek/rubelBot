FROM python
COPY . /app

WORKDIR /app

RUN ["pip", "install", "-r", "rubelBot.txt"]

CMD [ "python3", "main.py" ]
