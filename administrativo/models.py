from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    correo = models.EmailField()

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.apellido,
                self.cedula,
                self.correo)

    def get_provincia(self):
        """
        """
        dato = self.cedula[0:2]
        valor = "Sin Provincia"
        if dato == "11":
            valor = "Loja"
        else:
            if dato == "17":
                valor = "Pichincha"
        return valor

    def obtener_costo_telefonos(self):
        """
        """
        valor = 0
        for t in self.numeros_telefonicos.all():
            valor += t.valor_mensual
        return valor

    def obtener_num_telefonos(self):
        """
        """
        return self.numeros_telefonicos.count()


class NumeroTelefonico(models.Model):
    telefono = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE,
            related_name="numeros_telefonicos")
    valor_mensual = models.FloatField(default= 0.0)

    def __str__(self):
        return "%s %s" % (self.telefono, self.tipo)
