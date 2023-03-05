from time import strftime
from tkinter import Label ,Tk

window = Tk()
window.title('Clock')
window.geometry("10x10")
window.configure(bg="black")
window.resizable(False,False)

#Label for the clock
clock_label = Label(window,bg="black",fg="cyan",font=("Times",30,'bold'), relief='flat')

clock_label.place(x=125,y=1000)

#Func For Updating Time

def update():
	cur_time = strftime('%H: %M : %S')
	clock_label.configure(text=cur_time)
	clock_label.after(80,update)

if __name__=='__main__':
	update()
	window.mainloop()
	