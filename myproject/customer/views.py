from django.shortcuts import render
from django.views import View

from customer.models import CustomerProfile


# from customer.forms import CustomerProfileForm


# from .models import CustomerProfile


# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, 'index.html')


class CustomerDashboard(View):
    def get(self, request):
        customer_users = CustomerProfile.objects.all()

        data = {
            'customer_users': customer_users
        }
        return render(request, 'customer.html', data)

# from django.shortcuts import render, redirect
# from .forms import CustomerProfileForm, PerformerProfileForm
# from .models import CustomerProfile, PerformerProfile
#
# def create_customer_profile(request):
#     if request.method == 'POST':
#         form = CustomerProfileForm(request.POST)
#         if form.is_valid():
#             customer_profile = form.save(commit=False)
#             customer_profile.user = request.user
#             customer_profile.save()
#             return redirect('index')
#     else:
#         form = CustomerProfileForm()
#     return render(request, 'create_profile.html', {'form': form})
#
# def create_performer_profile(request):
#     if request.method == 'POST':
#         form = PerformerProfileForm(request.POST)
#         if form.is_valid():
#             performer_profile = form.save(commit=False)
#             performer_profile.user = request.user
#             performer_profile.save()
#             return redirect('index')
#     else:
#         form = PerformerProfileForm()
#     return render(request, 'create_profile.html', {'form': form})
