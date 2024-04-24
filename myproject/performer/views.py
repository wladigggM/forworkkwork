from django.shortcuts import render
from django.views import View

from performer.models import PerformerProfile


# Create your views here.

class PerformerProfileView(View):
    def get(self, request):
        performer_users = PerformerProfile.objects.all()

        data = {
            'performer_users': performer_users
        }

        return render(request, 'performer.html', data)
