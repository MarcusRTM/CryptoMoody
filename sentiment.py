"""
sentiment.py

Módulo para análise de sentimentos em textos relacionados a criptomoedas.

Funções:
- fetch_social_mentions(symbol, limit=100): faz a obtenção de menções para um símbolo.
- analyze_sentiment(text): calcula polaridade do texto.
- aggregate_sentiment(symbol, limit=100): calcula o sentimento médio para o símbolo.

Dependências:
- vaderSentiment (pip install vaderSentiment)

"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text: str) -> float:
    """
    Analisa o sentimento de um texto e retorna um score entre -1 (negativo) e 1 (positivo).

    :param text: Texto a ser analisado.
    :return: Valor de sentimento composto.
    """
    scores = analyzer.polarity_scores(text)
    return scores["compound"]

def fetch_social_mentions(symbol: str, limit: int = 100) -> list[str]:
    """
    Obtém menções de mídias sociais para um símbolo de criptomoeda.

    Este é um placeholder para integração com APIs de redes sociais como Twitter, Reddit ou feeds de notícias.
    Para uso real, substitua esta função por chamadas de API que retornem textos relevantes.

    :param symbol: Símbolo da criptomoeda (ex: 'BTC', 'ETH').
    :param limit: Número de menções a serem coletadas.
    :return: Lista de textos mencionando a criptomoeda.
    """
    # Exemplo estático de textos de exemplo
    examples = [
        f"{symbol} é a próxima grande coisa! Vamos para a lua!",
        f"Estou preocupado com o mercado de {symbol} hoje.",
        f"O preço de {symbol} está estável. Nada de novo."
    ]
    return examples[:limit]

def aggregate_sentiment(symbol: str, limit: int = 100) -> float:
    """
    Calcula o sentimento médio para um símbolo de criptomoeda.

    :param symbol: Símbolo da criptomoeda (ex: 'BTC', 'ETH').
    :param limit: Número de menções a serem agregadas.
    :return: Sentimento médio (valor entre -1 e 1).
    """
    mentions = fetch_social_mentions(symbol, limit)
    if not mentions:
        return 0.0
    scores = [analyze_sentiment(m) for m in mentions]
    return sum(scores) / len(scores)
