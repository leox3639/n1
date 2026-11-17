from django.contrib import admin
from .models import Proveedor, OrdenServicio

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    # Columnas visibles en la lista del panel
    list_display = ('razon_social', 'rut_empresa', 'contacto_nombre', 'rubro', 'plazo_entrega_dias', 'activo')
    
    # Filtros laterales para la búsqueda y control
    list_filter = ('rubro', 'activo')
    
    # Campos habilitados para la barra de búsqueda
    search_fields = ('razon_social', 'rut_empresa', 'contacto_nombre', 'correo')

@admin.register(OrdenServicio)
class OrdenServicioAdmin(admin.ModelAdmin):
    # Columnas visibles para las órdenes de servicio
    list_display = ('numero_orden', 'tipo_servicio', 'fecha_ingreso', 'fecha_estimada_entrega', 'prioridad', 'total_estimado', 'estado')
    
    # Filtros laterales de estado, prioridad y tipo de servicio
    list_filter = ('estado', 'prioridad', 'tipo_servicio')
    
    # Búsqueda por número de orden o descripción
    search_fields = ('numero_orden', 'descripcion_falla')