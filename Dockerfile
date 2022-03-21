FROM fedora:latest
COPY . /app
WORKDIR /app
RUN ["dnf", "install", "python3", "-y"]

RUN ["dnf", "install", "conda", "-y"]

RUN [ "conda", "env", "create", "--file", "rubelBot.yaml" ]

SHELL ["conda", "run", "-n", "rubelBot", "/bin/bash", "-c"]

RUN ["mkdir", "-p",  "/root/.conda/envs/rubelBot/etc/conda/"]

RUN ["mv", "activate.d", "/root/.conda/envs/rubelBot/etc/conda/"]

RUN ["mv", "deactivate.d", "/root/.conda/envs/rubelBot/etc/conda/"]

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "rubelBot", "python", "main.py"]
