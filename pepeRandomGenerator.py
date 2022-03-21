import random

def getRandomPepe() -> str:
    extensions_pos = ["png", "jpg", "gif"] 
    ext_num = random.randrange(0,2)
    if ext_num == 1:
        num = random.randrange(1,1258)
    elif ext_num == 0:
        num = random.randrange(1,897)
    else:
        num = random.randrange(1, 99)
    return f"pepe_photos/{num}{extensions_pos[ext_num]}.{extensions_pos[ext_num]}"
