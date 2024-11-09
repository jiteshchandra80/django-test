from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

@login_required
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return render(request, 'thanks.html', {'name': name})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('contact')  # Redirect to a protected view or homepage
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})