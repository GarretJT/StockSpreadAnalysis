# Function to determine tick size
def get_tick(price):
    if price < 200:
        return 1
    elif 200 <= price <= 500:
        return 2
    elif 500 < price <= 2000:
        return 5
    elif 2000 < price <= 5000:
        return 10
    else:  # price > 5000
        return 25

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
            tick = get_tick(bid)  # Determine tick size based on bid price
            real_spread = spread - (tick * 2)  # Calculate real spread
            spread_percent = (real_spread / bid) * 100 if bid > 0 else 0
            
            # Fetch historical data for frequency and volume details (1-day interval)
            hist_data = stock.history(period="1d", interval="1d")  # Last 7 days of data
            
            # Check if hist_data is empty or has missing values
            if not hist_data.empty:
                hist_volume = hist_data['Volume'].iloc[0]  # Latest volume data
                frequency = len(hist_data)  # Frequency based on number of days with data in the last 7 days
            else:
                hist_volume = 0
                frequency = 0
            
            spread_data.append({
                "Ticker": ticker, "Bid": bid, "Ask": ask, "Spread": spread,
                "Real Spread": real_spread, "Spread (%)": spread_percent,
                "Volume": hist_volume, "Frequency": frequency
            })
    
    # Create DataFrame
    df = pd.DataFrame(spread_data)
    return df
