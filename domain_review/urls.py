from django.contrib import admin
from django.urls import path
from reviews import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('domain/<int:domain_id>/', views.domain_detail, name='domain_detail'),
]
