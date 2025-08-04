# function 

cities = ["barisal","Patakhali","dhaka", "k"]

def count_of_lenth(list : list):
    print(len(list))


def list_single_line(list : list):
     for item in list : 
          print(item,end=" ")



def factorial(n) : 
     final = 1
     for num in range(1, n+1) :
          final *= num
     print(final) 


def usd_to_taka(usd): 
     taka_rate = 122.23
     taka = usd * taka_rate
     print(usd,"USD =",taka,".TK")


def funtaion():
     value = int(input("Input a number : "))
     if(value % 2 ==0) : print("This is EVEN")
     else  : print("This is ODD")


def sumofnubmer(n):
     if(n==0) :
          return 0
     return n + sumofnubmer(n-1)


def recursiveList(list,ind=0):
     if(len(list) == ind) : return
     print(list[ind])
     recursiveList(list,ind + 1)


list = ["Agun", "Bagun",True,"JFF",55]

print(recursiveList(list))
