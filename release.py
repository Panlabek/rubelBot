#!/bin/python3.10
import subprocess
import datetime

destinedDirectory = "~/Documents/rubelArchives"

today = datetime.datetime.now().strftime("%d")
subprocess.run(["docker", "build", "-t", f"rubel-bot{today}", "."])
subprocess.run(f"docker save rubel-bot{today} > {destinedDirectory}/rubel-bot{today}.tar", shell=True)
