from django.db import models


# Create your models here.
class Title(models.Model):
    Id = models.AutoField(db_column='tltidpk', primary_key=True)
    Name = models.CharField(db_column='tltname', max_length=255, blank=True, null=True)
    ShortName = models.CharField(db_column='tltshtname', max_length=255, blank=True,
                                 null=True)
    CreationDate = models.DateField(db_column='tltcreationdate', blank=True, null=True)
    LastEditDate = models.DateTimeField(db_column='tltlasteditdate', blank=True,
                                        null=True)

    class Meta:
        managed = False
        db_table = 'tbltitles'


class Country(models.Model):
    Id = models.AutoField(db_column='ctyidpk', primary_key=True)
    Name = models.CharField(db_column='ctyname', max_length=255, blank=True, null=True)
    ShortName = models.CharField(db_column='ctyshtname', max_length=10, blank=True, null=True)
    Code = models.CharField(db_column='ctycode', max_length=20, blank=True, null=True)
    CreationDate = models.DateField(db_column='ctycreateddate', blank=True, null=True)  # Field name made lowercase.
    LastEditDate = models.DateTimeField(db_column='ctylasteditdate', blank=True,
                                        null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcountries'


class State(models.Model):
    Id = models.AutoField(db_column='staidpk', primary_key=True)
    Name = models.CharField(db_column='staname', max_length=255, blank=True, null=True)
    ShortName = models.CharField(db_column='stashtname', max_length=10, blank=True, null=True)
    CountryId = models.ForeignKey(Country, models.DO_NOTHING, db_column='ctyidfk', blank=True, null=True)
    CreationDate = models.DateField(db_column='stacreateddate', blank=True, null=True)
    LastEditDate = models.DateTimeField(db_column='stalasteditdate', blank=True,
                                        null=True)

    class Meta:
        managed = False
        db_table = 'tblstates'


class Address(models.Model):
    Id = models.AutoField(db_column='adridpk', primary_key=True)
    AddressStateId = models.ForeignKey('State', models.DO_NOTHING, db_column='staidfk', blank=True,
                                       null=True)
    StreetNumber = models.CharField(db_column='adrstreetnumber', max_length=255, blank=True, null=True)
    HouseNumber = models.CharField(db_column='adrhousenumber', max_length=255, blank=True, null=True)
    GpsAddress = models.CharField(db_column='adrgpsaddress', max_length=255, blank=True, null=True)
    CreationDate = models.DateField(db_column='adrcreateddate', blank=True, null=True)
    LastEditDate = models.DateTimeField(db_column='adrlasteditdate', blank=True,
                                        null=True)

    class Meta:
        managed = False
        db_table = 'tbladdresses'
