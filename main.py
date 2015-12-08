# Just a simple module with functions to make data analysis bit easier




#delete collumn from a list
def delCollumn(row,i):

    for row in row:
        del row[i]


# returns a new list with the elements of ith collumn in the array
def getCollumn(array,i):
    row = []

    for element in array:
        row.append (element[i])
    return row

#returns a new list with range of collumns specified
def getCollumnRange(array,x,y):
    newArray = []
    for i in range(x,y):
        col = getCollumn(array,i)
        newArray = addCollumn(newArray,col)
    return newArray


# returns the list with row added collumn wise
def addCollumn(array,row):
    if ( len(array) == 0):
        array = [[] for i in range (len(row))]

    for i in range(len(row)):
        array[i].append(row[i])
    return array






