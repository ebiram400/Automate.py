from django.db import models

# Create your models here.
class users(models.Model):
    GEN_CHOICE=(
        ('f','famel'),
        ('m','mel')
    )
    name=models.CharField(default="کاربر ناشناس",max_length=20)
    age=models.IntegerField()
    gen=models.CharField(max_length=1,choices=GEN_CHOICE)
    created=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="images", height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.name
    