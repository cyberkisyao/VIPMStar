from tkinter import *
from tkinter import ttk

def close_prog():
    window.destroy()
    print("Закрытие программы...")


window = Tk()
window.title("MS VIP")
window.geometry('180x500+700+300')
window.resizable(False, False)
# window.iconbitmap(default='MSVIP_icon.ico')


head = ttk.Label(text="Рассчет очков VIP")
head.pack(anchor=NW)

time_value = StringVar()
time_frame = ttk.Frame(padding=[8, 10])
time_label = ttk.Label(time_frame, text="Количество \nчасов в игре")
time_entry = ttk.Entry(time_frame, textvariable=time_value)
time_frame.pack(anchor=NW); time_label.pack(anchor=NW); time_entry.pack(anchor=NW)
tv = time_entry.get()

dance_value = StringVar()
dance_count_frame = ttk.Frame(padding=[8, 10])
dance_count_label = ttk.Label(dance_count_frame, text="Количество танцев")
dance_count_entry = ttk.Entry(dance_count_frame, textvariable=dance_value)
dance_count_frame.pack(anchor=NW); dance_count_label.pack(anchor=NW); dance_count_entry.pack(anchor=NW)
dc = dance_count_entry.get()

donate_value = StringVar()
donate_frame = ttk.Frame(padding=[8, 10])
donate_label = ttk.Label(donate_frame, text="Количество \nпотраченного кеша")
donate_entry = ttk.Entry(donate_frame, textvariable=donate_value)
donate_frame.pack(anchor=NW); donate_label.pack(anchor=NW); donate_entry.pack(anchor=NW)
dv = donate_entry.get()

couple_value = StringVar()
couple_frame = ttk.Frame(padding=[8, 10])
couple_label = ttk.Label(couple_frame, text="Уровень пары")
couple_entry = ttk.Entry(couple_frame, textvariable=couple_value)
couple_frame.pack(anchor=NW); couple_label.pack(anchor=NW), couple_entry.pack(anchor=NW)
cv = couple_entry.get()


mark = IntVar()
club_chek = ttk.Checkbutton(text="Нахождение в клубе", variable=mark)
club_chek.pack(padx=11, pady= 5, anchor=NW)

def show_value():
    time = int(time_entry.get()) * 6
    dance = int(dance_count_entry.get())
    donate = (int(donate_entry.get()) / 100) * 2
    couple = int(couple_entry.get()) * 10
    if mark.get() == 0:
        texttv["text"] = time
        textdc["text"] = dance
        textdv["text"] = donate
        textcv["text"] = couple
        textres["text"] = time + dance + donate + couple
    else:
        texttv["text"] = time
        textdc["text"] = dance
        textdv["text"] = donate
        textcv["text"] = couple
        textres["text"] = time + dance + donate + couple + 30

texttv = ttk.Label(); textdc = ttk.Label(); textdv = ttk.Label(); textcv = ttk.Label()
texttv.pack(anchor=NW); textdc.pack(anchor=NW); textdv.pack(anchor=NW); textcv.pack(anchor=NW)  
textres = ttk.Label()
textres.pack(anchor=NW)


get_res = ttk.Button(text="Рассчитать", command=show_value)
get_res.pack(anchor=NW, padx=11, pady=5)    

window.protocol('WM_DELETE_WINDOW', close_prog)

window.mainloop()
