# Generated by Django 4.2.7 on 2023-12-17 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shift_manager', '0002_alter_shift_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='Worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shift_manager.worker'),
        ),
    ]
