# Generated by Django 4.0.4 on 2022-05-21 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0002_tag_space_remove_tag_tags_tag_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='space',
        ),
        migrations.AddField(
            model_name='space',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='spaces.tag'),
        ),
    ]
