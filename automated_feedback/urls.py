
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
urlpatterns = [
    path('health', lambda request : HttpResponse('okay')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/', include('feedbackapp.api.urls'), name='api_url'),   
]
