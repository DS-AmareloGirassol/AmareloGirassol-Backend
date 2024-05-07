from rest_framework.routers import DefaultRouter
from subjects import views

router = DefaultRouter()

router.register(r'subject', views.SubjectViewSet)