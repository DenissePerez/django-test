from django.core.validators import RegexValidator
from django.db import models
#from django.contrib.gis.db import models

class Solicitante(models.Model):
    id_solicitante = models.CharField(primary_key=True, max_length=30, validators=[RegexValidator(r'^\d{1,30}$')])
    nombre = models.CharField(max_length=200)
    cedula = models.IntegerField()
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)



class Coordinacion(models.Model):
    id_coordinacion = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Anexos(models.Model):
    id_anexo = models.CharField(primary_key=True, max_length=12)
    nombre = models.CharField(max_length=200)
    anexo = models.FilePathField(null=True)


class Acta(models.Model):
    id_acta = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=300)
    acta = models.FilePathField(null=True)


class Ficha_individuo(models.Model):
    id_arbol = models.CharField(primary_key=True, max_length=8)
    #coordenadas!!! geodjango con point
    #coordenadas = Point(x=...., y=...., z=0, srid=....) #LocationPoint()
    latitud = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    longitud = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    nombre = models.CharField(max_length=100)
    familia = models.CharField(max_length=100)
    estado = models.CharField(max_length=300)
    altura = models.FloatField()
    dap = models.FloatField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)


class Coordinador(models.Model):
    id_coordinador = models.CharField(primary_key=True, max_length=12, validators=[RegexValidator(r'^\d{1,12}$')])
    id_coordinacion = models.ForeignKey(Coordinacion, blank=True, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=10)
    def __str__(self):
        return self.nombre


class Tecnico(models.Model):
    id_tecnico = models.CharField(primary_key=True, max_length=12, validators=[RegexValidator(r'^\d{1,12}$')])
    id_coordinacion = models.ForeignKey(Coordinacion, blank=True, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=10)

    # Lo que me va a retornar al hacer un query, para que deje de ser "objeto <tecnico>"
    def __str__(self):
        return self.nombre
        # Necesito nombre de la solicitud!!!! D:


class Solicitud(models.Model):
    id_solicitud = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=200)  # Agregar en el modelo!!! Importante!!!!
    id_solicitante = models.ForeignKey(Solicitante, blank=True, null=True, on_delete=models.CASCADE)
    id_tecnico = models.ForeignKey(Tecnico, blank=True, null=True, on_delete=models.CASCADE)
    id_coordinador = models.ForeignKey(Coordinador, blank=True, null=True, on_delete=models.CASCADE)
    id_anexo = models.ForeignKey(Anexos, blank=True, null=True, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100, default=' ')
    barrio = models.CharField(max_length=100, default=' ')
    municipio = models.CharField(max_length=100, default=' ')
    fecha = models.DateField(blank=True, null=True)  # Agregar!

    def __str__(self):
        return self.id_solicitud


class Visita(models.Model):
    id_visita = models.CharField(primary_key=True, max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])
    detalles = models.CharField(max_length=300)
    id_arbol = models.ForeignKey(Ficha_individuo, blank=True, null=True, on_delete=models.CASCADE)
    id_acta = models.ForeignKey(Acta, on_delete=models.CASCADE)
    id_solicitud = models.ForeignKey(Solicitud, blank=True, null=True, on_delete=models.CASCADE)
    id_tecnico = models.ForeignKey(Tecnico, blank=True, null=True, on_delete=models.CASCADE)
    fecha = models.DateField()


class Expediente(models.Model):
    id_expediente = models.CharField(primary_key=True, max_length=5, validators=[RegexValidator(r'^\d{1,5}$')])
    id_solicitud = models.ForeignKey(Solicitud, blank=True, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    resolucion = models.CharField(max_length=12, blank=True, null=True)
    autorizacion = models.CharField(max_length=12, blank=True, null=True)


class Informe_tecnico(models.Model):
    id_informe = models.CharField(primary_key=True, max_length=8, validators=[RegexValidator(r'^\d{1,8}$')])
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    Informe = models.FilePathField(null=True)


class Balance(models.Model):
    id_balance = models.CharField(primary_key=True, max_length=8, validators=[RegexValidator(r'^\d{1,8}$')])
    descripcion = models.CharField(max_length=200)
    valor_compensado = models.DecimalField(max_digits=8, decimal_places=2)
    valor_afectacion = models.DecimalField(max_digits=8, decimal_places=2)
    valor_balance = models.DecimalField(max_digits=8, decimal_places=2)


class Seguimiento(models.Model):
    id_seguimiento = models.CharField(primary_key=True, max_length=8, validators=[RegexValidator(r'^\d{1,8}$')])
    id_balance = models.ForeignKey(Balance, blank=True, null=True, on_delete=models.CASCADE)
    id_visita = models.ForeignKey(Visita, blank=True, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    adjunto = models.FilePathField(null=True)


