# Generated by Django 2.1.5 on 2019-02-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='doc_file',
            field=models.FileField(blank=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
    ]
