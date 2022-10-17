from tkinter.ttk import Style
from django import forms

class investigaciones(forms.Form):

    nombre_dominio = forms.CharField(max_length=40, help_text='Nombre del dominio.')
    creador_investigacion = forms.CharField(max_length=40, help_text='Creador/es de la investigación.')
    nombre_investigacion = forms.CharField(max_length=40, help_text='Nombre de la investigación.')
    fecha_investigacion = forms.DateField(help_text='Fecha de la investigación.')
    resumen_investigacion = forms.CharField(max_length= 500, help_text='Breve descripción de la investigación.')
    # investigation_media = 

class errores(forms.Form):

    dominio_error = forms.CharField(max_length= 20, help_text='Nombre o código del error.')
    fecha_error = forms.DateField(help_text='Fecha en la que ocurrió el error.')
    reportante_error = forms.CharField(max_length= 40, help_text='Nombre o TAG del colaborador.')
    descripcion_error = forms.CharField(max_length= 500, help_text='Descripción del error.')
    #bugs_media = models.

class refuerzos(forms.Model):

    creador_tips = forms.CharField(max_length= 80, help_text='Nombre creador/es del refuerzo.')
    nombre_tips = forms.CharField(max_length= 250, help_text='Tema del refuerzo.')
    descripcion_tips = forms.CharField(max_length= 500, help_text='Breve descripción del refuerzo.')
    fecha_tips = forms.DateField(help_text='Fecha del refuerzo.')
    email_tips = forms.EmailField(help_text='Correo electrónico del creador/es.')
    #media_tips = 
    link_tips = forms.URLField(help_text='Link a la presentación del refuerzo.')