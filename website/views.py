from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, AddTicketForm
from .models import Record, Ticket

def home(request):
	records = Record.objects.all()


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
		return render(request, 'home.html', {'records':records})






def logout_user(request):
	logout(request)
	messages.success(request, "You've been logged out successfully")
	return redirect('home')



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






def record_list(request):
	if request.user.is_authenticated:
		records = Record.objects.all()
		return render(request, 'record_list.html', {'records':records})

	else:
		messages.success(request, "you must be logged in to view this page")
		return redirect('home')



def customer_record(request, pk):
	if request.user.is_authenticated:
		customer_record = Record.objects.get(id = pk)
		return render(request, 'record.html', {'customer_record': customer_record})

	else:
		messages.success(request, "you must be logged in to view this page")
		return redirect('home')



def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid:
				add_record = form.save()
				messages.success(request, "Record added successfully")
				return redirect('record_list')

		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You must be logged in to add records")
		return redirect('home')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record updated successfully")
			return redirect('record', pk=current_record.id)

		return render(request, 'update_record.html', {'form': form, 'current_record': current_record})

	else:
		messages.success(request, "You must be logged in to update records")
		return redirect('home')



def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id = pk)
		delete_it.delete()
		messages.success(request, "Record deleted successfully")
		return redirect('record_list')

	else:
		messages.success(request, "you must be logged in delete records")
		return redirect('home')






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



def customer_ticket(request, pk):
	if request.user.is_authenticated:
		customer_ticket = Ticket.objects.get(id = pk)
		return render(request, 'ticket.html', {'customer_ticket': customer_ticket})

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
