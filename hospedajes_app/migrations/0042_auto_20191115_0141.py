# Generated by Django 2.2.6 on 2019-11-15 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospedajes_app', '0041_remove_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospedajes_app.Host'),
        ),
    ]
