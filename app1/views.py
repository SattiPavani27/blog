from django.shortcuts import render, HttpResponse, redirect
from .models import Contact, Login_details, Registration, Posts, User
from django.http import JsonResponse
from language_tool_python import LanguageTool
from .models import TextCheck
from requests.exceptions import RequestException


def home(request):
    # return HttpResponse("hello")
    context = {'name':'Harika', 'course':'django'}
    return render(request, 'home.html', context)
def contact(request):
    if request.method=="POST":
       id=request.POST['id']
       name = request.POST['name']
       phone = request.POST['phone']
       email = request.POST['email']
       ins = Contact(id, name, phone, email)
       ins.save()
    # return HttpRespo?nse("harika")
    return render(request, 'contact.html')
def about(request):
    # return HttpResponse("how are you")
    return render(request, 'about.html')
def projects(request):
   # return HttpResponse("i am fine")#projects pag
    return render(request, 'projects.html')
def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        # Check if a user with the provided name exists
        if User.objects.filter(name=name).exists():
            # Check if the password matches
            user = User.objects.get(name=name)
            if user.password == password:
                # Redirect to another page upon successful login
                return redirect('http://127.0.0.1:8000/content/')  # Replace with the actual URL or name of your desired page
            else:
                return render(request, 'login.html', {'error': 'Invalid password. Please try again.'})
        else:
            return render(request, 'login.html', {'error': 'User with this name does not exist.'})

    return render(request, 'login.html')
# def registration(request):
#     if request.method=="POST":
#        name=request.POST['name']
#        email = request.POST['email']
#        your_password=request.POST['your_password']
#        phnumber=request.POST['phnumber']
#        inst= Registration(name,email,your_password,phnumber)
#        inst.save()
#     return render(request, 'registration.html')
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if the name already exists
        if Registration.objects.filter(name=name).exists():
            return render(request, 'registration.html', {'error': 'Name already exists. Please choose a different name.'})

        # Check if the email is already registered
        if Registration.objects.filter(email=email).exists():
            return render(request, 'registration.html', {'error': 'Email already exists. Please use a different email.'})

        # Check if password and confirm password match
        if password != confirm_password:
            return render(request, 'registration.html', {'error': 'Password and Confirm Password do not match.'})

        # Create a new user
        user = Registration.objects.create(name=name, phone=phone, email=email, password=password)

        # Redirect to the login page or any other desired page after successful registration
        return redirect('http://127.0.0.1:8000/login/')  # Replace 'login' with the actual name or URL pattern of your login page

    return render(request, 'registration.html')
def home_page(request):
    return render(request, 'home_page.html')
def content(request):
    return render(request, 'content.html')
def posts(request):
    if request.method=="POST":
        title=request.POST['title']
        description=request.POST['description']
        date_and_time=request.POST['date_and_time']
        instan=Posts(title,description,date_and_time) 
        instan.save()
    return render(request, 'posts.html')
def index(request):
    return render(request, 'index.html')
def check_text(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')

        try:
            tool = LanguageTool('en-US')
            matches = tool.check(input_text)
            corrected_text = tool.correct(input_text)
            text_check = TextCheck.objects.create(original_text=input_text, corrected_text=corrected_text)
            
            return render(request, 'result.html', {'text_check': text_check, 'matches': matches})

        except RequestException as e:
            return JsonResponse({'error': f'Error in LanguageTool API response: {str(e)}'})

    return JsonResponse({'error': 'Invalid request. Please enter text.'})

def page(request):
    texts=TextCheck.objects.all()
    return render(request, 'edit_page_output.html',{'texts':texts})
def posts_data(request):
    data=Posts.objects.all()
    return render(request, 'posts_data.html', {'data':data})
def reference(request):
    return render(request, 'reference.html')
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if the name already exists
        if User.objects.filter(name=name).exists():
            return render(request, 'register.html', {'error': 'Name already exists. Please choose a different name.'})

        # Check if the email is already registered
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already exists. Please use a different email.'})

        # Check if password and confirm password match
        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Password and Confirm Password do not match.'})

        # Create a new user
        user = User.objects.create(name=name, phone=phone, email=email, password=password)

        # Redirect to the login page or any other desired page after successful registration
        return redirect('http://127.0.0.1:8000/login/')  # Replace 'login' with the actual name or URL pattern of your login page

    return render(request, 'register.html')


# views.py





