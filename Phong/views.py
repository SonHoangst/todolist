from django.shortcuts import render
from .models import Phong as Phong_model


# Create your views here.
def get_phong(request):
    phong_list = Phong_model.objects.filter().order_by("maphong")
    return render(request, "Phong/danhsachphong.html", {"phong_list": phong_list})