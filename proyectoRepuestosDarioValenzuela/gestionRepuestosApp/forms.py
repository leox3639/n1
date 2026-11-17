from django import forms
from .models import Proveedor, OrdenServicio

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'razon_social': forms.TextInput(attrs={'class': 'form-control'}),
            'rut_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'contacto_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'sitio_web': forms.URLInput(attrs={'class': 'form-control'}),
            'rubro': forms.Select(attrs={'class': 'form-select'}),
            'plazo_entrega_dias': forms.NumberInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class OrdenServicioForm(forms.ModelForm):
    class Meta:
        model = OrdenServicio
        fields = '__all__'
        widgets = {
            'numero_orden': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_falla': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tipo_servicio': forms.Select(attrs={'class': 'form-select'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_estimada_entrega': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'costo_mano_obra': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_estimado': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'prioridad': forms.Select(attrs={'class': 'form-select'}),
            'observaciones_mecanico': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }