import tkinter as tk
import pandas as pd
import numpy as np

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

        # TODO: clear up
        tk.Label(self.frame, text="Property Area").pack()
        tk.Radiobutton(self.frame, text='Rural', state=tk.DISABLED).pack()
        tk.Radiobutton(self.frame, text='Urban', state=tk.DISABLED).pack()
        tk.Radiobutton(self.frame, text='SemiUrban', state=tk.DISABLED).pack()

        # tk.Button(self.frame, text="Submit", command=self.submit).pack()

    def get_data(self):

        r = 0.00833
        loan_amount = float(self.loan_amount.get())
        loan_amount_term = float(self.loan_amount_term.get())
        stuff = {
            "gender": 1,
            "married": 1,
            "dependants": np.int64(self.dependants.get()),
            "education": np.int64(self.education.get()),
            "self_employed": np.int64(self.self_employed.get()),
            "applicant_income": np.float64(self.applicant_income.get()),
            "coapplicant_income": np.float64(self.coapplicant_income.get()),
            "loan_amount": np.float64(loan_amount),
            "loan_amount_term": np.float64(loan_amount_term),
            "credit_history": np.int64(self.credit_history.get()),
            "property_area": 0,
            "total_income": np.float64(self.applicant_income.get() + self.coapplicant_income.get()),
            "EMI": np.float64(loan_amount * r * ((1+r) ** loan_amount_term) / ((1+r) ** (loan_amount_term - 1)))
        }

        data = pd.read_csv('preprocesseddata.csv')

        stuff["applicant_income"] = (stuff['applicant_income'] - data["ApplicantIncome"].min()) / (data["ApplicantIncome"].max() - data["ApplicantIncome"].min())
        stuff["loan_amount"] = (stuff["loan_amount"] - data["LoanAmount"].min()) / (data["LoanAmount"].max() - data["LoanAmount"].min())
        stuff["coapplicant_income"] = (stuff["coapplicant_income"] - data["CoapplicantIncome"].min()) / (data["CoapplicantIncome"].max() - data["CoapplicantIncome"].min())
        stuff["property_area"] = (stuff["property_area"] - data["Property_Area"].min()) / (data["Property_Area"].max() - data["Property_Area"].min())
        stuff["loan_amount_term"] = (stuff["loan_amount_term"] - data["Loan_Amount_Term"].min()) / (data["Loan_Amount_Term"].max() - data["Loan_Amount_Term"].min())
        stuff["total_income"] = (stuff["total_income"] - data["TotalIncome"].min()) / (data["TotalIncome"].max() - data["TotalIncome"].min())
        stuff["EMI"] = (stuff["EMI"] - data["EMI"].min()) / (data["EMI"].max() - data["EMI"].min())

        return stuff

