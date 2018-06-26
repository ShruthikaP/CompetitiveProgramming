  def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('Atleast 2 prices required')
    price  = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]
    for i in xrange(1, len(stock_prices)):
        current = stock_prices[i]
        profit = current - price
        max_profit = max(max_profit, profit)
        price  = min(price, current)
    return max_profit