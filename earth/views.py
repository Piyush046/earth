from django.shortcuts import render
from django.http import HttpResponse

def home(request):
 
 r=  """<div style="width: 200px; height: 100px; background-color: #27ae60; color: #fff; text-align: center; line-height: 100px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
    Hello, piyush!
  </div>"""
  
 return HttpResponse(r)