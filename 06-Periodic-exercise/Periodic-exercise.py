# ============================
# Mini Project 1
# Topics Used:
# - Data type
# - Type conversion
# - Operators
# - input function
# - round function
# - string indexing
# ============================


# --Data type exercises--
z = 5
print (type(z))

print (float (z))

print (str(z) * 10)  # String multiplication



# --Find error exercises--

'''      
x = 'ali # Syntax error (')
y = 2
print (type(y))
'''

'''
s.5 = 10  # Syntax error (variable name rules) special character
print (type (s.5))
'''

'''   # Syntax error (variable rules)
1.    1number = 5  

2.    my-number = 10

3.    for = 20

4.    my number = 30

5.    @variable = 40

6.    float! = 50

7.    #score = 60

8.    123abc = 70

9.    class = 80

10.total sum = 90
'''

'''
t = 10
t = y + t   # Because the variable y was used before it was defined.
y = 5
print (t)
'''


# --Type conversion exercises--

a_2 = 2  # >> float
print (float (a_2))

b_2 = 2.4 # >> int 
print (int (b_2))

c_s = '1.2' # >> float 
print (float(c_s))

e_t = True # >> int
print (int(e_t))



# --input function exercises--

xis = input('input a word')
print (xis * 10)

xii = int(input ('a number'))
print (xii * 10)

# Get the ages of two people from the user and calculate the difference between their ages

sen1 = int(input('sen 1 >>'))
sen2 = int(input('sen 2 >>'))
print ('The difference between their : ' , sen2 - sen1)

# Get two numbers from the user and adding them

adad1 = int (input('adad 1 >>'))
adad2 = int (input('adad 2 >>'))
jadad = print ('The sum of these two numbers is' , adad1 + adad2)

# Get a radius from the user and calculating the perimeter and area

radius = float (input('Input a radius >>'))
print ('Perimeter is >>' , radius * 2 * 3.14 , 'and area is >>' , radius * radius * 3.14)



# --round function exercises--

# A program for round number

xro = float (input('input a number'))
print (round(xro , 2)) 











