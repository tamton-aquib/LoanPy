import tkinter as tk

class HomeLoan:
    def __init__(self, main_frame) -> None:
        self.frame = tk.Frame(main_frame)

        tk.Label(self.frame, text="Home Loan", bg="red", font=(None, 12)).pack()

        tk.Label(self.frame, text="Applicant Income").pack()
        self.applicant_income = tk.Entry(self.frame); self.applicant_income.pack()

        tk.Label(self.frame, text="Co-Applicant Income").pack()
        self.coapplicant_income = tk.Entry(self.frame); self.coapplicant_income.pack()

        tk.Label(self.frame, text="Loan Amount").pack()
        self.loan_amount = tk.Entry(self.frame); self.loan_amount.pack()

        tk.Label(self.frame, text="Loan Amount Term").pack()
        self.loan_amount_term = tk.Entry(self.frame); self.loan_amount_term.pack()

        self.credit_history = tk.IntVar()
        tk.Checkbutton(self.frame, text="Credit History", variable=self.credit_history).pack()

        self.dependants = tk.IntVar()
        tk.Checkbutton(self.frame, text="Dependants", variable=self.dependants).pack()

        self.education = tk.IntVar()
        tk.Checkbutton(self.frame, text="Education", variable=self.education).pack()

        self.self_employed = tk.IntVar()
        tk.Checkbutton(self.frame, text="Self Employed", variable=self.self_employed).pack()

        tk.Label(self.frame, text="Property Area").pack()
        tk.Radiobutton(self.frame, text='Rural').pack()
        tk.Radiobutton(self.frame, text='Urban').pack()
        tk.Radiobutton(self.frame, text='SemiUrban').pack()

        # tk.Button(self.frame, text="Submit", command=self.submit).pack()

    def get_data(self):
        return {
            "self_employed": self.self_employed.get(),
            "education": self.education.get(),
            "dependants": self.dependants.get(),
            "credit_history": self.credit_history.get(),
            "applicant_income": self.applicant_income.get(),
            "gender": 1,
            "married": 1
        }

