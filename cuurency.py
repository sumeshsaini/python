from tkinter import *

def currency():
    # Get the values from entry fields
    money_type = your_c2_value.get().upper()
    amount = float(your_amount_c2.get())
    convert_to = country_2.get().upper()

    # Define currency conversion rates (dummy values)
    # You should replace these with real conversion rates
    conversion_rates = {
        'USD': {'EUR': 0.85, 'GBP': 0.73, 'JPY': 105.85, 'AUD': 1.30, 'CAD': 1.26, 'CHF': 0.90, 'CNY': 6.35, 'INR': 73.21},
        'EUR': {'USD': 1.18, 'GBP': 0.86, 'JPY': 126.10, 'AUD': 1.55, 'CAD': 1.51, 'CHF': 1.07, 'CNY': 7.54, 'INR': 86.12},
        'GBP': {'USD': 1.38, 'EUR': 1.16, 'JPY': 144.83, 'AUD': 1.77, 'CAD': 1.72, 'CHF': 1.22, 'CNY': 8.58, 'INR': 99.65},
        'JPY': {'USD': 0.0095, 'EUR': 0.0079, 'GBP': 0.0069, 'AUD': 0.012, 'CAD': 0.011, 'CHF': 0.008, 'CNY': 0.056, 'INR': 0.69},
        'AUD': {'USD': 0.77, 'EUR': 0.65, 'GBP': 0.56, 'JPY': 82.68, 'CAD': 0.97, 'CHF': 0.69, 'CNY': 4.86, 'INR': 56.32},
        'CAD': {'USD': 0.79, 'EUR': 0.66, 'GBP': 0.58, 'JPY': 89.25, 'AUD': 1.03, 'CHF': 0.71, 'CNY': 5.01, 'INR': 57.89},
        'CHF': {'USD': 1.12, 'EUR': 0.94, 'GBP': 0.82, 'JPY': 123.20, 'AUD': 1.45, 'CAD': 1.41, 'CNY': 7.04, 'INR': 81.21},
        'CNY': {'USD': 0.16, 'EUR': 0.13, 'GBP': 0.12, 'JPY': 17.86, 'AUD': 0.21, 'CAD': 0.20, 'CHF': 0.14, 'INR': 11.21},
        'INR': {'USD': 0.014, 'EUR': 0.012, 'GBP': 0.010, 'JPY': 1.45, 'AUD': 0.018, 'CAD': 0.017, 'CHF': 0.012, 'CNY': 0.089}
    }

    # Perform the conversion
    if money_type in conversion_rates and convert_to in conversion_rates[money_type]:
        conversion_rate = conversion_rates[money_type][convert_to]
        converted_amount = amount * conversion_rate
        result_label.config(text=f"{amount} {money_type} equals {converted_amount:.2f} {convert_to}")
    else:
        result_label.config(text="Conversion not available for the selected currencies")

root = Tk()
root.title("Currency Exchanger")
root.geometry("400x200")

# Background Image
background_image = PhotoImage(file=r"C:\Users\Sumesh Saini\Desktop\pexels-photo-730547.png")
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Labels and Entry Widgets
Label(root, text="Your Currency").grid(row=0, column=0)
Label(root, text="Amount").grid(row=1, column=0)
Label(root, text="Required Currency").grid(row=2, column=0)
currency_menue=Menu(root)
con =Menu(currency_menue,tearoff=0)
con.add_command(label='USD')
con.add_command(label='Eur')
con.add_command(label='GBR')
con.add_command(label='IND')
con.add_command(label='JPY')
con.add_command(label='CAD')
con.add_command(label='CHF')
con.add_command(label='CNY')

your_c2_value = StringVar()
your_amount_c2 = StringVar()
country_2 = StringVar()

Entry(root, textvariable=your_c2_value).grid(row=0, column=1)
Entry(root, textvariable=your_amount_c2).grid(row=1, column=1)
Entry(root, textvariable=country_2).grid(row=2, column=1)
root.config(menu=currency_menue)
currency_menue.add_cascade(label="Curency Options",menu=con)
# Buttons
Button(root, text="Submit", command=currency).grid(row=3, column=1)
Button(root, text="Exit", command=root.quit).grid(row=3, column=0)

# Result Label
result_label = Label(root, text="")
result_label.grid(row=4, columnspan=2)

root.mainloop()
