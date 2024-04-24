from django.urls import path

from performer.views import PerformerProfileView

app_name = 'performer'

urlpatterns = [
    path('performer/', PerformerProfileView.as_view(), name='performer'),

]
