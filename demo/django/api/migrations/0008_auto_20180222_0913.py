# Generated by Django 2.0.2 on 2018-02-22 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20180221_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='m2m',
            field=models.ManyToManyField(related_name='_testmodel_m2m_+', to='api.City'),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='foreign_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.City'),
        ),
    ]
