from django.urls import path

from pages.views import HomeTemplateView, AboutTemplateView, ContactCreateView

app_name = 'pages'

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('', HomeTemplateView.as_view(), name='home'),
]
