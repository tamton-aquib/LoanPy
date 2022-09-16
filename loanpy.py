# TODO: better styling
from loanpy import home, car, welcome
from threading import Thread

def importing():
    import tensorflow as tf

import tkinter as tk

root = tk.Tk()
root.geometry(f"800x500")
root.title("Loan Py")

main_frame = tk.Frame(root)

homepage = home.HomeLoan(main_frame)
carpage = car.CarLoan(main_frame)

main_frame.pack(expand=True)

welcomepage = welcome.Welcome(main_frame)
welcomepage.frame.pack()

outputpage = tk.Frame(main_frame)

pages = [carpage.frame, homepage.frame]

def set_page(f: tk.Frame):
    submit_button.forget()
    welcomepage.frame.forget()
    for p in pages: p.forget()
    f.pack()
    submit_button.pack(side=tk.BOTTOM)

def submit():
    set_page(outputpage)
    nice = homepage.get_data()
    model = tf.keras.models.load_model('newmodel.h5')
    value = model.predict([list(nice.values())])[0][0]
    value_output = "Yes" if value > 0.5 else "No"
    tk.Label(outputpage, text=f"here is the output: {value_output}!").pack()

bottom = tk.Frame(root)
submit_button = tk.Button(bottom, text="Submit", command=submit, fg="green")
car_button = tk.Button(bottom, text="Car Loan", command=lambda: set_page(carpage.frame))
car_button.pack(side=tk.LEFT, padx=10)
home_button = tk.Button(bottom, text="Home Loan", command=lambda: set_page(homepage.frame))
home_button.pack(side=tk.RIGHT, padx=10)
bottom.pack(side=tk.BOTTOM)

Thread(target=importing).start()
root.mainloop()
