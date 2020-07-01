from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages


@login_required
def myPassowrdChangeDone(request):
    messages.add_message(request, messages.INFO, 'Sua senha foi atualizada!')
    return redirect('prontuarios:home')
