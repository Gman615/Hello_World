# Generated by Django 3.1.4 on 2020-12-03 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20201203_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='Prefix',
            field=models.CharField(choices=[('Ms', 'Ms'), ('Mr', 'Mr'), ('Mrs', 'Mrs')], default='---------', max_length=60),
        ),
    ]
