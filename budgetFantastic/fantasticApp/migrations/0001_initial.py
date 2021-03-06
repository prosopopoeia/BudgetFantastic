# Generated by Django 3.0.2 on 2020-01-23 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('monthly_total', models.DecimalField(decimal_places=2, default=0, max_digits=11)),
                ('total_entries', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Overall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grandTotal', models.DecimalField(decimal_places=2, default=0, max_digits=11)),
                ('montlyTotal', models.DecimalField(decimal_places=2, default=0, max_digits=11)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=11)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fantasticApp.Category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='overallTotals',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fantasticApp.Overall'),
        ),
        migrations.AddField(
            model_name='category',
            name='owningUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fantasticApp.User'),
        ),
    ]
