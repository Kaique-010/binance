import numpy as np

def calcular_rsi(precos, periodo=14):
    """
    Calcula o Índice de Força Relativa (RSI).
    
    :param precos: Lista de preços de fechamento.
    :param periodo: Período para o cálculo do RSI (padrão: 14).
    :return: Valor RSI.
    """
    precos = np.array(precos)
    deltas = np.diff(precos)
    ganhos = np.where(deltas > 0, deltas, 0)
    perdas = np.where(deltas < 0, -deltas, 0)

    media_ganhos = np.mean(ganhos[:periodo])
    media_perdas = np.mean(perdas[:periodo])

    for i in range(periodo, len(precos)):
        delta = deltas[i - 1]
        ganho = max(delta, 0)
        perda = -min(delta, 0)

        media_ganhos = (media_ganhos * (periodo - 1) + ganho) / periodo
        media_perdas = (media_perdas * (periodo - 1) + perda) / periodo

    rs = media_ganhos / media_perdas if media_perdas != 0 else 0
    rsi = 100 - (100 / (1 + rs))
    return rsi

def sinal_rsi(precos, periodo=14):
    """
    Gera um sinal com base no RSI.

    :param precos: Lista de preços de fechamento.
    :param periodo: Período para o cálculo do RSI.
    :return: "COMPRA", "VENDA" ou "MANTER".
    """
    rsi = calcular_rsi(precos, periodo)
    if rsi < 30:
        return "COMPRA"
    elif rsi > 70:
        return "VENDA"
    return "MANTER"
