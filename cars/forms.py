from django import forms
from cars.models import Car, Brand


class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = [
            'model',
            'brand',
            'factory_year',
            'plate',
            'model_year',
            'value',
            'photo',
            'bio',
        ]
        widgets = {
            'model':forms.TextInput(attrs={'class': 'form-control',}),
            'brand':forms.Select(attrs={'class': 'form-control',}),
            'factory_year':forms.DateInput(attrs={'class': 'form-control',}),
            'plate':forms.TextInput(attrs={'class': 'form-control',}),
            'model_year':forms.DateInput(attrs={'class': 'form-control',}),
            'value':forms.NumberInput(attrs={'class': 'form-control','placeholder': '00.00',}),
            'photo':forms.FileInput(attrs={'class': 'form-control',}),
            'bio':forms.Textarea(attrs={'class' : 'form-control', 'rows':'5'}),
            
        }
        

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 2000:
            self.add_error('value', 'Valor mínimo do carro deve ser de R$ 5.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Não é possivel cadastrar carros fabricados antes de 1975.')
        return factory_year

class CarBrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'  