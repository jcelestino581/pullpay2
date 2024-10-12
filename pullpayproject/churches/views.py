from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Church, User  # Ensure you use the correct model
from .forms import ChurchForm, UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")


@login_required
def edit_church_screen(request):
    return render(request, "Churches/edit_church_screen.html")


def topChurches(request):
    # Fetch the Church object or return a 404 error if not found
    # church = get_object_or_404(Church, pk=church_id)
    top_five_churches = Church.objects.order_by("-size_int")[:5]

    # Return a formatted response
    context = {"top_five_churches": top_five_churches}

    return render(request, "Churches/top_churches.html", context)


def view_churches(request):
    # Fetch the Church object or return a 404 error if not found
    # church = get_object_or_404(Church, pk=church_id)
    view_churches = Church.objects.all().values()

    # Return a formatted response
    context = {"view_churches": view_churches}

    return render(request, "Churches/view_churches.html", context)


def view_users(request):
    # Fetch the Church object or return a 404 error if not found
    # church = get_object_or_404(Church, pk=church_id)
    view_users = User.objects.all().values()

    # Return a formatted response
    context = {"view_users": view_users}

    return render(request, "Churches/view_users.html", context)


def add_church(request):
    if request.method == "POST":
        form = ChurchForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Church added successfully!")
            return redirect(
                "add_church"
            )  # Redirect to the same page to display the message
    else:
        form = ChurchForm()

    return render(request, "Churches/add_church.html", {"form": form})


def delete_church(request, id):
    church = get_object_or_404(Church, id=id)

    if request.method == "POST":
        church_name = church.church_name_text
        church.delete()
        messages.success(request, f"Successfully deleted church: {church_name}")
        return redirect("view_churches")

    return render(request, "Churches/delete_church.html", {"church": church})


def update_church(request, id):
    church = get_object_or_404(Church, id=id)

    if request.method == "POST":
        form = ChurchForm(request.POST, instance=church)
        if form.is_valid():
            form.save()  # Save the updated church details
            messages.success(
                request, f"{church.church_name_text} updated successfully!"
            )
            return redirect(
                "Churches/view_churches"
            )  # Redirect to the church list page
    else:
        form = ChurchForm(
            instance=church
        )  # Pre-populate the form with current church data

    return render(
        request, "Churches/update_church.html", {"form": form, "church": church}
    )


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect("user_list")  # Redirect to a success page
    else:
        form = UserForm()

    return render(request, "Users/create_user.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            # return redirect("index")  # Redirect to the home page or any other page
    else:
        form = UserCreationForm()
    return render(request, "Login/register.html", {"form": form})


def user_profile(request, user_id):
    user = User.objects.get(id=user_id)  # Fetch the user by ID
    return render(request, "user_profile.html", {"user": user})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(
                "index"
            )  # Redirect to your home page after successful login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "Login/login_view.html")  # Your login template


def success(request):
    return HttpResponse("Church added successfully!")


def user_list(request):
    users = User.objects.all()
    return render(request, "Users/user_list.html", {"users": users})
