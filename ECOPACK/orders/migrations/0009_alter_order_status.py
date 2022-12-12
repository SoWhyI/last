# Generated by Django 4.1.2 on 2022-11-20 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_order_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[(0, 'Готовится'), (1, 'Доставляется'), (2, 'Выполнен')], default=0, max_length=15, null=True),
        ),
    ]
