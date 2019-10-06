from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,get_user_model
from .forms import ContactForm,LoginForm,RegisterForm



def home_page(request):
    context = {"title":"Hello Venky",
               "Content": "Home page Content",
              }
    if request.user.is_authenticated:
        context["Premium_Content"] = "This is Premium Content"
    return render(request,"render.html",context)


def about_page(request):
    context = {"title": "About Page",
                        "Content": "About page Content"}

    return render(request,"render.html",context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {"title": "Contact Page",
                "Content": "Contact page Content",
               "form": contact_form}
    if contact_form.is_valid():
      print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)
    # if request.method == 'POST':
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('msg'))



def login_page(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}
    print("user loggied in ")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not  None:
            login(request,user)
            context['form'] = LoginForm()
            return redirect("/login")
        else:
            print("Error")


    return render(request,"auth/login.html",context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        newuser = User.objects.create_user(username,email,password)
        print(newuser)
    return render(request,"auth/register.html",context)