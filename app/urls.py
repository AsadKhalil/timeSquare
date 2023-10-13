from django.urls import path
from . import views

urlpatterns = [
    # Add more paths as needed
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='services'),
    path('web-development/', views.web_development_view, name='web-development'),
    path('app-development/', views.app_development_view, name='app-development'),
    path('seo-services/', views.seo_services_view, name='seo-services'),
    path('ppc-management/', views.ppc_management_view, name='ppc-management'),
    path('social-media-marketing/', views.social_media_marketing_view, name='social-media-marketing'),
    path('content-marketing/', views.content_marketing_view, name='content-marketing'),
    path('cyber-security/', views.cyber_security_view, name='cyber-security'),
    path('careers/', views.careers_view, name='careers'),
    path('blog/', views.blog_view, name='blog'),
    path('contact/', views.contact_view, name='contact'),
    path('terms-condition/', views.terms_view, name='terms-condition'),
    path('privacy-policy/', views.privacy_view, name='privacy-policy'),
]
