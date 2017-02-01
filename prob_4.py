#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
palindrome_list = []
def matching_nums(x):
    if str(x)[::-1] == str(x):
        palindrome_list.append(x)
    print(palindrome_list)


first_num = 100
products =[]
while first_num < 999:
    second_num = first_num + 1
    product = first_num * second_num
    print(str(first_num) + ' * ' + str(second_num) + ' = ' + str(product))
    products.append(product)
    first_num += 1
    
#counter = 0
#for product_number in products:
#    print(product_number)
#    matching_nums(product_number)
#product = 99 * 91
#matching_nums(product, product)
