# Generated by Django 4.2.6 on 2024-02-07 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('School_name', models.CharField(max_length=100)),
                ('Scl_principal', models.CharField(max_length=100)),
            ],
        ),
    ]
