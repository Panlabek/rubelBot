FROM fedora:latest
COPY . /app
WORKDIR /app
RUN ["dnf", "install", "python3", "-y"]

RUN ["dnf", "install", "python-pip", "-y"]

RUN ["pip", "install", "-r", "rubelBot.txt"]

ENTRYPOINT [ "python3", "main.py" ]
