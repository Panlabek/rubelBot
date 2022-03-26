FROM python

WORKDIR /app

ADD . /app

RUN ["pip", "install", "-r", "rubelBot.txt"]

CMD [ "python3", "main.py" ]
