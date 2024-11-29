from django.db import models

class MarketSignal(models.Model):
    symbol = models.CharField(max_length=20)  # Par de moedas (ex: BTCUSDT)
    signal = models.CharField(max_length=10)  # "BUY", "SELL", "HOLD"
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.symbol} - {self.signal} @ {self.price}"
