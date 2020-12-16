from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from faq.api.views import FaqViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("faq", FaqViewSet)

app_name = "api"
urlpatterns = router.urls