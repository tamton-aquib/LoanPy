# TODO: better styling
from loanpy import home, car, welcome
import tensorflow as tf
import tkinter as tk

root = tk.Tk()
root.geometry(f"900x600")
root.title("Loan Py")

main_frame = tk.Frame(root)

homepage = home.HomeLoan(main_frame)
carpage = car.CarLoan(main_frame)

main_frame.pack(expand=True)

welcomepage = welcome.Welcome(main_frame)
welcomepage.frame.pack()

outputpage = tk.Frame(main_frame)
output_label = tk.Label(outputpage, text="Application status: !")
output_label.pack()

pages = [homepage.frame]

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
    value_output = "Your loan has been approved" if value > 0.5 else "Sorry! your loan was rejected"
    output_label.configure(text=f"Application status: {value_output}!")

bottom = tk.Frame(root)
submit_button = tk.Button(bottom, text="Submit", command=submit, fg="green")
home_button = tk.Button(bottom, text="Home Loan", command=lambda: set_page(homepage.frame))
home_button.pack(side=tk.RIGHT, padx=10)
bottom.pack(side=tk.BOTTOM)

root.mainloop()
