# Generated by Django 5.0.6 on 2024-06-24 19:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile_page', '0007_liked_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile_page.profile')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile_page.post')),
            ],
        ),
    ]