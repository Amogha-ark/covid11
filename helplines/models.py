from django.db import models

# Create your models here.
class Allocated(models.Model):
    TYPE = (
        ('GOVT','Government'),
        ('PRIV','Private'),
    )
    name = models.CharField(max_length=50)
    hositalType = models.CharField(max_length=10, choices=TYPE)
    hdu = models.IntegerField()
    oxygenated = models.IntegerField()
    ventilators = models.IntegerField()
    icu = models.IntegerField()
    normal = models.IntegerField()
    total = models.IntegerField()
    ahdu = models.IntegerField()
    aoxygenated = models.IntegerField()
    aventilators = models.IntegerField()
    aicu = models.IntegerField()
    anormal = models.IntegerField()
    atotal = models.IntegerField()

    def __str__(self):
        return self.name
