from django.shortcuts import render
from django.http import HttpResponse
from.models import *
# Create your views here.
def index(request):
  content = Post.objects.all()
  context= { 'content': content }
  return render(request,'index.html',context)

