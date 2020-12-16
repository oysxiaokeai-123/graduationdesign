# Generated by Django 3.1.2 on 2020-11-07 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.CharField(max_length=18)),
                ('seller', models.CharField(max_length=18)),
                ('status', models.IntegerField()),
                ('comment', models.CharField(max_length=200)),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Model.commodity')),
            ],
        ),
    ]
