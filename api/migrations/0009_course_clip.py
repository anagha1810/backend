# Generated by Django 2.2.4 on 2019-08-19 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_course_clip'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='clip',
            field=models.URLField(max_length=250, null=True),
        ),
    ]
