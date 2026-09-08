def split_bill(bill_amount, tip_percent, people):
    tip_amount = bill_amount * (tip_percent / 100)
    grand_total = bill_amount + tip_amount
    persons_share = grand_total / people
    persons_share = round(persons_share, 2)
    return persons_share

split_bill(100, 10, 2)
split_bill(60, 20, 3)
split_bill(50, 0, 1)