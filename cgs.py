import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("Stock Spread Analysis")

# Updated Input Tickers (Adding new tickers and removing duplicates)
tickers = [
    "CBUT.JK", "RSGK.JK", "TCID.JK", "TRST.JK", "ASBI.JK", "MTLA.JK", "ASRM.JK",
    "SURE.JK", "IDPR.JK", "APII.JK", "PGLI.JK", "ASJT.JK", "BSIM.JK", "LCKM.JK",
    "MASB.JK", "ALKA.JK", "TIRA.JK", "BBLD.JK", "INPP.JK", "INRU.JK", "RELI.JK",
    "TGKA.JK", "BBMD.JK", "BBSI.JK", "LIFE.JK", "SMMA.JK", "DUTI.JK", "IPAC.JK", "NICK.JK",
    "APLI.JK", "ATIC.JK", "SHIP.JK", "DCII.JK", "MEGA.JK", "YULE.JK", "PTSP.JK", "TRUS.JK", "SAPX.JK", "DAYA.JK"
]

# Remove duplicates (if any)
tickers = list(set(tickers))

# Function to fetch and calculate spreads, volume, and frequency
def fetch_data():
    spread_data = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data = stock.info
        bid, ask = data.get("bid"), data.get("ask")
        volume = data.get("regularMarketVolume")  # Get volume from stock info
        
        if bid and ask:
            spread = ask - bid
            spread_percent = (spread / bid) * 100 if bid > 0 else 0
            
            # Fetch historical data for frequency and volume details (1-day interval)
            hist_data = stock.history(period="7d", interval="1d")  # Last 7 days of data
            
            # Check if hist_data is empty or has missing values
            if not hist_data.empty:
                hist_volume = hist_data['Volume'].iloc[0]  # Latest volume data
                frequency = len(hist_data)  # Frequency based on number of days with data in the last 7 days
            else:
                hist_volume = 0
                frequency = 0
            
            spread_data.append({
                "Ticker": ticker, "Bid": bid, "Ask": ask, "Spread": spread, "Spread (%)": spread_percent,
                "Volume": hist_volume, "Frequency": frequency
            })
    
    # Create DataFrame
    df = pd.DataFrame(spread_data)
    return df

# Fetch data initially when the app is first launched
df = fetch_data()

# Display Table
st.write("### Spread Data")
st.dataframe(df)

# Top 3 Spreads by Percentage (using "Spread (%)" column)
st.write("### Top 3 Stocks with Highest Percentage Spread")
top_spreads = df.nlargest(5, "Spread (%)")  # Sorting by "Spread (%)" instead of raw "Spread"
st.table(top_spreads)

# Full Spread Data Sorted by Spread
st.write("### All Stocks Sorted by Spread (Descending)")
sorted_df = df.sort_values(by="Spread", ascending=False)
st.dataframe(sorted_df)

# Visualization
if not df.empty:
    st.write("### Spread Visualization")
    fig, ax = plt.subplots()
    sorted_df.plot.bar(x="Ticker", y="Spread (%)", ax=ax, color="orange", legend=False)
    plt.title("Spread (%) per Ticker")
    plt.xlabel("Ticker")
    plt.ylabel("Spread (%)")
    st.pyplot(fig)

# Visualization for Volume
if not df.empty:
    st.write("### Volume Visualization")
    fig, ax = plt.subplots()
    sorted_df.plot.bar(x="Ticker", y="Volume", ax=ax, color="green", legend=False)
    plt.title("Volume per Ticker")
    plt.xlabel("Ticker")
    plt.ylabel("Volume")
    st.pyplot(fig)

# Visualization for Frequency
if not df.empty:
    st.write("### Frequency Visualization")
    fig, ax = plt.subplots()
    sorted_df.plot.bar(x="Ticker", y="Frequency", ax=ax, color="blue", legend=False)
    plt.title("Frequency per Ticker")
    plt.xlabel("Ticker")
    plt.ylabel("Frequency")
    st.pyplot(fig)

# Refresh Button to fetch new data
if st.button('Refresh Data'):
    df = fetch_data()  # Fetch new data
    st.write("### Updated Spread Data")
    st.dataframe(df)
    st.write("### Top 3 Stocks with Highest Spread (Updated)")
    top_spreads = df.nlargest(3, "Spread (%)")
    st.table(top_spreads)
    st.write("### All Stocks Sorted by Spread (Descending)")
    sorted_df = df.sort_values(by="Spread", ascending=False)
    st.dataframe(sorted_df)
    st.write("### Updated Visualizations")
    # Visualization for Spread
    fig, ax = plt.subplots()
    sorted_df.plot.bar(x="Ticker", y="Spread (%)", ax=ax, color="orange", legend=False)
    plt.title("Spread (%) per Ticker (Updated)")
    plt.xlabel("Ticker")
    plt.ylabel("Spread (%)")
    st.pyplot(fig)

    # Visualization for Volume
    fig, ax = plt.subplots()
    sorted_df.plot.bar(x="Ticker", y="Volume", ax=ax, color="green", legend=False)
    plt.title("Volume per Ticker (Updated)")
    plt.xlabel("Ticker")
    plt.ylabel("Volume")
    st.pyplot(fig)

    # Visualization for Frequency
    fig, ax = plt.subplots()
    sorted_df.plot.bar(x="Ticker", y="Frequency", ax=ax, color="blue", legend=False)
    plt.title("Frequency per Ticker (Updated)")
    plt.xlabel("Ticker")
    plt.ylabel("Frequency")
    st.pyplot(fig)

st.write("Analysis Complete!")
