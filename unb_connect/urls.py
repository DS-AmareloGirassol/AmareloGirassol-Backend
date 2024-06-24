from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from persons.authentications import Authentication, Logout

from persons.urls import router as person_router
from posts.urls import router as post_router

router = DefaultRouter()

router.registry.extend(person_router.registry)
router.registry.extend(post_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/token/', Authentication.as_view()),
    path('api/token/logout/', Logout.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path(r'api/', include(router.urls)),
]
