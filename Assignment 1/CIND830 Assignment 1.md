## CIND830 - Python Programming for Data Science  
### Ilhak Park
### Assignment 1 (10% of the final grade)
### Due on October 12, 2020 11:59 PM  

*****
This is a Jupyter Notebook document that extends a simple formatting syntax for authoring HTML and PDF.
Review [this](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html) website for more details on using Juputer Notebook.

Use the JupyterHub server on the Google Cloud Platform,
provided by your designated instructor, for this assignment.
Complete the assignment by inserting your Python code wherever you see the string
"#INSERT YOUR ANSWER HERE."

When you click the `File` button, from the top navigation bar, then select `Export Notebook As ...`,
a document (PDF or HTML format) will be generated that includes
 both the assignment content and the output of any embedded Python code chunks.

Using [these](https://www.ryerson.ca/courses/students/tutorials/assignments/) guidelines,
submit **both** the IPYNB and the exported file (PDF or HTML).
Failing to submit both files will be subject to mark deduction.

*****

### Question 1:
Based on Canada's government [labour market indicators](https://www150.statcan.gc.ca/n1/pub/71-607-x/71-607-x2017001-eng.htm) in August 2020, the unemployment population in Toronto decreased to approximately 518 thousand in August of 2020 with a month-to-month change rate of -2.5 percent.

*****

**a)** Create four variables:
`cityName` as String (Toronto),
`augPopulation` as Integer (518),
`changeRate` as Floating-point number (-2.5%),
and `decreasing` as Boolean (True).


```python
cityName = "Toronto"
augPopulation = 518
changeRate = -0.025
decreasing = True
```

**b)** Print every literal and type of the variables in Q1.a in a separate new line.


```python
print ("cityName:", cityName, type(cityName))
print ("augPopulation:", augPopulation, type (augPopulation))
print ("changeRate:", changeRate, type(changeRate))
print ("decreasing:", decreasing, type(decreasing))
```

    cityName: Toronto <class 'str'>
    augPopulation: 518 <class 'int'>
    changeRate: -0.025 <class 'float'>
    decreasing: True <class 'bool'>


**c)** If the unemployment rate stays the same in September, find how many people would still be unemployed? Round off the answer to the nearest whole number.


```python
sepPopulation = round(augPopulation * (1+changeRate),0)
print("The unemployment population in September might be", sepPopulation, "thousand.")
```

    The unemployment population in September might be 505.0 thousand.


**d)** Find the difference between the unemployment population
of August and that of September.


```python
print ("The difference is approximately", abs(augPopulation - sepPopulation), "thousand.")
```

    The difference is approximately 13.0 thousand.


**e)** Convert the variable `augPopulation` to a floating-point number
then print the new literal and type.


```python
augPopulation = float (augPopulation)
print (augPopulation, type (augPopulation))
```

    518.0 <class 'float'>


**f)** Given that `var1` is the `sepPopulation` variable rounded to the nearest whole number,
and `var2` is the `changeRate` variable rounded to two decimal places.
Print the following statement:
The unemployment populaton might be `var1` thousand in September 2020, which is a `var2` month-to-month change rate.


```python
var1 = sepPopulation
var2 = round(changeRate,2)
print("The unemployment populaton might be" , var1, "thousand in September 2020, which is a ", var2, " month-to-month change rate.")
```

    The unemployment populaton might be 505.0 thousand in September 2020, which is a  -0.03  month-to-month change rate.


*****

### Question 2:
Create a list of numbers called `nmbrs` starting at 0 and ending at 21, using the following code:


```python
# a list of numbers from 0 to 21
nmbrs = list(range(22))
print(nmbrs, end = ' ')
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21] 

**a)**  Print the `nmbrs` list in reverse order using a simple `for` loop.


```python
#Q asking to make a list.
reverse_nmbrs = [] 
for i in nmbrs[::-1]:
    reverse_nmbrs.append(i)
print(reverse_nmbrs)
```

    [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


**b)**  Print only the numbers that are divisible by 7.


```python
#Q not asking to make a list
new_nmbrs = []
for x in range(22):
    if x%7==0:
        new_nmbrs.append(str(x))
print (', '.join(new_nmbrs))
```

    0, 7, 14, 21


**c)**  Print the odd numbers that are multiple of 3.


```python
new_nmbrs1 = []
for x in nmbrs:
    if x %2!=0 and x%3==0:
        new_nmbrs1.append(str(x))
print(', '.join(new_nmbrs1))
```

    3, 9, 15, 21


**d)**  Create another list called `nmrls` that includes the corresponding english names of the numbers in the `nmbrs` list, starting at `zero` and ending at `twenty-one`. 
Hint:  Import the [inflect](https://pypi.org/project/inflect/) library, then use the `number_to_words()` function to convert numbers into words.


```python
import inflect
nmrls = []
i = 0
for num in nmbrs:
    inflector = inflect.engine()
    nmrls.append(inflector.number_to_words(nmbrs[i]))
    i= i+1
print (nmrls)
```

    ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one']


**e)**  Use a nested loop to count the letters
 of each element in the `nmrls` list, then print the
 element along with its number of letters.


```python
counter =0
for item in nmrls:
    for letter in item:
        counter +=1
    print(item, "has" ,counter, "letters.")
    counter=0

```

    zero has 4 letters.
    one has 3 letters.
    two has 3 letters.
    three has 5 letters.
    four has 4 letters.
    five has 4 letters.
    six has 3 letters.
    seven has 5 letters.
    eight has 5 letters.
    nine has 4 letters.
    ten has 3 letters.
    eleven has 6 letters.
    twelve has 6 letters.
    thirteen has 8 letters.
    fourteen has 8 letters.
    fifteen has 7 letters.
    sixteen has 7 letters.
    seventeen has 9 letters.
    eighteen has 8 letters.
    nineteen has 8 letters.
    twenty has 6 letters.
    twenty-one has 10 letters.


**f)**  Print the elements in the `nmrls` list that
 have more than or equal to 7 letters and has either the letter 'o' or the letter 'g'.


```python
new_nmrls = []
for letter in nmrls:
    if len(letter)>=7: 
        if 'o' in letter or 'g'in letter:
            new_nmrls.append(letter)
print(new_nmrls)
```

    ['fourteen', 'eighteen', 'twenty-one']


*****

### Question 3:
Write a program that accepts the lengths of three sides of a triangle as
inputs, using the following code, then prints the type of the triangle according to the conditions listed below.


```python
# Acquiring Inputs
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))
```

    Enter the first side: 3
    Enter the second side: 4
    Enter the third side: 5


**a)**  Equilateral Triangle: If the triangle has three congruent sides.


```python
if side1==side2==side3:
    print("The Triangle is Equilateral.")
else:
    print("The Triangle is not Equilateral.")
```

    The Triangle is not Equilateral.


**b)**  Isosceles Triangle: If the triangle has two equal sides.


```python
if side1==side2!=side3 or side1==side3!=side2 or side1!=side2==side3:
    print("The Triangle is Isosceles.")
else:
    print("The Triangle is not Isosceles.")
```

    The Triangle is not Isosceles.


**c)**  Scalene Triangle: If the triangle has no congruent sides, and
 each side have a different length.


```python
if side1!=side2!=side3:
    print("The Triangle is Scalene.")
else:
    print("The Triangle is not Scalene.")
```

    The Triangle is Scalene.


**d)**  Right Triangle: If the square of one side equals the sum of the squares of the other
two sides.


```python
rightTriangle =(side2*side2) + (side3*side3) or (side2*side2) == (side1*side1) + (side3*side3) or (side3*side3) == (side2*side2) + (side1*side1)
if (side1*side1) == (side2*side2) + (side3*side3) or (side2*side2) == (side1*side1) + (side3*side3) or (side3*side3) == (side2*side2) + (side1*side1):
    print("The Triangle is a Right Triangle.")
else:
    print("The Triangle is not a Right Triangle.")
```

    The Triangle is a Right Triangle.


**e)**  Combine your answers in Q3a, Q3b, Q3c, and Q3d and write one program that decides the type of a given triangle according to its sides' length. Notably, a right triangle might be isosceles or scalene. (e.g. A triangle with the following sides: 3, 4, and 5 cm is a right scalene triangle)


```python
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
```

    The Triangle is a Right Scalene Triangle.


#### This is the end of assignment 1
