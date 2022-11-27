from django.shortcuts import render, redirect
from .models import BankAccount
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm


# Create your views here.
def transfer_funds(request):
    if request.method == "POST":
        account_number = request.POST['account_number']
        amount = float(request.POST['amount'])
        sender = BankAccount.objects.get(user=request.user.id)
        receiver = BankAccount.objects.get(account_number=account_number)
        if sender.balance > 0:
            sender.balance = sender.balance - amount
            receiver.balance = receiver.balance + amount
            sender.save()
            receiver.save()
            return redirect('dashboard')
    if request.method == "GET":
        return render(request, 'transfer_page.html')


def dashboard(request):
    context = {}
    account_detail = BankAccount.objects.get(user=request.user.id)
    print(account_detail.image.url)
    context['account_detail'] = account_detail
    return render(request, 'dashboard.html', context)


def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pwd']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if not BankAccount.objects.filter(user=user.id).exists():
                account_number = BankAccount.objects.create(user=user)
                account_number.save()
            return redirect("dashboard")
        else:
            return redirect(request.path)
    return render(request, 'sign_in.html')


def user_logout(request):
    logout(request)
    return redirect('sign_in')


def register(request):
    context = {}
    if request.method == "GET":
        form = RegistrationForm()
        context['form'] = form
        return render(request, 'register.html', context)
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
        else:
            return redirect(request.path)
