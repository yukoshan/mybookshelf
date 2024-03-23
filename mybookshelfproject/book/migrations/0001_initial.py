# Generated by Django 5.0.3 on 2024-03-10 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.TextField()),
                ('rate', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('category', models.CharField(choices=[('novel', '小説'), ('essay', 'エッセイ'), ('practical', '実用書')], default='-', max_length=100)),
                ('text', models.TextField(null=True)),
            ],
        ),
    ]
