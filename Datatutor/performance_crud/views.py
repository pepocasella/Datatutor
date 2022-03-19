from django.shortcuts import render
from matplotlib.style import context

from performance_crud.models import Performance_Forms, User

# Create your views here.
def home(request):
    return render(request, './portal_templates/home.html')
    
def performance_forms(request):
    performance_forms = Performance_Forms.objects.all()
    context = {
        'performance_forms': performance_forms
    }

    return render(request, './performance_crud_templates/performance_forms.html', context)


def user(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, './performance_crud_templates/simple.html', context)