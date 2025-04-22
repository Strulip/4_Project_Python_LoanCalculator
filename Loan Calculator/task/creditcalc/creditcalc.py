import math
import argparse


def calculate_nominal_interest(i):
    nom_int = i / 12 / 100
    return nom_int


def calculate_monthly_payments(pr, pa, i):
    interest = calculate_nominal_interest(i)
    num_months = math.log((pa / (pa - interest * pr)), interest + 1)
    num_months_rounded = math.ceil(num_months)
    years = num_months_rounded // 12
    months = num_months_rounded % 12
    overpayment = math.ceil(num_months_rounded * pa - pr)
    if months == 0:
        return (f'It will take {years} years to repay this loan!\n'
                f'Overpayment = {overpayment}')
    if years == 0:
        return (f'It will take {months} months to repay this loan!\n'
                f'Overpayment = {overpayment}')
    else:
        return (f'It will take {years} years and {months} months to repay this loan!\n'
                f'Overpayment = {overpayment}')


def calculate_annuity_payment(pr, pe, i):
    interest = calculate_nominal_interest(i)
    annuity_payment = pr * (interest * math.pow(1 + interest, pe)/(math.pow(1 + interest, pe)-1))
    annuity_payment_rounded = math.ceil(annuity_payment)
    overpayment = math.ceil(annuity_payment_rounded * pe - pr)
    return (f'Your monthly payment = {annuity_payment_rounded}!\n'
            f'Overpayment = {overpayment}')


def calculate_loan_principal(pa, pe, i):
    interest = calculate_nominal_interest(i)
    loan_principal = (pa / (interest * math.pow(1 + interest, pe) /(math.pow(1 + interest, pe) - 1)))
    loan_principal_rounded = math.floor(loan_principal)
    overpayment = math.ceil(pa * pe - loan_principal_rounded)
    return (f'Your loan principal = {loan_principal_rounded}!\n'
            f'Overpayment = {overpayment}')


def launch_annuity_calculator(pr, pa, pe, i):
    if [pr, pa, pe, i].count(None) > 1:
        return 'Incorrect parameters: too many missing values.'
    if pe is None:
        return calculate_monthly_payments(pr, pa, i)
    if pa is None:
        return calculate_annuity_payment(pr, pe, i)
    if pr is None:
        return calculate_loan_principal(pa, pe, i)


def calculate_differentiated_payment(pr, pe, i):
    interest = calculate_nominal_interest(i)
    month_counter = 1
    total_payment = 0
    for month in range(int(pe)):
        differentiated_payment = math.ceil(pr / pe + interest * (pr - pr * (month_counter - 1) / pe))
        print(f"Month {month_counter}: payment is {differentiated_payment}")
        month_counter += 1
        total_payment += differentiated_payment
    overpayment = int(total_payment - pr)
    return f"\nOverpayment = {overpayment}"


def select_calculator(ty, pr, pa, pe, i):
    if ty not in ['annuity', 'diff'] or i is None:
        print("Incorrect parameters.")

    if any(x is not None and x < 0 for x in [pr, pa, pe, i]):
        print("Incorrect parameters.")

    if sum(param is None for param in [pr, pa, pe]) > 1:
        print("Incorrect parameters.")

    if ty == 'diff':
        if pa is not None:
            print("Incorrect parameters.")
        if all(x is not None for x in [pr, pe, i]):
            print(calculate_differentiated_payment(pr, pe, i))


    if ty == 'annuity':
        if [pr, pa, pe].count(None) == 1:
            print(launch_annuity_calculator(pr, pa, pe, i))


    print("Incorrect parameters.")



parse = argparse.ArgumentParser(description='This program will help with loan calculations')

parse.add_argument('-ty','--type')
parse.add_argument('-pr','--principal', type=float)
parse.add_argument('-pa','--payment', type=float)
parse.add_argument('-pe','--periods', type=float)
parse.add_argument('-i','--interest', type=float)

args = parse.parse_args()

select_calculator(args.type, args.principal, args.payment, args.periods, args.interest)
