# Generated by Django 4.0.2 on 2022-02-07 05:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=10)),
                ('state', models.CharField(choices=[('Alabama, AL', 'Alabama'), ('Añaska, AK', 'Alaska'), ('Arizona, AZ', 'Arizona'), ('Arkansas, AR', 'Arkansas'), ('California, CA', 'California'), ('Colorado, CO', 'Colorado'), ('Connecticut, CT', 'Connecticut'), ('Delaware, DE', 'Delaware'), ('Tennessee, TN', 'Tennessee'), ('Texas, TX', 'Texas'), ('Utah, UT', 'Utah'), ('Vermont, VT', 'Vermont'), ('Virginia, VA', 'Virginia'), ('Washington, WA', 'Washington'), ('West Virginia, WV', 'West Virginia'), ('Wisconsin, WI', 'Wisconsin'), ('Wyoming, WY', 'Wyoming')], default='Alabama, AL', max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('other', models.CharField(max_length=50)),
                ('start_date', models.CharField(max_length=25)),
                ('end_date', models.CharField(max_length=25)),
                ('category', models.CharField(max_length=25)),
                ('list_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'crud_app',
            },
        ),
    ]
