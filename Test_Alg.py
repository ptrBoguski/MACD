def test_alg(MACD, signal ,buy_i ,sell_i ,dane, alg, name, initial_wealth,period):
    print("Algorithm: " + name)
    print("Initial Wealth: " + initial_wealth.__str__())
    final_wealth = alg(MACD, signal, buy_i, sell_i, dane, initial_wealth,period)
    print("Final Wealth: " + final_wealth.__str__())
    print("Income: " + (final_wealth - initial_wealth).__str__())
    print("Graph in: " + name + ".jpg")
    return
