def most_expensive_product(products):
    '''
    Find the product with the highest price.

    Parameters:
        products (dict): Dictionary of product: price pairs.

    Returns:
        tuple: (product_name, price) of the highest priced product.
    '''
    return max(products.items(), key=lambda x: x[1])
    # Take one item called x and return its second element.
    # key=lambda x: x[1] - Use the price to compare the items.
    # max() returns the original item that produced the highest comparison value.
    # max(iterable, key=function) means: "Look at every item, use the function to decide what value to compare, and return the original item that has the largest comparison value."



products = {
    "Laptop": 80000,
    "Phone": 60000,
    "Tablet": 35000,
    "Monitor": 15000
}

product, price = most_expensive_product(products)
print(f"The most expensive product is '{product}' with price {price}.")
