from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
from django.views import generic
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib.auth import login, authenticate
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
# from django.contrib.auth.forms import UserCreationForm
# from .models import *
# from .forms import OrderForm


from django.shortcuts import render, get_object_or_404,redirect
from .models import Post,CommentModel



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

# def registerPage(request):
#     form = UserCreationForm()


#     if request.method == 'POST':
#          form = UserCreationForm(request.POST)
#          if form.is_valid():
#              form.save()

#     context = {'form':form}
#     return render(request, 'register.html', context)

# def loginPage(request):
#     context = {}
#     return render(request, 'login.html', context)





def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("http://127.0.0.1:8000/login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("http://127.0.0.1:8000/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("http://127.0.0.1:8000/")


def post_admin(request):
    return HttpResponseRedirect('http://127.0.0.1:8000/admin')

def policy(request):
    return render(request,'policy.html')


def about_us(request):
    return render(request,'about_us.html')

def contact(request):
    if request.method =="POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #send an email 
        send_mail(
            message_name, # subject
            message , # message
            message_email, # from email
            ['browniepoints@gmail.com'], # To email
        )

        return render(request, 'contact.html', {'message_name': message_name })

    else:    
        return render(request,'contact.html', {})    


from .models import Post



def BlogDetailView(request,_id):
    try:
        data =Post.objects.get(id =_id)
        comments = CommentModel.objects.filter(blog = data)
    except Post.DoesNotExist:
        raise Http404('Data does not exist')

    if request.method == 'POST':
        your_name=request.POST.get('your_name')
        comment_text=request.POST.get('comment_text')
        comment=CommentModel(your_name=your_name,comment_text=comment_text,blog=data)
        comment.save()
        return redirect(f'/blog/{_id}')
    context = {
            'data':data,
            'comments':comments,
        }
    return render(request,'post_detail.html',context)

def login_request(request):
	if request.method == "POST":
			username = request.POST.get('email')
			password = request.POST.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("http://127.0.0.1:8000/")
			else:
				messages.error(request,"Invalid username or password.")

	return render(request=request, template_name="login.html")