from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def index(response, name):
	ls = ToDoList.objects.get(name=name)
	item = ls.item_set.get(id=1)
	return render(response, "'main'/home.html", {"name":ls.name})

def home(response):
	return render(response, "'main'/home.html", {"name": "E"})


def create(response):
	if response.method == "POST":
		form = CreateNewList(response.POST)

		if form.is_vaild():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()

		return HttpResponseRedirect("/%i" %t.id)
	else:
		form = CreateNewList()

	return render(response, "'main'/create.html", {"form":form})