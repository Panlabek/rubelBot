import numpy
def convertFromRtoP(rubelPrice: str) -> str:
    # TODO fetch gbp price from yahoo
    gbp_price = str(numpy.float64(rubelPrice) / 1.3180)
    return gbp_price[:11]
def convertFromRtoE(rubelPrice: str) -> str:
    # TODO fetch eur price from yahoo
    eur_price = str(numpy.float64(rubelPrice) / 1.1062)
    return eur_price[:11]
