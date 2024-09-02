# Generated by Django 3.2.4 on 2022-09-03 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_myproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='maincate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('picture', models.ImageField(null=True, upload_to='static/mcategory')),
                ('cdata', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='myproduct',
            name='mcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.maincate'),
        ),
    ]
