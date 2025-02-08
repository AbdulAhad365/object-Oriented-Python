# square = []
# for num in nums:
#     if num >= 5:
#      square.append(num ** 2)
# print(square)
# squares = [num **2 for num in nums if num >= 5]
# print("List comprehension", squares)

# problem: return the number that are gretaer than 10 first multiply by 2 and add by 3
arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
value=[]
                                    # WAY 1: TO SOLVE THE PROBLEM
# for n in arr:
#     if (n>10):
#         # print(n)
#         value.append((n*2)+3)
def print_values():
    for x in value:
        print(x)

                                    # WAY 2: TO SOLVE THE PROBLEM

value=[(n*2)+3 for n in arr if n>10]
print_values()