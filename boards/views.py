from django.shortcuts import render

from .models import Board
# Create your views here.

def BoardListView(request):
    board = Board.objects.all()
    return render(request,"board_list.html",{"board":board})

def BoardDetailView(request):
    pass

def RelatedBoardListView(request):
    pass