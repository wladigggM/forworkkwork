from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .forms import RegisterForm, LoginUser
from .models import PerformerProfile, CustomerProfile, User
from .services import all_objects


# Create your views here.

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        return response


class LoginUserView(LoginView):
    form_class = LoginUser
    template_name = 'users/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class PerformerView(View):
    def get(self, request):
        data = {
            'performer_users': all_objects(PerformerProfile.objects)
        }

        return render(request, 'users/performer/performer.html', data)


class CustomerView(View):
    def get(self, request):
        data = {
            'customer_users': all_objects(CustomerProfile.objects)
        }
        return render(request, 'customer.html', data)


class ProfileView(View):
    def get(self, request, user_id):
        current_user = request.user
        user_by_id = User.objects.get(id=user_id)

        data = {
            'user_by_id': user_by_id
        }

        if PerformerProfile.objects.filter(user=user_by_id).exists():
            data['performer_info'] = PerformerProfile.objects.get(user=user_by_id)
        elif CustomerProfile.objects.filter(user=current_user).exists():
            data['customer_info'] = CustomerProfile.objects.get(user=user_by_id)

        return render(request, 'users/profile/profile.html', data)
