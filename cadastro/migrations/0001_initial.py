# Generated by Django 3.0.2 on 2020-01-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outros')], max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('idade', models.IntegerField()),
            ],
        ),
    ]