from django.shortcuts import render,redirect
from django.contrib import auth
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from .models import *
# Create your views here.
def home(request):
	return render(request,'home.html')

# Registration
def register(request):
	if request.method == 'POST':
		try:	
				# Remove Spaces
				username = request.POST['username']
				username = str(username)
				username = "".join(username.split())

				user = User.objects.get(username = username)
				# print(user)
				return render(request,'register.html')
		# print(request.POST['username'],request.POST['name'],request.POST['email'],request.POST['phone'],request.POST['position'],request.FILES['profile'])
		except User.DoesNotExist:
				user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
				# print(request.POST['username'])
				profile_file = request.FILES['profile_pic']
				# print(profile_file)
				fs = FileSystemStorage(location='media/images/')
				filename = fs.save(profile_file.name,profile_file)
				# print(name,file)
				url = fs.url(filename)
				new_user = PMS(username = user , name = request.POST['name'] , profile = url , phone = request.POST['phone'] , email = request.POST['email'] , occupation = request.POST['position'])
				new_user.save()
				print('User created')
				return render(request,'register.html')
	else:
		return render(request,'register.html')


# Login
def login(request):
	if request.method == 'POST':
		try:
			# Check User in DB
	 		uname = request.POST['username']
	 		pwd = request.POST['password']
	 		user_authenticate = auth.authenticate(username=uname,password=pwd)
	 		if user_authenticate is not None:
	 			auth.login(request,user_authenticate)
	 			print('Successfully Login')	 				
	 			return redirect('profile')
	 		else:
	 			print('Login Failed')	
	 			return redirect('login')
		except:
			return render(request,'login.html')
	else:
		return render(request,'login.html')


#  Profile
def profile(request):
	if not request.user.is_authenticated:
		return redirect('login')
	if request.user.is_superuser:
		return redirect('login')
	data = PMS.objects.get(username = request.user)
	return render(request,'profile.html',{'data':data})
	
# Logout
def logout(request):
	auth.logout(request)
	print('Logout')
	return redirect('/login')

# Edit Password
def edit_pass(request):
	if not request.user.is_authenticated:
		return redirect('login')
	if request.method == 'POST':
		old_pass = request.POST['old_pass']
		new_pass = request.POST['new_pass']
		confirm_pass = request.POST['confirm_pass']
		print(old_pass,new_pass,confirm_pass)

		if old_pass =="" or new_pass =="" or confirm_pass == "" :
			error = "Empty Fields"
			return render(request,'login.html' , {'error' : error})
			
		user = auth.authenticate(username=request.user, password=request.POST['old_pass'])
		
		if user != None:
			if new_pass!=confirm_pass:
				error = "New password and Confirm password do not match"
				return render(request, 'edit_pass.html', {'error':error})
			user = User.objects.get( username = request.user )
			user.set_password(new_pass)
			user.save()
		return render(request , 'login.html')

	else:
		return render(request , 'edit_pass.html')