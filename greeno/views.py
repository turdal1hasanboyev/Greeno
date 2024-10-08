from django.shortcuts import render, redirect

from .models import OurWonderfulPlants, Contact, Gallery


def home(request):
    query = request.GET.get('query')
    url = request.META.get('HTTP_REFERER')

    plants = OurWonderfulPlants.objects.all()
    gallery = Gallery.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message,
            phone=phone,
        )

        return redirect(url)
    
    context = {
        'plants': plants.order_by('id')[:6],
        'gallery': gallery.order_by('-id')[:6],
    }

    return render(request, 'index.html', context)
