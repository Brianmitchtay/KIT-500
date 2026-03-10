"""
Calculate the monthly repayments of a fixed term loan at a give interest rate based on user inputs.
"""

__author__ = "Brian Taylor"

def calc_monthly_payment(principal: int, months: int, annual_rate: float) -> float:
    monthly_payment = ((annual_rate/12) * principal) / (1 - (1 + annual_rate/12) ** (-months))
    return monthly_payment

def main():
    monthly_repayment1 = calc_monthly_payment(826000, 240, .0625)
    monthly_repayment2 = calc_monthly_payment(648000, 360, .0587)
    
    print(f"Monthly repayment 1: {monthly_repayment1} \nMonthly repayment 2: {monthly_repayment2}" ) #print boilerplate examples

    """Collect user inputs for loan calculation"""
    principal: int = int(input("Input the principal amount ($): "))
    annual_rate: float = float(input("Input annual interest rate (percent): ")) /100
    months: int = int(input("Input loan duration (years): ")) * 12 #Multiply by 12 to convert years to months

    print("Calculating. . . ")
    """Calculate and print the monthly payment amount"""
    print(f"Monthly repayment: ${calc_monthly_payment(principal, months, annual_rate):.2f}")

if __name__ == "__main__":
    main()
