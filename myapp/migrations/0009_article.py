# Generated by Django 2.2.5 on 2019-10-21 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_delete_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('brief_content', models.TextField()),
                ('content', models.TextField()),
                ('publish_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]