import random

def getRandomPepe() -> str:
    extensions_pos = ["png", "jpg", "gif"] 
    ext_num = random.randrange(0,2)
    num = random.randrange(1,900)
    return f"pepe_photos/{num}{extensions_pos[ext_num]}.{extensions_pos[ext_num]}"
