from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Church  # Ensure you use the correct model


def index(request):
    return HttpResponse("Hello, world. You're at the homepage.")


def topChurches(request):
    # Fetch the Church object or return a 404 error if not found
    # church = get_object_or_404(Church, pk=church_id)
    top_five_churches = Church.objects.order_by("-size_int")[:5]

    # Return a formatted response
    context = {"top_five_churches": top_five_churches}

    return render(request, "index.html", context)
