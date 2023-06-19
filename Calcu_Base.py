import math
import numpy

numpy.set_printoptions(3, suppress=True)

tn = int(input('Enter the total number of nodes : ')) #total nodes
te = int(input('Enter the total number of Elements : ')) #total elements
xco = [] #x co ordinate of nodes
yco = [] #y co ordinate of nodes
for i in range(tn):
    x = float(input('Enter the x co-ordinate of node '+str(i+1)+' in mm : '))
    y = float(input('Enter the y co-ordinate of node '+str(i+1)+' in mm : '))
    xco.append(x)
    yco.append(y)

#print(xco)
#print(yco)
    
A = int(200)
E = float('210000')

snofel = [] #start node of elements
enofel = [] #end node of elements
lenofel = [] #length of the element
elcon = [] #constant of the element
cosofel = [] #cos of element
sinofel = [] #sin of element

for i in range(te):  
    a = int(input('Enter the Start node of element '+str(i+1)+' : '))
    b = int(input('Enter the End node of element '+str(i+1)+' : '))
   # print(a)
   # print(b)
    x1 = float(xco[a-1])
    y1 = float(yco[a-1])
    x2 = float(xco[b-1])
    y2 = float(yco[b-1])
    l = math.sqrt((x2-x1)**2+(y2-y1)**2)
    con = A*E/l
    cos = (x2-x1)/l
    sin = (y2-y1)/l
    
    snofel.append(a)
    enofel.append(b)
    lenofel.append(l)
    elcon.append(con)
    cosofel.append(cos)
    sinofel.append(sin)
    
    #print(snofel)
    #print(enofel)
    #print(lenofel)
    #print(elcon)
    #print(cosofel)
    #print(sinofel)

elstmat = [] #element stiffness matrix

for i in range(te):
    cc = float(cosofel[i])**2
    ss = float(sinofel[i])**2
    cs = float(cosofel[i])*float(sinofel[i])
    
    mat = elcon[i]*numpy.array([[cc, cs, -cc, -cs],
                      [cs, ss, -cs, -ss],
                      [-cc, -cs, cc, cs],
                      [-cs, -ss, cs, ss]])

    elstmat.append(mat)
    #print('matriz')
    #print(elstmat)


gstmatmap = []                          ## Global stiffness matrix mapping, gstmatmap will be the sqare matrix of tn*
for i in range(te):                     ## do this for each elements
    m = snofel[i]*2                     ## taking the start node of element(i) and multiply by 2
    n = enofel[i]*2                     ## taking the end node of element(i) and multiply by 2
    add = [m-1, m, n-1, n]              ## Address of columns and rows of gstmatmap for elemet(i)
                                            # if startnode is 1 and end node is 2 then add=[1,2,3,4]
                                            # if startnode is 1 and end node is 3 then add=[1,2,5,6]
    gmat = numpy.zeros((tn*2, tn*2))    ## global stiffness matrix loaded with zeros for element(i)
    elmat = elstmat[i]                  ## taking the element stiffness matrix of element(i)
    for j in range(4):                  
        for k in range(4):              
            a = add[j]-1                ## addressing row of GST matrix for element(i)
            b = add[k]-1                ## addressing column of GST matrix for element(i)
            gmat[a,b] = elmat[j,k]      ## updating the values in GST matrix with EST matrix of element(i)
    gstmatmap.append(gmat)              ## storing the resultant matrix in gstmatmap list
   # print('numpy around')
#print(numpy.around(gmat, 3))

GSM = numpy.zeros((tn*2, tn*2))         ## creating an empyty GSM matrix
for mat in gstmatmap:
    GSM = GSM+mat                       ## adding all the matrix in the gstmatmap list
                                            # this will result in assembled stiffness matrix of the truss structure

#print('\nGlobal Stiffness Matrix of the Truss\n')
#print(numpy.around(GSM, 3))

#-----------------------Boundry condition and Loading---------------------#

displist = []
forcelist = []
for i in range(tn):
    a = str('u')+str(i+1)
    displist.append(a)
    b = str('v')+str(i+1)
    displist.append(b)
    c = str('fx')+str(i+1)
    forcelist.append(c)
    d = str('fy')+str(i+1)
    forcelist.append(d)

print(displist)
print(forcelist)
    
print('\n\n________________Support Specifications______________\n')

dispmat = numpy.ones((tn*2,1))
tsupn = int(input('Enter the total number of nodes having supports : ')) #total number of supported nodes
supcondition = ['P = pinned',
                'H = Horizonal restrained (vertical is free to move)',
                'V = Vertical restrained (Horizontal is free to move)']
   
for i in range(tsupn):
    supn = int(input('\nEnter the node number of suuport : ')) #supported node
    for a in supcondition:
        print(a)
    condition = str(input('\nEnter the condition of the support : '))
    if condition in['P', 'p']:
        dispmat[supn*2-2, 0] = 0
        dispmat[supn*2-1, 0] = 0
    elif condition in['H', 'h']:
        dispmat[supn*2-2, 0] = 0
    elif condition in['V', 'v']:
        dispmat[supn*2-1, 0] = 0
    else:
        print('Please enter valid entries')
##print(dispmat)


print('\n_________________Loading____________________\n')
forcemat = numpy.zeros((tn*2,1))
tlon = int(input('Enter the total number of loaded nodes : ')) #total number of loaded nodes

for i in range(tlon):
    lon = int(input('\nEnter the node number of Loading : ')) #Loaded node
    fx = float(input('Enter the Horizontal load at this node in N : '))
    fy = float(input('Enter the Vertical load at this node in N : '))
    forcemat[lon*2-2, 0] = fx
    forcemat[lon*2-1, 0] = fy

##print(forcemat)    


###_________________Matrix Reduction_________________###


rcdlist = []
for i in range(tn*2):
    if dispmat[i,0] == 0:
        rcdlist.append(i)

rrgsm = numpy.delete(GSM, rcdlist, 0) #row reduction
crgsm = numpy.delete(rrgsm, rcdlist, 1) #column reduction
rgsm = crgsm #reduced global stiffness matrix
rforcemat = numpy.delete(forcemat, rcdlist, 0) #reduced force mat
rdispmat = numpy.delete(dispmat, rcdlist, 0) #reduced disp mat

###_______________Solving____________________###

dispresult = numpy.matmul(numpy.linalg.inv(rgsm), rforcemat)
rin = 0
for i in range(tn*2):
    if dispmat[i,0] == 1:
        dispmat[i,0] = dispresult[rin,0]
        rin = rin+1
##print(dispmat)

forceresult = numpy.matmul(GSM, dispmat)
##print(forceresult)

print('\n\nGlobal Stiffness Matrix of the Truss\n')
print(GSM)
print('\n\nDisplacement matrix of nodes\n')
print(dispmat)
print('\n\nForce matrix of nodes\n')
print(forceresult)

##____________________new co ordinates of nodes____________####

newxco = []
newyco = []
count = 0
for i in range(tn):
    k = xco[i]+dispmat[count,0]
    newxco.append(k)
    count = count+1
    l = yco[i]+dispmat[count,0]
    newyco.append(l)
    count = count+1

###____________________new length of memebers______________####
    
newlenofel = []
for i in range(te):
    a, b = snofel[i], enofel[i]
    x1 = float(newxco[a-1])
    y1 = float(newyco[a-1])
    x2 = float(newxco[b-1])
    y2 = float(newyco[b-1])
    l = math.sqrt((x2-x1)**2+(y2-y1)**2)
    newlenofel.append(l)

##print(newlenofel)
##print(lenofel)

###______________strain in elements_______________________###
    
numpy.set_printoptions(3, suppress=False)

elstrain = numpy.zeros((te,1))
for i in range(te):
    elstrain[i,0] = (newlenofel[i]-lenofel[i])/(lenofel[i])
print('\n***Positive is Tensile\nNegetive is Compressive***\n')

print('\n\nStrain in the elements')
print(elstrain)
numpy.set_printoptions(3, suppress=True)

###__________________stress in elements______________________###

elstress = numpy.zeros((te,1))
for i in range(te):
    elstress[i,0] = E * elstrain[i,0]
    
print('\n\nStress in the elements')
print(elstress)

###_________________Member forces____________________#########

eforce = numpy.zeros((te,1))
for i in range(te):
    eforce[i,0] = A * elstress[i,0]

print('\n\nForce in the element')
print(eforce)

##numpy.delete(mat, row, 0)
##numpy.delete(mat, col, 1)
##numpy.matmul(mat1, mat2)
##numpy.linalg.inv(mat)
##numpy.arange(start, end, step)
##array.reshape(row, col)
##numpy.zeros((row,col))
##numpy.ones((row,col))

