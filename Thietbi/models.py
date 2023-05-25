from django.db import models
from Phong.models import Phong
from Loai.models import Loai
from datetime import datetime

# Create your models here.
class Thietbi(models.Model):
    mathietbi = models.AutoField(primary_key=True)
    maphong = models.ForeignKey(Phong, on_delete=models.CASCADE)
    tenloai = models.ForeignKey(Loai, on_delete=models.CASCADE)
    tenthietbi = models.CharField(max_length=45, default="Không xác định")
    giamua = models.IntegerField(default=0)
    ngaymua = models.DateTimeField(default=datetime.now())
    ngaythem =  models.DateTimeField(auto_now_add=True)
    thoigianbaohanh = models.IntegerField(default=0)
    mota = models.TextField(default="", blank=True, null=True)
    
    def __str__(self):
        return f"{self.mathietbi}, {self.maphong}, {self.tenloai}, {self.tenthietbi}, {self.giamua}, {self.ngaymua}, {self.ngaythem}, {self.thoigianbaohanh}"