from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from .views import (
    start,
    upload_video,
    register
)


urlpatterns = [
    path('', start, name='start_page'),
    path('upload/', upload_video, name='upload_video'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', register, name='registration'),
    path('passwordchange/', PasswordChangeView.as_view(), name='passwordchange'),
    path('passwordchangedone/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('passwordreset/', PasswordResetView.as_view(), name='password_reset'),
    path('passwordresetdone/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('passwordreset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('passwordreset/done', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
