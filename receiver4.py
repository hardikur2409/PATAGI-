from tkinter import *
from paho.mqtt import client as mqtt_client
import json
from time import strftime
import datetime as dt
import requests
from  geopy.geocoders import Nominatim
from tkinter import messagebox
from tkinter import ttk

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        client.subscribe("PATAGI")
    
    client = mqtt_client.Client()
    client.on_connect = on_connect
    client.username_pw_set("TMDG2022", password='TMDG2022')
    client.connect("rmq2.pptik.id", 1883)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, message1):
        dato = json.loads(message1.payload.decode("utf-8"))
        dota = float(dato)
        state = str(message1.payload.decode("utf-8"))
        arr = list(state)
        berat = (dato/3)*100
        if (arr[len(arr)-1]=='0'):
            smoke_label.config(text="Leakage Detected",fg="red")
            hum = str("%.2f" % round(berat,2))
            hum_label.config(text="Vol: "+ hum + "%",fg="black")  
        if (arr[len(arr)-1]=='1'):
            smoke_label.config(text="Safe",fg="black")
            hum = str("%.2f" % round(berat,2))
            hum_label.config(text="Vol: "+ hum + "%",fg="black")
            if (dota>3):
                hum = str("100")
                hum_label.config(text="Vol: "+ hum + "%",fg="black")
        lbl.config(text="Time : " + strftime('%H:%M:%S %p'))
        date = dt.datetime.now()
        lbl1.config(text="Date : "+ f"{date:%A, %d %B %Y}")
        
    client.on_message = on_message
    client.subscribe("PATAGI") 

def show_msg():
   send_to_telegram("Hallo...."+"\n"+"Gas dirumahku sudah habis. Tolong diantar ke alamat sesuai koordinat ini:"+"\n"+"lati: "+datalat+"\n"+"long: "+datalong)
   messagebox.showinfo("Informasi","Cieee yang gas nya habis. Tenang, order sudah kita kirim. Harap menunggu sebentar lagi dihubungi kok sama penjual. Love You")

def send_to_telegram(message):
    apiToken = '5721059506:AAH-YKAQkKd3IJrUdc5NH_7xvZ-vt4pCnls'
    chatID = '1126319316'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
    except Exception as e:
        print(e)

loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode("BANDUNG")
datalat = str(getLoc.latitude)
datalong = str(getLoc.longitude)

window = Tk()
window.title("MQTT Dashboard")
window.geometry('395x675')
window.resizable(False,False)

canvas = Canvas(window,width=395,height=135)
canvas.place(x=0,y=5)
img = PhotoImage(file="head.png")
canvas.create_image(0,0,anchor=NW,image=img)

hum_label = Label(window,text="  %",fg="black",font=("Helvetica", 32))
hum_label.place(relx=0.5, rely=0.5, anchor=CENTER)

smoke1_label = Label(window,text="Informasi Detector Gas",fg="black",font=("Times", 16))
smoke1_label.place(relx=0.5, y=470, anchor=CENTER)
smoke_label = Label(window,text="",fg="black",font=("Helvetica", 16))
smoke_label.place(relx=0.5, y=500, anchor=CENTER)

foot_label = Label(window,text="Tugas Besar Kelompok 1 Kendali IoT Project",fg="black",font=("Times", 10))
foot_label.place(relx=0.5, y=645, anchor=CENTER)
foot_label = Label(window,text="EL5006 Desain Aplikasi Interaktif 2022",fg="black",font=("Times", 10))
foot_label.place(relx=0.5, y=665, anchor=CENTER)

lbl = Label(window,text=strftime('%H:%M:%S %p'),fg="black",font=("Times", 10))
lbl.place(x=10, y=145, anchor=W)
lbl1 = Label(window,text="",fg="black",font=("Times", 10))
lbl1.place(x=200, y=145, anchor=W)

tombol = Button(window,text='Pesan LPG',command = show_msg,fg="black")  
tombol.pack(pady=200)


client = connect_mqtt()
subscribe(client)
client.loop_start()
window.mainloop()
client.loop_stop()