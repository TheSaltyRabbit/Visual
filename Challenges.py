import math

def Challenge1(n):
  #1. Write a Python program to check if a given positive integer is a power of two.
  return (bool(n%2==0))

def Challenge2(n):
  #2. Write a Python program to check if a given positive integer is a power of three.
  return (bool(n%3==0))

def Challenge3(n):
  #3. Write a Python program to check if a given positive integer is a power of four.
  return (bool(n%4==0))

def Challenge4(n):
  #4. Write a Python program to check if a number is a perfect square.
  x = math.sqrt(n)
  number = (int(x//1), x%1)
  if number[0]>0 and number[1]==0:
    return True
  else:
    return False

def Challenge5(n,m):
  #5. Write a Python program to check if an integer is the power of another integer.
  x = n**(1.0/float(m))
  number = [int(x//1),x%1]
  if number[1]>0.9999999999999:
    number[0]+=1
    number[1]=0
  if number[0]>0 and number[1]==0:
    return True
  else:
    return False

def Challenge6(n,m):
  #6. Write a Python program to check if a number is a power of a given base.
  i = 0
  j = 0
  while i<n:
    j+=1
    i = m**j
    if i==n: return True
  return False

def Challenge7(x):
  #7. Write a Python program to find a missing number from a sequential list.
  i = 0
  missing = 0
  for num in x:
    if x[i]+1!=x[i+1]: missing = x[i]+1
    i+=1
    if i==len(x)-1 : return missing

def Challenge8(x):
  #8. Write a Python program to find missing numbers from a list.
  j = 0
  missing = []
  for i in range (x[0],x[-1]):
    if i!= x[j]:
      j-=1
      missing.append(i)
    j+=1
  return missing

def Challenge9(x):
  #Write a Python program to find three numbers from an array such that the sum of three numbers equal to zero.
  #Note : Find the unique triplets in the array.
  index1=0
  index2=1
  index3=2
  zeroes=[]
  while True:
    if x[index1]+x[index2]+x[index3]==0: zeroes.append([x[index1],x[index2],x[index3]])
    if index3==len(x)-1 and index2==len(x)-2 and index1==len(x)-3: return zeroes
    elif index3==len(x)-1 and index2==len(x)-2 and index1!=len(x)-3:
      index1+=1
      index2=index1+1
      index3=index2+1
    elif index3==len(x)-1 and index2!=len(x)-2:
      index2+=1
      index3=index2+1
    else:
      index3+=1
    
def Challenge10(x):
  #10. Write a Python program to find three numbers from an array such that the sum of three numbers equal to a given number.
  index1=0
  index2=1
  index3=2
  zeroes=[]
  while True:
    if x[0][index1]+x[0][index2]+x[0][index3]==x[-1]: zeroes.append([x[0][index1],x[0][index2],x[0][index3]])
    if index3==len(x[0])-1 and index2==len(x[0])-2 and index1==len(x[0])-3: return zeroes
    elif index3==len(x[0])-1 and index2==len(x[0])-2 and index1!=len(x[0])-3:
      index1+=1
      index2=index1+1
      index3=index2+1
    elif index3==len(x[0])-1 and index2!=len(x[0])-2:
      index2+=1
      index3=index2+1
    else:
      index3+=1

def Challenge11(x):
  #11. Write a Python program to compute and return the square root of a given 'integer'.
  #Note : The returned value will be an 'integer'
  return round(math.sqrt(x))

def Challenge12(x):
  #12. Write a Python program to find the single number in a list that doesn't occur twice.
  inputarray=x
  deletenumber = 0
  end = len(inputarray)
  j=0
  while len(inputarray)>1:
    i=j+1
    while i<len(inputarray):
      if inputarray[j]==inputarray[i]: 
        deletenumber = inputarray[i]
        inputarray.remove(deletenumber)
        inputarray.remove(deletenumber)
        j=0
        i=1
      else: i+=1
    j+=1
  return inputarray

def Challenge13(x):
  #13. Write a Python program to find the single element in a list where every element appears three times except for one.
  index1=0
  index2=1
  index3=2
  deletenumber=0
  while len(x)>1:
    if x[index1]==x[index2]==x[index3]:#all 3 equal, delete and reset
      deletenumber=x[index1]
      for i in range (0,3): x.remove(deletenumber)
      index1=0
      index2=1
      index3=2
    elif index3<len(x)-1: #index 3 is below cap
      index3+=1
    elif index2<len(x)-2: #index 3 at cap, 2 below
      index2+=1
      index3=index2+1
    elif index1<len(x)-3: #3 at cap, 2 at cap, 1 below
      index1+=1
      index2=index1+1
      index3=index2+1
  return x

def Challenge14(x):
  #14. Write a Python program to find the single element appears once in a list where every element appears four times except for one.
  index1=0
  index2=1
  index3=2
  index4=3
  deletenumber=0
  while len(x)>1:
    if x[index1]==x[index2]==x[index3]==x[index4]:#all 4 equal, delete and reset
      deletenumber=x[index1]
      for i in range (0,4): x.remove(deletenumber)
      index1=0
      index2=1
      index3=2
      index4=3
    elif index4<len(x)-1: #index 4 is below cap
      index4+=1
    elif index3<len(x)-2: #index 4 at cap, 3 below
      index3+=1
      index4=index3+1
    elif index2<len(x)-3: #4 at cap, 3 at cap, 2 below
      index2+=1
      index3=index2+1
      index4=index3+1
    elif index1<len(x)-4: #4 at cap, 3 at cap, 2 at cap, 1 below
      index1+=1
      index2=index1+1
      index3=index2+1
      index4=index3+1
  return x

def Challenge15(x):
  #15. Write a Python program to find two elements don't appear twice in a list where all the other elements appear exactly twice in the list.
  inputarray=x
  deletenumber = 0
  j=0
  while True:
    i=j+1
    while i<len(inputarray):
      if inputarray[j]==inputarray[i]: 
        deletenumber = inputarray[i]
        inputarray.remove(deletenumber)
        inputarray.remove(deletenumber)
        j=0
        i=1
      else: i+=1
    if j<len(inputarray): j+=1
    else: return inputarray

def Challenge16(x):
  #16. Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit.
  tenplus = 0
  ones = 0
  combined = x
  while combined>9:
    tenplus = combined//10
    ones=combined%10
    combined = ones+tenplus
  return combined
  
def Challenge17():
  #17. Write a Python program to find whether it contains an additive sequence or not.
  #Also, you can split a number into one or more digits to create an additive sequence.
  #Note : Numbers in the additive sequence cannot have leading zeros.
  return ("FIX LATER")

def Challenge18(x):
  #18. Write a Python program to reverse the digits of an integer.
  numstr = str(x)
  output = []
  length = len(numstr)-1
  if numstr[0]=="-": 
    output.insert(0,"-")
    end=0
  else:
    end=-1
  for i in range (length,end,-1):
    output.append(numstr[i])
  return int("".join(output))
    
#def Challenge19(x):
  #19. Write a Python program to reverse the bits of an integer (32 bits unsigned).
