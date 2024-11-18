from django import forms
 
from .models import Bateau, Port
 
class BoatForm(forms.ModelForm):
 
    class Meta:
        model = Bateau
        fields = ['id_bateau', 'etat', 'type', 'capacite', 'photo', 'lieu']

class PortForm(forms.ModelForm):
 
    class Meta:
        model = Port
        fields = ['id_port', 'disponibilite', 'photo']

class TravelForm(forms.Form):
    bateau = forms.ModelChoiceField(
        queryset=Bateau.objects.filter(etat='en service'),  # Filtrer les bateaux en service
        label="Choisissez un bateau"
    )
    port_destination = forms.ModelChoiceField(
        queryset=Port.objects.all(),
        label="Choisissez un port de destination"
    )

class Reparation(forms.ModelForm):

    class Meta:
        model = Bateau
        fields = ['etat']

class MaintenanceForm(forms.Form):
    bateau = forms.ModelChoiceField(
        queryset=Bateau.objects.filter(etat='en maintenance'),
        label="Choisissez un bateau en maintenance",
        required=True
    )
