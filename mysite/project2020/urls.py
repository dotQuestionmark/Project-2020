from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('project2020/', include('project2020.urls')),
    path('admin/', admin.site.urls),
]
