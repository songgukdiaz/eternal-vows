from django.shortcuts import render, redirect
from django.contrib import messages
from .models import InvitationCode

# Create your views here.
# def eternalvows(request):
#     return render(request, 'frontend/eternalvows.html')

# def index(request):
#     return render(request, 'frontend/index.html')

def index(request):
    # Check if the user submitted a code (POST request)
    if request.method == 'POST':
        code = request.POST.get('invitationCode', '').strip().upper()  # Match the name in your HTML form

        try:
            # Try to find the code in the database
            invitation = InvitationCode.objects.get(code=code, is_active=True)

            # Code is valid, set session variable and redirect
            request.session['has_access'] = True
            request.session['invitation_code'] = code

            # Redirect to the protected page
            return redirect('eternalvows')

        except InvitationCode.DoesNotExist:
            # Invalid code
            messages.error(request, "Código inválido. Por favor, intenta nuevamente.")

    # Display the index page (either initially or after failed validation)
    return render(request, 'frontend/index.html')

def eternalvows(request):
    # Check if user has access first
    if not request.session.get('has_access'):
        # User doesn't have access, redirect to landing page
        messages.error(request, "Por favor, ingresa el código de invitación que recibiste para acceder a los detalles de nuestra boda.")
        return redirect('index')
    
    # User has access, show the protected page   
    messages.success(request, "¡Bienvenido a nuestra boda!")
    return render(request, 'frontend/eternalvows.html')

def logout(request):
    if 'has_access' in request.session:
        del request.session['has_access']
    if 'invitation_code' in request.session: 
        del request.session['invitation_code']
    
    return redirect('index')