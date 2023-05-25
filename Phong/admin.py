from django.contrib import admin
from Phong.models import Phong
from Loai.models import Loai
from Thietbi.models import Thietbi

# Register your models here.
class TablePhong(admin.ModelAdmin):
    list_display = ("maphong", "sotang", "tenphong", "mota")
    search_fields = ["tenphong"]
    list_filter = ("maphong", "sotang", "tenphong", "mota")

class TableLoai(admin.ModelAdmin):
    list_display = ("maloai", "tenloai", "mota")
    search_fields = ["tenloai"]
    list_filter = ("maloai", "tenloai", "mota")
    
class TableThietBi(admin.ModelAdmin):
    list_display = ("mathietbi", "maphong", "tenloai", "tenthietbi", "mathietbi", "giamua", "ngaymua", "ngaythem", "thoigianbaohanh", "mota")
    search_fields = ["tenloai"]
    list_filter = ("mathietbi", "maphong", "tenloai", "tenthietbi", "mathietbi", "giamua", "ngaymua", "ngaythem", "thoigianbaohanh", "mota")

admin.site.register(Phong, TablePhong)
admin.site.register(Loai, TableLoai)
admin.site.register(Thietbi, TableThietBi)