# Generated by Django 2.2.28 on 2024-11-17 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bateau',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='bateaux/'),
        ),
        migrations.AlterField(
            model_name='port',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='ports/'),
        ),
    ]
