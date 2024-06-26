# Generated by Django 4.2 on 2024-03-22 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_category_post_category_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='user_name',
            field=models.CharField(default='', max_length=120, verbose_name='category name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=60, verbose_name='name'),
        ),
    ]
