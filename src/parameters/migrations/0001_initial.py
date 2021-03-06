# Generated by Django 2.2 on 2019-06-03 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Etnic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameEtnic', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StatusMarital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameMaritalStatus', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TypeAchievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameAchievementsType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TypePosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namePositionType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TypeStudies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameStudiesType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TypeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=50)),
            ],
        ),
    ]
