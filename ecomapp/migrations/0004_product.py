# Generated by Django 2.1.7 on 2019-04-24 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0003_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('available', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.Category')),
            ],
        ),
    ]
