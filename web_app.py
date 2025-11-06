import streamlit as st
from sentiment import fetch_social_mentions, aggregate_sentiment
from backtest import backtest_strategy, load_historical_data


def main():
    st.title("CryptoMoody - Quantitative Trading with Sentiment Analysis")
    symbol = st.text_input("Cryptocurrency Symbol (e.g., BTC)")

    if st.button("Run Sentiment Analysis"):
        if symbol:
            mentions = fetch_social_mentions(symbol)
            score = aggregate_sentiment(mentions)
            st.write(f"Sentiment score for {symbol}: {score:.4f}")
        else:
            st.write("Please enter a cryptocurrency symbol.")

    if st.button("Run Backtest"):
        if symbol:
            historical_data = load_historical_data(symbol)
            result = backtest_strategy(historical_data)
            st.write(result)
        else:
            st.write("Please enter a cryptocurrency symbol.")


if __name__ == "__main__":
    main()
