# TODO: better styling
from loanpy import home, car, welcome

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

pages = [carpage.frame, homepage.frame]

def submit():
    print(homepage.get_data())

count = 0
def set_page(f: tk.Frame):
    # if f.winfo_id() != homepage.frame.winfo_id():
    global count
    submit_button.forget()
    welcomepage.frame.forget()
    for p in pages: p.forget()
    f.pack()
    submit_button.pack(side=tk.BOTTOM)

bottom = tk.Frame(root)
submit_button = tk.Button(bottom, text="Submit", command=submit, fg="green")
car_button = tk.Button(bottom, text="Car Loan", command=lambda: set_page(carpage.frame))
car_button.pack(side=tk.LEFT, padx=10)
home_button = tk.Button(bottom, text="Home Loan", command=lambda: set_page(homepage.frame))
home_button.pack(side=tk.RIGHT, padx=10)
bottom.pack(side=tk.BOTTOM)

root.mainloop()
