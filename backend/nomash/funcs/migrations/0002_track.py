# Generated by Django 4.2.3 on 2023-07-25 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.UUIDField(db_column='track_guid', primary_key=True, serialize=False)),
                ('time', models.IntegerField()),
                ('created', models.DateTimeField(blank=True, db_column='created', null=True)),
                ('updated', models.DateTimeField(blank=True, db_column='updated', null=True)),
                ('user', models.ForeignKey(blank=True, db_column='order_user', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tracks', to='funcs.user')),
            ],
            options={
                'db_table': 'track',
                'managed': True,
            },
        ),
    ]
