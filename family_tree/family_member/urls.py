from rest_framework.routers import DefaultRouter
from .views import  MemberRegisterViewset


member_router = DefaultRouter()
member_router.register("", MemberRegisterViewset , basename= "member_register")
urlpatterns = member_router.urls