from bs4 import BeautifulSoup
import requests
import time
import random

def scraper_bot():
    urls = ["https://en.wikipedia.org/wiki/Google"]
    visited_urls = set()

    while urls:
        current_url = urls.pop()
        print("time to crawl: " + current_url)
        time.sleep(random.uniform(1, 3))
        try:
            responce = requests.get(current_url)
            responce.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to retrieve {current_url}: {e}")
            continue

        webpage = BeautifulSoup(responce.content, "html.parser")

        hyperlinks = webpage.select("a[href]")

        for hyperlink in hyperlinks:
            url = hyperlink["href"]

            if url.startswith("#"):
                continue
            if url.startswith("//"):
                url = "https:" + url
            elif url.startswith("/"):
                base