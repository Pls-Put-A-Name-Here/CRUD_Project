# from rest_framework import serializers
#
#
# """syntax for serializer
# class serializer_name(serializers.ModelSerializer):
#     class Meta:
#         model = model_name
#         fields = '__all__' or ['field1', 'field2', 'field3']
# """
#
#
# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "CartItem"
#         fields = '__all__'
#
#
# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "Customer"
#         fields = '__all__'
#
#
# class AddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "Address"
#         fields = '__all__'
#
#
# class CountrySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "Country"
#         fields = '__all__'
#
#
# class StateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "State"
#         fields = '__all__'
#
#
# class DiscountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "Discount"
#         fields = '__all__'
#
#
# class GenderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "Gender"
#         fields = '__all__'
#
#
# class InventorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "Inventory"
#         fields = '__all__'
#
# class InventoryItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "InventoryItem"
#         fields = '__all__'
#
#
# class Order(serializers.ModelSerializer):
#     class Meta:
#         model = "Order"
#         fields = '__all__'
#
#
# class OrderItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "OrderItem"
#         fields = '__all__'
#
#
# class PaymentStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "PaymentStatus"
#         fields = '__all__'
#
#
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "Product"
#         fields = '__all__'
#
#
# class ProductBrandSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "ProductBrand"
#         fields = '__all__'
#
#
# class ProductCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "ProductCategory"
#         fields = '__all__'
#
#
# class ProductSubCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "ProductSubCategory"
#         fields = '__all__'
#
#
# class PurchasesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "Purchases"
#         fields = '__all__'
#
#
# class ReturnsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "Returns"
#         fields = '__all__'
#
#
# class ReviewsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "Reviews"
#         fields = '__all__'
#
#
# class ShippingMethodSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "ShippingMethod"
#         fields = '__all__'
#
#
# class ShoppingCartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "ShoppingCart"
#         fields = '__all__'
#
#
# class SupplierSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "Supplier"
#         fields = '__all__'
#
#
# class TaxSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "Tax"
#         fields = '__all__'
#
#
# class TittleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "Tittle"
#         fields = '__all__'
