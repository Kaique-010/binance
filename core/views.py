from django.shortcuts import render
import plotly.express as px
import pandas as pd
from utils.binance_api import get_account_balance
from core.models import MarketSignal
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    balances = get_account_balance()
    signals = MarketSignal.objects.all().order_by('-timestamp')[:10]
    return render(request, 'core/dashboard.html', {"balances": balances, "signals": signals})


def grafico(request):
    dados = MarketSignal.objects.all()

    # Criar o DataFrame com os dados
    df = pd.DataFrame({
        'data': [sinal.created_at for sinal in dados],
        'preco': [sinal.preco for sinal in dados],
    })

    # Criar o gráfico utilizando o DataFrame
    fig = px.line(
        df,
        x='data',  # Coluna 'data' para o eixo X
        y='preco',  # Coluna 'preco' para o eixo Y
        labels={'data': 'Data', 'preco': 'Preço'},
        title='Histórico de Preços'
    )

    # Converter o gráfico para HTML
    grafico_html = fig.to_html(full_html=False)

    return render(request, 'grafico.html', {'grafico': grafico_html})