import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import time
import random

# Streamlit App Title
st.title("Stock Spread Analysis")

# Tickers List (example, you can add your full list of tickers)
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

# Fetch data with delay and retry logic
def fetch_data():
    spread_data = []
    batch_size = 50  # Smaller batch size to avoid overloading the server
    retries = 3  # Number of retry attempts if 429 error occurs
    for i in range(0, len(tickers), batch_size):
        batch = tickers[i:i + batch_size]
        for ticker in batch:
            for attempt in range(retries):
                try:
                    stock = yf.Ticker(ticker)
                    data = stock.info
                    bid, ask = data.get("bid"), data.get("ask")

                    if bid and ask:
                        spread = ask - bid
                        tick = calculate_tick(bid)
                        real_spread = spread - (tick * 2)
                        spread_percent = (real_spread / bid) * 100 if bid > 0 else 0
                        gain_trade = (real_spread / bid) * 100 if bid > 0 else 0

                        spread_data.append({
                            "Ticker": ticker, 
                            "Bid": bid, 
                            "Ask": ask, 
                            "Spread": spread, 
                            "Real Spread": real_spread, 
                            "Spread (%)": spread_percent,
                            "Gain/Trade (%)": gain_trade
                        })

                    # Random delay between requests to avoid rate-limiting
                    time.sleep(random.uniform(3, 5))  # Random delay between 3 and 5 seconds
                    break  # Exit retry loop if successful
                except Exception as e:
                    print(f"Error fetching data for {ticker} (Attempt {attempt + 1}): {e}")
                    if attempt < retries - 1:
                        # Wait for a longer period before retrying
                        time.sleep(random.uniform(10, 20))  # Increase sleep for retry attempts
                    else:
                        print(f"Failed to fetch data for {ticker} after {retries} attempts.")
                
        # Sleep for a longer period after each batch to be more cautious
        time.sleep(random.uniform(10, 20))  # Longer delay between batches

    return pd.DataFrame(spread_data)

# Fetch data initially
df = fetch_data()

# Display data
st.write("### Spread Data with Gain/Trade (%)")
st.dataframe(df)

# Top 3 by Gain/Trade (%)
st.write("### Top 3 Stocks by Gain/Trade (%)")
st.table(df.nlargest(5, "Gain/Trade (%)"))

# Visualization
if not df.empty:
    st.write("### Gain/Trade (%) Visualization")
    fig, ax = plt.subplots()
    df.dropna().plot.bar(x="Ticker", y="Gain/Trade (%)", ax=ax, color="blue", legend=False)
    plt.title("Gain/Trade (%) per Ticker")
    plt.xlabel("Ticker")
    plt.ylabel("Gain/Trade (%)")
    st.pyplot(fig)

# Refresh button
if st.button("Refresh Data"):
    df = fetch_data()
    st.dataframe(df)
