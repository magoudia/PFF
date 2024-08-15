from django.shortcuts import render

# Create your views here.
def home(request,*args,**kwargs):
    """Renders the home page."""
    return render(request,'shop.html')