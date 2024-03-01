# Generated by Django 3.2 on 2023-12-05 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_text', models.TextField()),
                ('corrected_text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='posts',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
