from django.shortcuts import render
from .models import Thietbi as Thietbi_model
from Phong.models import Phong as Phong_model

# Create your views here.
def get_thietbi(request, id):
    thietbi_list = Thietbi_model.objects.filter(maphong = id)
    phong = Phong_model.objects.get(maphong = id)
    return render(request, "Thietbi/danhsachthietbi.html", {"thietbi_list": thietbi_list, "phong": phong})