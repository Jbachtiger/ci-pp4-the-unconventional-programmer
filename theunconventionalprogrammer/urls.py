from django.contrib import admin
from django.urls import path, include
from profiles import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('programmerblog.urls')),
    path('accounts/', include('allauth.urls')),
    path('profile/', user_views.profile, name='profile'),
]
