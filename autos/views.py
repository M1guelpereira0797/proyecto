from django.shortcuts import render
from autos.models import Vehiculo
from autos.forms import Buscar
from django.views import View 

def index(request):
    return render(request, "Carros/Presentacion_de_carros.html")

def buscar_carros(resquest):
    lista_de_marca_de_carros=["Mercedes", "Ferrari", "Lamborgini", "Mclaren", "Chevrolet"]
    query=resquest.GET["q"]
    if query in lista_de_marca_de_carros:
        indice_de_resultado = lista_de_marca_de_carros.index(query)
        resultado=lista_de_marca_de_carros[indice_de_resultado]
    else: 
        resultado= "no hay registro en la base de datos"
    return render(resquest, 
    "autos/buscar_carros.html",
    {"resultado": resultado})

def mostrar_carros(request):
  lista_carros = Vehiculo.objects.all()
  return render(request, "autos/Carros.html", {"lista_carros": lista_carros})

class BuscarCarro(View):
    form_class = Buscar
    template_name = 'autos/Carros.html'
    initial = {"Marca":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("Marca")
            lista_carros = Vehiculo.objects.filter(marca__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_carros':lista_carros})
        return render(request, self.template_name, {"form": form})