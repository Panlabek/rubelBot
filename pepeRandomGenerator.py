import random
import os

def getRandomPepe() -> str:
    extensions_pos = ["png", "jpg", "gif"] 
    ext_num = random.randrange(0,2)
    if ext_num == 0:
        num = random.randrange(1,len([name for name in os.listdir("pepe_photos") if ".png" in name]))
    elif ext_num == 1:
        num = random.randrange(1,len([name for name in os.listdir("pepe_photos") if ".jpg" in name]))
    else:
        num = random.randrange(1,len([name for name in os.listdir("pepe_photos") if ".gif" in name]))
    return f"pepe_photos/{num}{extensions_pos[ext_num]}.{extensions_pos[ext_num]}"
