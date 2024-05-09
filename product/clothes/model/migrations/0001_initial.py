# Generated by Django 4.0.1 on 2024-04-08 08:48

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.PositiveBigIntegerField()),
                ('old_price', models.PositiveBigIntegerField(blank=True, default=None, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('status', models.PositiveIntegerField(default=1)),
                ('quantity', models.PositiveBigIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.PositiveBigIntegerField(default=0)),
                ('categories', models.ManyToManyField(to='category.Category')),
            ],
            options={
                'verbose_name_plural': 'Clothes',
                'db_table': 'clothes',
            },
        ),
    ]