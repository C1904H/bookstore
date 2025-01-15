from django.shortcuts import render, redirect 
#Django authentication libraries
from django.contrib.auth import authenticate, login, logout
#Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
  #initialize:
  #error_message to None                                 
  error_message = None   
  #form object with username and password fields 
  form = AuthenticationForm()
  
  #when user hits 'login' button, then POST request is generated
  if request.method == 'POST':
    #read data sent by form via POST request
    form =AuthenticationForm(data=request.POST)

    if form.is_valid():
      username=form.cleaned_data.get('username')
      password=form.cleaned_data.get('password')

      #Django authenticate function to validate user
      user=authenticate(username=username, password=password)
      if user is not None: #ie user authenticated
        #use pre-defined Django function to login
        login(request, user)
        return redirect('sales:records') #& send user to desired page
      else: 
        error_message= 'ooops... something went wrong'

  #prepare data to send from view to template
  context ={                                             
      'form': form,                                 #send the form data
      'error_message': error_message                     #and the error_message
  }
  #load the login page using "context" information
  return render(request, 'auth/login.html', context) 

#define a function view called logout_view that takes a request from user
def logout_view(request):                                  
   logout(request)             #the use pre-defined Django function to logout
   return redirect('login')    #after logging out go to login form (or whichever page you want)  