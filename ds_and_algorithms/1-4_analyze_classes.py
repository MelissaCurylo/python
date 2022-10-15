"""
Classes

Creating a class is creating my own data type. 

Constructor constructs object in a class.
    # def __init__(self,color)
        # def = define
        # __init__ = initialize
        # (self,color) = instance of class Cookie binded with parameter color being passed into method. 
        # self represents an instance of the class.
            # If self is included then it is a method and part of a class.
            # self gives access to class attributes and methods. 
            # self binds attributes with the given arguments , if there is one passed in.
            # self is needed at Python does not use @ syntax to refer to instance attributes. 


"""
# Cookie class
class Cookie:
    def __init__(self, color):  # constructor with parameters
        self.color = color

    def get_color(self): # method with only self so no arguments being passed and will return whatever color is being passed in.
        return self.color

    def set_color(self, color): # method with a parameter to pass it a color and this method will change that cookies color. 
        self.color = color


# Creating Cookies
cookie_one = Cookie('green') # variable being set to type Cookie and passing the color green through the constructor to create a green cookie.
cookie_two = Cookie('blue')


# Printing results of creation
print('\nCookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

# 
cookie_one.set_color('pink')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())