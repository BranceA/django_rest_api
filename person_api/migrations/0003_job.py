# Generated by Django 3.2.3 on 2021-05-27 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person_api', '0002_auto_20210525_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person_api.person')),
            ],
        ),
    ]