# Generated by Django 3.2.20 on 2024-01-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=254, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('latitude', models.TextField(blank=True, default='', null=True)),
                ('longitude', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MemberSerializers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
