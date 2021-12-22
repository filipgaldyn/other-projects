import yfinance as yf
import streamlit as st
import pandas as pd

st.write(""" Simple Stock Price App
         Shown are the stock closing price and volume of Google!
         """)
         
tickerSymbol = "GOOGL"
tickerSymbol2 = "AMZN"
tickerData = yf.Ticker(tickerSymbol)
tickerData2 = yf.Ticker(tickerSymbol2)

tickerDf = tickerData.history(peroid='1h', start='2021-9-15', end = '2021-12-21')
tickerDf2 = tickerData2.history(peroid='1h', start='2021-9-15', end = '2021-12-21')
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf2.Close)
st.line_chart(tickerDf.Volume)
st.line_chart(tickerDf2.Volume)
