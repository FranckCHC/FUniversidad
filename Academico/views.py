from django.shortcuts import render, redirect
from .models import Curso

# Create your views here.
def home(request):
    cursoListado = Curso.objects.all()
    return render(request, 'gestioncursos.html', {'cursos': cursoListado})
def eliminarCurso(request, id):
    curso = Curso.objects.get(id = id)
    curso.delete()
    return redirect('/')
 
def registrarCurso(request):
    nombre = request.POST['txtnombre']
    creditos = request.POST['numcreditos']
    curso = Curso.objects.create(nombre = nombre, creditos = creditos)
    return redirect('/')


