from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Django Allauth URLs
    path('', include('mainApp.urls')),  # Main app URLs

]
