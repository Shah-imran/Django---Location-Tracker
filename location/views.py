from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

def home(request):
	context = {
		
	}
	return render(request, "location/home.html", context)


def dashboard(request):
	context = {
		"title": "Dashboard"
	}
	return render(request, "location/dashboard.html", context)


def sign_up(request):
	messages.info(request, "Sorry, User registration is currently not available!")
	return redirect('sign_in')


@login_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			return redirect('change_password')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user)

	context = {
		'form': form
	}
	return render(request, 'location/change_password.html', context)


def logout_user(request):
	logout(request)
	messages.info(request, "You have been logged out successfully!")
	return redirect('sign_in')


def reset_password(request):
	if request.user.is_authenticated:
		return redirect('index')
	return render(request, "users/reset_password.html")