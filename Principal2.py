import math
import numpy
import tkinter        as tk
import customtkinter  as ctk 


numpy.set_printoptions(3, suppress=True)

numpy.set_printoptions(3, suppress=True)

window = ctk.CTk()                  # Cria a nossa janela
window._set_appearance_mode('dark') 
window.title('Calculadora de Treliçãs')
sw = window.winfo_screenwidth()
sh = window.winfo_screenheight()
ww = int(5*sw/6)
wh = int(5*sh/6)
who = int(1*(sh-wh)/3)
wwo = int((sw-ww)/2)
window.minsize(800,600)
winsize = str(ww)+'x'+str(wh)+'+'+str(wwo)+'+'+str(who) 
window.geometry(winsize)

                            # Configuração dos frames
window.columnconfigure([0,1], weight=1)
window.rowconfigure(1, weight=1)
titleframe = ctk.CTkFrame(window,bg_color='#030e11')  # Frame do Titulo
guiframe = ctk.CTkFrame(window,bg_color='#030e11')    # Frame Principal
graphframe = ctk.CTkFrame(window,bg_color='#030e11')  # Frame Grafíco
titleframe.grid(row=0,column=0,columnspan=2,sticky='nsew')
guiframe.grid(row=1,column=0,sticky='nsew')
graphframe.grid(row=1,column=1,sticky='nsew')

                            # Frame Do Título
titleframe.columnconfigure(0, weight=1)
titlelbl = ctk.CTkLabel(titleframe, text='Calculadora de Treliças 2d',bg_color='#020a0d',text_color='white')
titlelbl.grid(row=0,column=0,sticky='nsew')

                            # Frame Principal
guiframe.columnconfigure(0, weight=1)
guiframe.rowconfigure(0, weight=1)
guiframe.grid_propagate(0)

guicanvs = ctk.CTkCanvas(guiframe, highlightthickness=0,background='#030e11',)                             
guivscrol = ctk.CTkScrollbar(guiframe, orientation='vertical', command=guicanvs.yview,bg_color='#030e11')  #scrollbar esquerda
guihscrol = ctk.CTkScrollbar(guiframe, orientation='horizontal', command=guicanvs.xview,bg_color='#030e11') #scrollbar direita
guicanvs.grid(row=0,column=0,sticky='nsew')
guivscrol.grid(row=0,column=1,rowspan=2,sticky='nsew')
guihscrol.grid(row=1,column=0,sticky='nsew')

guicanvs.columnconfigure(0, weight=1)
guicanvs.rowconfigure(0, weight=1)
containerframe = ctk.CTkFrame(guicanvs,fg_color='#030e11') # ContainerFrame 
containerframe.grid(row=0,column=0,sticky='nsew')

guicanvs.create_window((0,0), width=ww/2-17, window=containerframe, anchor='nw', tags=('canwin'))

containerframe.bind('<Configure>', lambda e: guicanvs.configure(scrollregion=guicanvs.bbox('all')))
guicanvs.configure(yscrollcommand=guivscrol.set, xscrollcommand=guihscrol.set)

containerframe.columnconfigure([0,1,2], weight=1)

graphframe.grid_propagate(0)
graphframe.columnconfigure(0, weight=1)
graphframe.rowconfigure(0, weight=1)
plotcanvs = ctk.CTkCanvas(graphframe,highlightthickness=0, width=ww/2,bg='#041216')       # cores tela canvas e tamanhop
plotcanvs.grid(row=0,column=0,sticky='nsew')

####____________________________________________________________________________________####

labellist=[]
entrylist=[]
buttonlist=[]

inputlist=[]

xco=[]
yco=[]

xplotpts=[]
yplotpts=[]

snofel=[]
enofel=[]

lenofel=[]
elcon=[]
cosofel=[]
sinofel=[]

elstmat=[]
gstmatmap=[]

displist=[]
forcelist=[]

numpymatlist=[]

def btnprs(btn):

    ###_____________________________________________________________________###

    if btn == 'btn1':
        def drawcoinp():
            tn = int(entrylist[0].get())
            te = int(entrylist[1].get())
            inputlist.append(tn)
            inputlist.append(te)
            for i in range(tn):                
                lbl = ctk.CTkLabel (containerframe , text = "posição X e Y do nó " + str(i+1) + ":",text_color='white')  
                labellist.append(lbl)
                lbl.grid(row=2+i,column=0,sticky='nsew')
                xent = ctk.CTkEntry(containerframe)
                entrylist.append(xent)
                yent = ctk.CTkEntry(containerframe)
                entrylist.append(yent)
                xent.grid(row=2+i,column=1,sticky='nsew')
                yent.grid(row=2+i,column=2,sticky='nsew')
            btn2 = ctk.CTkButton(containerframe, text='Plot', command = lambda: btnprs('btn2'))
            buttonlist.append(btn2)
            btn2.grid(row=2+tn,column=0,columnspan=2,sticky='nsew')
        if len(inputlist)==0:
            drawcoinp()
        else:
            for i in range(2,len(labellist)):
                labellist[i].destroy()
            for i in range(2, len(entrylist)):
                entrylist[i].destroy()
            for i in range(1, len(buttonlist)):
                buttonlist[i].destroy()
                
            del inputlist[0:]
            del labellist[2:]
            del entrylist[2:]
            del buttonlist[1:]
            xco.clear()
            yco.clear()
            xplotpts.clear()
            yplotpts.clear()
            snofel.clear()
            enofel.clear()
            plotcanvs.delete('all')
            drawcoinp()
    ###_____________________________________________________________________###
            
    if btn == 'btn2':
        def getcoordinates():
            btn3 = ctk.CTkButton(containerframe, text='OK', command=lambda: btnprs('btn3'))
            buttonlist.append(btn3)
            btn3.grid(row=2+inputlist[0],column=2,columnspan=2,sticky='nsew')
            count=0
            for i in range(inputlist[0]):
                xco.append(float(entrylist[2+count].get()))
                yco.append(float(entrylist[3+count].get()))
                count = count+2
            ###________________###
            def draw():
                plotcanvs.update()
                w = plotcanvs.winfo_width()-30
                h = plotcanvs.winfo_height()-30
                xmax, ymax, xmin, ymin = max(xco), max(yco), min(xco), min(yco)
                if xmin<=0:
                    alpax = w/xmax-xmin
                else:
                    alpax = w/xmax
                if ymin<=0:
                    alpay = h/ymax-ymin
                else:
                    alpay = h/ymax
                for i in range(len(xco)):
                    x, y = int(xco[i]), int(yco[i])
                    vert = (h-alpay*0.8*y)-h/9
                    yplotpts.append(vert)
                    hori = (alpax*0.8*x)+w/8
                    xplotpts.append(hori)
                    x1, y1, x2, y2 = hori-6, vert-6, hori+6, vert+6
                    plotcanvs.create_oval(x1,y1,x2,y2, width=2, fill='blue', tags='nodes')
                    t = 'N'+str(i+1)
                    plotcanvs.create_text(x2+10, y2+10, text=t, font=('Areal 10 bold'), tags='nodenum')
            draw()
            ###______________###
        if len(xco)==0:
            getcoordinates()
        else:
            xco.clear()
            yco.clear()
            xplotpts.clear()
            yplotpts.clear()
            plotcanvs.delete('all')
            for i in range(2, len(buttonlist)):
                buttonlist[i].destroy()
            del buttonlist[2:]
            getcoordinates()
    ###_____________________________________________________________________###          

    if btn == 'btn3':
        tn = inputlist[0]
        te = inputlist[1]
        def getstennodes():
            for i in range(te):
                lbl = ctk.CTkLabel (containerframe , text = "qual o nó inicial do elemento " + str(i+1) + "?",text_color='white')  
                labellist.append(lbl)
                lbl.grid(row=2+tn+1+i, column=0, sticky='nsew')
                snentry = ctk.CTkEntry(containerframe)
                entrylist.append(snentry)
                snentry.grid(row=2+tn+1+i, column=1, sticky='nsew')
                enentry = ctk.CTkEntry(containerframe)
                entrylist.append(enentry)
                enentry.grid(row=2+tn+1+i, column=2, sticky='nsew')
            btn4 = ctk.CTkButton(containerframe, text='Colocar elemento', command=lambda: btnprs('btn4'))
            buttonlist.append(btn4)
            btn4.grid(row=2+tn+1+te, column=0, columnspan=2, sticky='nsew')

        if len(labellist)==2+tn:
            getstennodes()
        else:
            for i in range(2+tn, len(labellist)):
                labellist[i].destroy()
            for i in range(2+2*tn, len(entrylist)):
                entrylist[i].destroy()

            del labellist[2+tn:]
            del entrylist[2+2*tn:]
            for i in range(3, len(buttonlist)):
                buttonlist[i].destroy()
            del buttonlist[3:]
            getstennodes()
    ###_____________________________________________________________________### 

    if btn == 'btn4':
        tn = inputlist[0]
        te = inputlist[1]
        btn5 = ctk.CTkButton(containerframe, text='OK', command=lambda: btnprs('btn5'))
        buttonlist.append(btn5)
        btn5.grid(row=2+tn+1+te,column=2,sticky='nsew')
        def plotelements():
            count=0
            for i in range(te):
                snofel.append(int(entrylist[2+2*tn+count].get()))
                enofel.append(int(entrylist[3+2*tn+count].get()))
                count = count+2
            for i in range(te):
                sn = snofel[i]
                en = enofel[i]
                x1 = xplotpts[sn-1]
                y1 = yplotpts[sn-1]
                x2 = xplotpts[en-1]
                y2 = yplotpts[en-1]
                plotcanvs.create_line(x1,y1,x2,y2, width=3, tags='elements')
                t = 'E'+str(i+1)
                plotcanvs.create_text(((x1+x2)/2)+15, ((y1+y2)/2)+15, text=t, font=('Arial 10 bold'), tags='elnum')
                
        if len(snofel)==0:
            plotelements()
        else:
            snofel.clear()
            enofel.clear()
            plotcanvs.delete('elements','elnum')
            plotelements()
    ###_____________________________________________________________________###

    if btn == 'btn5':
        tn = inputlist[0]
        te = inputlist[1]

        for labels in labellist:
            labels.configure(state='disabled')
        for entries in entrylist:
            entries.configure(state='disabled')
        for buttons in buttonlist:
            buttons.configure(state='disabled')
        
        tsnlbl = ctk.CTkLabel (containerframe , text = "Quantidades de suportes nos nós",text_color='white')      
        labellist.append(tsnlbl)
        tsnlbl.grid(row=2+tn+1+te+1, column=0, sticky='nsew')
        tsnentry = ctk.CTkEntry(containerframe)
        entrylist.append(tsnentry)
        tsnentry.grid(row=2+tn+1+te+1, column=1, sticky='nsew')
        btn6 = ctk.CTkButton(containerframe, text='OK', command=lambda: btnprs('btn6'))
        buttonlist.append(btn6)
        btn6.grid(row=2+tn+1+te+1, column=2, sticky='nsew')
        
        for i in range(te):  
            a = snofel[i]
            b = enofel[i]
            x1 = float(xco[a-1])
            y1 = float(yco[a-1])
            x2 = float(xco[b-1])
            y2 = float(yco[b-1])
            l = math.sqrt((x2-x1)**2+(y2-y1)**2)
            A = 200
            E = 2e5
            con = A*E/l
            cos = (x2-x1)/l
            sin = (y2-y1)/l
            lenofel.append(l)
            elcon.append(con)
            cosofel.append(cos)
            sinofel.append(sin)

        for i in range(te):
            cc = float(cosofel[i])**2
            ss = float(sinofel[i])**2
            cs = float(cosofel[i])*float(sinofel[i])
            
            mat = elcon[i]*numpy.array([[cc, cs, -cc, -cs],
                              [cs, ss, -cs, -ss],
                              [-cc, -cs, cc, cs],
                              [-cs, -ss, cs, ss]])

            elstmat.append(mat)                     
        for i in range(te):                     
            m = snofel[i]*2                     
            n = enofel[i]*2                     
            add = [m-1, m, n-1, n]                                              
            gmat = numpy.zeros((tn*2, tn*2))    
            elmat = elstmat[i]                  
            for j in range(4):                  
                for k in range(4):              
                    a = add[j]-1                
                    b = add[k]-1                
                    gmat[a,b] = elmat[j,k]      
            gstmatmap.append(gmat)              

        GSM = numpy.zeros((tn*2, tn*2))         
        for mat in gstmatmap:
            GSM = GSM+mat
        numpymatlist.append(GSM)



    if btn == 'btn6':
        tn = inputlist[0]
        te = inputlist[1]
        for i in range(tn):
            a = str('u')+str(i+1)
            displist.append(a)
            b = str('v')+str(i+1)
            displist.append(b)
            c = str('fx')+str(i+1)
            forcelist.append(c)
            d = str('fy')+str(i+1)
            forcelist.append(d)

        dispmat = numpy.ones((tn*2,1))
        numpymatlist.append(dispmat)
        tsupn = int(entrylist[2+tn*2+te*2].get())
        inputlist.append(tsupn)
        t = 'Digita "P" para suporte Fixo\nDigita "H" para suporte horizontal (vertical é livre para se mover)\nDigita "V" para suporte Vertical (Horizontal é livre para se mover)'
        infolbl = ctk.CTkLabel(containerframe, text=t,text_color='white')
        infolbl.grid(row=2+tn+1+te+1+1, column=0, columnspan=3, sticky='nsew')

        count=0
        for i in range(tsupn):
            lbl1 = ctk.CTkLabel(containerframe, text='Entra com o numero do nó que vai receber o suporte',text_color='white')
            labellist.append(lbl1)
            entry1 = ctk.CTkEntry(containerframe)
            entrylist.append(entry1)
            lbl2 = ctk.CTkLabel(containerframe, text='Escolha o tipo do suporte',text_color='white')
            labellist.append(lbl2)
            entry2 = ctk.CTkEntry(containerframe)
            entrylist.append(entry2)
            lbl1.grid(row=2+tn+1+te+1+1+1+count, column=0, sticky='nsew')
            lbl2.grid(row=2+tn+1+te+1+1+1+count+1, column=0, sticky='nsew')
            entry1.grid(row=2+tn+1+te+1+1+1+count, column=1, sticky='nsew')
            entry2.grid(row=2+tn+1+te+1+1+1+count+1, column=1, sticky='nsew')
            count = count+2
        btn7 = ctk.CTkButton(containerframe, text='OK', command=lambda: btnprs('btn7'))
        buttonlist.append(btn7)
        btn7.grid(row=2+tn+1+te+1+1+1, column=2, rowspan=2*tsupn, sticky='nsew')

    if btn == 'btn7':
        tn = inputlist[0]
        te = inputlist[1]
        tsupn = int(inputlist[2])
        dispmat = numpymatlist[1]
        count=0
        for i in range(tsupn):
            supn = int(entrylist[2+2*tn+2*te+1+count].get())
            condition = str(entrylist[2+2*tn+2*te+1+1+count].get())
            if condition in['P', 'p']:
                dispmat[supn*2-2, 0] = 0
                dispmat[supn*2-1, 0] = 0
                x = xplotpts[supn-1]
                y = yplotpts[supn-1]
                plotcanvs.create_polygon(x,y,x+15,y+25,x-15,y+25, fill='gray', tags='suports')
                plotcanvs.create_text(x,y+20, text='P', font=('Arial 15 bold'))
            elif condition in['H', 'h']:
                dispmat[supn*2-2, 0] = 0
                x = xplotpts[supn-1]
                y = yplotpts[supn-1]
                plotcanvs.create_polygon(x,y,x+25,y+15,x-25,y+15, fill='red', tags='suports')
                plotcanvs.create_text(x,y+20, text='H', font=('Arial 15 bold'))
            elif condition in['V', 'v']:
                dispmat[supn*2-1, 0] = 0
                x = xplotpts[supn-1]
                y = yplotpts[supn-1]
                plotcanvs.create_polygon(x,y,x+15,y+25,x-15,y+25, fill='lightgreen', tags='suports')
                plotcanvs.create_text(x,y+20, text='V', font=('Arial 15 bold'))
            count=count+2

        loadlbl = ctk.CTkLabel(containerframe, text='Enter the total number of loaded nodes',text_color='white')
        labellist.append(loadlbl)
        ent = ctk.CTkEntry(containerframe)
        entrylist.append(ent)
        btn8 = ctk.CTkButton(containerframe, text='OK', command=lambda: btnprs('btn8'))
        buttonlist.append(btn8)

        loadlbl.grid(row=2+tn+1+te+1+1+2*tsupn+1, column=0, sticky='nsew')
        ent.grid(row=2+tn+1+te+1+1+2*tsupn+1, column=1, sticky='nsew')
        btn8.grid(row=2+tn+1+te+1+1+2*tsupn+1, column=2, sticky='nsew')
        

    if btn == 'btn8':
        tn = inputlist[0]
        te = inputlist[1]
        tsupn = int(inputlist[2])
        tlon = int(entrylist[2+2*tn+2*te+1+2*tsupn].get())
        inputlist.append(tlon)
        count=0
        for i in range(tlon):
            
            lonlbl = ctk.CTkLabel(containerframe, text='Enter the node number of Loading : ')
            labellist.append(lonlbl)
            fxlbl = ctk.CTkLabel(containerframe, text='Força Horizontal do nó em N : ')
            labellist.append(fxlbl)
            fylbl = ctk.CTkLabel(containerframe, text='Força Vertical do nó em N : ')
            labellist.append(fylbl)
            lonent = ctk.CTkEntry(containerframe)
            entrylist.append(lonent)
            fxent = ctk.CTkEntry(containerframe)
            entrylist.append(fxent)
            fyent = ctk.CTkEntry(containerframe)
            entrylist.append(fyent)

            lonlbl.grid(row=2+tn+1+te+1+1+2*tsupn+1+1+count, column=0, sticky='nsew')
            fxlbl.grid(row=2+tn+1+te+1+1+2*tsupn+1+1+count+1, column=0, sticky='nsew')
            fylbl.grid(row=2+tn+1+te+1+1+2*tsupn+1+1+count+2, column=0, sticky='nsew')
            lonent.grid(row=2+tn+1+te+1+1+2*tsupn+1+1+count, column=1, columnspan=2, sticky='nsew')
            fxent.grid(row=2+tn+1+te+1+1+2*tsupn+1+1+count+1, column=1, columnspan=2, sticky='nsew')
            fyent.grid(row=2+tn+1+te+1+1+2*tsupn+1+1+count+2, column=1, columnspan=2, sticky='nsew')
            

        count=count+3
        btn9 = ctk.CTkButton(containerframe, text='OK', command=lambda: btnprs('btn9'))
        buttonlist.append(btn9)
        btn9.grid(row=2+tn+1+te+1+1+2*tsupn+1+1+3*tlon, column=0, columnspan=3, sticky='nsew')
            
        
  
    if btn == 'btn9':
        tn = inputlist[0]
        te = inputlist[1]
        tsupn = int(inputlist[2])
        tlon = int(inputlist[3])
        forcemat = numpy.zeros((tn*2,1))
        count=0
        for i in range(tlon):
            lon = int(entrylist[2+2*tn+2*te+1+2*tsupn+1+count].get())
            fx = float(entrylist[2+2*tn+2*te+1+2*tsupn+1+count+1].get())
            fy = float(entrylist[2+2*tn+2*te+1+2*tsupn+1+count+2].get())
            forcemat[lon*2-2, 0] = fx
            forcemat[lon*2-1, 0] = fy
            x = xplotpts[lon-1]
            y = yplotpts[lon-1]

            
            plotcanvs.create_line(x,y,x-50,y, width=2, arrow=ctk.FIRST)
            plotcanvs.create_line(x,y,x,y+50, width=2, arrow=ctk.FIRST)
            plotcanvs.create_text(x-55, y-10, text = str(fx))
            plotcanvs.create_text(x, y+50, text= str(fy))
            count=count+3
        numpymatlist.append(forcemat)
        btn10 = ctk.CTkButton(containerframe, text='Resolver', command=lambda: btnprs('btn10'))
        buttonlist.append(btn10)
        btn10.grid(row=2+tn+1+te+1+1+2*tsupn+1+1+3*tlon+1, column=0, columnspan=3, sticky='nsew')
        
  
    if btn == 'btn10':
        tn = inputlist[0]
        te = inputlist[1]
        tsupn = int(inputlist[2])
        tlon = int(inputlist[3])
        GSM = numpymatlist[0]
        dispmat = numpymatlist[1]
        forcemat = numpymatlist[2]
        A = 200
        E = 2e5


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
        numpymatlist[1] = dispmat

        forceresult = numpy.matmul(GSM, dispmat)
        numpymatlist.append(forceresult)

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


        newpltxco = []
        newpltyco = []
        newxpltpts = []
        newypltpts = []
        count=0
        for i in range(tn):
            k = xco[i]+50*dispmat[count,0]
            newpltxco.append(k)
            count = count+1
            l = yco[i]+50*dispmat[count,0]
            newpltyco.append(l)
            count = count+1
        

        for i in range(len(newpltxco)):
            plotcanvs.update()
            w = plotcanvs.winfo_width()-30
            h = plotcanvs.winfo_height()-30
            xmax, ymax, xmin, ymin = max(newpltxco), max(newpltyco), min(newpltxco), min(newpltyco)
            if xmin<=0:
                alpax = w/xmax-xmin
            else:
                alpax = w/xmax
            if ymin<=0:
                alpay = h/ymax-ymin
            else:
                alpay = h/ymax
            for i in range(len(newpltxco)):
                x, y = int(newpltxco[i]), int(newpltyco[i])
                vert = (h-alpay*0.8*y)-h/9
                newypltpts.append(vert)
                hori = (alpax*0.8*x)+w/8
                newxpltpts.append(hori)
                x1, y1, x2, y2 = hori-6, vert-6, hori+6, vert+6
                plotcanvs.create_oval(x1,y1,x2,y2, width=2, fill='blue', tags='nodes')
    

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




tnlbl = label = ctk.CTkLabel (containerframe , text = "Número Total de nós",text_color='white')      

labellist.append(tnlbl)
telbl = ctk.CTkLabel(containerframe, text='Número total de barras : ',text_color='white')
labellist.append(telbl)
tnety = ctk.CTkEntry(containerframe)
entrylist.append(tnety)
teety = ctk.CTkEntry(containerframe)
entrylist.append(teety)
btn1 = ctk.CTkButton(containerframe, text='OK', command = lambda: btnprs('btn1'))
buttonlist.append(btn1)

tnlbl.grid(row=0,column=0,sticky='nsew')
telbl.grid(row=1,column=0,sticky='nsew')
tnety.grid(row=0,column=1,sticky='nsew')
teety.grid(row=1,column=1,sticky='nsew')
btn1.grid(row=0,column=2,rowspan=2,sticky='nsew')
    















window.mainloop()



##
####numpy.delete(mat, row, 0)
####numpy.delete(mat, col, 1)
####numpy.matmul(mat1, mat2)
####numpy.linalg.inv(mat)
####numpy.arange(start, end, step)
####array.reshape(row, col)
####numpy.zeros((row,col))
####numpy.ones((row,col))
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
