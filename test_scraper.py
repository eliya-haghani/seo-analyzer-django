import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def analyze_url(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        parsed_url = urlparse(url)
        domain = parsed_url.netloc

        # ===== Basic SEO Data =====
        title = soup.title.string.strip() if soup.title else "No title found"

        meta_desc_tag = soup.find("meta", attrs={"name": "description"})
        meta_desc = meta_desc_tag["content"].strip() if meta_desc_tag else "No meta description"

        h1_tag = soup.find("h1")
        h1 = h1_tag.get_text(strip=True) if h1_tag else "No H1 found"

        h2_tags = [h.get_text(strip=True) for h in soup.find_all("h2")]

        images = soup.find_all("img")
        images_without_alt = [img for img in images if not img.get("alt")]

        # ===== Link Analysis =====
        internal_links = []
        external_links = []

        for link in soup.find_all("a", href=True):
            href = link["href"]

            # تبدیل لینک‌های نسبی به کامل
            full_url = urljoin(url, href)
            parsed_link = urlparse(full_url)

            if parsed_link.netloc == domain:
                internal_links.append(full_url)
            elif parsed_link.netloc != "":
                external_links.append(full_url)

        print("\n===== SEO ANALYSIS =====")
        print("URL:", url)
        print("Title:", title)
        print("Meta Description:", meta_desc)
        print("H1:", h1)
        print("Number of H2:", len(h2_tags))

        print("\nImages:", len(images))
        print("Images without alt:", len(images_without_alt))

        print("\nTotal Links:", len(internal_links) + len(external_links))
        print("Internal Links:", len(internal_links))
        print("External Links:", len(external_links))

    except Exception as e:
        print("Error:", e)


url = input("Enter a website URL: ")
analyze_url(url)
