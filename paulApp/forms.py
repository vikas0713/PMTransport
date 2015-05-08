from django import forms
from models import OrderModel, DriverModel,Contacts
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, ButtonHolder
from crispy_forms.bootstrap import FormActions


class OrderForm(forms.ModelForm):
    helper=FormHelper()
    helper.layout = Layout(
        Div(
        Div(
            Div('load', css_class='col-md-6'),
            Div('status',css_class='col-md-6'),
            css_class='row-fluid'),
        
       Div(
            Div('customer', css_class='col-md-4'),
            Div('driver_name',css_class='col-md-4'),
            Div('types',css_class='col-md-4'),
            
            
        css_class='row-fluid'),
           
       Div(
            Div('currency_type',css_class='col-md-6'),
            Div('equipment_type',css_class='col-md-6'),
            css_class='row-fluid'
            ),
            
        Div(
            Div('truck',css_class='col-md-6'),
            Div('trailer',css_class='col-md-6'),
            css_class='row-fluid'
            ),  
        
        Div(
            Div('origin',css_class='col-md-4'),
            Div('destination',css_class='col-md-4'),
            Div('weight_in_lbs',css_class='col-md-4'),
            css_class='row-fluid'
            ),
        Div(
            Div('ship_date',css_class='col-md-4'),
            Div('del_date',css_class='col-md-4'),
            Div('total_km',css_class='col-md-4'),
            css_class='row-fluid'
            ),
        Div(
            Div('usd',css_class='col-md-4'),
            Div('edit_date',css_class='col-md-4'),
            Div('other_charges',css_class='col-md-4'),
            css_class='row-fluid'
            ),
        
        
        css_class="container-fluid"),
        
        ButtonHolder(
                Submit('submit', 'Submit', css_class='btn btn-large btn-info')
            ),
           
        )
    
    
    
    class Meta:
        model= OrderModel
        exclude=[]
        dateTimeOptions = {'format': 'yyyy/mm/dd', 'autoclose': True,'showMeridian' : True}
#        widgets = {
#            #Use localization and bootstrap 3
#            'datetime': DateTimeWidget(attrs={'id':"datetime"}, usel10n = True, bootstrap_version=3)
#        }
    def __init__(self , *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['del_date'].widget.attrs.update({'id':'datepicker'})
        self.fields['ship_date'].widget.attrs.update({'id':'datepicker1'})
    
class DriverForm(forms.ModelForm):
    
    class Meta:
        model= DriverModel
        exclude=[]
        
    def __init__(self, *args, **kwargs):
        super(DriverForm, self).__init__(*args, **kwargs)
        self.fields['dl_expiry'].widget.attrs.update({'id':'datepicker'})
        
class ContactsForm(forms.ModelForm):
    helper=FormHelper()
    
    helper.layout = Layout(
        Div(
            Div('customer',css_class='col-md-4'),
            Div('address',css_class='col-md-4'),
            Div('city',css_class='col-md-4'),
            Div('state',css_class='col-md-4'),
            Div('contact',css_class='col-md-4'),
            Div('email',css_class='col-md-4'),
            Div('total_sale',css_class='col-md-4'),
            css_class='container-fluid',
            ),
        ButtonHolder(
                Submit('submit', 'Submit', css_class='btn btn-large btn-info')
            ),
           
        )
    class Meta:
        model=Contacts
        exclude=[]