from django.urls import path
from rest_framework import routers
from linkkeep.api.views import LinkDataReadCreate

app_name = "api"


router = routers.SimpleRouter()
router.register(r'linkdata',LinkDataReadCreate,basename="linkdata")

urlpatterns = router.urls