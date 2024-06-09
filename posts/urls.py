from rest_framework.routers import DefaultRouter
from posts import views

router = DefaultRouter()

router.register(r'post', views.PostViewSet)