"""Calculate a tip and the total bill."""


def main():
    bill_amount = float(input("Enter the bill amount: "))
    tip_percentage = float(input("Enter the tip percentage: "))

    tip_amount = bill_amount * tip_percentage / 100
    total = bill_amount + tip_amount

    print(f"Tip amount: ${tip_amount:.2f}")
    print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()
