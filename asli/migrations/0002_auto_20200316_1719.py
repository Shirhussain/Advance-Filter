# Generated by Django 3.0.2 on 2020-03-16 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asli', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roznama',
            name='publish_date',
            field=models.DateTimeField(),
        ),
    ]
