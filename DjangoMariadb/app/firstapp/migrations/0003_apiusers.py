# Generated by Django 3.0.3 on 2020-03-22 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('api_key', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'api_users',
                'managed': False,
            },
        ),
    ]