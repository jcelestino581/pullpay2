from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Church, Users  # Ensure you use the correct model
from .forms import ChurchForm, UsersForm


def index(request):
    return render(request, "index.html")


def topChurches(request):
    # Fetch the Church object or return a 404 error if not found
    # church = get_object_or_404(Church, pk=church_id)
    top_five_churches = Church.objects.order_by("-size_int")[:5]

    # Return a formatted response
    context = {"top_five_churches": top_five_churches}

    return render(request, "top_churches.html", context)


def view_churches(request):
    # Fetch the Church object or return a 404 error if not found
    # church = get_object_or_404(Church, pk=church_id)
    view_churches = Church.objects.all().values()

    # Return a formatted response
    context = {"view_churches": view_churches}

    return render(request, "view_churches.html", context)


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

    return render(request, "add_church.html", {"form": form})


def delete_church(request, id):
    church = get_object_or_404(Church, id=id)

    if request.method == "POST":
        church_name = church.church_name_text
        church.delete()
        messages.success(request, f"Successfully deleted church: {church_name}")
        return redirect("view_churches")

    return render(request, "delete_church.html", {"church": church})


def update_church(request, id):
    church = get_object_or_404(Church, id=id)

    if request.method == "POST":
        form = ChurchForm(request.POST, instance=church)
        if form.is_valid():
            form.save()  # Save the updated church details
            messages.success(
                request, f"{church.church_name_text} updated successfully!"
            )
            return redirect("view_churches")  # Redirect to the church list page
    else:
        form = ChurchForm(
            instance=church
        )  # Pre-populate the form with current church data

    return render(request, "update_church.html", {"form": form, "church": church})


def create_user(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect("user_list")  # Redirect to a success page
    else:
        form = UsersForm()

    return render(request, "create_user.html", {"form": form})


def success(request):
    return HttpResponse("Church added successfully!")


def user_list(request):
    users = Users.objects.all()
    return render(request, "user_list.html", {"users": users})
