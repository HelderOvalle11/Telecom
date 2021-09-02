'''
Universidad del Valle de Guatemala
Sistemas de telecomunicaciones 1
Proyecto 1

Luis Gómez 18291
Helder Ovalle 18349

'''

import requests
import networkx
import networkx as nx
import matplotlib.pyplot as plt
import re
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkscrolledframe import ScrolledFrame
import pydot
import pylab as plt

ventana = tk.Tk()
ventana.title('Proyecto 1 Sistemas de telecomunicaciones 1') #titulo
ventana.geometry('700x600') #ancho y alto de la ventana

#Creando 2 tabs, 1 para ingresar datos y otro para los resultados
tabControl = ttk.Notebook(ventana)
s = ttk.Style()
s.configure('new.TFrame', background='#0277BD')

tab1 = ttk.Frame(tabControl, style = 'new.TFrame')
tab2 = ttk.Frame(tabControl, style = 'new.TFrame')
tab3 = ttk.Frame(tabControl, style = 'new.TFrame')
tab4 = ttk.Frame(tabControl, style = 'new.TFrame')

tabControl.add(tab1, text ='Ingreso de datos')
tabControl.add(tab2, text ='Diagramas y resultados')
tabControl.add(tab3, text ='Mensajes Eventos')
tabControl.add(tab4, text ='Listado de ASN')
tabControl.pack(expand = 1, fill ="both")

sf = ScrolledFrame(tab3)
sf2 = ScrolledFrame(tab4)

sf.pack(side="top", expand=1, fill="both")
sf2.pack(side="top", expand=1, fill="both")

sf.bind_arrow_keys(tab3)
sf.bind_scroll_wheel(tab3)
sf2.bind_arrow_keys(tab4)
sf2.bind_scroll_wheel(tab4)

inner_frame = sf.display_widget(Frame)
inner_frame2 = sf2.display_widget(Frame)

G1 = nx.Graph()
G2 = nx.Graph()
G3 = nx.Graph()


#--------------------------------- MENSAJES DE BIENVENIDA ------------------------------------------------------------------------
bienvenida = tk.Label(tab1,text="Proyecto 1 Sistemas de telecomunicaciones 1",
                      bg="black",fg="white",font=("Verdana",16))
bienvenida2 = tk.Label(tab1,text="Integrantes: Luis Gómez 18291; Helder Ovalle 18349",
                       bg="black",fg="white",font=("Verdana",10))

bienvenida.pack(fill=tk.X) #Ubicación del título
bienvenida2.pack(fill=tk.X)

#--------------------------------- IP ------------------------------------------------------------------------

etiqueta_ip = tk.Label(tab1,text="IP: ",
                       bg="black",fg="white") #Etiqueta para ingresar ip
etiqueta_ip.place(x=10, y=70) #Ubicación de la etiqueta_ip


entry_ip = ttk.Entry(tab1) #Caja de texto para ingresar ip
entry_ip.place(x=10, y=95) #Ubicación de la caja de texto
etiqueta_ip2 = tk.Label(tab1,text="La ip ingresada es: ",
                        bg="black",fg="white") #Etiqueta para confirmar la ip ingresada
etiqueta_ip2.place(x=150, y=95) #Ubicación de la etiqueta_ip2

def ingresar_ip():
        ip1 = entry_ip.get()
        etiqueta_ip2.config(text="La ip ingresada es: "+ip1)

        return

B_ip = tk.Button(tab1, text ="Submit IP",
        bg="#BDBDBD",fg="black",height = 2, width = 10,
                 command = ingresar_ip) #Boton para ingresar ip
B_ip.place(x=10, y=120) #Ubicación del botón

#------------------------ STARTIME Y ENDTIME --------------------------------------------
etiqueta_start = tk.Label(tab1,text="Tiempo de inicio (Año-Mes-DíaTHora:Min): ",
                       bg="black",fg="white") #Etiqueta para ingresar startime
etiqueta_end = tk.Label(tab1,text="Tiempo de finalización (Año-Mes-DíaTHora:Min): ",
                       bg="black",fg="white") #Etiqueta para ingresar startime

etiqueta_start.place(x=10, y=180) #Ubicación de startime
etiqueta_end.place(x=10, y=220) #Ubicación de endtime

entry_start = ttk.Entry(tab1) #Caja de texto para ingresar startime
entry_end = ttk.Entry(tab1) #Caja de texto para ingresar endtime

entry_start.place(x=250, y=180) #Ubicación de la caja de texto startime
entry_end.place(x=280, y=220) #Ubicación de la caja de texto endtime

etiqueta_start2 = tk.Label(tab1,text="Startime ingresado: ",
                        bg="black",fg="white") #Etiqueta para confirmar startime
etiqueta_end2 = tk.Label(tab1,text="Endtime ingresado: ",
                        bg="black",fg="white") #Etiqueta para confirmar endtime
etiqueta_start2.place(x=380, y=180) #Ubicación de la etiqueta_start2
etiqueta_end2.place(x=410, y=220) #Ubicación de la etiqueta_end2

def ingresar_tiempo():
        startime = entry_start.get()
        endtime = entry_end.get()
        etiqueta_start2.config(text="Startime ingresado: "+startime)
        etiqueta_end2.config(text="Endtime ingresado: "+endtime)
        return

B_tiempo = tk.Button(tab1, text ="Submit Periodo de tiempo",
        bg="#BDBDBD",fg="black",height = 2, width = 20, command = ingresar_tiempo) #Boton para ingresar tiempo
B_tiempo.place(x=10, y=250) #Ubicación del botón

etiqueta_tipow = tk.Label(inner_frame,text="No existe path en el timestamp:",bg="black",fg="white",font=("Verdana",16)) #Etiqueta para tipo w
etiqueta_tipow.pack(fill=tk.X)
#--------------------------------- BUSQUEDA ASN EN EVENTOS ------------------------------------------------------------------------
etiqueta_asn = tk.Label(tab1,text="ASN: ",
                       bg="black",fg="white") #Etiqueta para ingresar asn
etiqueta_asn.place(x=10, y=300) #Ubicación de asn

entry_asn = ttk.Entry(tab1) #Caja de texto para ingresar el asn
entry_asn.place(x=10, y=325) #Ubicación de la caja de texto asn

etiqueta_b_asn = tk.Label(tab1,text="ASN ingresado: ",
                                bg="black",fg="white") #Etiqueta para confirmar ASN
etiqueta_b_asn.place(x=140, y=325) #Ubicación de la etiqueta_b_asn
def encontrar_ASN():
        b_ASN = entry_asn.get()

        etiqueta_b_asn.config(text="ASN ingresado: "+b_ASN)
        return

B_tiempo = tk.Button(tab1, text ="Submit ASN",
        bg="#BDBDBD",fg="black",height = 2, width = 20, command = encontrar_ASN) #Boton para encontrar asn
B_tiempo.place(x=10, y=355) #Ubicación del botón

etiqueta_listado = tk.Label(inner_frame2,text="Listado de ASN:",bg="black",fg="white",font=("Verdana",16)) #Listado ASN
etiqueta_listado.pack(fill=tk.X)

#------------------------ DEF RIPE Y BGP --------------------------------------------
def RIPE():
        ip = entry_ip.get()
        if not ip:
                messagebox.showwarning( "WARNING", "No ha ingresado todos los datos")

        elif ip:        
                url = 'https://stat.ripe.net/data/ris-peerings/data.json?resource={}'.format(ip)
                
                resp = requests.get(url)
                try:
                                cantidad = len(resp.json()['data']['peerings'])
                                #print(url)
                                for i in range(cantidad):              
                                        cont = len(resp.json()['data']['peerings'][i]['peers'])
                                       # print(cont)
                                        for x in range(cont): 
                                            as_path = resp.json()['data']['peerings'][i]['peers'][x]['routes'] 
                                            A = ("%s\n" %as_path)
                                            if A != "[]\n":                                           
                                                dato = [int(s) for s in re.findall(r'\b\d+\b', A)] 
                                              #  print(dato)
                                                nx.add_path(G1, dato)     

                                plt.figure(1, figsize =(10, 7)) #Defino mi figura
                                ax1 = plt.gca()
                                ax1.set_title("Diagrama de anuncios para la ip: \n"+ip, fontsize = 25, weight = 25) #Coloco un titulo
                                nx.draw(G1,pos=nx.nx_pydot.pydot_layout(G1, prog="dot"),node_color='#FC947E', with_labels=True, font_size=7, node_size = 50)
                                #nx.draw(G1,pos=nx.spring_layout(G1),node_color='#FC947E', with_labels=True, font_size=10, node_size = 30)
                                #plt.savefig("RIPE")         
                                plt.show()
                                plt.close()
                                
                except KeyError:
                     msg = messagebox.showerror( "ERROR", "Reviste los datos en la pestaña de Ingreso de Datos")
                
        return

def BGP():
    ip = entry_ip.get()
    startime = entry_start.get()
    endtime = entry_end.get()
    if not ip and startime and endtime:
        messagebox.showwarning( "WARNING", "No ha ingresado todos los datos")
    elif ip and startime and endtime:   

            url = 'https://stat.ripe.net/data/bgplay/data.json?resource={}&starttime={}&endtime={}'.format(ip,startime,endtime)
            resp = requests.get(url)
            

            
            try:
                    
                        cantidad = len(resp.json()['data']['events'])
                                
                        for j in range(cantidad):     
                                tipo = (resp.json()['data']['events'][j]['type'])
                                tipo_l = len(resp.json()['data']['events'][j]['type'])
                                time_stamp = (resp.json()['data']['events'][j]['timestamp'])
                                #print(tipo_l)
                                
                                if tipo == "A":
                                    path = (resp.json()['data']['events'][j]['attrs']['path'])
                                    B = ("%s\n" %path)
                                    if B != "[]\n":
                                        dato = [int(s) for s in re.findall(r'\b\d+\b', B)] 
                                        mens = Message(inner_frame2,text=(str(dato[0])+"\n"+"-----------------------"+"\n"),bg="black",fg="white",width="400",font=("Verdana",12)) #mensaje para ASN
                                        mens.pack(fill=tk.X) 
                                        nx.add_path(G2, dato) 
                                    
                                elif tipo == "W":
                                        # msg = messagebox.showinfo( "AVISO","No existe path en el timestamp: "+time_stamp+"\nes de tipo: "+tipo)

                                        msg = Message(inner_frame,text=time_stamp+"\n"+"-----------------------"+"\n",bg="black",fg="white",width="400",font=("Verdana",16)) #mensaje para tipo w
                                        msg.pack(fill=tk.X)
                                         
                                         
                        plt.figure(1, figsize =(10, 8)) #Defino mi figura
                        ax2 = plt.gca()
                        ax2.set_title("Diagrama de eventos para la ip: \n"+ip+"\nEn el período: \n"+startime+"  -  "+endtime, fontsize = 10, weight = 25) #titulo                        
                        nx.draw(G2,pos=nx.nx_pydot.pydot_layout(G2, prog="dot"),node_color='green', with_labels=True, font_size=10, node_size = 30)
                        #plt.savefig(grafo)
                        plt.show()    
                        plt.close()
            except (UnboundLocalError,KeyError):
                    
                    msg2 = messagebox.showwarning( "WARNING", "No ha ingresado algún dato o Ingrese otro periodo de tiempo, ya que no existen path en eventos")

    return




def BUSCAR_ASN():
    ip = entry_ip.get()
    startime = entry_start.get()
    endtime = entry_end.get()
    b_ASN = entry_asn.get()
    I_ASN = []
    T_ASN = []
    if not ip and startime and endtime and b_ASN:
        messagebox.showwarning( "WARNING", "No ha ingresado todos los datos")
    elif ip and startime and endtime and b_ASN:     
            url = 'https://stat.ripe.net/data/bgplay/data.json?resource={}&starttime={}&endtime={}'.format(ip,startime,endtime)
            resp = requests.get(url)
         
            try:

                            cantidad = len(resp.json()['data']['events'])           
                            
                            for j in range(cantidad):     
                                tipo = (resp.json()['data']['events'][j]['type'])
                                tipo_l = len(resp.json()['data']['events'][j]['type'])
                                time_stamp = (resp.json()['data']['events'][j]['timestamp'])
                                #print(tipo_l)
                                
                                if tipo == "A":
                                    path = (resp.json()['data']['events'][j]['attrs']['path'])
                                    B = ("%s\n" %path)
                                    if B != "[]\n":
                                        dato = [int(s) for s in re.findall(r'\b\d+\b', B)] 
                                        T_ASN.append(dato) #todos los datos
                                        I_ASN.append(dato[0]) #casilla del ASN
                                elif tipo == "W":
                                        # msg = messagebox.showinfo( "AVISO","No existe path en el timestamp: "+time_stamp+"\nes de tipo: "+tipo)
                                          msg = Message(inner_frame,text=time_stamp+"\n"+"-----------------------"+"\n",bg="black",fg="white",width="400",font=("Verdana",16)) #mensaje para tipo w
                                          msg.pack(fill=tk.X)
                                          
                            if b_ASN in str(I_ASN):
                                for ASN in T_ASN:
                                    if b_ASN in str(ASN[0]):     
                                       nx.add_path(G3, ASN)                                     
                                plt.figure(1, figsize =(10, 5)) #Defino mi figura
                                ax3 = plt.gca()
                                ax3.set_title("Diagrama de eventos para el ASN: \n"+b_ASN+"\nEn el período: \n"+startime+"  -  "+endtime
                                              ,fontsize = 7, weight = 25) #titulo 
                                nx.draw(G3,pos=nx.nx_pydot.pydot_layout(G3, prog="dot"), node_color='blue', with_labels=True, font_size=12, node_size = 28)
                                #plt.savefig(grafo)         
                                plt.show()
                                plt.close()
                            else:
                               msg2= messagebox.showerror( "ERROR","Verificar los datos ingresados") 
                        
                    
                    
            except (UnboundLocalError,KeyError):
                    
                    msg3 = messagebox.showwarning( "WARNING", "No ha ingresado algún dato o Ingrese otro periodo de tiempo, ya que no existen path en eventos")

    return


def EVENTOS():
    ip = entry_ip.get()
    startime = entry_start.get()
    endtime = entry_end.get()
    b_ASN = entry_asn.get()
    I_ASN = []
    T_ASN = []
    if not ip and startime and endtime and b_ASN:
        messagebox.showwarning( "WARNING", "No ha ingresado todos los datos")
    elif ip and startime and endtime and b_ASN:     
            url = 'https://stat.ripe.net/data/bgplay/data.json?resource={}&starttime={}&endtime={}'.format(ip,startime,endtime)
            resp = requests.get(url)
    
            try:
                    
                            cantidad = len(resp.json()['data']['events'])           
                            
                            for j in range(cantidad):     
                                tipo = (resp.json()['data']['events'][j]['type'])
                                tipo_l = len(resp.json()['data']['events'][j]['type'])
                                time_stamp = (resp.json()['data']['events'][j]['timestamp'])
                                #print(tipo_l)
                                
                                if tipo == "A":
                                    path = (resp.json()['data']['events'][j]['attrs']['path'])
                                    B = ("%s\n" %path)
                                    if B != "[]\n":
                                        dato = [int(s) for s in re.findall(r'\b\d+\b', B)]
                                        nx.add_path(G2,dato)
                                        T_ASN.append(dato) #todos los datos
                                        I_ASN.append(dato[0]) #casilla del ASN
                                elif tipo == "W":
                                        # msg = messagebox.showinfo( "AVISO","No existe path en el timestamp: "+time_stamp+"\nes de tipo: "+tipo)
                                          msg = Message(inner_frame,text=time_stamp+"\n"+"-----------------------"+"\n",bg="black",fg="white",width="400",font=("Verdana",16)) #mensaje para tipo w
                                          msg.pack(fill=tk.X)
                                          
                            if b_ASN in str(I_ASN):
                                for ASN in T_ASN:
                                    if b_ASN in str(ASN[0]):     
                                       nx.add_path(G3, ASN)
                                       
                                plt.figure(1, figsize =(10, 8)) #Defino mi figura
                                ax3 = plt.gca()
                                ax3.set_title("Diagrama de eventos para la ip: \n"+ip+"\nEn el período: \n"+startime+"  -  "+endtime+"\nMarcando la ruta del ASN: "+b_ASN
                                              ,fontsize = 7, weight = 25) #titulo 
                                nx.draw(G2,pos=nx.nx_pydot.pydot_layout(G2, prog="dot"),node_color='green', with_labels=True, font_size=10, node_size = 30)
                                nx.draw(G3,pos=nx.nx_pydot.pydot_layout(G2, prog="dot"), node_color='blue', with_labels=True, font_size=10, node_size = 30)
                                #plt.savefig(grafo)         
                                plt.show()
                                plt.close()
                            else:
                               msg2= messagebox.showerror( "ERROR","Verificar los datos ingresados") 
                        
                    
                    
            except (UnboundLocalError,KeyError):
                    
                    msg3 = messagebox.showwarning( "WARNING", "No ha ingresado algún dato o Ingrese otro periodo de tiempo, ya que no existen path en eventos")

    return
#------------------------ DIAGRAMA ANUNCIOS --------------------------------------------
B_anuncios = tk.Button(tab2, text ="Diagrama de anuncios",bg="#BDBDBD",fg="black",height = 2, width = 20, command = RIPE) #Boton para anuncios
B_anuncios.place(x=10, y=10) #Ubicación del botón

B_evento = tk.Button(tab2, text ="Diagrama de eventos", bg="#BDBDBD",fg="black",height = 2, width = 20, command = BGP) #Boton para eventos
B_evento.place(x=200, y=10) #Ubicación del botón

B_asn = tk.Button(tab2, text ="Diagrama para ASN en específico",bg="#BDBDBD",fg="black",height = 2, width = 30, command = BUSCAR_ASN) #Boton para ASN en específico
B_asn.place(x=10, y=110) #Ubicación del botón

B_asn2 = tk.Button(tab2, text ="Diagrama eventos y ASN",bg="#BDBDBD",fg="black",height = 2, width = 30, command = EVENTOS) #Boton para ASN en específico
B_asn2.place(x=10, y=210) #Ubicación del botón
#--------------------------------- mainloop ------------------------------------------------------------------------
ventana.mainloop()

