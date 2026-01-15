import requests

# Code Testing the Currency API, plus practice with error handling and backup URLs

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

try:
    data = fetch_data("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json")
except Exception as e:
    print(e)
    try:
        print("Primary source failed, Trying backup...")
        data = fetch_data("https://latest.currency-api.pages.dev/v1/currencies/usd.json")
    except Exception as e:
        print(e)
        exit(1)
    

pkr_rate = data['usd']['pkr']
print(f"USD/PKR rate: 1/{pkr_rate}, as of {data['date']}") # USD/PKR rate: 1/280.27388674, as of 2026-01-14
