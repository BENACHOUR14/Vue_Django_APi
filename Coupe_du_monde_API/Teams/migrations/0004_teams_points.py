# Generated by Django 4.1.4 on 2023-01-19 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teams', '0003_alter_teams_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='points',
            field=models.CharField(default=0, max_length=1),
            preserve_default=False,
        ),
    ]