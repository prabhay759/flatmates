from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input("Hey user, enter the bill amount "))
period = input("Enter the period e.g. December 2021? ")
name1 = input("what is your name? ")
days_in_house = int(input("Number of days stay in the house "))

name2 = input("what is the name of other flatmate? ")
days_in_house_2 = int(input("Number of days stay in the house "))

the_bill = Bill(amount=amount, period=period)

marry = Flatmate(name=name1, days_in_house=days_in_house)
john = Flatmate(name=name2, days_in_house=days_in_house_2)

print(f"{name1} pays: ", round(john.pays(bill=the_bill, flatmate2=marry), 2))
print(f"{name2} pays: ", round(marry.pays(bill=the_bill, flatmate2=john), 2))
pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)
