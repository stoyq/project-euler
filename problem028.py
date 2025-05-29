# The pattern of the diagonals appear to be 1^2, 3^2, 5^2 on the top right diagonals
# So sum that up to 1001^2
#
# Then on the other diagonals, it's 
#   [1] + 2 + 2 + 2
#   [9] + 4 + 4 + 4
#   [25] + 6 + 6 + 6
#   ...
#   ...
#   [999*999] + 1000 + 1000 + 1000
#   
#   Above is my initial observation
#
#

TOTAL = 0

for i in range(1,1002,2):
    #print(i,"*",i)
    TOTAL = TOTAL + i*i
    #Except i = 1001
    if i != 1001:
        TOTAL = TOTAL + 3*i*i + 6*(i+1)

print(TOTAL)
