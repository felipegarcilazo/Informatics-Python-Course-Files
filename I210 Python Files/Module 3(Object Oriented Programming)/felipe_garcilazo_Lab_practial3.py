class Product(object):
    # List that tracks all products
    all_products = []

    # Prints out the products that are in the all_products list if any.
    @staticmethod
    def show_products():
        if Product.all_products:
            print("\nThe following products exist:")
            for product in Product.all_products:
                print(product)
        else:
            print("No Products exist at this time.\n")

    #The initializer
    def __init__(self, name, category, price):
        self.__name = name
        print(self.__name, "is now a Product.")
        self.__category = category
        self.__price = price
        self.__sale = False
        Product.all_products.append(self)

    # The string that is printed of the basic information of the product.
    def __str__(self):
        reply = self.__name + " (" + self.__category + "), $" + str(self.__price)
        if self.__sale == False:
            reply += " [NOT YET FOR SALE]"
        else:
            reply += " [ON SALE NOW]"
        return reply

    # The getter method
    def get_price(self):
        return self.__price

    # 2 setter methods. that can set the name and price.
    def set_name(self, name):
        if self.__name == name:
            print("Warning: The product already has that name!")
        elif not name:
            print("Warning: The product must have a name!")
        else:
            self.__name = name

    def set_price(self, price):
        if self.__price == price:
            print("Warning: The product already has that price!")
        elif price <= 0:
            print("Warning: The product must have a positive price!")
        else:
            self.__price = price

    #Approves the product for selling
    def approve(self):
        self.__sale = True

    #Overides the less than and equal to methods.
    def __lt__(self, other):
        return Product.get_price(self) < Product.get_price(other)

    def __eq__(self, other):
        return Product.get_price(self) == Product.get_price(other)


### MY CHILD CLASS lUXURY DOES NOT WORK PROPERLY BUT MY CODE WORKS PROPERLY WITHOUT IT
##class Luxury(Product):
##    def __init__(self, name, category, price, markup, slogan):
##        super().__init__(name, category, price) to work.
##        self.__name = name
##        print(self.__name, "is now a Product.\n(It's a Luxury good!)")
##        self.__category = category
##        self.__price = price
##        self.__sale = False
##        self.__markup = markup
##        self.__slogan = slogan
##        Product.all_products.append(self)
##
##    def __str__(self):
##        reply = self.__name + " (" + self.__category + "), $" + str(self.__price)
##        if self.__sale == False:
##            reply += " [NOT YET FOR SALE]"
##        else:
##            reply += " [ON SALE NOW]"
##        reply += "\n(Of Couse, it will actually sell for $" +\
##                 str(int(self.__price * self.__markup)) + " - " + self.__slogan + "!!)"
##        return reply

# Main
Product.show_products()
print("Let's create some products:")
car = Product("Cheap EV", "Car", 36200)
book = Product("Doors of Stone", "Book", 30)
banana = Product("Bluth Banana", "Fruit", 10)
book2 = Product("Oathbringer", "Book", 16)

##melon = Luxury("Square Watermelon", "Fruit", 25, 8, "Taste the price")
##car2 = Luxury("Tesla Model S", "Car", 65600, 1.25, "Good luck getting one")

print("\nHere we test warning cases. We should get 4 warning signs:")
car.set_name("")
car.set_name("Cheap EV")
car.set_name("Tesla Model 3")
car.set_price(-1)
car.set_price(36200)

car.approve()
banana.approve()

print("\nSort and show all products:")
Product.all_products.sort()
Product.show_products()
