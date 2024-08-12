from django.shortcuts import render
from .models import Car , ContactMessage
from django.views.generic import TemplateView




def home(request):
    cars = Car.objects.all()
    for car in cars:
        # Préparer les variables pour les étoiles pleines et vides
        car.full_stars = int(car.review)  # Étoiles pleines
        car.empty_stars = 5 - car.full_stars  # Étoiles vides
    return render(request, 'index.html', {'cars': cars})


def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def car(request):
    cars = Car.objects.all()
    for car in cars:
        # Préparer les variables pour les étoiles pleines et vides
        car.full_stars = int(car.review)  # Étoiles pleines
        car.empty_stars = 5 - car.full_stars  # Étoiles vides
    return render(request, 'cars.html', {'cars': cars})


class SuccessView(TemplateView):
    template_name = 'success.html'



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and phone and subject and message:
            data = ContactMessage(name=name, email=email, phone=phone, subject=subject, message=message)
            data.save()
            return render(request, 'contact.html', {'success': 'Message sent successfully'})
        else:
            return render(request, 'contact.html', {'error': 'All fields are required'})

    return render(request, 'contact.html')
