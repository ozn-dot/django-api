from django.db import models

# esta clase hereda de models.Model
# por defecto django le da a cada modelo el siguiente campo
# id = models.AutoField(primary_key=True)

class Note(models.Model):

    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True)
    # por simplicidad lo pongo como texto y no como FileField
    adjunto = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(
            'User',
            on_delete=models.CASCADE,
            null=True
    )
    task_choices = [
            (True, 'Yes'),
            (False, 'No'),
    ]
    task = models.BooleanField(choices=task_choices, blank=True, null=True)
    # probablmente en un caso real el modelo tag debería ser ManyToManyField, lo dejo como Char para simplificar
    tag = models.CharField(max_length=15, blank=True, null=True)
    type_choices = [
            ('Primero', 'Tipo1'),
            ('Segundo', 'Tipo2'),
            ('Tercero', 'Tipo3'),
    ]
    type = models.CharField(
            max_length=15,
            choices=type_choices,
            default='Primero',   
    )

    class Meta: 
        ordering = ['-date']

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    # para que el panel admin de django muestre el nombre en vez del objeto y se vean los nombres de los usuarios en el desplegable   
    def __str__(self):
            return self.name