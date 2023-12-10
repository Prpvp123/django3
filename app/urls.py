from django.urls import path, include
from . import views


product_urls = [
    path('product', views.product, name='product_page'),
    path('card', views.card, name='card_page'),
    path('order', views.order, name='order_page'),
]

urlpatterns = [
    path('', views.main, name='main_page'),
    path('news', views.news, name='news_page'),
    path('shop/<int:pk>/', include(product_urls)),
    path('faq', views.faq, name='faq_page'),
]