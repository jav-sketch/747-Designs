# Generated by Django 3.1 on 2020-08-20 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Design_Site', '0003_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
