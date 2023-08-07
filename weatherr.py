import tkinter as tk
from PIL import Image,ImageTk

root=tk.Tk()


root.title("Weather Forecasting App")
root.geometry("600x500")

# 7687fab0bd3fb2994063220994d2bbc3
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def get_weather(city):
    weather_key='7687fab0bd3fb2994063220994d2bbc3'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units':'imperial'}
    response = requests.get(url,params)
    print(response.json())

    print (weather['name'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])

img=Image.open('./weatherr.jpg')
img=img.resize((600,500),Image.LANCZOS)
img_photo=ImageTk.PhotoImage(img)

bg_label=tk.Label(root,image=img_photo)
bg_label.place(x=0,y=0,width=600,height=500)

heading_title=tk.Label(bg_label,text="Entire Earth's weather",fg='red',bg='sky blue',font=('times new roman',18,'bold'))
heading_title.place(x=80,y=18)

frame_one=tk.Frame(bg_label,bg="#9090EE",bd=5)
frame_one.place(x=80,y=60,width=450,height=50)

txt_box=tk.Entry(frame_one,font=('times new roman',25),width=17)
txt_box.grid(row=0,column=0,sticky='w')

btn = tk.Button(frame_one,text='Get weather',fg='black',font=('times new roman',16,'bold'),command=lambda:get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=11)

frame_two=tk.Frame(bg_label,bg="#9090EE",bd=5)
frame_two.place(x=80,y=130,width=450,height=300)

result=tk.Label(frame_two,font=40,bg='white')
result.place(relwidth=1,relheight=1)


root.mainloop()