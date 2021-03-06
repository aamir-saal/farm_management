# Generated by Django 3.0.8 on 2020-07-25 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0002_auto_20200725_2051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='farm',
            options={'permissions': (('can_view_farm', 'Can View Farm'),), 'verbose_name': 'Farm', 'verbose_name_plural': 'Farms'},
        ),
        migrations.AlterField(
            model_name='farm',
            name='name',
            field=models.CharField(max_length=550, verbose_name='farm Name'),
        ),
    ]
