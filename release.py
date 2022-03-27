#!/bin/python3.10
import subprocess
import datetime
import datetime

destinedDirectory = "~/Documents/rubelArchives"

hour = datetime.datetime.now().strftime("%H")

today = datetime.datetime.now().strftime("%d")
subprocess.run(["docker", "build", "-t", f"rubel-bot{today}{hour}", "."])
subprocess.run(f"docker save rubel-bot{today} > {destinedDirectory}/rubel-bot{today}.tar", shell=True)
