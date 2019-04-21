from random import randint          # Importing `randint` method from `random` package
from typing import Dict, List       # Importing `Dict`, and `List` from package `typing`

#   This method gets an integer as a parameter which indicates the length of the function's product
def get_random_list(n: int) -> list:
    a = []                          # The list we are building (The product of the function)
    for i in range(n):              
        a.append(randint(0,100))    # Appending a random number between 0 and 100 (including 100 for `randint`, 
                                    # it some other random methods it might be not included such as `randrage(0, 100 + 1)`) 
                                    # to the list
    return a

# This method gets a list as the parameter and returns the sum of the elements of the list
def get_sum(a: list) -> int:
    sum = 0             # The variable which is going to hold the value of sum (this is the variable that we return)
    for i in a:         # Looping through the list. `i` picks an ELEMENT of the list every time (in every iteration).
        # sum = sum + i # Adding i to the sum
        sum += i        # Adding i to the sum 
    return sum

# Given a list of words (strings) the function returns a sentence (a String)
def sentences(words: list) -> str:
    sen = ""
    for word in words:
        #################################################################################
        ################################### IMPORTANT ###################################
        #################################################################################
        # I have commented the codes below (4 lines of code), becase if we have a dupl- #
        # icate value in the list as the last element, the function will still recogni- #
        # zes the element as the final element. Take a look at the following example.   #
        #                                                                               #
        # >>> the_list = ["Hello,", "this", "is", "a", "very", "amazing", "day.",       #
        #  "Very", "amazing"]                                      ^                    #
        #              ^                                           |------> This element holds the same value, although they             
        #              |----> This is the actual final word                are located at different indices 
        #                                                                               #
        #   Using that method, the above code would have the following output           #
        # >>> "Hello this ia a very amazingday. Very amazing"                           #
        #                                  ^                                            #
        #                                  |---> As you can see, there is a space       #
        #                                        missing here due to this LOGICAL ERROR #
        #################################################################################

        # if word == words[len(words) - 1]: # Check if this is the last word
            # sen = sen + word              # Add the word to the sentence without a space, because last word doesn't
                                            # need a space afterwards 
        # else:                             # Else if it is not the last word
            # sen = sen + word + " "        # Add the word to the sentence and one space at the end



        sen += word + " "                   # Add the word and a space to the sentence
        # sen = str.strip(sen)              # Remove all the leading and tailing white spaces from the string and assign it
                                            # to the same variable again

                                            #############################################################################
                                            # The `strip` function in the above line of code removes the                #
                                            # white spaces and RETURNs a COPY of the string (it doesn't change the      #
                                            # string in the variable) and that's why we are assigning it to `sen` again #
                                            # I have commented the line of code above and used the function directly on #
                                            # the `return` line below                                                   #
                                            #############################################################################

    return str.strip(sen)                   # Return the sentence with leading and tailing whitespaces removed

# def sentences2(words: list) -> str:
#     sen = ""
#     for word in words:
#         sen = sen + word
#         if word != words[len(words) - 1]:
#             sen += " "
#     return sen

#    Given two lists, return the common items in the two lists as a list
def two_list(list1: list, list2: list) -> list:
    a = []                      # The final variable
    for i in list1:             # For i in lost1 (i will represent an ELEMENT of list1 each time)
        if list2.count(i) > 0:  # If the number of elements that are the same as i (The value which is currently picked 
                                # for the loop) in list two is more than ONE, that means this element also exists in list2, so
            a.append(i)         # Append i to the final list
    return a                    # Return the final list
 
 #nested loop         
 # Given a list of lists or a list of strings, return the final sentence (no space)  
def sentences3(list_of_list: list) -> str:
    sen = ""
    for thelist in list_of_list:        # for a list of chars in the list of lists (or a word in list of words)
        for char in thelist:            # for a char in the list of chars or for a char in a word
            sen = sen + char            # append the char to the sen
    return sen

def digital_sum(nums_list: list) -> int:
    """Return the sum of all the digits in all strings in nums_list."""
    sums = 0
    for nums in nums_list:              # for nums in (an element of) list of nums
        for num in nums:                # for a num in nums
            sums = sums + int(num)      # add the int of the num to the sum
    return sums

#dictionary
def express_checkout(product_to_quantity: Dict[str, int]) -> bool:
    for prods in product_to_quantity:
        if product_to_quantity[prods] > 8:
            return False
    return True

def express_checkout2(product_list):
    for value in product_list.values():
        if(value > 8):
            return False
    return True

def dictkeys(productlist):
    a = []
    for product in productlist:
        if product["rate"] > 4 and product["price"] < 100:
            a.append(product)
    return a