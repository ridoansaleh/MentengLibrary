from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Visitor, Book
from .forms import SignUpForm

def home(request):
    data = Book.objects.all()
    context = {'data': data}
    return render(request, 'signup/base.html', context)

def detail(request, id):
    book = Book.objects.get(id=id)
    context = {'book': book}
    return render(request, 'signup/detail.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the visitor instance created by the signal
            user.visitor.gender = form.cleaned_data.get('gender')
            user.visitor.address = form.cleaned_data.get('address')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup/registration.html', {'form': form})

def profile(request):
    return render(request, 'signup/profile.html', {})
