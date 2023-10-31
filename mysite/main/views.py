from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(response, id ):
	l = len(str(id))
	som = 0
	while id:
		

		r = id % 10

		som += r
		id  = id // 10

	if som % l == 0: 	
		return HttpResponse("<h1>Deze siteswap bestaat</h1>" )
	else: 
		return HttpResponse("<h1>Deze siteswap bestaat niet </h1>" )


