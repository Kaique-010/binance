from celery import shared_task
from utils.binance_api import get_market_data
from core.models import MarketSignal
from estrategias.rsi import sinal_rsi
from estrategias.sma import sinal_sma

@shared_task
def monitor_market(symbol, interval):
    data = get_market_data(symbol, interval)
    latest_price = data[-1][4]  # Preço de fechamento mais recente
    # Adicione lógica de estratégia para determinar sinais (ex.: "BUY", "SELL")
    signal = "HOLD"  # Placeholder
    MarketSignal.objects.create(symbol=symbol, signal=signal, price=latest_price)


@shared_task
def monitorar_mercado(simbolo, intervalo):
    dados = get_market_data(simbolo, intervalo)
    precos_fechamento = [float(candle[4]) for candle in dados]

    # Aplicar estratégias
    sinal_rsi_estrategia = sinal_rsi(precos_fechamento)
    sinal_sma_estrategia = sinal_sma(precos_fechamento)

    # Determinar sinal final (prioridade para RSI)
    sinal_final = sinal_rsi_estrategia if sinal_rsi_estrategia != "MANTER" else sinal_sma_estrategia

    # Preço atual
    preco_atual = precos_fechamento[-1]

    # Salvar sinal no banco
    MarketSignal.objects.create(simbolo=simbolo, sinal=sinal_final, preco=preco_atual)