# Generated by Django 4.2.7 on 2023-12-31 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderpic',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='sliders/'),
        ),
    ]