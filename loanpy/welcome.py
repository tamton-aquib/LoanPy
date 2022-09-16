import tkinter as tk

class Welcome:
    # ltv = 85, etc
    def __init__(self, main_frame) -> None:
        self.frame = tk.Frame(main_frame)

        tk.Label(self.frame, text="Welcome to LoanPy", bg="green", font=(None, 24)).pack()

