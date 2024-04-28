from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from users.views import RegisterView, LoginUserView, PerformerView, CustomerView, ProfileView

app_name = 'users'

urlpatterns = [
    path('registration/', RegisterView.as_view(success_url=reverse_lazy('users:login')), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('performer/', PerformerView.as_view(), name='performer'),
    path('customer/', CustomerView.as_view(), name='customer'),
    path('profile/<role>/<int:user_id>', ProfileView.as_view(), name='profile'),
]
