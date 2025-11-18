from django.contrib import admin
from django.urls import path, include  # <-- Make sure to import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Send all traffic to the salesapp's URLs
    path('', include('salesapp.urls')),
]