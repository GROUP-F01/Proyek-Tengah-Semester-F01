# Generated by Django 4.2.4 on 2023-12-11 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart_checkout', '0005_belibuku_buku_alter_keranjang_list_buku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='belibuku',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
