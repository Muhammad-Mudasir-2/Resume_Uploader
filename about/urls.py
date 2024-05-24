from .views import ProfileView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from about import views

urlpatterns = [
    path('resume/', views.ProfileView.as_view(), name='resume'),
    path('list/', views.ProfileView.as_view(), name='list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
