from django.shortcuts import render,redirect
import json

from ExpenseTracker.models import ExpenseRecords
from ExpenseTracker.forms import ExpenseForm

from .helper_functions import *

def dashboard(request):
    records = ExpenseRecords.objects.all().values()

    context = {}
    for i,data in enumerate(get_data()):
        context[f"{fields[i]}"]=data

    return render(request,"ExpenseTracker/dashboard.html", {"records":records,"data_json":json.dumps(context)})

def add_expense(request):
    context = {}
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(dashboard)

    form = ExpenseForm()
    context["form"] = form
    return render(request,"ExpenseTracker/add_expense.html", context)