from django.shortcuts import render
from .models import BankAccount


# Create your views here.
def sign_in(request):
    if request.method == "POST":
        account_number = request.POST['account_number']
        amount = float(request.POST['amount'])
        sender = BankAccount.objects.get(account_number="03082219027")
        receiver = BankAccount.objects.get(account_number=account_number)
        if sender.balance > 0:
            sender.balance = sender.balance - amount
            receiver.balance = receiver.balance + amount
            sender.save()
            receiver.save()
            return render(request, 'sign_in.html')
    if request.method == "GET":
        return render(request, 'sign_in.html')


def dashboard(request):
    context = {}
    account_detail = BankAccount.objects.get(account_number="03082219027")
    context['account_detail'] = account_detail
    return render(request, 'dashboard.html', context)
