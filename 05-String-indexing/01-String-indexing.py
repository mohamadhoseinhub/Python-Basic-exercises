# String indexing

s = 'Hello world' # H : 0 , e : 1 , l : 2 , ... , d : 10




# To access a character of a string :

t = s[4] # Output : 'o'




# To slice a part of a string and access it :

tb = s[4:8] # Output : 'o wo'    




# To slice from one section to the next

tba = s[4 : ] # Output : 'o world'

'or s [4 : 11]'




# Negative index of strings

s2 = 'hello'  # o : -1 , l : -2 , ... , h :-5




# There is a step for cutting

s3 = 'salam khobi ?' 

tbg = s3[2 : 12 : 2] # Output : 'lmkoi'




# Step cut to reverse

s4 = 'mohamad' 

sm = s4[ : :-1]  # Output : 'damahom'




# The string arithmetic operators are * and + 

'Example for + '


s5 = 'moha'

s6 = 'mad ast'

sj = s5 + s6[ : 3] # Output : 'mohamad'



'Example for * '

'Note: String can only be multiplied by number'

s7 = 'salam'

sz = s7 * 3 # Output : 'salamsalamsalam'





# String is an immutable data type 

s8 = 'ali akbar'

s8[5] = 'm'  # Output : error


