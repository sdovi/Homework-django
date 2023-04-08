from django.shortcuts import render
from .forms import UsersForm


def register(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save() 
        
        else:
            form = UsersForm
       

    form = UsersForm()
    
    return render(request, 'register.html', {'form': form})
