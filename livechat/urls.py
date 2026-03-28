from django.urls import path
from .views import index,Get,Create,game
urlpatterns = [
    path('',index, name="test_home" ),
    path("get/", Get.as_view(), name="api_view"),
    path("create/", Create.as_view(), name="api_viewc"),
    path("game/",game, name="game")

]