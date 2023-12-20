from django.db import models


class Product(models.Model):
    Id = models.AutoField(db_column='prdidpk', primary_key=True)
    Name = models.CharField(db_column='prdname', max_length=255, blank=True, null=True)
    Brand = models.ForeignKey('ProductBrand', models.DO_NOTHING, blank=True,db_column='prdbrandidfk',
                              null=True)
    CategoryId = models.ForeignKey('ProductCategory', models.DO_NOTHING,db_column='prdcategoryidfk',
                                   blank=True, null=True)
    SubcategoryId = models.ForeignKey('ProductSubcategory', models.DO_NOTHING,db_column='prdsubcategoryidfk',
                                      blank=True, null=True)
    Description = models.CharField(db_column='prddescription', max_length=255, blank=True,
                                   null=True)
    Price = models.DecimalField(db_column='prdprice', max_digits=10, decimal_places=2, blank=True,
                                null=True)

    class Meta:
        managed = False
        db_table = 'tblproduct'


class ProductBrand(models.Model):
    Id = models.AutoField(db_column='prdbrandidpk', primary_key=True)  # Field name made lowercase.
    Name = models.CharField(db_column='prdbrandname', max_length=255, blank=True,
                            null=True)
    Description = models.CharField(db_column='prdbranddesc', max_length=255, blank=True,
                                    null=True)

    class Meta:
        managed = False
        db_table = 'tblproductbrand'


class ProductCategory(models.Model):
    Id = models.AutoField(db_column='prdcategoryidpk', primary_key=True)  # Field name made lowercase.
    Name = models.CharField(db_column='prdcategoryname', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    Description = models.CharField(db_column='prdcategorydesc', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproductcategory'


class ProductSubCategory(models.Model):
    Id = models.AutoField(db_column='prdsubcategoryidpk',
                          primary_key=True)  # Field name made lowercase.
    Name = models.CharField(db_column='prdsubcategoryname', max_length=255, blank=True,
                            null=True)  # Field name made lowercase.
    Description = models.CharField(db_column='prdsubcategorydesc', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproductsubcategory'
