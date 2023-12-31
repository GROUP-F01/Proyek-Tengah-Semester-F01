# Generated by Django 4.2.6 on 2023-10-28 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('publisher', models.CharField(blank=True, max_length=255, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
