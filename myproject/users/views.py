from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

from customer.models import CustomerProfile
from performer.models import PerformerProfile
from users.forms import RegisterForm, LoginUser


# Create your views here.

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        role = form.cleaned_data['role']

        if role == 'Заказчик':
            CustomerProfile.objects.create(user=user)
        elif role == 'Исполнитель':
            PerformerProfile.objects.create(user=user)
        return response


class LoginUserView(LoginView):
    form_class = LoginUser
    template_name = 'users/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
