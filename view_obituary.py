from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Obituary

def view_obituaries(request):
    obituaries_list = Obituary.objects.all().order_by('-dod')  
    paginator = Paginator(obituaries_list, 10)  

    page_number = request.GET.get('page')
    obituaries = paginator.get_page(page_number)

    return render(request, "view_obituaries.html", {"obituaries": obituaries})
