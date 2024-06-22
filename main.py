product_value = float(input("What is the price of the product?"))
product_discount = float(input("What is the discount of the product?"))
product_discount_value = (product_value -  product_value * (product_discount/100))
print(f"The original price of the product is {product_value} The discount is {product_discount} and the new price of the product is {product_discount_value}")