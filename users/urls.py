from django.urls import path
from .views import MyPasswordResetDoneView, MyPasswordChangeView

app_name = 'users'

urlpatterns = [
    path('change-password/',MyPasswordChangeView.as_view(), name='users.password-change-view'),
    path('change-password/done/', MyPasswordResetDoneView.as_view(), name='users.password-change-done-view'),
]