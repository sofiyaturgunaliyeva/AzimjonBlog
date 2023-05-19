from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=100)
    matn = models.TextField()
    rasm = models.FileField()
    sana = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.sarlavha