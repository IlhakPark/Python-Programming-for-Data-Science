#!/usr/bin/env python
# coding: utf-8

# ## CIND830 - Python Programming for Data Science  
# ### Ilhak Park
# ### Assignment 3 (10% of the final grade)
# ### Due on December 07, 2020 11:59 PM

# *****
# This is a Jupyter Notebook document that extends a simple formatting syntax for authoring HTML and PDF.
# Review [this](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html) website for more details on using Jupyter Notebook.
# 
# Use the JupyterHub server on the Google Cloud Platform,
# provided by your designated instructor, for this assignment.
# Complete the assignment by inserting your Python code wherever you see the string
# "#INSERT YOUR ANSWER HERE." or "##CODE HERE##"
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

# **a)** Write a code segment to create and print a two-dimensional 5x4 array (i.e. grid). The elements of the grid should be randomly selected from the inclusive interval \[-50, 50\].

# In[78]:


import random
class iArray():
    def __init__(self, capacity, fillValue = None):
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, newItem):
        self._items[index] = newItem

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)
    
    
class iGrid():
    def __init__(self, rows, columns, fillValue = None):
        self._data = iArray(rows)
        for row in range(rows):
            self._data[row] = iArray(columns, fillValue)

    def getRows(self):
        return len(self._data)

    def getColumns(self):
        return len(self._data[0])

    def __getitem__(self, index):
        return self._data[index]

    def __str__(self):
        result = ' '
        for row in range(self.getRows()):
            for col in range(self.getColumns()):
                result += str(self._data[row][col]) + ' '
            result += '\n'
        return result

myGrid = iGrid(5,4)
for i in range (myGrid.getRows()):
    for j in range (myGrid.getColumns()):
        myGrid[i][j] = random.randrange(-50, 50)
print (myGrid)


# **b)** Write a code segment that searches the `Grid` object in `Q1a` for all the negative integers, and prints them.

# In[79]:


lst=[]
for i in range (myGrid.getRows()):
    for j in range (myGrid.getColumns()):
        myGrid[i][j] = random.randrange(-50, 50)
        if myGrid[i][j] < 0:
                lst.append(myGrid[i][j])

print (myGrid)
print ("The negative numbers are:",lst)


# **c)** Given that `iList = [1, -1, 2, -2]`, add each element of `iList` to its corresponding element of `Q1a` `Grid` row-wise.  
# 
# For example, if the Grid is equal to: $$\begin{pmatrix} 1 & 2 & 1 & 1 \\ 3 & 0 & 1 & 6 \\ 0 & 2 & 4 & 6 \\ 4 & 5 &0 & 2 \\ 3 & 6 & 4 & 3 \end{pmatrix}$$
# 
# Then the output should be:
# $$\begin{pmatrix} 1+1 & 2-1 & 1+2 & 1-2 \\ 3+1 & 0-1 & 1+2 & 6-2 \\ 0+1 & 2-1 & 4+2 & 6-2 \\ 4+1 & 5-1 &0+2 & 2-2 \\ 3+1 & 6-1 & 4+2 & 3-2 \end{pmatrix}$$

# In[80]:


myGrid = iGrid(5,4)
for i in range (myGrid.getRows()):
    for j in range (myGrid.getColumns()):
        myGrid[i][j] = random.randrange(-50, 50)
print (myGrid)

iList = [1,-1,2,-2 ]
for i in range(myGrid.getRows()):
    for j in range(myGrid.getColumns()):
        myGrid[i][j] = myGrid[i][j] + iList[j]
print ("The updated grid is:")
print (myGrid)


# **d)** Write a code segment that creates a ragged grid with three rows.  The first row contains 2 positions, the second row contains 4 positions, and the third row contains 6 positions. 

# In[81]:


class iGrid():
    def __init__(self, rows, fillValue = None):
        self._data = iArray(rows)
        columns= rows - 1
        for row in range(rows):
            self._data[row] = iArray(columns, fillValue)
            columns = columns +  2
    def getRows(self):
        return len(self._data)

    def getColumns(self):
        return len(self._data[0])

    def __getitem__(self, index):
        return self._data[index]

    def __str__(self):
        result = ' '
        for row in range(self.getRows()):
            for col in range(self.getColumns()):
                result += str(self._data[row][col]) + ' '
            result += '\n'
        return result
               
newGrid = iGrid(3)
for i in range(newGrid.getRows()):
    print(newGrid[i])


# 
# 
# ### Question 2:
# A search algorithm `iSearch` and a variable `ilist` have been defined as follows:
# 
# 
# 

# In[82]:


def iSearch(target, lyst):
    left = 0
    right = len(lyst) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target == lyst[midpoint]:
            return midpoint
        elif target < lyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1

iList = [11, 20, 29, 33, 41, 55, 56, 62, 66, 74, 88]


# **a)**  If the target element is `11`, trace the values of the variables `left`, `right`, and `midpoint` after applying the `iSearch` algorithm to the `iList` structure. 
# 
# 

# In[83]:


def iSearch(target, lyst):
    left = 0
    right = len(lyst) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target == lyst[midpoint]:
            
            return midpoint
        elif target < lyst[midpoint]:
            right = midpoint - 1
            print("The current value of left is ", left)
            print("The current value of right is", right)
            print("The current value of midpoint is", midpoint)
        else:
            left = midpoint + 1
            
        
    return -1

iList = [11, 20, 29, 33, 41, 55, 56, 62, 66, 74, 88]
print("\nThe position of the target element is", iSearch(11,iList))
print("Since the target is less than the midpoint, the final values of left, right, and midpoint are 0, 1, 2, respectively.")


# **b)**  Repeat the tracing process in `Q1a` for target element `55`.

# In[85]:


def iSearch(target, lyst):
    left = 0
    right = len(lyst) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target == lyst[midpoint]:
            print("The value of midpoint variable is",midpoint)
            print("The value of left variable is",left)
            print("The value of right variable is",right)
            return midpoint
        elif target < lyst[midpoint]:
            right = midpoint - 1
        else: 
            left = midpoint + 1
    return -1
    

iList = [11, 20, 29, 33, 41, 55, 56, 62, 66, 74, 88]
print("The reason why the left and right variables do not change is because we find the target, at once, at the midpoint, which is",iSearch(55,iList))


# **c)**  Why does the iSearch algorithm run faster in `Q1b` scenario than in `Q1a` scenario?

# In[ ]:


'''
iSearch uses the Binary Search method to find the postion of the target number.
Since the iSearch compares the target element to the middle position item first in the list,
iSearch algorithm run faster to trace '55' than '11' in iList.
'''


# **d)** Modify the `iSearch` algorithm, so it can run in `Q1a` scenario as fast as it does in `Q1b` scenario.

# In[49]:


def new_iSearch(target, lyst):
    position = 0
    while position <len(lyst):
        if target == lyst[position]:
            return position
        position +=1
    return -1

iList = [11, 20, 29, 33, 41, 55, 56, 62, 66, 74, 88]
print(new_iSearch(11,iList))
print(new_iSearch(55,iList))


# **e)** For a problem of size $n$, if algorithm `X` performs $n^4$ instructions, and algorithm `Y` performs $2^n$ instructions.  At what point does one of the algorithms begin to be more efficient and perform better than the other? Justify your answer.

# In[ ]:


'''
If you draw the graphs of X and Y, X is below than Y in the range of (0, 1.24).
This means X takes less number of steps to solve a problem when the size is smaller than 1.24.
As the size gets larger, above 1.24, the algorithm X takes more number of steps than the algorithm Y.
Therefore, we can generally say that X is more efficient when the size is equal to 1, and Y is moer efficient when the size is greater than 1.
'''


# *****

# ### Question 3:
# 
# 

# Emulate the stack behaviour using the list data structure.

# **a)** Complete the methods of the following `Stack` class according to their description

# In[86]:


class Stack:
  def __init__(self):
    """ Initialize a new stack """
    self.elements = []
  def push(self, new_item):
    """ Append the new item to the stack """
    self.elements.append(new_item)
  def pop(self):
    """ Remove and return the last item from the stack """
    return self.elements.pop()
    
  def size(self):
    """ Return the total number of elements in the stack """
    return len(self.elements)
    
  def is_empty(self):
    """ Return True if the stack is empty and False if it is not empty """
    return self.elements == []
    
  def peek(self):
    """ Return the element at the top of the stack or return None if the stack is empty """
    return self.elements[len(self.elements) -1]


# **b)** Use the `Stack` class that you defined in `Q3a` to complete the code of the `is_valid()` function, which checks whether the order of the brackets of an arithmetic expression is correct. Some examples are given below:

# In[87]:


exp1 = "(2+3)+(1-5)" # True
exp2 = "((3*2))*(7/3))" # False
exp3 = "(3*5))]" # False


# In[94]:


def is_valid(exp):
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    stk = Stack()
    for i in exp:
        if i in opening:
            stk.push(i)
        elif i in closing:
            if stk.is_empty():
                return False
            iFromStack = stk.pop()
            if i == ']' and iFromStack != '[' or i == ')' and iFromStack != '(' or i== '}' and iFromStack != '{':
                return False
    return stk.is_empty()
  
print(is_valid(exp1))
print(is_valid(exp2))
print(is_valid(exp3))


# **c)** Use the `Stack` class that you defined in `Q3a` to complete the code of the `count_pairs()` function, which returns the number of the valid bracket pairs of an arithmetic expression. Some examples are given below:

# In[90]:


exp1 = "(2+3)+(1-5)" # 2 pairs
exp2 = "((([()])))" # 5 pairs
exp3 = "[([])" # 2 pairs


# In[93]:


def count_pairs(exp):
    """
    Count the valid number of brackets
    Returns the total number of valid brackets in the string
    """
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    count = 0
    lst = []
    for i in exp:
        if i in opening:
            lst.append(i)
        elif i in closing:
            if len(lst) == 0:
                pass
            else:
                lst.pop()
                count = count + 1
    return count
print(count_pairs(exp1),"pairs")
print(count_pairs(exp2),"pairs")
print(count_pairs(exp3),"pairs")


# ### Question 4:
# According to each method's documentation, complete the code of the `TextProcessor` class and its subclass `TextAnalyzer`.

# In[92]:


class TextProcessor:
  def __init__(self, text):
    self._text = text
  def setStopWords(self, stopWords):
    ''' set stop words as recieved in the parameters '''
    self._stopWords = stopWords
  def getStopWords(self):
    ''' return stop words '''
    return self._stopWords
  def getUniqWords():
    return set(self._text.split())
  def getFilteredText(self):
    ''' remove filter words from the text 
        return filtered text
    '''
    words = self._text.split()
    newWord =''
    for i in words:
        if i not in self._stopWords:
            newWord =newWord + ' ' + i
            newWord.strip()
    return newWord
    
class TextAnalyzer(TextProcessor):
  def __init__(self, text):
    ''' Construct the class '''
    TextProcessor.__init__(self, text)
  def getWordFrequency(self):
    ''' Call the getFilteredText() method
        Create a dictionary of words
        key = word and value= frequency
        return the dictionary
    '''
    frequencyDict = dict()
    filteredText = self.getFilteredText()
    filteredWords = filteredText.split()
    for j in filteredWords:
        if j not in frequencyDict.keys():
            frequencyDict[j] = 1
        else:
            frequencyDict[j] += 1
    return frequencyDict

#1
ta = TextAnalyzer("a quick brown fox " + "a quick brown fox jumps " +  "a quick brown fox jumps over " + "a quick brown fox jumps over the " + "a quick brown fox jumps over the lazy " + "a quick brown fox jumps over the lazy dog")
#2
ta.setStopWords(['a', 'the'])
#3
getFrequencyDict = ta.getWordFrequency()
#4
print(getFrequencyDict)


# Verify the correctness of your code using the following steps:
# 
# 1. Instantiate the `TextAnalyzer` class by creating an object called `ta` as follows:
# 
# `ta = TextAnalyzer("a quick brown fox " + 
#                   "a quick brown fox jumps " + 
#                   "a quick brown fox jumps over " + 
#                   "a quick brown fox jumps over the " + 
#                   "a quick brown fox jumps over the lazy " + 
#                   "a quick brown fox jumps over the lazy dog")`
# 
# 2. Assign a list of stop words using the `setStopWords()` method:
# `ta.setStopWords(['a', 'the'])`
# 
# 3. Count the occurrences of each word using the `getWordFrequency()` method:
# `ta.getWordFrequency()`
# 
# 4. The output should be as follows
# `{'quick': 6, 'brown': 6, 'fox': 6, 'jumps': 5, 'over': 4, 'lazy': 2, 'dog': 1}}`
# 

# #### This is the end of assignment 3
