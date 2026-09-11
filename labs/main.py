def format_line_item(description, amount, tax_rate=7.5, currency="$"):
    # TODO: calculate the taxed total using tax_rate, round to 2 decimal places,
    # and return "{description}: {currency}{total}"
    total = amount + (amount * tax_rate / 100)
    rounded_tax_total = round(total, 2)
    return (f"{description}: {currency}{total}") 
    pass