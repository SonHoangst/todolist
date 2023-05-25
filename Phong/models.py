from django.db import models

# Create your models here.
class Phong(models.Model):
    maphong = models.AutoField(primary_key=True)
    sotang = models.IntegerField(default=0)
    tenphong = models.CharField(max_length=45, default="Phòng không có tên", unique=True)
    mota = models.TextField(default="", blank=True, null=True)
    
    def __str__(self):
        return f"{self.maphong}, {self.sotang}, {self.tenphong}"