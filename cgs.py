import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("Stock Spread Analysis")

# Tickers List
tickers = [
    "CBUT", "RSGK", "TCID", "TRST", "ASBI", "MTLA", "ASRM", "SURE", "IDPR", "APII", 
    "PGLI", "ASJT", "BSIM", "LCKM", "MASB", "ALKA", "TIRA", "BBLD", "INPP", "INRU", 
    "RELI", "TGKA", "BBMD", "BBSI", "LIFE", "SMMA", "DUTI", "IPAC", "NICK", "APLI", 
    "ATIC", "SHIP", "DCII", "MEGA", "YULE", "PTSP", "TRUS", "SAPX", "DAYA", "SKBM", 
    "EDGE", "MERK", "TBMS", "RANC", "HDFA", "GHON", "SOTS", "BINA", "LINK", "PURI", 
    "IFSH", "SIPD", "HERO", "GEMA", "KEJU", "PNGO", "GLVA", "INDR", "BPFI", "BRAM", 
    "SDRA", "ARGO", "MORA", "ALDO", "INTD", "POLU", "BINO", "MMLP", "LPLI", "BALI", 
    "BOGA", "BUKK", "AMIN", "GMTD", "SHID", "BTON", "MPRO", "TALF", "CSAP", "TRUK", 
    "JECC", "FUJI", "IKBI", "MICE", "BPII", "MGLV", "SGRO", "TRIS", "PEHA", "AMOR", 
    "BMSR", "SKBM", "CASH", "BMHS", "SHIP", "CEKA", "BABY", "CINT", "SAFE", "GOLD", 
    "LFLO", "BESS", "GDYR", "PDES", "IMJS", "ASDM", "OILS", "INCI", "SMMA"
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
            gain_trade = (real_spread / bid) * 100 if bid > 0 else None  # Gain per Trade (%)
            
            spread_data.append({
                "Ticker": ticker, 
                "Bid": bid, 
                "Ask": ask, 
                "Spread": spread, 
                "Real Spread": real_spread, 
                "Gain/Trade (%)": gain_trade
            })
    return pd.DataFrame(spread_data)

# Fetch data initially
df = fetch_data()

# Display data
st.write("### Spread Data with Gain per Trade (%)")
st.dataframe(df)

# Top 3 by Gain per Trade (%)
st.write("### Top 5 Stocks by Gain per Trade (%)")
st.table(df.nlargest(5, "Gain/Trade (%)"))

# Visualization
if not df.empty:
    st.write("### Gain per Trade (%) Visualization")
    fig, ax = plt.subplots()
    df.dropna().plot.bar(x="Ticker", y="Gain/Trade (%)", ax=ax, color="blue", legend=False)
    plt.title("Gain per Trade (%) per Ticker")
    plt.xlabel("Ticker")
    plt.ylabel("Gain per Trade (%)")
    st.pyplot(fig)

# Refresh button
if st.button("Refresh Data"):
    df = fetch_data()
    st.dataframe(df)
