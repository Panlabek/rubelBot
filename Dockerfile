# FROM python

# WORKDIR /app

# ADD . /app

# RUN ["pip", "install", "-r", "rubelBot.txt"]

# CMD [ "python3", "main.py" ]
FROM fedora:latest

RUN ["dnf", "update", "-y"]

RUN ["dnf", "install", "python3", "-y"]

RUN ["dnf", "install", "python3-pip", "-y"]

WORKDIR /app

ADD . /app

RUN ["pip", "install", "-r", "rubelBot.txt"]

CMD ["python3", "main.py"]

