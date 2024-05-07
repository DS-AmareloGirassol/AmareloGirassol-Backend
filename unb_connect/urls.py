from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from subjects.urls import router as subjectRouter

router = DefaultRouter()

router.registry.extend(subjectRouter.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path(r'api/', include(router.urls)),
]