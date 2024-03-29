# Generated by Django 4.0.6 on 2023-06-06 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderTracker',
            fields=[
                ('updateId', models.AutoField(primary_key=True, serialize=False)),
                ('updateDesc', models.CharField(max_length=1000)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
            ],
        ),
    ]
