from django.db import models


class Proveedor(models.Model):
    """Modelo que representa a las empresas proveedoras de la maestranza."""
    
    RUBRO_CHOICES = [
        ('LUBRICANTES', 'Lubricantes'),
        ('FRENOS_SUSPENSION', 'Frenos y suspensión'),
        ('HERRAMIENTAS_ELECTRICAS', 'Herramientas eléctricas'),
        ('TORNILLERIA', 'Tornillería'),
    ]

    razon_social = models.CharField(
        max_length=150, 
        verbose_name="Razón Social"
    )
    rut_empresa = models.CharField(
        max_length=12, 
        unique=True, 
        verbose_name="RUT Empresa"
    )
    contacto_nombre = models.CharField(
        max_length=100, 
        verbose_name="Nombre de Contacto"
    )
    correo = models.EmailField(
        verbose_name="Correo Corporativo"
    )
    telefono = models.CharField(
        max_length=20, 
        verbose_name="Teléfono"
    )
    direccion = models.CharField(
        max_length=255, 
        verbose_name="Dirección Física"
    )
    sitio_web = models.URLField(
        blank=True, 
        null=True, 
        verbose_name="Sitio Web"
    )
    rubro = models.CharField(
        max_length=40, 
        choices=RUBRO_CHOICES, 
        verbose_name="Rubro"
    )
    plazo_entrega_dias = models.IntegerField(
        verbose_name="Plazo de Entrega (Días Hábiles)"
    )
    activo = models.BooleanField(
        default=True, 
        verbose_name="Convenio Activo"
    )

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['razon_social']

    def __str__(self):
        return f"{self.razon_social} ({self.rut_empresa})"


class OrdenServicio(models.Model):
    """Modelo que registra las órdenes de servicio técnico de la maestranza."""

    TIPO_SERVICIO_CHOICES = [
        ('PREVENTIVO', 'Mantenimiento preventivo'),
        ('REPARACION_MAYOR', 'Reparación mayor'),
        ('DIAGNOSTICO_ELEC', 'Diagnóstico eléctrico'),
        ('ALINEACION', 'Alineación'),
    ]

    ESTADO_CHOICES = [
        ('RECIBIDO', 'Recibido'),
        ('EN_PROCESO', 'En proceso'),
        ('ESPERA_REPUESTOS', 'En espera de repuestos'),
        ('FINALIZADO', 'Finalizado'),
        ('ENTREGADO', 'Entregado'),
    ]

    PRIORIDAD_CHOICES = [
        ('BAJA', 'Baja'),
        ('NORMAL', 'Normal'),
        ('URGENTE', 'Urgente'),
    ]

    numero_orden = models.CharField(
        max_length=20, 
        unique=True, 
        verbose_name="Número de Orden"
    )
    descripcion_falla = models.TextField(
        verbose_name="Descripción de Falla / Trabajo"
    )
    tipo_servicio = models.CharField(
        max_length=30, 
        choices=TIPO_SERVICIO_CHOICES, 
        verbose_name="Tipo de Servicio"
    )
    fecha_ingreso = models.DateField(
        verbose_name="Fecha de Ingreso"
    )
    fecha_estimada_entrega = models.DateField(
        verbose_name="Fecha Estimada de Entrega"
    )
    costo_mano_obra = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        verbose_name="Costo Mano de Obra"
    )
    total_estimado = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        verbose_name="Total Estimado"
    )
    estado = models.CharField(
        max_length=25, 
        choices=ESTADO_CHOICES, 
        default='RECIBIDO', 
        verbose_name="Estado de la Orden"
    )
    prioridad = models.CharField(
        max_length=15, 
        choices=PRIORIDAD_CHOICES, 
        default='NORMAL', 
        verbose_name="Prioridad"
    )
    observaciones_mecanico = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Observaciones del Mecánico"
    )

    class Meta:
        verbose_name = "Orden de Servicio"
        verbose_name_plural = "Órdenes de Servicio"
        ordering = ['-fecha_ingreso']

    def __str__(self):
        return f"Orden {self.numero_orden} - {self.get_estado_display()}"