import Create_Graph


def alg_all_in(MACD, signal, buy_i, sell_i, data, kwota_startowa, period_length):
    wallet = kwota_startowa
    stock = 0
    shares_count = []
    shares_value = []
    wealth_history = []
    for x in range(period_length):
        if x in buy_i:
            shares_volume = wallet // data[x]
            wallet = wallet - shares_volume * data[x]
            stock += shares_volume
        elif x in sell_i:
            wallet += stock * data[x]
            stock = 0
        shares_count.append(stock)
        shares_value.append(stock * data[x])
        wealth_history.append(wallet)
    Create_Graph.make_graph(shares_count, shares_value, wealth_history, "ALL IN_", period_length)
    return wallet + stock * data[period_length - 1]
