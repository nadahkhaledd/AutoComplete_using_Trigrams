import tkinter as tk
from assigmentnlp import output

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

label1 = tk.Label(root, text='Auto complete', font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

r = tk.StringVar()
r.set('')
entry1 = tk.Entry(root, textvariable=r)
canvas1.create_window(200, 70, window=entry1)

result = tk.StringVar()
def get_result(event):
    global result
    result.set('%s' % output(r.get()))


entry1.bind('<Return>', get_result)

button1 = tk.Button(text='Search', command=get_result, bg='green', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 100, window=button1)

label = tk.Label(root, textvariable=result)
canvas1.create_window(180, 170, window=label)

root.mainloop()
