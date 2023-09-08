# Generated by Django 4.2.5 on 2023-09-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=64)),
                ('publico', models.TextField(null=True)),
                ('descricao', models.TextField(null=True)),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, null=True, verbose_name='order')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
