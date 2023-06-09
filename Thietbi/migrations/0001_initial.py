# Generated by Django 4.1.7 on 2023-04-08 19:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Loai', '0001_initial'),
        ('Phong', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThietBi',
            fields=[
                ('mathietbi', models.AutoField(primary_key=True, serialize=False)),
                ('tenthietbi', models.CharField(default='Không xác định', max_length=45)),
                ('giamua', models.IntegerField(default=0)),
                ('ngaymua', models.DateTimeField(default=datetime.datetime(2023, 4, 9, 2, 13, 49, 260760))),
                ('ngaythem', models.DateTimeField(auto_now_add=True)),
                ('thoigianbaohanh', models.IntegerField(default=0)),
                ('mota', models.TextField(blank=True, default='', null=True)),
                ('maphong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Phong.phong')),
                ('tenloai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Loai.loai')),
            ],
        ),
    ]
