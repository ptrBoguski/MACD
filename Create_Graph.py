import numpy as np
from matplotlib import pyplot as plt


def make_graph(shares_count, market_shares, wealth_history, save_name, period_length):
    y = np.arange(period_length)
    plt.plot(y, wealth_history, color='red', label='CASH', linewidth=4)
    plt.plot(y, market_shares, color='blue', label='SHARE VALUE', linewidth=4)
    m = []
    for i in range(period_length):
        m.append(market_shares[i] + wealth_history[i])
    plt.plot(y, m, color='black', label='SHARES + CASH', linewidth=8)
    sv = save_name + ".jpg"
    plt.legend(loc="lower left", fontsize=32, markerscale=2.0)
    plt.savefig(sv)
    plt.clf()


