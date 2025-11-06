"""
CryptoMoody - bot de trading com analise de sentimentos e IA.

Este script usa analise de sentimentos e mudancas de preco para sugerir acoes de negociacao de criptomoedas.
Ele depende do modulo `sentiment` para coletar mencoes sociais e calcular o sentimento agregado, e do modulo `backtest` para avaliar estrategias com dados historicos. Use apenas para fins educativos; nao utilize em trading real sem testes completos.
"""

import time
from typing import Optional

try:
    import ccxt  # type: ignore
except ImportError:
    ccxt = None  # placeholder

# Importa modulos internos
from sentiment import fetch_social_mentions, aggregate_sentiment  # funções de sentimento
from backtest import backtest_strategy, load_historical_data  # funções de backtesting


def fetch_price(exchange, symbol: str) -> float:
    """Obtém o preço mais recente para um par de negociação na exchange."""
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']


def fetch_sentiment(symbol: str, limit: int = 100) -> float:
    """Coleta e agrega sentimento para um símbolo usando o módulo de sentimento."""
    mentions = fetch_social_mentions(symbol, limit=limit)
    return aggregate_sentiment(mentions)


def decision_logic(sentiment_score: float, price_trend: float) -> str:
    """Decide se deve ir long, short ou ficar neutro (hold) com base no sentimento e na tendência de preço."""
    if sentiment_score > 0 and price_trend > 0:
        return "long"
    elif sentiment_score < 0 and price_trend < 0:
        return "short"
    else:
        return "hold"


def main_live():
    """Loop principal para decisões de trading ao vivo."""
    if ccxt is None:
        print("A biblioteca ccxt não está instalada. Instale via `pip install ccxt` para buscar dados de mercado.")
        return
    exchange = ccxt.binance()
    symbol = "BTC/USDT"
    last_price = fetch_price(exchange, symbol)

    while True:
        sentiment = fetch_sentiment(symbol)
        current_price = fetch_price(exchange, symbol)
        price_trend = current_price - last_price
        action = decision_logic(sentiment, price_trend)
        print(f"Sentimento: {sentiment:.3f} | Tendência de preço: {price_trend:.2f} | Ação sugerida: {action}")
        last_price = current_price
        time.sleep(60)


def run_backtest():
    """Executa um backtest usando dados históricos para avaliar a estratégia."""
    prices, sentiments = load_historical_data()
    result = backtest_strategy(prices, sentiments)
    print(f"Retorno do backtest: {result:.2%}")


if __name__ == "__main__":
    # Executa o backtest como demonstração; em produção, escolha entre backtest ou live via argumentos de linha de comando ou config
    run_backtest()
    # Para trading ao vivo, descomente a linha abaixo:
    # main_live()
