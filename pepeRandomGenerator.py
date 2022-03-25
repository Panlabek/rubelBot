import random
import os

def getRandomPepe() -> str:
    extensionsPos = ["png", "jpg", "gif"] 
    extNum = random.randrange(0,2)
    if extNum == 0:
        num = random.randrange(1,len([name for name in os.listdir("pepe_photos") if ".png" in name]))
    elif extNum == 1:
        num = random.randrange(1,len([name for name in os.listdir("pepe_photos") if ".jpg" in name]))
    else:
        num = random.randrange(1,len([name for name in os.listdir("pepe_photos") if ".gif" in name]))
    return f"pepe_photos/{num}{extensionsPos[extNum]}.{extensionsPos[extNum]}"
