# Generated by Django 4.2.6 on 2023-11-27 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sending', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sending',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sending.sending'),
        ),
    ]
