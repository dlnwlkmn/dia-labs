# Generated by Django 3.1.5 on 2021-01-05 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Partnership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=200, verbose_name='Цель партнерства')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DZApp.partner')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100, verbose_name='Название продукта')),
                ('expire_time', models.IntegerField(verbose_name='Годен дней')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('phone', models.IntegerField(verbose_name='Телефон')),
                ('partners', models.ManyToManyField(through='DZApp.Partnership', to='DZApp.Partner')),
            ],
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название таблицы')),
            ],
        ),
        migrations.CreateModel(
            name='Waybill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('destination', models.CharField(max_length=150, verbose_name='Пункт назначения')),
                ('date', models.DateField(verbose_name='Дата')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DZApp.product')),
                ('provider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DZApp.provider')),
            ],
        ),
        migrations.AddField(
            model_name='partnership',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DZApp.provider'),
        ),
    ]