largest = 0 

#for i in range(1000):
#    for j in range(1000):
#        product = i * j
#        text = str(product)
#        if(text == text[::-1]):
#            # it's a palindrome, check if it's bigger
#            if product > largest:
#                largest = product 
#                print(i, "*", j, "=", text)

# with optimizations
# - only multiply 3 digit numbers
# - go backwards and exit inner loop early
# - avoid duplicates (i.e. i*j = j*i)


for i in range(1000, 99, -1):
    for j in range(i, 99, -1):
        #print(i, "*", j)
        product = i * j
        text = str(product)
        if product < largest:
            #print(i, "*", j, "< largest (", largest, ") BREAK inner loop!")
            break
        if(text == text[::-1]):
            #it's a palindrome, check if it's bigger
            if product > largest:
                largest = product 
                print(i, "*", j, "=", text)


print("Largest palindrome:", largest)
