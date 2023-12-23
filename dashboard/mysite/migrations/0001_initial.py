# Generated by Django 5.0 on 2023-12-23 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=255)),
                ('agency', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('ยังไม่ได้ดำเนินการ', 'In plan'), ('ส่ง สจล.', 'Submit Project'), ('ดำเนินการแล้ว', 'Project finish')], max_length=20, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=15, null=True)),
                ('withdraw', models.DecimalField(decimal_places=2, max_digits=15, null=True)),
            ],
        ),
    ]