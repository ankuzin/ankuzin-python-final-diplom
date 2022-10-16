# Generated by Django 4.0.1 on 2022-02-06 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_user_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='file',
        ),
        migrations.AddField(
            model_name='category',
            name='cat_id',
            field=models.PositiveIntegerField(max_length=10, null=True, verbose_name='ИД категории'),
        ),
        migrations.CreateModel(
            name='ShopFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='uploaded_data')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.shop')),
            ],
        ),
    ]