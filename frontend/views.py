from django.shortcuts import render

# Create your views here.
def eternalvows(request):
    #return render(request, 'eternalvows.html')
    return render(request, 'frontend/eternalvows.html')

def home(request):
    return render(request, 'frontend/eternalvows.html')