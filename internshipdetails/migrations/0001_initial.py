# Generated by Django 5.0.1 on 2024-02-22 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('college_name', models.CharField(max_length=255)),
                ('nationality', models.CharField(choices=[('1', 'Iran'), ('2', 'England'), ('3', 'USA'), ('4', 'Germanny'), ('5', 'France'), ('6', 'SouthKorea')], default='USA', max_length=255)),
                ('offer_status', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField(auto_now=True)),
                ('end_date', models.DateTimeField(auto_now=True)),
                ('proj_report', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
