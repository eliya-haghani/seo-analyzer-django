from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('analyzer.urls')), # این خط آدرس‌های اپلیکیشن تو را وصل می‌کند
]
