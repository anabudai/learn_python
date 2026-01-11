import requests

news_api_token="9c8d08d51e63436da7a820e72786a9f0"

query = "artificial intelligence"
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-12-11&sortBy=publishedAt&apiKey={news_api_token}"

print(f"url={url}")

response = requests.get(url)

print(f"responseCode={response.status_code}")
print("===========================================================")
articles = response.json()["articles"]

for article in articles:
    print(f"author={article["author"]}")
    print(f"title={article["title"]}")
    print(f"url={article["url"]}")
    print("")




