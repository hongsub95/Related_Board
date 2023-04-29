from django.shortcuts import render

from .models import Board
from .services import FindRelatedBoard
# Create your views here.

def BoardListView(request):
    boards = Board.objects.all()
    return render(request,"board_list.html",{"boards":boards})

def BoardDetailView(request,id):
    board = Board.objects.filter(id=id).first()
    related_boards = FindRelatedBoard(id)
    return render(request,"board_detail.html",{"board":board,"related_boards":related_boards})

