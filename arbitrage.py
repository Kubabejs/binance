import ccxt

def get_btc_spread():
    # Initialize exchanges
    binance = ccxt.binance()
    kraken = ccxt.kraken()

    # Fetch BTC prices
    btc_binance = binance.fetch_ticker('BTC/USDT')['last']
    btc_kraken = kraken.fetch_ticker('BTC/USD')['last']

    # Calculate spread
    spread = btc_kraken - btc_binance
    print(f"Spread: {spread:.2f} USD")
    return spread

# Run the function
if __name__ == "__main__":
    get_btc_spread()

# Fetch ticker data
btc_ticker = binance.fetch_ticker('BTC/USDT')
print(btc_ticker)


# Check if 'coinbasepro' is a valid attribute
print(hasattr(ccxt, 'coinbasepro'))  # Should print True if the class exists

# If False, try 'coinbase' instead:
# coinbase = ccxt.coinbase()

# In your get_btc_spread function:
def get_btc_spread():
    # Inicializace burz
    binance = ccxt.binance()
    # Changed coinbase to coinbasepro to match the class name in the ccxt library.
    # If 'coinbasepro' is not a valid attribute, try 'coinbase' instead
    # Use 'coinbase' instead of 'coinbasepro'
    coinbase = ccxt.coinbase() 

    # ... rest of your code ...

    # Nainstalujte ccxt (pokud už není nainstalováno)
    # This line is redundant as ccxt is already installed at the beginning
    #!pip install ccxt -q  

# Importujte knihovnu
# This line is redundant as ccxt is already imported at the beginning
#import ccxt

# Funkce pro výpočet spreadu
#def get_btc_spread():  # This function is already defined above
    # Inicializace burz
    #binance = ccxt.binance() # This is already defined above
    #coinbase = ccxt.coinbasepro()  # Správný název burzy # This line is causing the error

    # Získání cen
    btc_binance = binance.fetch_ticker('BTC/USDT')['last']
    btc_coinbase = coinbase.fetch_ticker('BTC/USD')['last'] * 23  # Převod na CZK

    # Výpočet spreadu
    spread = btc_coinbase - btc_binance
    return spread

# Zavolejte funkci a zobrazte výsledek
print(f"Aktuální spread BTC: {get_btc_spread():.2f} Kč")
