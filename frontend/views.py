from django.shortcuts import render, redirect
from django.contrib import messages
from .models import InvitationCode

# Create your views here.
# def eternalvows(request):
#     return render(request, 'frontend/eternalvows.html')

# def index(request):
#     return render(request, 'frontend/index.html')

def index(request):
    if request.session.get('has_access'):
        # User already has access, redirect to wedding page
        return redirect('wedding_details')
        
    if request.method == 'POST':
        code = request.POST.get('invitation_code', '').strip().upper()
        
        try:
            # Try to find the code in the database
            invitation = InvitationCode.objects.get(code=code, is_active=True)
            
            # Code is valid, set session variable and redirect
            request.session['has_access'] = True
            request.session['invitation_code'] = code
            
            return redirect('eternalvows')
            
        except InvitationCode.DoesNotExist:
            # Invalid code
            messages.error(request, "Código inválido. Por favor, intenta nuevamente.")
    
    return render(request, 'frontend/index.html')

def eternalvows(request):
    if not request.session.get('has_access'):
        # User doesn't have access, redirect to landing page
        return redirect('index')
        
    return render(request, 'frontend/eternalvows.html')

def logout(request):
    if 'has_access' in request.session:
        del request.session['has_access']
    if 'invitation_code' in request.session: 
        del request.session['invitation_code']
    
    return redirect('index')