# Generated by Django 4.0.5 on 2022-06-05 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Explanations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('tweet_id', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'explanations',
                'unique_together': {('id', 'text')},
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_id', models.CharField(max_length=200, unique=True)),
                ('list_name', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'list',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('token', models.TextField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Explanationusers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_id', models.IntegerField()),
                ('explanation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='questionnaireapp.explanations')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='questionnaireapp.users')),
            ],
            options={
                'db_table': 'explanationUsers',
            },
        ),
        migrations.CreateModel(
            name='Explanationlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('explnataion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='questionnaireapp.explanations')),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='questionnaireapp.list')),
            ],
            options={
                'db_table': 'explanationList',
                'unique_together': {('explnataion', 'list')},
            },
        ),
    ]
