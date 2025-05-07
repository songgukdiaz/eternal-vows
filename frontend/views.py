from django.shortcuts import render, redirect
from django.contrib import messages
from .models import InvitationCode

# Create your views here.
# def eternalvows(request):
#     return render(request, 'frontend/eternalvows.html')

# def index(request):
#     return render(request, 'frontend/index.html')

def index(request):
    return render(request, 'frontend/index.html')

def eternalvows(request):
    if not request.session.get('has_access'):
        print("User doesn't have access")
        messages.error(request, "The code you entered is invalid. Please try again.")
        return redirect('index')
        
    print("User has access")
    return render(request, 'frontend/eternalvows.html')

def logout(request):
    if 'has_access' in request.session:
        del request.session['has_access']
    if 'invitation_code' in request.session: 
        del request.session['invitation_code']
    
    return redirect('index')