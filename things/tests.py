from django.test import TestCase
from django import forms
from django.test import TestCase
from .models import Thing
from .forms import ThingForm

class ThingFormTestCase(TestCase):
    """Unit test of the signup form."""

    def setUp(self):
        self.form_input= {
                    'name': 'Red Ball', 
                    'description': 'There are 33 red balls in this room!', 
                    'quantity': 3 
                    }
        

    def test_valid_ThingForm(self):
        form= ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_has_necessaryFields(self):
        form= ThingForm()
        self.assertIn('name', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('quantity', form.fields)
        quantity_field= form.fields['quantity']
        self.assertTrue(isinstance(quantity_field, forms.IntegerField))
        quantity_widget= form.fields['quantity'].widget
        self.assertTrue(isinstance(quantity_widget, forms.NumberInput))
        description_widget= form.fields['description'].widget
        self.assertTrue(isinstance(description_widget, forms.Textarea))
              
    def test_form_uses_modelValidation(self):
        self.form_input['quantity']= -22
        form= ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_invalid_quantity_not_number(self):
        self.form_input['quantity']= 'not_a_number'
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())
    
    def test_invalid_quantity_not_negative(self):
        self.form_input['quantity']= -600
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())
    
    def test_quantity_must_contain_number(self):
        self.form_input['quantity']= 33
        form= ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())
    
    def test_quantity_can_contain_zero(self):
        self.form_input['quantity']= 0
        form= ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())