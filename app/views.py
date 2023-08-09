from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from app.models import *
class schoollist(ListView):
    model=School
    context_object_name='allso'

class schoolDetail(DetailView):
    model=School
    context_object_name='DOSI'

class schoolcreate(CreateView):
    model=School
    fields='__all__'

class schoolupdate(UpdateView):
    model=School
    fields='__all__'