# Generated by Django 4.0.4 on 2022-06-07 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0003_eventos_alter_entradas_blog_imagen_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entradas_blog',
            new_name='Blog',
        ),
    ]
