import numpy as np


def EMAC(tab, i, rang, period):
    nominator = 0  # tab[i]
    denominator = 0  # 1
    if (rang + i >= period):
        rang = period - i
    for x in range(0, rang):
        if (x + i >= period):
            break
        b = np.power((1 - (2 / (rang + 1))), x)
        nominator += b * tab[x + i]
        denominator += b
    return nominator / denominator


def MACDC(tab, i, period):
    EMA12 = EMAC(tab, i, 12, period)
    EMA26 = EMAC(tab, i, 26, period)
    return EMA12 - EMA26
