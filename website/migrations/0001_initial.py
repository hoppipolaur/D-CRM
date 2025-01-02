# Generated by Django 5.1.4 on 2025-01-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=10)),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
    ]
