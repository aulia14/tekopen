# Generated by Django 2.2 on 2019-04-20 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190420_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='alamat',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='jadwal',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='no_telp',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profesi',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='status',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='temlahir',
        ),
    ]