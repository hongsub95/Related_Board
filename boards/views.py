
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import FormView

from .models import Board
from .forms import BoardCreateForm
from .services import FindRelatedBoard
# Create your views here.

def BoardListView(request):
    boards = Board.objects.all()
    return render(request,"board/board_list.html",{"boards":boards})

def BoardCreateView(request):
    if request.method == "POST":
        form = BoardCreateForm(request.POST)
        if form.is_valid():
            board = Board()
            board.title = form.cleaned_data["title"]
            board.content = form.cleaned_data["content"]
            board.save()
            return redirect("board:board_list",board.pk)
    else:
        form = BoardCreateForm()
        return render(request,"board/board_create.html",{"form":form})
        

def BoardDetailView(request,id):
    board = Board.objects.filter(id=id).first()
    related_boards = FindRelatedBoard(id)
    return render(request,"board/board_detail.html",{"board":board,"related_boards":related_boards})