from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from website.forms import SignupForm, AddRecordForm
from website.models import Record
# Create your views here.

def home(request):
    records = Record.objects.all()
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been loggedin')
            return redirect('home')
        else:
            messages.warning(request, 'There was an error while logging in')
            return redirect('home')
    else:
        return render(request, 'website/home.html', {'records':records})



def logout_user(request):
    logout(request)
    messages.success(request, 'you have been logged out!')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Authenticate and Login 
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = authenticate(username=username, password=password)
            # login(request, user)
            messages.success(request, 'Successfully Register!')
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'website/register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Lookup records
        record = Record.objects.get(id=pk)
        return render(request, 'website/record.html', {'record':record})
    else:
        messages.warning(request, 'You must be logged in to access the page!')
        return render(request, 'website/record.html')
    
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            delete_it = Record.objects.get(id=pk)
            delete_it.delete()
            messages.success(request, 'Record Deleted Successfully')
            return redirect('home')
        else:
            print('Error while deleting!')
            return redirect('home')
    else:
        messages.warning(request, 'You must be logged in to Delete!')
        return redirect('home')
    
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record Added Successfully!!')
                return redirect('home')
        return render(request, 'website/add_record.html', {'form':form})
    else:
        messages.warning(request, 'You must be logged in!!')
        return render(request, 'website/add_record.html', {'form':form})
    
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Updated Successfully')
            return redirect('home')
        return render(request, 'website/update_record.html', {'form':form})
    else:
        messages.error(request, 'You must be logged in!')
        return redirect('home')