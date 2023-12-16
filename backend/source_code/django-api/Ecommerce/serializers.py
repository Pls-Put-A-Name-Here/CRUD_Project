from rest_framework import serializers

# Serializer for userTbl 

# class UserTblSerializer(serializers.Serializer):
#     userIdpk = serializers.IntegerField()
#     usergndIdfk = serializers.IntegerField()
#     # usertlt

# class SupplierSerializer(serializers.Serializer):
#     splidpk = serializers.IntegerField()
#     splname = serializers.CharField()
#     spladdress = serializers.CharField()
#     splcontact = serializers.CharField()
#     splcontract = serializers.CharField()

"""syntax for serializer
class serializer_name(serializers.ModelSerializer):
    class Meta:
        model = model_name
        fields = '__all__' or ['field1', 'field2', 'field3']
"""

class CartItemSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tblcartitem"
        fields = '__all__'

class TblcustomerSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tblcustomer"
        fields = '__all__'

class TblcustomeraddressSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tblcustomeraddress"
        fields = '__all__'
class TblcustomercountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = "Tblcustomercountry"
        fields = '__all__'

class TblcustomerstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = "Tblcustomerstate"
        fields = '__all__'
class TbldiscountSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tbldiscount"
        fields = '__all__'
class TblgndSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tblgnd"
        fields = '__all__'
class TblinventorySerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tblinventory"
        fields = '__all__'
class TblorderSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tblorder"
        fields = '__all__'
class TblorderitemsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tblorderitems"
        fields = '__all__'
class TblpaymentstatusSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tblpaymentstatus"
        fields = '__all__'
class TblproductSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tblproduct"
        fields = '__all__'
class TblproductbrandSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tblproductbrand"
        fields = '__all__'
class TblproductcategorySerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tblproductcategory"
        fields = '__all__'
class TblproductsubcategorySerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tblproductsubcategory"
        fields = '__all__' 
class TblpurchasesSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tblpurchases"
        fields = '__all__'
class TblreturnSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tblreturn"
        fields = '__all__'
class TblreviewsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tblreviews"
        fields = '__all__'
class TblshippingmethodSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tblshippingmethod"
        fields = '__all__'
class TblshoppingcartSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tblshoppingcart"
        fields = '__all__'
class TblsupplierSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tblsupplier"
        fields = '__all__'
class TbltaxSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tbltax"
        fields = '__all__'
class TbltittleSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tbltittle"
        fields = '__all__'
class TbluserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = "Tbluser"
        fields = '__all__'