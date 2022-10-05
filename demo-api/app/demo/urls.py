from django.urls import include, path
from rest_framework import routers
from demoapp import views

router = routers.DefaultRouter()
router.register(r"cat", views.CatViewSet)
router.register(r"dog", views.DogViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
