# Generated by Django 3.1.4 on 2020-12-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setup2',
            fields=[
                ('auflagen', models.CharField(blank=True, db_column='Auflagen', max_length=255, null=True)),
                ('author', models.CharField(blank=True, db_column='Author', max_length=255, null=True)),
                ('bemerkug', models.TextField(blank=True, db_column='Bemerkug', null=True)),
                ('betreuer', models.CharField(blank=True, db_column='Betreuer', max_length=255, null=True)),
                ('dk_kennzeichnung', models.CharField(blank=True, db_column='DK_Kennzeichnung', max_length=50, null=True)),
                ('dk_nummer', models.FloatField(blank=True, db_column='DK_nummer', null=True)),
                ('dk_etikett_buch', models.CharField(blank=True, db_column='DK_Etikett_Buch', max_length=255, null=True)),
                ('dk_etikett_andere', models.TextField(blank=True, db_column='DK_Etikett_Andere', null=True)),
                ('entleiher', models.CharField(blank=True, db_column='Entleiher', max_length=100, null=True)),
                ('entleiher_bem', models.TextField(blank=True, db_column='Entleiher_Bem', null=True)),
                ('erfasserkuerzel', models.CharField(blank=True, db_column='Erfasserkuerzel', max_length=25, null=True)),
                ('erscheinungsdatum', models.CharField(blank=True, db_column='Erscheinungsdatum', max_length=50, null=True)),
                ('erscheinungsjahr', models.IntegerField(blank=True, db_column='Erscheinungsjahr', null=True)),
                ('erscheinungsort', models.CharField(blank=True, db_column='Erscheinungsort', max_length=50, null=True)),
                ('inventarnummer', models.CharField(blank=True, db_column='Inventarnummer', max_length=255, null=True)),
                ('isbn_nummer', models.CharField(blank=True, db_column='ISBN_Nummer', max_length=100, null=True)),
                ('sprache', models.CharField(blank=True, db_column='Sprache', max_length=25, null=True)),
                ('standort', models.CharField(blank=True, db_column='Standort', max_length=50, null=True)),
                ('titel', models.TextField(blank=True, db_column='Titel', null=True)),
                ('dokumenttyp', models.CharField(blank=True, db_column='Dokumenttyp', max_length=50, null=True)),
                ('verlag', models.CharField(blank=True, db_column='Verlag', max_length=25, null=True)),
                ('verlagsnummer', models.CharField(blank=True, db_column='Verlagsnummer', max_length=255, null=True)),
                ('zustand', models.CharField(blank=True, db_column='Zustand', max_length=50, null=True)),
                ('freies_stichwort', models.CharField(blank=True, db_column='Freies_Stichwort', max_length=50, null=True)),
                ('medium', models.CharField(blank=True, db_column='Medium', max_length=50, null=True)),
                ('merker', models.TextField(blank=True, db_column='Merker', null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'setup2',
                'managed': True,
            },
        ),
    ]
