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
numchars=input("How many characters do you want on your sign? " )
woodType=input("What type of wood do you want your sign to be made of? " )
color=input("What color do you want your sign to be? " )
if int (numchars) >5 and woodType=="oak" and color== "gold":
  charge=(int(numchars)-5)*4+mini_Charge+15+20
 
if int (numchars)>5 and woodType=="pine" and color=="gold":
  charge=(int(numchars)-5)*4+mini_Charge+15

if int(numchars)>5 and woodType=="oak" and color=="black":
  charge=(int(numchars)-5)*4+mini_Charge+20
if int(numchars)>5 and woodType=="oak" and color=="white":
  charge=(int(numchars)-5)*4+mini_Charge+20
      

else:
  print("the charge for your sign is " +  str(charge) )


   


  

  
  





# Declare and initialize variables here.
# Charge for this sign.
# Number of characters.
# Color of characters.
# Type of wood.

# Write assignment and if statements here as appropriate.

# Output Charge for this sign.

