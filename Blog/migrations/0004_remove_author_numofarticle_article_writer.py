# Generated by Django 4.0.2 on 2022-02-15 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_author_numofarticle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='numofarticle',
        ),
        migrations.AddField(
            model_name='article',
            name='writer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Blog.author'),
            preserve_default=False,
        ),
    ]
