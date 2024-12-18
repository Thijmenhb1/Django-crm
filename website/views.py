from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddClientForm, AddTicketForm
from .models import Client, Ticket

def home(request):
	clients = Client.objects.all()


	#Check if logged in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		#Authenticate
		user = authenticate(request, username = username, password=password)

		if user is not None:
			login(request, user)
			messages.success(request, "You've been logged in")
			return redirect('home')

		else:
			messages.success(request, "There's been an error logging in, please try again")
			return redirect('home')

	else:
		return render(request, 'home.html', {'clients':clients})




# Logout function
def logout_user(request):
	logout(request)
	messages.success(request, "You've been logged out successfully")
	return redirect('home')


# Register function
def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()

			#Auth and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username = username, password = password)
			login(request, user)
			messages.success(request, f"You're successfully registered, welcome {username}")
			return redirect('home')

	else:
		form = SignUpForm()  
		return render(request, 'register.html', {'form': form})

	return render(request, 'register.html', {'form': form})




# Client functions
def client_list(request):
	if request.user.is_authenticated:
		clients = Client.objects.all()
		return render(request, 'client_list.html', {'clients':clients})

	else:
		messages.success(request, "you must be logged in to view this page")
		return redirect('home')



def view_client(request, pk):
	if request.user.is_authenticated:
		view_client = Client.objects.get(id = pk)
		return render(request, 'client.html', {'view_client': view_client})

	else:
		messages.success(request, "you must be logged in to view this page")
		return redirect('home')



def add_client(request):
	form = AddClientForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid:
				add_client = form.save()
				messages.success(request, "Client added successfully")
				return redirect('client_list')

		return render(request, 'add_client.html', {'form':form})

	else:
		messages.success(request, "You must be logged in to add clients")
		return redirect('home')



def update_client(request, pk):
	if request.user.is_authenticated:
		current_client = Client.objects.get(id=pk)
		form = AddClientForm(request.POST or None, instance=current_client)
		if form.is_valid():
			form.save()
			messages.success(request, "Client updated successfully")
			return redirect('client', pk=current_client.id)

		return render(request, 'update_client.html', {'form': form, 'current_client': current_client})

	else:
		messages.success(request, "You must be logged in to update clients")
		return redirect('home')



def delete_client(request, pk):
	if request.user.is_authenticated:
		delete_it = Client.objects.get(id = pk)
		delete_it.delete()
		messages.success(request, "Client deleted successfully")
		return redirect('client_list')

	else:
		messages.success(request, "you must be logged in delete clients")
		return redirect('home')




# Ticket functions
def ticket_list(request):
	if request.user.is_authenticated:
		tickets = Ticket.objects.all()
		return render(request, 'ticket_list.html', {'tickets':tickets})

	else:
		messages.success(request, "you must be logged in to view this page")
		return redirect('home')



def add_ticket(request):
	form = AddTicketForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid:
				add_ticket = form.save()
				messages.success(request, "Ticket added successfully")
				return redirect('ticket_list')

		return render(request, 'add_ticket.html', {'form':form})
		
	else:
		messages.success(request, "You must be logged in to add tickets")
		return redirect('home')



def view_ticket(request, pk):
	if request.user.is_authenticated:
		view_ticket = Ticket.objects.get(id = pk)
		return render(request, 'ticket.html', {'view_ticket': view_ticket})

	else:
		messages.success(request, "you must be logged in to view this page")
		return redirect('home')



def update_ticket(request, pk):
	if request.user.is_authenticated:
		current_ticket = Ticket.objects.get(id=pk)
		form = AddTicketForm(request.POST or None, instance=current_ticket)
		if form.is_valid():
			form.save()
			messages.success(request, "Ticket updated successfully")
			return redirect('ticket', pk=current_ticket.id)

		return render(request, 'update_ticket.html', {'form': form, 'current_ticket': current_ticket})

	else:
		messages.success(request, "You must be logged in to update tickets")
		return redirect('home')



def delete_ticket(request, pk):
	if request.user.is_authenticated:
		delete_it = Ticket.objects.get(id = pk)
		delete_it.delete()
		messages.success(request, "Ticket deleted successfully")
		return redirect('ticket_list')

	else:
		messages.success(request, "you must be logged in delete tickets")
		return redirect('home')
