from django.shortcuts import render, redirect
from django.views import View
from cars.models import Car
from cars.forms import CarModelForm


class CarsView(View):

   def get(self, request):
      cars = Car.objects.all().order_by('model')
      search = request.GET.get('search')
      
      if search:
         cars = Car.objects.filter(model__icontains=search).order_by('model')

      return render(request, 'cars.html', {'cars': cars})
      

class NewCarView(View):

   def post(self, request):
      new_car_form =CarModelForm(request.POST, request.FILES)
      if new_car_form.is_valid():
         new_car_form.save()
         return redirect('cars_list')
   
   def get(self, request):
         new_car_form = CarModelForm()

         return render(request, 'new_car.html', { 'new_car_form': new_car_form })


class UpdateCarView(View):
   ...

