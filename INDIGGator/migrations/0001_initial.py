# Generated by Django 4.0.4 on 2022-05-28 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=255)),
                ('walletAddress', models.CharField(max_length=255)),
                ('referralCode', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
