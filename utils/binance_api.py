from binance.client import Client


API_KEY = '98XF10UX3hFJNcgH7dv0Mqw8JOd64YFslajAiHfgEyxzpKW4tuJ6v77AGELaBdyX'
API_SECRET = 'NSpFx6xKH6V5hbIB8oLA68KlN7Lup55GXP47sbNqX1IF5B9zRjY7GH0kEm8PGYgS'


client = Client(API_KEY, API_SECRET)

def get_account_balance():
    """
    Retorna o saldo de todas as moedas com saldo positivo.
    """
    account_info = client.get_account()
    balances = [
        {
            "asset": b['asset'],
            "free": float(b['free']),
            "locked": float(b['locked'])
        }
        for b in account_info['balances']
        if float(b['free']) > 0 or float(b['locked']) > 0
    ]
    return balances

def get_market_data(symbol, interval, limit=100):
    """
    Retorna dados de velas (candlesticks) para análise de mercado.
    """
    candlesticks = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    return candlesticks