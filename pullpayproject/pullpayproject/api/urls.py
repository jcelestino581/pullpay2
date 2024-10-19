from rest_framework.routers import DefaultRouter
from churches.api.urls import user_router
from django.urls import path, include

router = DefaultRouter()
#Users
router.registry.extend(user_router.registry)

urlpatterns = [
    path('', include(router.urls))
]

#Churches