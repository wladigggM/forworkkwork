from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from users.forms import RegisterForm, LoginUser
from users.models import PerformerProfile, CustomerProfile


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


class PerformerProfileView(View):
    def get(self, request):
        performer_users = PerformerProfile.objects.all()

        data = {
            'performer_users': performer_users
        }

        return render(request, 'users/performer/performer.html', data)


class CustomerDashboard(View):
    def get(self, request):
        customer_users = CustomerProfile.objects.all()

        data = {
            'customer_users': customer_users
        }
        return render(request, 'customer.html', data)
