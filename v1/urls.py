from django.urls import path
from .views import *
from rest_framework import routers

# URL Patterns for the API
urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='Upload File'),
]

router = routers.DefaultRouter() # Created a default router to handle the modelviewset apis
router.register('data', OutputDataViewSet, 'data')

urlpatterns += router.urls