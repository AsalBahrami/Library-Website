# Generated by Django 3.1.4 on 2021-03-06 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0005_auto_20210306_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setup2',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]