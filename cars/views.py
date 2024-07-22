from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from cars.models import Car
from cars.forms import CarModelForm


class CarsListView(ListView):
   model = Car
   template_name = 'cars.html'
   context_object_name = 'cars'

   def get_queryset(self):
      cars = super().get_queryset().order_by('model')
      search = self.request.GET.get('search')
      if search:
          cars = cars.filter(model_icontains=search)
      return cars
      

class NewCarView(CreateView):

   def post(self, request):
      new_car_form =CarModelForm(request.POST, request.FILES)
      if new_car_form.is_valid():
         new_car_form.save()
         return redirect('cars_list')
   
   def get(self, request):
         new_car_form = CarModelForm()

         return render(request, 'new_car.html', { 'new_car_form': new_car_form })




