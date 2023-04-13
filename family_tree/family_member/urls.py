from rest_framework.routers import DefaultRouter
from .views import  MemberViewset


member_router = DefaultRouter()
member_router.register("", MemberViewset , basename= "member_register")
urlpatterns = member_router.urls