# Generated by Django 4.0.6 on 2022-07-20 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingSlot',
            fields=[
                ('parking_slot_id', models.AutoField(primary_key=True, serialize=False)),
                ('responsible_name', models.CharField(max_length=70)),
                ('car', models.CharField(max_length=70)),
                ('apartment', models.CharField(max_length=10)),
                ('block', models.CharField(max_length=10)),
            ],
        ),
    ]
