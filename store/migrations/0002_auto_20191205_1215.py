# Generated by Django 3.0 on 2019-12-05 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producer',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('price', models.FloatField(default=0)),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Producer')),
            ],
        ),
    ]
