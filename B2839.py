'''
Sang-geun has been delivering sugar from the sugar factory lately.
상Sang-geun must now deliver exactly N kilograms of sugar to the sweet shop.
The sugar produced at the factory comes in bags.
There are 3-kilogram bags and 5-kilogram bags.

Sang-geun finds this troublesome and wants to carry as few bags as possible.
For example, when he needs to deliver 18 kilograms of sugar,
he could take 6 x 3-kilogram bags,
but he could deliver it using fewer bags by taking 3 x 5-kilogram bags and 1 x 3-kilogram bag.

Write a programme to determine the number of bags Sang-geun needs to take when he must deliver exactly N kilograms of sugar.
---
Input:
The first line contains an integer N. (3 ≤ N ≤ 5000)

---
Output:
Output the minimum number of bags Sang-geun must deliver. If it is impossible to make exactly N kilograms, output -1.
'''
import sys
def main(n:int):

    #Initialising the DP table
    dp = [float('inf')]*((n//5)+1)
    # Increase the number of 5kg bags by one each
    for i in range((n//5)+1):
        # If the remainder after removing the 5-kilogramme bag is divided into 3-kilogramme portions,
        if (n-i*5)%3 == 0:
            # i(Number of 5kg bags) + Number of 3kg bags
            dp[i] = i+ (n-i*5)//3
    # If inf is the minimum, return -1.
    if min(dp) == float('inf'):
        return -1
    # Output the minimum number found by DP search
    return min(dp)

if __name__ == '__main__':
    sys.stdout.write(str(main(int(sys.stdin.readline()))))
