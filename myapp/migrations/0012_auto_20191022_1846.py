# Generated by Django 2.2.5 on 2019-10-22 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_user_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(null=True, upload_to='icons')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='icon',
        ),
    ]
