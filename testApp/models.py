from django.db import models

# class Staff(models.Model):
#     staffid = models.AutoField(db_column='staffId', primary_key=True)  # Field name made lowercase.
#     staffname = models.CharField(db_column='staffName', max_length=30, blank=True, null=True)  # Field name made lowercase.
#
#     def __str__(self):
#         return self.staffname
#     class Meta:
#         managed = False
#         db_table = 'staff'

class Setup2(models.Model):

    STANDORT=(
        ('Archive','Archive'),
        ('Bibliothek','Bibliothek'),
        ('Speicher','Speicher')
    )

    ZUSTAND=(
        ('fehlt','fehlt'),
    ('in Ordnung','in Ordnung'),
    ('in Reparatur','in Reparatur')
    )

    MEDIUM=(
        ('CD-Rom','CD-Rom'),
        ('DAT','DAT'),
        ('Diskette','Diskette'),
        ('Magnetband','Magnetband'),
        ('MO-Disk','MO-Disk'),
        ('Wechselplatte','Wechselplatte'),
        ('USB-Stick','USB-Stick')
    )

    SPRACHE=(
        ('Chinesisch','Chinesisch'),
        ('Deutsch','Deutsch'),
        ('Englisch','Englisch'),
        ('Französisch','Französisch'),
        ('Italienisch','Italienisch'),
        ('Japanisch','Japanisch'),
        ('Polnisch','Polnisch'),
        ('Russisch','Russisch'),
        ('Spanisch','Spanisch'),
        ('Weitere...','Weitere...')
    )

    DOKUMENTTYPE=(
        ('Allg. Schriftstück','Allg. Schriftstück'),
        ('Bericht','Bericht'),
        ('Buch','Buch'),
        ('Datenträger','Datenträger'),
        ('Dia','Dia'),
        ('Diplomarbeit','Diplomarbeit'),
        ('Dissertation','Dissertation'),
        ('Dokumente','Dokumente'),
        ('Film','Film'),
        ('Folie','Folie'),
        ('Studienarbeit(exp.)','Studienarbeit(exp.)'),
        ('Studienarbeit(konstr.)','Studienarbeit(konstr.)'),
        ('Zeitschrift','Zeitschrift'),
    )


# auflagen
# author
# bemerkung
# betreuer
# dk_kennzeichnung
# dk_nummer
# dk_etikett_buch
# dk_etikett_andere
# entleiher
# entleiher_bem
# erfasserkuerzel
# erscheinungsdatum
# erscheinungsort
# inventarnummer
# isbn_nummer
# sprache
# standort
# titel
# dokumenttyp
# verlag
# verlagsnummer
# zustand
# freies_stichwort
# medium
# merker
    auflagen = models.CharField(db_column='Auflagen', max_length=255, blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bemerkung = models.TextField(db_column='Bemerkug', blank=True, null=True)  # Field name made lowercase.
    betreuer = models.CharField(db_column='Betreuer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dk_kennzeichnung = models.CharField(db_column='DK_Kennzeichnung', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dk_nummer = models.FloatField(db_column='DK_nummer', blank=True, null=True)  # Field name made lowercase.
    dk_etikett_buch = models.CharField(db_column='DK_Etikett_Buch', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dk_etikett_andere = models.CharField(db_column='DK_Etikett_Andere',  max_length=50,blank=True, null=True)  # Field name made lowercase.
    entleiher = models.CharField(db_column='Entleiher', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entleiher_bem = models.TextField(db_column='Entleiher_Bem', blank=True, null=True)  # Field name made lowercase.
    erfasserkuerzel = models.CharField(db_column='Erfasserkuerzel', max_length=25, blank=True, null=True)  # Field name made lowercase.
    erscheinungsdatum = models.CharField(db_column='Erscheinungsdatum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    erscheinungsjahr = models.IntegerField(db_column='Erscheinungsjahr', blank=True, null=True)  # Field name made lowercase.
    erscheinungsort = models.CharField(db_column='Erscheinungsort', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inventarnummer = models.CharField(db_column='Inventarnummer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isbn_nummer = models.CharField(db_column='ISBN_Nummer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sprache = models.CharField(db_column='Sprache', max_length=25, blank=True, null=True, choices=SPRACHE)  # Field name made lowercase.
    standort = models.CharField(db_column='Standort', max_length=50, blank=True, null=True,choices=STANDORT)  # Field name made lowercase.
    titel = models.CharField(db_column='Titel', blank=True, null=True,max_length=500)  # Field name made lowercase.
    dokumenttyp = models.CharField(db_column='Dokumenttyp', max_length=50, blank=True, null=True, choices=DOKUMENTTYPE)  # Field name made lowercase.
    verlag = models.CharField(db_column='Verlag', max_length=25, blank=True, null=True)  # Field name made lowercase.
    verlagsnummer = models.CharField(db_column='Verlagsnummer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    zustand = models.CharField(db_column='Zustand', max_length=50, blank=True, null=True,choices=ZUSTAND)  # Field name made lowercase.
    freies_stichwort = models.CharField(db_column='Freies_Stichwort', max_length=50, blank=True, null=True)  # Field name made lowercase.
    medium = models.CharField(db_column='Medium', max_length=50, blank=True, null=True, choices=MEDIUM)  # Field name made lowercase.
    merker = models.TextField(db_column='Merker', blank=True, null=True)  # Field name made lowercase.
    id = models. AutoField(primary_key=True)

    def __str__(self):
        if self.titel == None:
            return "ERROR- Title wurde nicht eigegeben"
        return self.titel
    class Meta:
        managed = True
        db_table = 'setup2'

