# 🔍 Django SEO Analyzer

یک ابزار تحلیل‌گر سئو (SEO Analyzer) قدرتمند و سریع که با فریم‌ورک جنگو ساخته شده است. این پروژه به صورت کاملاً عملیاتی روی سرورهای ابری مستقر شده است.

## 🌐 لینک پیش‌نمایش زنده (Live Demo)
شما می‌توانید نسخه آنلاین این پروژه را در آدرس زیر مشاهده کنید:
👉 **[https://seo-analyzer-django-production.up.railway.app/](https://seo-analyzer-django-production.up.railway.app/api/analyze)**

برخی وب‌سایت‌ها ممکن است به دلیل تنظیمات امنیتی یا محدودیت‌های شبکه، از سمت محیط ابری قابل تحلیل نباشند.


---

## 🚀 ویژگی‌ها (Features)
- **تحلیل تگ‌های متا:** بررسی دقیق Title، Meta Description و سلسله مراتب تگ‌های H1.
- **بررسی تصاویر:** شناسایی تصاویر فاقد تگ `alt` برای بهبود دسترسی‌پذیری.
- **آنالیز لینک‌ها:** شمارش و تفکیک لینک‌های داخلی (Internal) و خارجی (External).
- **بررسی فایل‌های فنی:** چک کردن خودکار وضعیت `robots.txt` و `sitemap.xml`.
- **تخمین سرعت:** محاسبه زمان پاسخگویی سرور (Load Speed).
- **سیستم امتیازدهی:** ارائه نمره نهایی (SEO Score) و لیست پیشنهادات هوشمند.
- **رابط کاربری مدرن:** طراحی واکنش‌گرا (Responsive) با استفاده از Bootstrap 5.

## 🛠 تکنولوژی‌ها
- **Backend:** Django 5.x
- **Parsing:** BeautifulSoup4 & Requests
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Deployment:** Railway (Gunicorn)

## 📡 استفاده از API
این پروژه دارای یک Endpoint اختصاصی برای تحلیل است. برای ارسال درخواست از طریق کد یا ابزارهایی مثل Postman:

- **URL:** `https://seo-analyzer-django-production.up.railway.app/api/analyze/`
- **Method:** `POST`
- **Body (JSON):**
```json
  {
"url": "https://example.com"
  }
  
