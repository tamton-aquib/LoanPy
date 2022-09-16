import tkinter as tk

class CarLoan:
    # ltv = 85, etc
    def __init__(self, main_frame) -> None:
        self.frame = tk.Frame(main_frame)

        tk.Label(self.frame, text="Car Loan", bg="green", font=(None, 12)).pack()

        tk.Label(self.frame, text="Disbursed Amount").pack()
        self.disbursed_amount = tk.Entry(self.frame); self.disbursed_amount.pack()

        tk.Label(self.frame, text="Asset cost").pack()
        self.asset_cost = tk.Entry(self.frame); self.asset_cost.pack()

        tk.Label(self.frame, text="Branch ID").pack()
        self.branch_id = tk.Entry(self.frame); self.branch_id.pack()

        tk.Label(self.frame, text="Manufacture ID").pack()
        self.manufacture_id = tk.Entry(self.frame); self.manufacture_id.pack()

        tk.Label(self.frame, text="State ID").pack()
        self.state_id = tk.Entry(self.frame); self.state_id.pack()

        self.self_employed = tk.IntVar()
        tk.Checkbutton(self.frame, text="Self Employed", variable=self.self_employed).pack()

        self.aadhar_flag = tk.IntVar()
        tk.Checkbutton(self.frame, text="Aadhar Flag", variable=self.aadhar_flag).pack()

        # tk.Button(self.frame, text="Submit", command=self.submit).pack()

    def get_data(self):
        return {
            "disbursed_amount": self.disbursed_amount.get(),
            "asset_cost": self.asset_cost.get(),
            "branch_id": self.branch_id.get(),
            "manufacture_id": self.manufacture_id.get(),
            "state_id": self.state_id.get(),
            "self_employed": self.self_employed.get(),
            "aadhar_flag": self.aadhar_flag.get()
        }

