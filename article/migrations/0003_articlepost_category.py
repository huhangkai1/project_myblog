# Generated by Django 2.1.7 on 2019-03-15 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_classification'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='article.Classification'),
            preserve_default=False,
        ),
    ]
