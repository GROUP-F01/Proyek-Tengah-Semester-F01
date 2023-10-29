# Generated by Django 4.2.6 on 2023-10-28 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20231026_0941'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jualbuku', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BukuUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.buku')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Jual',
        ),
    ]
