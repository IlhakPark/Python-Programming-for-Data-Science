#!/usr/bin/env python
# coding: utf-8

# ## CIND830 - Python Programming for Data Science  
# ### Ilhak Park
# ### Assignment 1 (10% of the final grade)
# ### Due on October 12, 2020 11:59 PM  

# *****
# This is a Jupyter Notebook document that extends a simple formatting syntax for authoring HTML and PDF.
# Review [this](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html) website for more details on using Juputer Notebook.
# 
# Use the JupyterHub server on the Google Cloud Platform,
# provided by your designated instructor, for this assignment.
# Complete the assignment by inserting your Python code wherever you see the string
# "#INSERT YOUR ANSWER HERE."
# 
# When you click the `File` button, from the top navigation bar, then select `Export Notebook As ...`,
# a document (PDF or HTML format) will be generated that includes
#  both the assignment content and the output of any embedded Python code chunks.
# 
# Using [these](https://www.ryerson.ca/courses/students/tutorials/assignments/) guidelines,
# submit **both** the IPYNB and the exported file (PDF or HTML).
# Failing to submit both files will be subject to mark deduction.

# *****

# ### Question 1:
# Based on Canada's government [labour market indicators](https://www150.statcan.gc.ca/n1/pub/71-607-x/71-607-x2017001-eng.htm) in August 2020, the unemployment population in Toronto decreased to approximately 518 thousand in August of 2020 with a month-to-month change rate of -2.5 percent.

# *****

# **a)** Create four variables:
# `cityName` as String (Toronto),
# `augPopulation` as Integer (518),
# `changeRate` as Floating-point number (-2.5%),
# and `decreasing` as Boolean (True).

# In[66]:


cityName = "Toronto"
augPopulation = 518
changeRate = -0.025
decreasing = True


# **b)** Print every literal and type of the variables in Q1.a in a separate new line.

# In[67]:


print ("cityName:", cityName, type(cityName))
print ("augPopulation:", augPopulation, type (augPopulation))
print ("changeRate:", changeRate, type(changeRate))
print ("decreasing:", decreasing, type(decreasing))


# **c)** If the unemployment rate stays the same in September, find how many people would still be unemployed? Round off the answer to the nearest whole number.

# In[68]:


sepPopulation = round(augPopulation * (1+changeRate),0)
print("The unemployment population in September might be", sepPopulation, "thousand.")


# **d)** Find the difference between the unemployment population
# of August and that of September.

# In[70]:


print ("The difference is approximately", abs(augPopulation - sepPopulation), "thousand.")


# **e)** Convert the variable `augPopulation` to a floating-point number
# then print the new literal and type.

# In[71]:


augPopulation = float (augPopulation)
print (augPopulation, type (augPopulation))


# **f)** Given that `var1` is the `sepPopulation` variable rounded to the nearest whole number,
# and `var2` is the `changeRate` variable rounded to two decimal places.
# Print the following statement:
# The unemployment populaton might be `var1` thousand in September 2020, which is a `var2` month-to-month change rate.

# In[72]:


var1 = sepPopulation
var2 = round(changeRate,2)
print("The unemployment populaton might be" , var1, "thousand in September 2020, which is a ", var2, " month-to-month change rate.")


# *****

# ### Question 2:
# Create a list of numbers called `nmbrs` starting at 0 and ending at 21, using the following code:

# In[33]:


# a list of numbers from 0 to 21
nmbrs = list(range(22))
print(nmbrs, end = ' ')


# **a)**  Print the `nmbrs` list in reverse order using a simple `for` loop.

# In[34]:


#Q asking to make a list.
reverse_nmbrs = [] 
for i in nmbrs[::-1]:
    reverse_nmbrs.append(i)
print(reverse_nmbrs)


# **b)**  Print only the numbers that are divisible by 7.

# In[35]:


#Q not asking to make a list
new_nmbrs = []
for x in range(22):
    if x%7==0:
        new_nmbrs.append(str(x))
print (', '.join(new_nmbrs))


# **c)**  Print the odd numbers that are multiple of 3.

# In[36]:


new_nmbrs1 = []
for x in nmbrs:
    if x %2!=0 and x%3==0:
        new_nmbrs1.append(str(x))
print(', '.join(new_nmbrs1))


# **d)**  Create another list called `nmrls` that includes the corresponding english names of the numbers in the `nmbrs` list, starting at `zero` and ending at `twenty-one`. 
# Hint:  Import the [inflect](https://pypi.org/project/inflect/) library, then use the `number_to_words()` function to convert numbers into words.

# In[41]:


import inflect
nmrls = []
i = 0
for num in nmbrs:
    inflector = inflect.engine()
    nmrls.append(inflector.number_to_words(nmbrs[i]))
    i= i+1
print (nmrls)


# **e)**  Use a nested loop to count the letters
#  of each element in the `nmrls` list, then print the
#  element along with its number of letters.

# In[65]:


counter =0
for item in nmrls:
    for letter in item:
        counter +=1
    print(item, "has" ,counter, "letters.")
    counter=0


# **f)**  Print the elements in the `nmrls` list that
#  have more than or equal to 7 letters and has either the letter 'o' or the letter 'g'.

# In[64]:


new_nmrls = []
for letter in nmrls:
    if len(letter)>=7: 
        if 'o' in letter or 'g'in letter:
            new_nmrls.append(letter)
print(new_nmrls)


# *****

# ### Question 3:
# Write a program that accepts the lengths of three sides of a triangle as
# inputs, using the following code, then prints the type of the triangle according to the conditions listed below.

# In[57]:


# Acquiring Inputs
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))


# **a)**  Equilateral Triangle: If the triangle has three congruent sides.

# In[63]:


if side1==side2==side3:
    print("The Triangle is Equilateral.")
else:
    print("The Triangle is not Equilateral.")


# **b)**  Isosceles Triangle: If the triangle has two equal sides.

# In[59]:


if side1==side2!=side3 or side1==side3!=side2 or side1!=side2==side3:
    print("The Triangle is Isosceles.")
else:
    print("The Triangle is not Isosceles.")


# **c)**  Scalene Triangle: If the triangle has no congruent sides, and
#  each side have a different length.

# In[60]:


if side1!=side2!=side3:
    print("The Triangle is Scalene.")
else:
    print("The Triangle is not Scalene.")


# **d)**  Right Triangle: If the square of one side equals the sum of the squares of the other
# two sides.

# In[61]:


rightTriangle =(side2*side2) + (side3*side3) or (side2*side2) == (side1*side1) + (side3*side3) or (side3*side3) == (side2*side2) + (side1*side1)
if (side1*side1) == (side2*side2) + (side3*side3) or (side2*side2) == (side1*side1) + (side3*side3) or (side3*side3) == (side2*side2) + (side1*side1):
    print("The Triangle is a Right Triangle.")
else:
    print("The Triangle is not a Right Triangle.")


# **e)**  Combine your answers in Q3a, Q3b, Q3c, and Q3d and write one program that decides the type of a given triangle according to its sides' length. Notably, a right triangle might be isosceles or scalene. (e.g. A triangle with the following sides: 3, 4, and 5 cm is a right scalene triangle)

# In[62]:


if side1==side2==side3:
    print("The Triangle is Equilateral, and it cannot be a Right Triangle.")
elif (side1==side2!=side3 or side1==side3!=side2 or side1!=side2==side3) and ((side1*side1) == (side2*side2) + (side3*side3) or (side2*side2) == (side1*side1) + (side3*side3) or (side3*side3) == (side2*side2) + (side1*side1)):
        print("The Triangle is a Right Isosceles Triangle.")
elif (side1==side2!=side3 or side1==side3!=side2 or side1!=side2==side3) and not ((side1*side1) == (side2*side2) + (side3*side3) or (side2*side2) == (side1*side1) + (side3*side3) or (side3*side3) == (side2*side2) + (side1*side1)):
    print("The Triangle is Isosceles, but it is not a Right Triangle.")
elif (side1!=side2!=side3) and (side1*side1) == (side2*side2) + (side3*side3) or (side2*side2) == (side1*side1) + (side3*side3) or (side3*side3) == (side2*side2) + (side1*side1):
    print("The Triangle is a Right Scalene Triangle.")
else:
    print("The Triangle is Scalene, but it is not a Right Triangle.")


# #### This is the end of assignment 1
