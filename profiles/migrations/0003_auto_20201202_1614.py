# Generated by Django 3.1.4 on 2020-12-02 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20201202_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='Prefix',
            field=models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], default='---------', max_length=60),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='Email',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='First_Name',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='Last_Name',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='Username',
            field=models.CharField(default='', max_length=60),
        ),
    ]
