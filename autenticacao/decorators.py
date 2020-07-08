from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, url='prontuarios:home'):
    """
    Decorator for views that checks that the logged in user is a student,
    redirects to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.medico,
        login_url=url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def user_is_admin(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.admin:
            return function(request, *args, **kwargs)
        else:
            # messages.add_message(request, messages.INFO, 'Permissão Negada!')
            return redirect('prontuarios:home')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def user_is_medico(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.medico:
            return function(request, *args, **kwargs)
        else:
            # messages.add_message(request, messages.INFO, 'Permissão Negada!')
            return redirect('prontuarios:home')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
