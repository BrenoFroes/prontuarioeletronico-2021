from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import *

app_name = "autenticacao"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='registration/my_password_change.html',
                                               success_url=reverse_lazy('autenticacao:password_change_done')),
         name='password_change'),

    path('password_change/done/', myPassowrdChangeDone,
         #auth_views.PasswordChangeDoneView.as_view(template_name='registration/my_password_change_done.html'),
         name='password_change_done'),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/my_password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/my_password_reset_confirm.html',
                                                     success_url=reverse_lazy('autenticacao:password_reset_complete')),
         name='password_reset_confirm'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(email_template_name='registration/my_password_reset_email.html',
                                              subject_template_name='registration/my_password_reset_subject.txt',
                                              template_name='registration/my_password_reset_form.html',
                                              success_url=reverse_lazy('autenticacao:password_reset_done')),
         name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/my_password_reset_complete.html'),
         name='password_reset_complete'),
]
