from django.urls import path, include
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")
router.register("groups", GroupViewSet, basename="groups")
router.register(r"^posts/(?P<post_id>\d+)/comments",
                CommentViewSet, basename="comment")

urlpatterns = [
    path("v1/api-token-auth/", views.obtain_auth_token),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("v1/", include(router.urls)),
]
