import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("Stock Spread Analysis")

# Tickers List
tickers = [
    "CBUT.JK", "RSGK.JK", "TCID.JK", "TRST.JK", "ASBI.JK", "MTLA.JK", "ASRM.JK",
    "SURE.JK", "IDPR.JK", "APII.JK", "PGLI.JK", "ASJT.JK", "BSIM.JK", "LCKM.JK",
    "MASB.JK", "ALKA.JK", "TIRA.JK", "BBLD.JK", "INPP.JK", "INRU.JK", "RELI.JK",
    "TGKA.JK", "BBMD.JK", "BBSI.JK", "LIFE.JK", "SMMA.JK", "DUTI.JK", "IPAC.JK", 
    "NICK.JK", "APLI.JK", "ATIC.JK", "SHIP.JK", "DCII.JK", "MEGA.JK", "YULE.JK", 
    "PTSP.JK", "TRUS.JK", "SAPX.JK", "DAYA.JK", "SKBM.JK", "EDGE.JK", "MERK.JK", 
    "TBMS.JK", "RANC.JK", "HDFA.JK", "GHON.JK", "SOTS.JK", "BINA.JK", "LINK.JK", 
    "PURI.JK", "IFSH.JK", "SIPD.JK", "KINO.JK", "MCAS.JK"
]

# Remove duplicates
tickers = list(set(tickers))

# Tick rules
def calculate_tick(price):
    if price < 200:
        return 1
    elif 200 <= price < 500:
        return 2
    elif 500 <= price < 2000:
        return 5
    elif 2000 <= price < 5000:
        return 10
    else:
        return 25

# Fetch data
def fetch_data():
    spread_data = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data = stock.info
        bid, ask = data.get("bid"), data.get("ask")
        
        if bid and ask:
            spread = ask - bid
            tick = calculate_tick(bid)
            real_spread = spread - (tick * 2)
            spread_percent = (real_spread / bid) * 100 if bid > 0 else 0
            gain_trade = ((real_spread / bid)*100) if bid > 0 else None  # Gain/Trade (%)
            
            spread_data.append({
                "Ticker": ticker, 
                "Bid": bid, 
                "Ask": ask, 
                "Spread": spread, 
                "Real Spread": real_spread, 
                "Spread (%)": spread_percent,
                "Gain/Trade (%)": gain_trade
            })
    return pd.DataFrame(spread_data)

# Highlighting Function
def highlight_gain(data, column):
    return [
        "background-color: lightgreen" if val > 5 else "background-color: lightcoral" 
        if val < 1 else "" for val in data[column]
    ]

# Fetch data initially
df = fetch_data()

# Display data
st.write("### Spread Data with Gain/Trade (%)")
if not df.empty:
    # Apply highlights
    styled_df = df.style.apply(highlight_gain, column="Gain/Trade (%)", subset=["Gain/Trade (%)"])
   
