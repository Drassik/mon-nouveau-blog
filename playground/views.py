from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Bateau, Port
from .forms import BoatForm, PortForm, TravelForm, MaintenanceForm

# Create your views here.
def accueil(request):
    return render(request, 'playground/accueil.html')

def boats_list(request):
    bateaux = Bateau.objects.all().order_by('id_bateau')
    return render(request, 'playground/boats_list.html', {'bateaux': bateaux})

def boats_detail(request, pk):
    bateau = get_object_or_404(Bateau, pk = pk)
    lieu = Bateau.lieu
    if request.method == 'POST':
        form = BoatForm(request.POST, request.FILES, instance=bateau)
        if form.is_valid():
            form.save()
            return redirect('boats_detail', pk=pk)  
    else:
        form = BoatForm(instance=bateau)

    return render(request, 'playground/boats_detail.html', {'form': form, 'lieu' : lieu, 'bateau' : bateau})

def create_boats(request):
    if request.method == 'POST':
        form = BoatForm(request.POST, request.FILES)
        if form.is_valid():
            bateau = form.save()
            return redirect('boats_detail', pk = bateau.id_bateau)  
    else:
        form = BoatForm()

    return render(request, 'playground/boats_create.html', {'form': form})

def modify_boats(request, pk):
    bateau = get_object_or_404(Bateau, pk = pk)
    lieu = Bateau.lieu
    if request.method == 'POST':
        form = BoatForm(request.POST, request.FILES, instance=bateau)
        if form.is_valid():
            form.save()
            return redirect('boats_detail', pk=pk)  
    else:
        form = BoatForm(instance=bateau)

    return render(request, 'playground/boats_modify.html', {'form': form, 'lieu' : lieu, 'bateau' : bateau})

def delete_boats(request, pk):
    bateau = get_object_or_404(Bateau, pk=pk)
    bateau.delete()
    return redirect('boats_list')

def ports_list(request):
    ports = Port.objects.all().order_by('id_port')
    return render(request, 'playground/ports_list.html', {'ports': ports})

def ports_detail(request, pk):
    port = get_object_or_404(Port, pk = pk)
    disponibilite = Port.disponibilite
    if request.method == 'POST':
        form = PortForm(request.POST, request.FILES, instance=port)
        if form.is_valid():
            form.save()
            return redirect('ports_detail', pk=pk)  
    else:
        form = PortForm(instance=port)

    return render(request, 'playground/ports_detail.html', {'form': form, 'disponibilite' : disponibilite, 'port' : port})

def create_ports(request):
    if request.method == 'POST':
        form = PortForm(request.POST, request.FILES)
        if form.is_valid():
            port = form.save()
            return redirect('ports_detail', pk=port.id_port)  
    else:
        form = PortForm()

    return render(request, 'playground/ports_create.html', {'form': form})

def modify_ports(request, pk):
    port = get_object_or_404(Port, pk = pk)
    disponibilite = Port.disponibilite
    if request.method == 'POST':
        form = PortForm(request.POST, request.FILES, instance=port)
        if form.is_valid():
            form.save()
            return redirect('modify_ports', pk=pk)  
    else:
        form = PortForm(instance=port)

    return render(request, 'playground/ports_modify.html', {'form': form, 'disponibilite' : disponibilite, 'port' : port})

def delete_ports(request, pk):
    port = get_object_or_404(Port, pk=pk)
    port.delete()
    return redirect('ports_list')


def voyager(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid():
            # Récupère le bateau et le port sélectionnés
            bateau = form.cleaned_data['bateau']
            port_destination = form.cleaned_data['port_destination']
            
            # Vérifie si le bateau est déjà au port de destination
            if bateau.lieu == port_destination:
                messages.info(request, f"Le bateau {bateau.id_bateau} se trouve déjà dans le port sélectionné ({port_destination.id_port}).")
            else:
                # Change l'état du bateau et son lieu
                bateau.etat = 'en maintenance'
                bateau.lieu = port_destination
                bateau.save()
                
                # Message de confirmation après le voyage
                messages.success(request, f"Le bateau {bateau.id_bateau} est bien arrivé à destination ({port_destination.id_port}) et a besoin de quelques réparations.")
            
            # Redirige vers la page d'accueil
            return redirect('accueil')
    else:
        form = TravelForm()
    
    return render(request, 'playground/voyage.html', {'form': form})

def maintenance(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            # Récupère le bateau sélectionné
            bateau = form.cleaned_data['bateau']
            
            # Change l'état du bateau à "en service"
            bateau.etat = 'en service'
            bateau.save()
            
            # Message de confirmation
            messages.success(request, f"Le bateau {bateau.id_bateau} a été réparé avec succès et est maintenant en service.")
            
            # Redirige vers la page d'accueil
            return redirect('accueil')
    else:
        form = MaintenanceForm()
    
    return render(request, 'playground/maintenance.html', {'form': form})
