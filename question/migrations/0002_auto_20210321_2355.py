# Generated by Django 2.0.13 on 2021-03-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='num',
            new_name='num1',
        ),
        migrations.AddField(
            model_name='question',
            name='num2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='num3',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='num4',
            field=models.CharField(max_length=20, null=True),
        ),
    ]