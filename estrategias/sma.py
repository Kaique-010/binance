import numpy as np

def calcular_sma(precos, periodo):
    """
    Calcula a Média Móvel Simples (SMA).

    :param precos: Lista de preços de fechamento.
    :param periodo: Período para o cálculo da SMA.
    :return: SMA calculada.
    """
    if len(precos) < periodo:
        return None
    return np.mean(precos[-periodo:])

def sinal_sma(precos, periodo_curto=10, periodo_longo=50):
    """
    Gera um sinal com base nas médias móveis simples (SMA).
    
    :param precos: Lista de preços de fechamento.
    :param periodo_curto: Período para a SMA curta.
    :param periodo_longo: Período para a SMA longa.
    :return: "COMPRA", "VENDA" ou "MANTER".
    """
    sma_curto = calcular_sma(precos, periodo_curto)
    sma_longo = calcular_sma(precos, periodo_longo)

    if sma_curto is None or sma_longo is None:
        return "MANTER"

    if sma_curto > sma_longo:
        return "COMPRA"
    elif sma_curto < sma_longo:
        return "VENDA"
    return "MANTER"
