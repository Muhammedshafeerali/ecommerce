# Generated by Django 3.1.2 on 2020-10-06 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod', '0022_auto_20201005_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='value',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(choices=[('Apparel', 'Apparel'), ('Acessories', 'Acessories')], max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('jeans', 'jeans'), ('shoe', 'shoe'), ('t-shirt', 't-shirt'), ('pant', 'pant'), ('shirt', 'shirt'), ('sunglass', 'sunglass')], max_length=300),
        ),
    ]
