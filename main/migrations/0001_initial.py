# Generated by Django 5.0.6 on 2024-07-04 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(1, 'Yaratildi'), (2, "To'landi"), (3, 'Bekor qilindi')], default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Order Payment',
                'verbose_name_plural': 'Order Payments',
            },
        ),
    ]
