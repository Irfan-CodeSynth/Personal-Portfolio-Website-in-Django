# views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse

def home(request):
    return render(request, "index.html")

def sendmail(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        full_message = f"Message from {name} ({email}):\n\n{message}"
        
        # Ensure email is valid
        if email and '@' in email:
            try:
                send_mail(
                    subject,  # Subject
                    full_message,  # Message
                    settings.EMAIL_HOST_USER,  # From email
                    [email],  # To email
                    fail_silently=False,
                )
                messages.success(request, "Email sent successfully!")
            except BadHeaderError:
                messages.error(request, "Invalid header found.")
            except Exception as e:
                messages.error(request, f"Error sending email: {str(e)}")
        else:
            messages.error(request, "Invalid email address.")
        
        return redirect('home')
    else:
        return HttpResponse(status=405)
