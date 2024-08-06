'''
Simple retail System Backend making Orders '''


'''
Product - Class 
add_product()
- Parameter(s): `cls`, `name`, `category`, `quantity`, `price`, and `supplier`.
- Behavior: 
    - Define the `product_id` assuming it's auto-generated incrementally.
    - Define a `new_product` variable that will call the constructor of the Product class.
    - Return the message `"Product added successfully"` to know that the product was added successfully.

### `update_product()`
- Parameter(s): `cls`, `product_id`, `quantity`, `price`, and `supplier`.
    - `quantity`, `price`, and `supplier` should have default values of `None`. 
- Behavior: 
    - Check if the `product_id` already exists in the `inventory`.
    - If `product_id` exists, check for the given parameters in the method if they have a value and update accordingly the product.
    - Return either one of these messages: `"Product information updated successfully."` or `"Product not found."`.

### `delete_product()`
- Parameter(s): `cls`, `product_id`.
- Behavior: 
    - Check in the inventory list if the given `product_id` was passed as a parameter.
    - If `product_id` exists then remove the product from the list.
    - Return either one of these messages: `"Product deleted successfully."` or `"Product not found."`.

'''
class Product:
    inventory=[]
    def __init__(self,product_id,name,category,quantity,price,supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier
        Product.inventory.append(self)
        
        
    @classmethod
    def add_product(cls,name,category,quantity,
                    price,supplier):
        product_id = len(cls.inventory)+1
        new_product = Product(product_id
                              ,name,category
                              ,quantity,price,
                              supplier)
        return 'Product added successfully'
    
    @classmethod
    def update_product(cls,product_id,
                       quantity=None,price=None,
                       supplier=None):
        Found = False
        prod = 0
        for product in cls.inventory:
            if product.product_id == product_id:
                prod = product
                Found = True
                break
                
        if Found == True:
            if quantity != None:
                prod.quantity = quantity
            if price != None:
                prod.price = price
            if supplier != None:
                prod.supplier = supplier
            return 'Product information updated successfully'
        else:
            return 'Product not found'
    
    @classmethod
    def delete_product(cls,product_id):
        Found = False
        for product in cls.inventory:
            if product.product_id == product_id:
                Found = True
                cls.inventory.remove(product)
                break
        if Found:
            return'Product deleted successfully'
        else:
            return 'Product not found'
        

'''
## `Order` method(s)

### `place_order()
- Parameter(s): `self`, `product_id`, `quantity`, and `customer_info`.
    - `customer_info`  has a default value of `None`.
- Behavior: 
    - Append to the `products` list a tuple containing `product_id` and `quantity`.
    - Assumming that each order can only take **one** product. 
    - Return the message: `"Order placed successfully. Order ID: {self.order_id}"`'''        
class Order:
    def __init__(self,order_id,products=[],
                 customer_info=None):
        self.order_id = order_id
        self.products = products
        self.customer_info =customer_info
    
    def place_order(self,product_id,quantity,
                    customer_info=None):
        prod = 0
        found = False
        for product in Product.inventory:
            if product.product_id == product_id and product.quantity >= quantity:
                found = True
                prod = product
                break
            
        if found:
            prod.quantity  -= quantity
            self.products.append((product_id,quantity))
            if customer_info:
                self.customer_info =customer_info
            return f'Order placed successfully. Order ID: {self.order_id}'
        else:
            return f'Order could not be placed. Product not found or insufficient quantity'


p1 = Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A")
update_p1 = Product.update_product(1, quantity=45, price=950)
#delete_p1 = Product.delete_product(1)
order = Order(order_id=1, products=[])
order_placement = order.place_order(1, 40, customer_info="John Doe")
print(order_placement)
