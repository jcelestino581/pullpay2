# Generated by Django 5.0.7 on 2024-10-04 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_first_name', models.CharField(max_length=200)),
                ('user_last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('payment_method', models.CharField(choices=[('VISA', 'Visa'), ('MASTERCARD', 'Mastercard'), ('DISCOVER', 'Discover'), ('AMEX', 'Amex'), ('NONE', 'None')], default='NONE', max_length=200)),
            ],
        ),
    ]
