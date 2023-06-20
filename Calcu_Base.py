import math
import numpy

numpy.set_printoptions(3, suppress=True)

tn = int(input('Entre com o numero total de nos:')) #nos totais
te = int(input('Entre com o numero total de elementos: ')) #elementos totais
xco = [] #coordenada do nos x
yco = [] #coordenada do nos y
for i in range(tn):
    x = float(input('Entre com a coordenada x do no '+str(i+1)+' in mm : '))
    y = float(input('Entre com a coordenada y do no '+str(i+1)+' in mm : '))
    xco.append(x)
    yco.append(y)

#print(xco)
#print(yco)
    
A = int(200)
E = float('210000')

snofel = [] #no do comeco do membro
enofel = [] #no final do membro
lenofel = [] #comprimento do membro
elcon = [] #constante do membro
cosofel = [] #cos do membro
sinofel = [] #sin do membro

for i in range(te):  
    a = int(input('Entre com o no inicial da barra '+str(i+1)+' : '))
    b = int(input('Entre com o no final da barra '+str(i+1)+' : '))
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


gstmatmap = []                          ## Mapeamento da matriz de rigidez global, gstmatmap será a matriz quadrada de tn*
for i in range(te):                     ## faça isso para cada elemento
    m = snofel[i]*2                     ## pegando o nó inicial do elemento(i) e multiplicando por 2
    n = enofel[i]*2                     ## pegando o nó final do elemento(i) e multiplicando por 2
    add = [m-1, m, n-1, n]              ## Endereço de colunas e linhas de gstmatmap para elemet(i)
                                            # se o nó inicial for 1 e o nó final for 2, adicione = [1,2,3,4]
                                            # se o nó inicial for 1 e o nó final for 3, adicione = [1,2,5,6]
    gmat = numpy.zeros((tn*2, tn*2))    ## matriz de rigidez global carregada com zeros para o elemento (i)
    elmat = elstmat[i]                  ## tomando a matriz de rigidez do elemento (i)
    for j in range(4):                  
        for k in range(4):              
            a = add[j]-1                ## linha de endereçamento da matriz GST para o elemento (i)
            b = add[k]-1                ## coluna de endereçamento da matriz GST para o elemento (i)
            gmat[a,b] = elmat[j,k]      ## atualizando os valores na matriz GST com a matriz EST do elemento(i)
    gstmatmap.append(gmat)              ## armazenando a matriz resultante na lista gstmatmap
   # print('numpy around')
#print(numpy.around(gmat, 3))

GSM = numpy.zeros((tn*2, tn*2))         ## criando uma matriz GSM vazia
for mat in gstmatmap:
    GSM = GSM+mat                       ## adicionando toda a matriz na lista gstmatmap
                                            # isso resultará na matriz de rigidez montada da estrutura de treliça

#print('\nGlobal Stiffness Matrix of the Truss\n')
#print(numpy.around(GSM, 3))

#-----------------------Condição de borda e carregamento---------------------#

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

#print(displist)
#print(forcelist)
    
print('\n\n________________Espcificacoes do suporte______________\n')

dispmat = numpy.ones((tn*2,1))
tsupn = int(input('Entre com o numero total de nos com suporte : ')) #número total de nós suportados
supcondition = ['Entre com o tipo do apoio:',
                'F = Fixo',
                'H = Horizontal',
                'V = Vertical ']
print('imprimindo')
print(tsupn)
for i in range(tsupn):
    supn = int(input('\nEntre com o numero do no com suporte : ')) #nó suportado
    for a in supcondition:
        print(a)
        


    condition = str(input('\nEntre com a condicao do suporte : '))
    if condition in['F', 'f']:
        dispmat[supn*2-2, 0] = 0
        dispmat[supn*2-1, 0] = 0
    elif condition in['H', 'h']:
        dispmat[supn*2-2, 0] = 0
    elif condition in['V', 'v']:
        dispmat[supn*2-1, 0] = 0
    else:
        print('Por favor, insira entradas válidas')
#print('imprimindo dispmat')
#print(dispmat)


print('\n_________________Carga____________________\n')
forcemat = numpy.zeros((tn*2,1))
tlon = int(input('Entre com o numero total de nos com carga : ')) #número total de nós com carga

for i in range(tlon):
    lon = int(input('\nEntre com o numero do no com a carga : ')) #nó da carga
    fx = float(input('Entre com a carga horizontal do no : '))
    fy = float(input('Entre com a carga vertical do no : '))
    forcemat[lon*2-2, 0] = fx
    forcemat[lon*2-1, 0] = fy

#print(forcemat)    


###_________________Redução de matriz_________________###


rcdlist = []
for i in range(tn*2):
    if dispmat[i,0] == 0:
        rcdlist.append(i)

rrgsm = numpy.delete(GSM, rcdlist, 0) #redução de linha
crgsm = numpy.delete(rrgsm, rcdlist, 1) #redução de coluna
rgsm = crgsm #matriz de rigidez global reduzida
rforcemat = numpy.delete(forcemat, rcdlist, 0) #reducao mat forca
rdispmat = numpy.delete(dispmat, rcdlist, 0) #reducao dis mat

###_______________Resolução____________________###

dispresult = numpy.matmul(numpy.linalg.inv(rgsm), rforcemat)
rin = 0
for i in range(tn*2):
    if dispmat[i,0] == 1:
        dispmat[i,0] = dispresult[rin,0]
        rin = rin+1
##print(dispmat)

forceresult = numpy.matmul(GSM, dispmat)
##print(forceresult)

print('\n\nMatriz de rigidez global da trelica\n')
print(GSM)
print('\n\nMatriz de deslocamento dos nos\n')
print(dispmat)
print('\n\nMatriz de forca dos nos\n')
print(forceresult)

##____________________nova coordenada dos nos____________####

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

###____________________novo comprimento dos membros______________####
    
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

###______________tensão em elementos_______________________###
    
numpy.set_printoptions(3, suppress=False)

elstrain = numpy.zeros((te,1))
for i in range(te):
    elstrain[i,0] = (newlenofel[i]-lenofel[i])/(lenofel[i])
print('\n***Positivo e tracao\nNegativo e compressao***\n')

print('\n\nTensao nos elementos')
print(elstrain)
numpy.set_printoptions(3, suppress=True)

###__________________estresse em elementos______________________###

elstress = numpy.zeros((te,1))
for i in range(te):
    elstress[i,0] = E * elstrain[i,0]
    
print('\n\nEstresse nos elementos')
print(elstress)

###_________________forças membros____________________#########

eforce = numpy.zeros((te,1))
for i in range(te):
    eforce[i,0] = A * elstress[i,0]

print('\n\nForca nos membros')
print(eforce)

##numpy.delete(mat, row, 0)
##numpy.delete(mat, col, 1)
##numpy.matmul(mat1, mat2)
##numpy.linalg.inv(mat)
##numpy.arange(start, end, step)
##array.reshape(row, col)
##numpy.zeros((row,col))
##numpy.ones((row,col))

