# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-05 02:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='area_conocimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('estatus', models.TextField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='canal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('estatus', models.TextField(max_length=1)),
                ('area', models.ManyToManyField(to='redsocial.area_conocimiento')),
            ],
        ),
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='seguimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seguidor', models.TextField()),
                ('id_seguido', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id_usuario', models.TextField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('apellido', models.TextField()),
                ('carrera', models.TextField()),
                ('promocion', models.TextField()),
                ('sexo', models.TextField()),
                ('fecha_nacimiento', models.DateField()),
                ('correo', models.TextField(unique=True)),
                ('telefono', models.TextField(max_length=11)),
                ('clave', models.TextField()),
                ('estatus', models.TextField(max_length=1)),
                ('imagen', models.ImageField(null=True, upload_to='')),
                ('area', models.ManyToManyField(to='redsocial.area_conocimiento')),
            ],
        ),
        migrations.AddField(
            model_name='publicacion',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publicacion', to='redsocial.usuario'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to='redsocial.usuario'),
        ),
        migrations.AddField(
            model_name='canal',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='canal', to='redsocial.usuario'),
        ),
    ]
