def gen_product(x, y, max_num):
    palindrome_list = []
    while x <= max_num:
        while y < max_num:
            product = x * y
            if str(product) == str(product)[::-1]:
                    palindrome_list.append(product)

            y += 1
        y = x
        x += 1
    return max(palindrome_list)


print(gen_product(100, 100, 999))
