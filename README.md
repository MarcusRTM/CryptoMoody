# CryptoMoody

CryptoMoody é um aplicativo de *trade* quantitativo que utiliza análise de sentimentos e inteligência artificial para auxiliar na tomada de decisão de compra e venda de ativos de criptomoedas. O objetivo é combinar dados de sentimento extraídos de redes sociais e notícias com sinais quantitativos de mercado para construir estratégias de investimento automatizadas.

## Funcionalidades principais

- **Coleta de dados de sentimento**: agrega informações de fontes como Twitter, Reddit e sites de notícias para estimar o humor do mercado em relação a diferentes criptomoedas. Algoritmos de classificação de sentimentos baseados em redes neurais e processamento de linguagem natural avaliam cada menção como positiva, neutra ou negativa.
- **Integração com dados de mercado**: obtém cotações em tempo real de exchanges através de APIs (por exemplo, usando a biblioteca `ccxt`) para monitorar preços, volumes e volatilidade.
- **Estratégias long/short baseadas em sentimento**: combina a direção do sentimento com a tendência de preço para abrir posições. Por exemplo, se o sentimento geral for positivo e o preço estiver em alta, o bot pode abrir uma posição **long**; se o sentimento for negativo e o preço mostrar fraqueza, pode abrir uma posição **short**.
- **Backtesting e ajuste de parâmetros**: oferece scripts para avaliar o desempenho histórico das estratégias de sentimento, permitindo ajustar parâmetros como janelas de tempo, pesos de sentimentos e filtros de volatilidade.
- **Relatórios e visualizações**: gera relatórios com o histórico de trades, curva de capital e estatísticas de risco (drawdown, Sharpe ratio etc.) para acompanhar a performance.

## Inspiração e pesquisas

Pesquisas recentes destacam a importância da análise de sentimentos nos mercados de criptomoedas. Artigos de 2025 sobre algoritmos de trading com IA ressaltam o uso de classificadores de sentimento baseados em redes neurais, análise de notícias via processamento de linguagem natural e estratégias de *reinforcement learning* que se adaptam continuamente ao mercado. Esses modelos ajudam a detectar hype inicial, filtrar ruído e combinar sinais de sentimento com métricas técnicas. Também nos inspiramos em projetos de código aberto que executam bots de trading conforme o sentimento: eles observam que, quando o sentimento é fortemente positivo em relação a um ativo e a tendência de preço confirma, abrir uma posição **long** pode ser lucrativo; já sentimentos negativos combinados com queda de preço podem sugerir **short**.

## Estrutura do repositório

- `crypto_moody.py`: script principal com a lógica de coleta de sentimentos, integração com cotações e tomada de decisão.
- `sentiment.py`: módulos auxiliares para processar e classificar textos de redes sociais/notícias.
- `backtest.py`: ferramentas de backtesting para avaliar estratégias com dados históricos.
- `requirements.txt`: lista de dependências Python (por exemplo, `ccxt`, `textblob`, `pandas`, `numpy`).

## Como contribuir

1. Clone este repositório e crie uma branch.
2. Instale as dependências listadas em `requirements.txt`.
3. Contribua com melhorias nas funções de análise de sentimento, integrações de API ou novas estratégias.
4. Abra um pull request descrevendo suas mudanças.

Este projeto está em fase inicial; sinta-se à vontade para sugerir ideias e colaborações!
