'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def pairSum(n,input_array):
    input_array.sort()
    if input_array[0]>n:
        print("no such elements")
    else:
        for i in range(len(input_array)):
            j = 1
            for j in range(len(input_array)):
                if input_array[i]+input_array[j] == n:
                    print(input_array[i],input_array[j])
            j = j+1
            
        
    
n = int(input())
input_array = []
for i in range(5):
    array_element = int(input())
    input_array.append(array_element)
pairSum(n,input_array)




