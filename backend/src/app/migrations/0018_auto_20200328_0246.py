# Generated by Django 2.2.6 on 2020-03-28 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20200328_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherprofile',
            name='avatar',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='user_type',
            field=models.CharField(default='teacher', max_length=200),
        ),
    ]
