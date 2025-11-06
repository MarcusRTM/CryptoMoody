"""
backtest.py

Módulo para realizar backtesting de estratégias de trading baseadas em sentimento.

Funções:
- backtest_strategy(prices: List[float], sentiments: List[float], threshold: float):
    Simula uma estratégia simples: entrar comprado quando sentimento > limiar, vendido quando sentimento < -limiar, caso contrário neutro.
    Usa variação de preço para calcular retorno cumulativo.
- load_historical_data(): placeholder para carregar dados históricos de preço e sentimento.

"""

from typing import List, Tuple

def backtest_strategy(prices: List[float], sentiments: List[float], threshold: float = 0.1) -> float:
    """
    Executa um backtest simples baseado em listas de preços e pontuações de sentimento.

    :param prices: Lista de preços históricos.
    :param sentiments: Lista de pontuações de sentimento correspondentes.
    :param threshold: Limiar de decisão para abrir posição.
    :return: Retorno percentual cumulativo da estratégia.
    """
    if len(prices) != len(sentiments):
        raise ValueError("As listas de preços e sentimentos devem ter o mesmo tamanho.")

    equity = 1.0  # valor inicial do investimento
    position = 0  # 1 para long, -1 para short, 0 para neutro

    for i in range(1, len(prices)):
        # define posição com base no sentimento anterior
        if sentiments[i - 1] > threshold:
            position = 1
        elif sentiments[i - 1] < -threshold:
            position = -1
        else:
            position = 0

        # calcula retorno do período
        price_return = (prices[i] - prices[i - 1]) / prices[i - 1]
        equity *= 1 + position * price_return

    return equity - 1

def load_historical_data() -> Tuple[list[float], list[float]]:
    """
    Placeholder para carregar dados históricos de preços e sentimentos.

    Substitua por carregamento real de dados a partir de arquivos ou APIs.

    :return: Tupla (precos, sentimentos)
    """
    prices = [100, 102, 101, 105, 104, 108]
    sentiments = [0.2, 0.1, -0.1, 0.05, -0.2, 0.3]
    return prices, sentiments

if __name__ == "__main__":
    # Exemplo de uso do backtester
    precos, sentimentos = load_historical_data()
    retorno = backtest_strategy(precos, sentimentos)
    print(f"Retorno da estratégia: {retorno:.2%}")
