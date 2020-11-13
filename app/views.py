from django.shortcuts import render

# Create your views here.

def temp(request):
    return render(request,'first.html')



#render(request,'html file path along with extension')