from rest_framework import routers

from apps.profile import views

router = routers.DefaultRouter()
router.register(
    r'profile',
    views.ProfileView,
    base_name=views.ProfileView.name
)

urlpatterns = [

]

urlpatterns += router.urls
