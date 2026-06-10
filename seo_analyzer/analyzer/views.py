import requests
import time
from bs4 import BeautifulSoup
from django.shortcuts import render
from urllib.parse import urlparse

def analyze_seo(request):
    result = None
    error = None

    if request.method == "POST":
        url = request.POST.get('url')
        if not url:
            error = "لطفاً یک آدرس معتبر وارد کنید."
        else:
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url

            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
            
            try:
                # محاسبه زمان لود
                start_time = time.time()
                response = requests.get(url, headers=headers, timeout=15)
                end_time = time.time()
                load_speed = round(end_time - start_time, 2)

                soup = BeautifulSoup(response.text, 'html.parser')
                domain = urlparse(url).netloc

                # استخراج اطلاعات
                title = soup.title.string.strip() if soup.title else "بدون عنوان"
                meta_desc = soup.find('meta', attrs={'name': 'description'})
                meta_description = meta_desc.get('content', '').strip() if meta_desc else "بدون توضیحات متا"
                
                h1_tags = soup.find_all('h1')
                h2_tags = soup.find_all('h2')
                
                images = soup.find_all('img')
                images_without_alt = sum(1 for img in images if not img.get('alt'))

                # تحلیل لینک‌ها
                all_links = soup.find_all('a', href=True)
                internal_links = 0
                external_links = 0
                for link in all_links:
                    href = link['href']
                    if domain in href or href.startswith('/'):
                        internal_links += 1
                    else:
                        external_links += 1

                # تعداد کلمات
                words = soup.get_text().split()
                word_count = len(words)

                # بررسی Robots و Sitemap (تقریبی)
                base_url = f"{urlparse(url).scheme}://{domain}"
                has_robots = requests.get(f"{base_url}/robots.txt", timeout=5).status_code == 200
                has_sitemap = requests.get(f"{base_url}/sitemap.xml", timeout=5).status_code == 200

                # نمره‌دهی پیشرفته
                score = 0
                recs = []
                
                if 30 <= len(title) <= 60: score += 20
                else: recs.append("طول عنوان باید بین 30 تا 60 کاراکتر باشد.")

                if 120 <= len(meta_description) <= 160: score += 20
                else: recs.append("طول توضیحات متا باید بین 120 تا 160 کاراکتر باشد.")

                if len(h1_tags) == 1: score += 20
                else: recs.append("هر صفحه باید دقیقاً یک تگ H1 داشته باشد.")

                if load_speed < 2: score += 20
                else: recs.append("سرعت لود سایت پایین است. حجم تصاویر را کم کنید.")

                if word_count > 300: score += 20
                else: recs.append("تعداد کلمات صفحه کم است (حداقل 300 کلمه توصیه می‌شود).")

                result = {
                    "seo_score": score,
                    "load_speed": load_speed,
                    "word_count": word_count,
                    "internal_links": internal_links,
                    "external_links": external_links,
                    "has_robots": "دارد" if has_robots else "ندارد",
                    "has_sitemap": "دارد" if has_sitemap else "ندارد",
                    "recommendations": recs,
                    "details": {
                        "title": title,
                        "meta_description": meta_description,
                        "h1_count": len(h1_tags),
                        "h2_count": len(h2_tags),
                        "images_total": len(images),
                        "images_without_alt": images_without_alt,
                    }
                }
            except Exception as e:
                error = f"خطا در تحلیل: {str(e)}"

    return render(request, 'analyzer/index.html', {'result': result, 'error': error})
