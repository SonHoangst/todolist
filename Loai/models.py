from django.db import models

# Create your models here.
class Loai(models.Model):
    maloai = models.AutoField(primary_key=True)
    tenloai = models.CharField(max_length=45, default="Chưa phân loại", unique=True)
    mota = models.TextField(default="", blank=True, null=True)
    
    def __str__(self):
        return f"{self.maloai}, {self.tenloai}"