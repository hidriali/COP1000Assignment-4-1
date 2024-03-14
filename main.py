"""
This program calculates prices for custom house signs.
"""
# Declare and initialize variables here.
# Charge for this sign.
# Number of characters.
# Color of characters.
# Type of wood.

woodType="oak"
color="gold"
numChars=8
mini_Charge=35
charge=0

#let the user to input the number of characters, woodTybe, and color.
numchars=input("How many characters do you want on your sign? " )
woodType=input("What type of wood do you want your sign to be made of? " )
color=input("What color do you want your sign to be? " )
#write the if statments for the four cases:

#if the input is less than 5 characters, nad the woodType is oak, and the color is gold

if int (numchars) >5 and woodType=="oak" and color== "gold":
  charge=(int(numchars)-5)*4+mini_Charge+15+20

#if the input is more than 5 characters, nad the woodType is pine, and the color is gold
 
if int (numchars)>5 and woodType=="pine" and color=="gold":
  charge=(int(numchars)-5)*4+mini_Charge+15

#if the input is more than 5 characters, nad the woodType is oak, and the color is black

if int(numchars)>5 and woodType=="oak" and color=="black":
  charge=(int(numchars)-5)*4+mini_Charge+20

#if the input is more than 5 characters, nad the woodType is oak, and the color is white
if int(numchars)>5 and woodType=="oak" and color=="white":
  charge=(int(numchars)-5)*4+mini_Charge+20

#output  charge statement      

else:
  print("the charge for your sign is " +  str(charge) )


   


  

  
  







