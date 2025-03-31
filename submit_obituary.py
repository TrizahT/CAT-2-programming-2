from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Obituary

def submit_obituary(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        dob = request.POST.get('dob', '').strip()
        dod = request.POST.get('dod', '').strip()
        content = request.POST.get('content', '').strip()
        author = request.POST.get('author', '').strip()


        if not name or not dob or not dod or not content or not author:
            messages.error(request, "All fields are required!")
            return redirect('obituary_form')

        try:
            obituary = Obituary(name=name, dob=dob, dod=dod, content=content, author=author)
            obituary.save()
            messages.success(request, "Obituary submitted successfully!")
        except Exception as e:
            messages.error(request, f"Error: {e}")

        return redirect('obituary_form')

    return render(request, "obituary_form.html")
