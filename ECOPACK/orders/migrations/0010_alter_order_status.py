# Generated by Django 4.1.2 on 2022-11-20 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Готовится', 'Готовится'), ('Доставляется', 'Доставляется'), ('Выполнен', 'Выполнен')], default=0, max_length=15, null=True),
        ),
    ]
