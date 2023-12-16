from django.db import models


class CartItem(models.Model):
    cartItemId = models.AutoField(db_column='crtItemIdpk', primary_key=True)
    cartItemCartId = models.ForeignKey('Shoppingcart', models.DO_NOTHING, db_column='cartIdfk')
    cartItemProductId = models.ForeignKey('Product', models.DO_NOTHING, db_column='prdIdfk')
    cartItemQuantity = models.DecimalField(db_column='crtItemQuantity', max_digits=10, decimal_places=3)
    cartItemPrice = models.DecimalField(db_column='crtItemPrice', max_digits=10, decimal_places=3)
    cartItemUpdatedDate = models.DateField(db_column='crtItemAddedDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcartitem'


class Customer(models.Model):
    customerId = models.AutoField(db_column='custIdpk', primary_key=True)
    customerUserId = models.ForeignKey('User', models.DO_NOTHING, db_column='custUsrIdfk', blank=True, null=True)
    customerFirstName = models.CharField(db_column='custFirstName', max_length=255, blank=True, null=True)
    customerLastName = models.CharField(db_column='custLastName', max_length=255, blank=True, null=True)
    customerOtherName = models.CharField(db_column='custOtherName', max_length=255, blank=True, null=True)
    customerEmail = models.CharField(db_column='custEmail', max_length=255, blank=True, null=True)
    customerAddressId = models.ForeignKey('CustomerAddress', models.DO_NOTHING, db_column='custAddressIdfk', blank=True,
                                          null=True)

    class Meta:
        managed = False
        db_table = 'tblcustomer'


class CustomerAddress(models.Model):
    customerAddressId = models.AutoField(db_column='custAddressIdpk', primary_key=True)
    customerAddressStateId = models.ForeignKey('State', models.DO_NOTHING, db_column='custStateIdfk', blank=True,
                                               null=True)
    customerStreetNumber = models.CharField(db_column='custStreetNumber', max_length=255, blank=True, null=True)
    customerHouseNumber = models.CharField(db_column='custHouseNumber', max_length=255, blank=True, null=True)
    customerGpsAddress = models.CharField(db_column='custGpsAddress', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcustomeraddress'


class Country(models.Model):
    countryId = models.AutoField(db_column='custCountryIdpk', primary_key=True)
    countryName = models.CharField(db_column='custCountryName', max_length=255, blank=True, null=True)
    countryShtName = models.CharField(db_column='custCountryShtName', max_length=10, blank=True, null=True)
    countryCode = models.CharField(db_column='custCountryCode', max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcustomercountry'


class State(models.Model):
    stateId = models.AutoField(db_column='custStateIdpk', primary_key=True)
    stateName = models.CharField(db_column='custStateName', max_length=255, blank=True, null=True)
    stateShtName = models.CharField(db_column='custStateShtName', max_length=10, blank=True, null=True)
    stateCountryId = models.ForeignKey(Country, models.DO_NOTHING, db_column='custCountryIdfk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcustomerstate'


class Discount(models.Model):
    discountId = models.AutoField(db_column='\xa0discountIdpk',
                                  primary_key=True)
    discountName = models.CharField(db_column='\xa0discountName',
                                    max_length=255)
    discountPercentage = models.DecimalField(db_column='\xa0discountPercentage', max_digits=10,
                                             decimal_places=2)
    discountType = models.CharField(db_column='\xa0discountType',
                                    max_length=255)

    class Meta:
        managed = False
        db_table = 'tbldiscount'


class Gender(models.Model):
    genderId = models.AutoField(db_column='gndIdpk', primary_key=True)
    genderShtName = models.CharField(db_column='gndShtName', max_length=2, blank=True,
                                     null=True)
    genderName = models.CharField(db_column='gndName', max_length=6, blank=True, null=True)
    genderIsActive = models.TextField(db_column='gndActive', blank=True,
                                      null=True)
    genderCreatedDate = models.DateTimeField(db_column='gndCreatedDate', blank=True,
                                             null=True, auto_now_add=True)
    genderLastEditDate = models.DateTimeField(db_column='gndLastEditDate', blank=True,
                                              auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'tblgender'


class Tblinventory(models.Model):
    invid = models.AutoField(db_column='invId', primary_key=True)  # Field name made lowercase.
    invitemprdidfk = models.IntegerField(db_column='invItemPrdIdfk', blank=True,
                                         null=True)  # Field name made lowercase.
    invitemsupplieridfk = models.IntegerField(db_column='invItemSupplierIdfk', blank=True,
                                              null=True)  # Field name made lowercase.
    invitemprice = models.DecimalField(db_column='invItemPrice', max_digits=10, decimal_places=2, blank=True,
                                       null=True)  # Field name made lowercase.
    invitemmodelnumber = models.CharField(db_column='invItemModelnumber', max_length=255, blank=True,
                                          null=True)  # Field name made lowercase.
    invitemwarranty = models.CharField(db_column='invItemWarranty', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    invitemdimensions = models.CharField(db_column='invItemDimensions', max_length=255, blank=True,
                                         null=True)  # Field name made lowercase.
    invitemreleasedate = models.DateField(db_column='invItemReleaseDate', blank=True,
                                          null=True)  # Field name made lowercase.
    invitemweight = models.CharField(db_column='invItemWeight', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    invitemcolor = models.CharField(db_column='invItemColor', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    invitemfeatures = models.CharField(db_column='invItemFeatures', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    invitemspecifications = models.CharField(db_column='invItemSpecifications', max_length=255, blank=True,
                                             null=True)  # Field name made lowercase.
    invitemquantity = models.IntegerField(db_column='invItemQuantity', blank=True,
                                          null=True)  # Field name made lowercase.
    invitemproductdescription = models.CharField(db_column='invItemProductDescription', max_length=255, blank=True,
                                                 null=True)  # Field name made lowercase.
    invitemproductreorderpoint = models.IntegerField(db_column='invItemProductReorderPoint', blank=True,
                                                     null=True)  # Field name made lowercase.
    invitemproductreorderquantity = models.IntegerField(db_column='invItemProductReorderQuantity', blank=True,
                                                        null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblinventory'


class Tblorder(models.Model):
    ordidpk = models.AutoField(db_column='ordIdpk', primary_key=True)  # Field name made lowercase.
    ordcustidfk = models.IntegerField(db_column='ordCustIdfk', blank=True, null=True)  # Field name made lowercase.
    orddate = models.DateField(db_column='ordDate', blank=True, null=True)  # Field name made lowercase.
    ordshippingaddressid = models.IntegerField(db_column='ordShippingAddressId', blank=True,
                                               null=True)  # Field name made lowercase.
    ordpaymentstatusid = models.IntegerField(db_column='ordPaymentStatusID', blank=True,
                                             null=True)  # Field name made lowercase.
    ordtotal = models.DecimalField(db_column='ordTotal', max_digits=10, decimal_places=2, blank=True,
                                   null=True)  # Field name made lowercase.
    ordnotes = models.CharField(db_column='ordNotes', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    orddiscountid = models.ForeignKey(Tbldiscount, models.DO_NOTHING, db_column='ordDiscountId', blank=True,
                                      null=True)  # Field name made lowercase.
    orddeliverystatusid = models.IntegerField(db_column='ordDeliveryStatusID', blank=True,
                                              null=True)  # Field name made lowercase.
    ordstatusidfk = models.IntegerField(db_column='ordStatusIdfk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblorder'


class Tblorderitems(models.Model):
    itemid = models.AutoField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    itemordidfk = models.ForeignKey(Tblorder, models.DO_NOTHING, db_column='itemOrdIdfk', blank=True,
                                    null=True)  # Field name made lowercase.
    itemprdidfk = models.ForeignKey('Tblproduct', models.DO_NOTHING, db_column='itemPrdIdfk', blank=True,
                                    null=True)  # Field name made lowercase.
    itemtaxidfk = models.ForeignKey('Tbltax', models.DO_NOTHING, db_column='itemTaxIdfk', blank=True,
                                    null=True)  # Field name made lowercase.
    itemshippingtax = models.DecimalField(db_column='itemShippingTax', max_digits=10, decimal_places=2, blank=True,
                                          null=True)  # Field name made lowercase.
    itemquantity = models.DecimalField(db_column='itemQuantity', max_digits=10, decimal_places=2, blank=True,
                                       null=True)  # Field name made lowercase.
    itemprice = models.DecimalField(db_column='itemPrice', max_digits=10, decimal_places=2, blank=True,
                                    null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblorderitems'


class Tblpaymentstatus(models.Model):
    paymentstatusidpk = models.AutoField(db_column='paymentStatusIdpk', primary_key=True)  # Field name made lowercase.
    paymentstatus = models.CharField(db_column='paymentStatus', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblpaymentstatus'


class Tblproduct(models.Model):
    prdidpk = models.AutoField(db_column='prdIdpk', primary_key=True)  # Field name made lowercase.
    prdname = models.CharField(db_column='prdName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prdbrandidfk = models.ForeignKey('Tblproductbrand', models.DO_NOTHING, db_column='prdBrandIdfk', blank=True,
                                     null=True)  # Field name made lowercase.
    prdcategoryidfk = models.ForeignKey('Tblproductcategory', models.DO_NOTHING, db_column='prdCategoryIdfk',
                                        blank=True, null=True)  # Field name made lowercase.
    prdsubcategoryidfk = models.ForeignKey('Tblproductsubcategory', models.DO_NOTHING, db_column='prdSubCategoryIdfk',
                                           blank=True, null=True)  # Field name made lowercase.
    prddescription = models.CharField(db_column='prdDescription', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    prdprice = models.DecimalField(db_column='prdPrice', max_digits=10, decimal_places=2, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct'


class Tblproductbrand(models.Model):
    prdbrandidpk = models.AutoField(db_column='prdBrandIdpk', primary_key=True)  # Field name made lowercase.
    prdbrandname = models.CharField(db_column='prdBrandName', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    prdbranddesc = models.CharField(db_column='prdBrandDesc', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproductbrand'


class Tblproductcategory(models.Model):
    prdcategoryidpk = models.AutoField(db_column='prdCategoryIdpk', primary_key=True)  # Field name made lowercase.
    prdcategoryname = models.CharField(db_column='prdCategoryName', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    prdcategorydesc = models.CharField(db_column='prdCategoryDesc', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproductcategory'


class Tblproductsubcategory(models.Model):
    prdsubcategoryidpk = models.AutoField(db_column='prdSubCategoryIdpk',
                                          primary_key=True)  # Field name made lowercase.
    prdsubcategoryname = models.CharField(db_column='prdSubCategoryName', max_length=255, blank=True,
                                          null=True)  # Field name made lowercase.
    prdsubcategorydesc = models.CharField(db_column='prdSubCategoryDesc', max_length=255, blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproductsubcategory'


class Tblpurchases(models.Model):
    pchidpk = models.AutoField(db_column='pchIdpk', primary_key=True)  # Field name made lowercase.
    pchordidfk = models.ForeignKey(Tblorder, models.DO_NOTHING, db_column='pchOrdIdfk', blank=True,
                                   null=True)  # Field name made lowercase.
    pchammount = models.DecimalField(db_column='pchAmmount', max_digits=10, decimal_places=2, blank=True,
                                     null=True)  # Field name made lowercase.
    pchpurchasedate = models.DateField(db_column='pchPurchaseDate', blank=True, null=True)  # Field name made lowercase.
    pchtypeid = models.IntegerField(db_column='pchTypeId', blank=True, null=True)  # Field name made lowercase.
    pchpaymentstatusidfk = models.ForeignKey(Tblpaymentstatus, models.DO_NOTHING, db_column='pchPaymentStatusIdfk',
                                             blank=True, null=True)  # Field name made lowercase.
    pchlasteditdate = models.DateTimeField(db_column='pchLastEditDate', blank=True,
                                           null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblpurchases'


class Tblreturns(models.Model):
    field_returnidpk = models.AutoField(db_column='\xa0returnIdPK',
                                        primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_customerid = models.IntegerField(
        db_column='\xa0customerId')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_orderid = models.IntegerField(
        db_column='\xa0orderId')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_productid = models.IntegerField(
        db_column='\xa0productId')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_returndate = models.DateField(
        db_column='\xa0returnDate')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_returnreason = models.CharField(db_column='\xa0returnReason',
                                          max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # Field renamed because it started with '_'.
    field_refundstatus = models.CharField(db_column='\xa0refundStatus',
                                          max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'tblreturns'


class Tblreviews(models.Model):
    rwvidpk = models.AutoField(db_column='rwvIdpk', primary_key=True)  # Field name made lowercase.
    rwvuseridfk = models.IntegerField(db_column='rwvUserIdfk', blank=True, null=True)  # Field name made lowercase.
    rwvproductidfk = models.IntegerField(db_column='rwvProductIdfk', blank=True,
                                         null=True)  # Field name made lowercase.
    rwvreveiewcontent = models.CharField(db_column='rwvReveiewContent', max_length=255, blank=True,
                                         null=True)  # Field name made lowercase.
    rwvratings = models.DecimalField(db_column='rwvRatings', max_digits=5, decimal_places=2, blank=True,
                                     null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblreviews'


class Tblshippingmethod(models.Model):
    field_shippingmethodidpk = models.AutoField(db_column='\xa0shippingMethodIdpk',
                                                primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_shippingmethodname = models.CharField(db_column='\xa0shippingMethodName',
                                                max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable
    # characters. Field renamed because it started with '_'.
    field_shippingcost = models.DecimalField(db_column='\xa0shippingCost', max_digits=10,
                                             decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_shippingdeliverytime = models.CharField(db_column='\xa0shippingDeliveryTime',
                                                  max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'tblshippingmethod'


class Tblshoppingcart(models.Model):
    cartidpk = models.OneToOneField(Tblcustomer, models.DO_NOTHING, db_column='cartIdpk',
                                    primary_key=True)  # Field name made lowercase.
    custidfk = models.IntegerField(db_column='custIdfk')  # Field name made lowercase.
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblshoppingcart'


class Tblsupplier(models.Model):
    splidpk = models.AutoField(db_column='splIdpk', primary_key=True)  # Field name made lowercase.
    splname = models.CharField(db_column='splName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    spladdress = models.CharField(db_column='splAddress', max_length=100, blank=True,
                                  null=True)  # Field name made lowercase.
    splcontact = models.CharField(db_column='splContact', max_length=15, blank=True,
                                  null=True)  # Field name made lowercase.
    splcontract = models.TextField(db_column='splContract', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsupplier'


supplier_obj = Tblsupplier()
supplier_obj.splname = "Bright"
supplier_obj.spladdress = "Mayten St."


class Tbltax(models.Model):
    field_taxidpk = models.AutoField(db_column='\xa0taxIdpk',
                                     primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_taxname = models.CharField(db_column='\xa0taxName',
                                     max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_taxpercentage = models.DecimalField(db_column='\xa0taxPercentage', max_digits=10,
                                              decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_taxtype = models.CharField(db_column='\xa0taxType',
                                     max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'tbltax'


class Tbltitle(models.Model):
    tltidpk = models.AutoField(db_column='tltIdpk', primary_key=True)  # Field name made lowercase.
    tltname = models.CharField(db_column='tltName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tltshtname = models.CharField(db_column='tltShtName', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    tltcreationdate = models.DateField(db_column='tltCreationDate', blank=True, null=True)  # Field name made lowercase.
    tltlasteditdate = models.DateTimeField(db_column='tltLastEditDate', blank=True,
                                           null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbltitle'


class Tbluser(models.Model):
    usridpk = models.AutoField(db_column='usrIdpk', primary_key=True)  # Field name made lowercase.
    usrgndidpk = models.ForeignKey(Tblgender, models.DO_NOTHING, db_column='usrGndIdpk', blank=True,
                                   null=True)  # Field name made lowercase.
    usrtltidfk = models.ForeignKey(Tbltitle, models.DO_NOTHING, db_column='usrTltIdfk', blank=True,
                                   null=True)  # Field name made lowercase.
    usrname = models.CharField(db_column='usrName', unique=True, max_length=25, blank=True,
                               null=True)  # Field name made lowercase.
    usraddress = models.CharField(db_column='usrAddress', max_length=25, blank=True,
                                  null=True)  # Field name made lowercase.
    usrpassword = models.CharField(db_column='usrPassword', max_length=25, blank=True,
                                   null=True)  # Field name made lowercase.
    usrisadmin = models.IntegerField(db_column='usrIsAdmin', blank=True, null=True)  # Field name made lowercase.
    usrisemployee = models.IntegerField(db_column='usrIsEmployee', blank=True, null=True)  # Field name made lowercase.
    usrismanager = models.IntegerField(db_column='usrIsManager', blank=True, null=True)  # Field name made lowercase.
    usrisactive = models.IntegerField(db_column='usrIsActive', blank=True, null=True)  # Field name made lowercase.
    usrregistrationdate = models.DateField(db_column='usrRegistrationDate', blank=True,
                                           null=True)  # Field name made lowercase.
    usrlasteditdate = models.DateTimeField(db_column='usrLastEditDate', blank=True,
                                           null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbluser'
