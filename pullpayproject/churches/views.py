from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Church  # Ensure you use the correct model
from .forms import ChurchForm


def index(request):
    return render(request, "index.html")


def topChurches(request):
    # Fetch the Church object or return a 404 error if not found
    # church = get_object_or_404(Church, pk=church_id)
    top_five_churches = Church.objects.order_by("-size_int")[:5]

    # Return a formatted response
    context = {"top_five_churches": top_five_churches}

    return render(request, "top_churches.html", context)

def add_church(request):
    if request.method == 'POST':
        form = ChurchForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Church added successfully!')
            return redirect('add_church')  # Redirect to the same page to display the message
    else:
        form = ChurchForm()
    
    return render(request, 'add_church.html', {'form': form})

def success(request):
    return HttpResponse("Church added successfully!")
