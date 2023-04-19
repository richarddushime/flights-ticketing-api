from django import forms
from django.forms import Select
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
import requests


class FlightSearchForm(forms.Form):
    origin = forms.CharField(max_length=50, label='From', widget=forms.Select(choices=[]))
    destination = forms.CharField(max_length=50, label='To', widget=forms.Select(choices=[]))
    departure_date = forms.DateField(label='Departure', widget=forms.DateInput(attrs={'type': 'date'}))
    return_date = forms.DateField(label='Return', widget=forms.DateInput(attrs={'type': 'date'}))
    passenger_count = forms.IntegerField(label='Passenger Count', widget=Select(choices=[(i, str(i)) for i in range(1, 11)]))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Search'))

        self.populate_airport_choices()

        self.helper.layout = Layout(
            Row(
                Column('origin', css_class='form-group col-md-6 mb-0'),
                Column('destination', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('departure_date', css_class='form-group col-md-6 mb-0'),
                Column('return_date', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('passenger_count', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        )

    def populate_airport_choices(self):
        url = 'https://skyscanner50.p.rapidapi.com/api/v1/searchFlights'
        params = {
            'access_key': 'e7811949dbmsh1bc1dad35f0d819p12c788jsn23611ad30e78',
            'offset': 0,
            'limit': 100,
        }
        response = requests.get(url, params=params)
        try:
            airports = response.json()['data']
        except KeyError:
            print("Error: 'data' key not found in API response")
            airports = []
        airport_choices = [(airport['airport_name'], airport['airport_name']) for airport in airports]
        self.fields['origin'].widget.choices = airport_choices
        self.fields['destination'].widget.choices = airport_choices
