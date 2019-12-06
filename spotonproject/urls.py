"""spotonproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views, apis

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #path('app/', include('store.store_urls'))

    # API urls
    path('api/producers', apis.get_producers),
    path('api/producers/<producer_id>', apis.get_producer),
    path('api/products', apis.get_products),
    path('api/products/<product_id>', apis.get_product),
    path('api/orders', apis.get_orders),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
