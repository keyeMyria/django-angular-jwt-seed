from rest_framework import routers

from profile_module import views

router = routers.DefaultRouter()
router.register(
    r'profile',
    views.ProfileSet,
    base_name=views.ProfileSet.name
)
urlpatterns = [

]

urlpatterns += router.urls
