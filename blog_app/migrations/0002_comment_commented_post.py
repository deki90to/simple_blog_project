# Generated by Django 4.0.3 on 2022-10-13 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commented_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog_app.post'),
        ),
    ]
