from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

# We need to remame the table and fields here according to a set covention
# We can also rename the columns or fields ie.That wont cause any issue since this: "db_column='crtItemIdpk'" exists for each column.
# We also need to consider whether we will make use of django's Object Relational Mapper or not

class Tblcartitem(models.Model):
    crtitemidpk = models.AutoField(db_column='crtItemIdpk', primary_key=True)  # Field name made lowercase.
    cartidfk = models.ForeignKey('Tblshoppingcart', models.DO_NOTHING, db_column='cartIdfk')  # Field name made lowercase.
    prdidfk = models.ForeignKey('Tblproduct', models.DO_NOTHING, db_column='prdIdfk')  # Field name made lowercase.
    crtitemquantity = models.DecimalField(db_column='crtItemQuantity', max_digits=10, decimal_places=2)  # Field name made lowercase.
    crtitemprice = models.DecimalField(db_column='crtItemPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    crtitemaddeddate = models.DateField(db_column='crtItemAddedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcartitem'


class Tblcustomer(models.Model):
    custidpk = models.AutoField(db_column='custIdpk', primary_key=True)  # Field name made lowercase.
    custusridfk = models.ForeignKey('Tbluser', models.DO_NOTHING, db_column='custUsrIdfk', blank=True, null=True)  # Field name made lowercase.
    custfirstname = models.CharField(db_column='custFirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custlastname = models.CharField(db_column='custLastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custothername = models.CharField(db_column='custOtherName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custemail = models.CharField(db_column='custEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custaddressidfk = models.ForeignKey('Tblcustomeraddress', models.DO_NOTHING, db_column='custAddressIdfk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomer'


class Tblcustomeraddress(models.Model):
    custaddressidpk = models.AutoField(db_column='custAddressIdpk', primary_key=True)  # Field name made lowercase.
    custstateidfk = models.ForeignKey('Tblcustomerstate', models.DO_NOTHING, db_column='custStateIdfk', blank=True, null=True)  # Field name made lowercase.
    custstreetnumber = models.CharField(db_column='custStreetNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custhousenumber = models.CharField(db_column='custHouseNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custgpsaddress = models.CharField(db_column='custGpsAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomeraddress'


class Tblcustomercountry(models.Model):
    custcountryidpk = models.AutoField(db_column='custCountryIdpk', primary_key=True)  # Field name made lowercase.
    custcountryname = models.CharField(db_column='custCountryName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custcountryshtname = models.CharField(db_column='custCountryShtName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    custcountrycode = models.CharField(db_column='custCountryCode', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomercountry'


class Tblcustomerstate(models.Model):
    custstateidpk = models.AutoField(db_column='custStateIdpk', primary_key=True)  # Field name made lowercase.
    custstatename = models.CharField(db_column='custStateName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custstateshtname = models.CharField(db_column='custStateShtName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    custcountryidfk = models.ForeignKey(Tblcustomercountry, models.DO_NOTHING, db_column='custCountryIdfk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomerstate'

#We also need to recheck the databse table column names for this:
class Tbldiscount(models.Model):
    field_discountidpk = models.AutoField(db_column='\xa0discountIdpk', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_discountname = models.CharField(db_column='\xa0discountName', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters. 
# Field renamed because it started with '_'.
    field_discountpercentage = models.DecimalField(db_column='\xa0discountPercentage', max_digits=10, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_discounttype = models.CharField(db_column='\xa0discountType', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters. 
# Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'tbldiscount'


class Tblgender(models.Model):
    gndidpk = models.AutoField(db_column='gndIdpk', primary_key=True)  # Field name made lowercase.
    gndshtname = models.CharField(db_column='gndShtName', max_length=2, blank=True, null=True)  # Field name made lowercase.
    gndname = models.CharField(db_column='gndName', max_length=6, blank=True, null=True)  # Field name made lowercase.
    gndactive = models.TextField(db_column='gndActive', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    gndlasteditdate = models.DateTimeField(db_column='gndLastEditDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblgender'


class Tblinventory(models.Model):
    invid = models.AutoField(db_column='invId', primary_key=True)  # Field name made lowercase.
    invitemprdidfk = models.IntegerField(db_column='invItemPrdIdfk', blank=True, null=True)  # Field name made lowercase.
    invitemsupplieridfk = models.IntegerField(db_column='invItemSupplierIdfk', blank=True, null=True)  # Field name made lowercase.
    invitemprice = models.DecimalField(db_column='invItemPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    invitemmodelnumber = models.CharField(db_column='invItemModelnumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invitemwarranty = models.CharField(db_column='invItemWarranty', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invitemdimensions = models.CharField(db_column='invItemDimensions', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invitemreleasedate = models.DateField(db_column='invItemReleaseDate', blank=True, null=True)  # Field name made lowercase.
    invitemweight = models.CharField(db_column='invItemWeight', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invitemcolor = models.CharField(db_column='invItemColor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invitemfeatures = models.CharField(db_column='invItemFeatures', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invitemspecifications = models.CharField(db_column='invItemSpecifications', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invitemquantity = models.IntegerField(db_column='invItemQuantity', blank=True, null=True)  # Field name made lowercase.
    invitemproductdescription = models.CharField(db_column='invItemProductDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invitemproductreorderpoint = models.IntegerField(db_column='invItemProductReorderPoint', blank=True, null=True)  # Field name made lowercase.
    invitemproductreorderquantity = models.IntegerField(db_column='invItemProductReorderQuantity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblinventory'


class Tblorder(models.Model):
    ordidpk = models.AutoField(db_column='ordIdpk', primary_key=True)  # Field name made lowercase.
    ordcustidfk = models.IntegerField(db_column='ordCustIdfk', blank=True, null=True)  # Field name made lowercase.
    orddate = models.DateField(db_column='ordDate', blank=True, null=True)  # Field name made lowercase.
    ordshippingaddressid = models.IntegerField(db_column='ordShippingAddressId', blank=True, null=True)  # Field name made lowercase.
    ordpaymentstatusid = models.IntegerField(db_column='ordPaymentStatusID', blank=True, null=True)  # Field name made lowercase.
    ordtotal = models.DecimalField(db_column='ordTotal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ordnotes = models.CharField(db_column='ordNotes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orddiscountid = models.ForeignKey(Tbldiscount, models.DO_NOTHING, db_column='ordDiscountId', blank=True, null=True)  # Field name made lowercase.
    orddeliverystatusid = models.IntegerField(db_column='ordDeliveryStatusID', blank=True, null=True)  # Field name made lowercase.
    ordstatusidfk = models.IntegerField(db_column='ordStatusIdfk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblorder'


class Tblorderitems(models.Model):
    itemid = models.AutoField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    itemordidfk = models.ForeignKey(Tblorder, models.DO_NOTHING, db_column='itemOrdIdfk', blank=True, null=True)  # Field name made lowercase.
    itemprdidfk = models.ForeignKey('Tblproduct', models.DO_NOTHING, db_column='itemPrdIdfk', blank=True, null=True)  # Field name made lowercase.
    itemtaxidfk = models.ForeignKey('Tbltax', models.DO_NOTHING, db_column='itemTaxIdfk', blank=True, null=True)  # Field name made lowercase.
    itemshippingtax = models.DecimalField(db_column='itemShippingTax', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemquantity = models.DecimalField(db_column='itemQuantity', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemprice = models.DecimalField(db_column='itemPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblorderitems'


class Tblpaymentstatus(models.Model):
    paymentstatusidpk = models.AutoField(db_column='paymentStatusIdpk', primary_key=True)  # Field name made lowercase.
    paymentstatus = models.CharField(db_column='paymentStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblpaymentstatus'


class Tblproduct(models.Model):
    prdidpk = models.AutoField(db_column='prdIdpk', primary_key=True)  # Field name made lowercase.
    prdname = models.CharField(db_column='prdName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prdbrandidfk = models.ForeignKey('Tblproductbrand', models.DO_NOTHING, db_column='prdBrandIdfk', blank=True, null=True)  # Field name made lowercase.
    prdcategoryidfk = models.ForeignKey('Tblproductcategory', models.DO_NOTHING, db_column='prdCategoryIdfk', blank=True, null=True)  # Field name made lowercase.
    prdsubcategoryidfk = models.ForeignKey('Tblproductsubcategory', models.DO_NOTHING, db_column='prdSubCategoryIdfk', blank=True, null=True)  # Field name made lowercase.
    prddescription = models.CharField(db_column='prdDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prdprice = models.DecimalField(db_column='prdPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct'


class Tblproductbrand(models.Model):
    prdbrandidpk = models.AutoField(db_column='prdBrandIdpk', primary_key=True)  # Field name made lowercase.
    prdbrandname = models.CharField(db_column='prdBrandName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prdbranddesc = models.CharField(db_column='prdBrandDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproductbrand'


class Tblproductcategory(models.Model):
    prdcategoryidpk = models.AutoField(db_column='prdCategoryIdpk', primary_key=True)  # Field name made lowercase.
    prdcategoryname = models.CharField(db_column='prdCategoryName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prdcategorydesc = models.CharField(db_column='prdCategoryDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproductcategory'


class Tblproductsubcategory(models.Model):
    prdsubcategoryidpk = models.AutoField(db_column='prdSubCategoryIdpk', primary_key=True)  # Field name made lowercase.
    prdsubcategoryname = models.CharField(db_column='prdSubCategoryName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prdsubcategorydesc = models.CharField(db_column='prdSubCategoryDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproductsubcategory'


class Tblpurchases(models.Model):
    pchidpk = models.AutoField(db_column='pchIdpk', primary_key=True)  # Field name made lowercase.
    pchordidfk = models.ForeignKey(Tblorder, models.DO_NOTHING, db_column='pchOrdIdfk', blank=True, null=True)  # Field name made lowercase.
    pchammount = models.DecimalField(db_column='pchAmmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pchpurchasedate = models.DateField(db_column='pchPurchaseDate', blank=True, null=True)  # Field name made lowercase.
    pchtypeid = models.IntegerField(db_column='pchTypeId', blank=True, null=True)  # Field name made lowercase.
    pchpaymentstatusidfk = models.ForeignKey(Tblpaymentstatus, models.DO_NOTHING, db_column='pchPaymentStatusIdfk', blank=True, null=True)  # Field name made lowercase.
    pchlasteditdate = models.DateTimeField(db_column='pchLastEditDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblpurchases'


class Tblreturns(models.Model):
    field_returnidpk = models.AutoField(db_column='\xa0returnIdPK', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_customerid = models.IntegerField(db_column='\xa0customerId')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_orderid = models.IntegerField(db_column='\xa0orderId')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_productid = models.IntegerField(db_column='\xa0productId')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_returndate = models.DateField(db_column='\xa0returnDate')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_returnreason = models.CharField(db_column='\xa0returnReason', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters. 
# Field renamed because it started with '_'.
    field_refundstatus = models.CharField(db_column='\xa0refundStatus', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters. 
# Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'tblreturns'


class Tblreviews(models.Model):
    rwvidpk = models.AutoField(db_column='rwvIdpk', primary_key=True)  # Field name made lowercase.
    rwvuseridfk = models.IntegerField(db_column='rwvUserIdfk', blank=True, null=True)  # Field name made lowercase.
    rwvproductidfk = models.IntegerField(db_column='rwvProductIdfk', blank=True, null=True)  # Field name made lowercase.
    rwvreveiewcontent = models.CharField(db_column='rwvReveiewContent', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rwvratings = models.DecimalField(db_column='rwvRatings', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblreviews'


class Tblshippingmethod(models.Model):
    field_shippingmethodidpk = models.AutoField(db_column='\xa0shippingMethodIdpk', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_shippingmethodname = models.CharField(db_column='\xa0shippingMethodName', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable 
# characters. Field renamed because it started with '_'.
    field_shippingcost = models.DecimalField(db_column='\xa0shippingCost', max_digits=10, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_shippingdeliverytime = models.CharField(db_column='\xa0shippingDeliveryTime', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'tblshippingmethod'


class Tblshoppingcart(models.Model):
    cartidpk = models.OneToOneField(Tblcustomer, models.DO_NOTHING, db_column='cartIdpk', primary_key=True)  # Field name made lowercase.
    custidfk = models.IntegerField(db_column='custIdfk')  # Field name made lowercase.
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblshoppingcart'


class Tblsupplier(models.Model):
    splidpk = models.AutoField(db_column='splIdpk', primary_key=True)  # Field name made lowercase.
    splname = models.CharField(db_column='splName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    spladdress = models.CharField(db_column='splAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    splcontact = models.CharField(db_column='splContact', max_length=15, blank=True, null=True)  # Field name made lowercase.
    splcontract = models.TextField(db_column='splContract', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsupplier'


class Tbltax(models.Model):
    field_taxidpk = models.AutoField(db_column='\xa0taxIdpk', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_taxname = models.CharField(db_column='\xa0taxName', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_taxpercentage = models.DecimalField(db_column='\xa0taxPercentage', max_digits=10, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_taxtype = models.CharField(db_column='\xa0taxType', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'tbltax'


class Tbltitle(models.Model):
    tltidpk = models.AutoField(db_column='tltIdpk', primary_key=True)  # Field name made lowercase.
    tltname = models.CharField(db_column='tltName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tltshtname = models.CharField(db_column='tltShtName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tltcreationdate = models.DateField(db_column='tltCreationDate', blank=True, null=True)  # Field name made lowercase.
    tltlasteditdate = models.DateTimeField(db_column='tltLastEditDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbltitle'


class Tbluser(models.Model):
    usridpk = models.AutoField(db_column='usrIdpk', primary_key=True)  # Field name made lowercase.
    usrgndidpk = models.ForeignKey(Tblgender, models.DO_NOTHING, db_column='usrGndIdpk', blank=True, null=True)  # Field name made lowercase.
    usrtltidfk = models.ForeignKey(Tbltitle, models.DO_NOTHING, db_column='usrTltIdfk', blank=True, null=True)  # Field name made lowercase.
    usrname = models.CharField(db_column='usrName', unique=True, max_length=25, blank=True, null=True)  # Field name made lowercase.
    usraddress = models.CharField(db_column='usrAddress', max_length=25, blank=True, null=True)  # Field name made lowercase.
    usrpassword = models.CharField(db_column='usrPassword', max_length=25, blank=True, null=True)  # Field name made lowercase.
    usrisadmin = models.IntegerField(db_column='usrIsAdmin', blank=True, null=True)  # Field name made lowercase.
    usrisemployee = models.IntegerField(db_column='usrIsEmployee', blank=True, null=True)  # Field name made lowercase.
    usrismanager = models.IntegerField(db_column='usrIsManager', blank=True, null=True)  # Field name made lowercase.
    usrisactive = models.IntegerField(db_column='usrIsActive', blank=True, null=True)  # Field name made lowercase.
    usrregistrationdate = models.DateField(db_column='usrRegistrationDate', blank=True, null=True)  # Field name made lowercase.
    usrlasteditdate = models.DateTimeField(db_column='usrLastEditDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbluser'
