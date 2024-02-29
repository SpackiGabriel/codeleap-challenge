# Generated by Django 5.0.2 on 2024-02-29 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
        ),
    ]
