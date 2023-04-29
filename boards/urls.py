from django.urls import path,include
from . import views

app_name = "board"
urlpatterns = [
    path("",views.BoardListView,name="board_list"),
    path("<int:board_id>",views.BoardDetailView,name="board_detail")
]
