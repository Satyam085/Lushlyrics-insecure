from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.
def userLogin(request):
    case = True
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(email = username):
            print('User exist with vaild email')
            user = User.objects.get(email = username)
        elif User.objects.filter(username = username):
            print('User exist with vaild username')
            user = User.objects.get(username = username)
        else:
            print("User don't exist")
            user = ''
            case = False

        if user and user.check_password(password):
            print('logged in')
            return redirect("")
        else:
            case = False
    context = { 'case' : case}

    return render(request, "login.html", context)

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False



def signup(request):
    email = True
    username = True
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']


        if User.objects.filter(username = username):
            username = False
            print('User already exists')
        elif User.objects.filter(email = email):
            email = False
            print('User already exists')
        else:
          newUser = User.objects.create(
              username = username,
              password = password,
              email = email,
          ) 
          newUser.save()
    context = {
        'email' : email,
        'username' : username
    }

    return render(request, 'signup.html', context)
