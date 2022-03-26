available_entry = ["Debit Card",
                   "Credit Card",
                   "Crypto",
                   "Paypal/Payonner",
                   "Cash"
                   ]
actual_choices = []
for i in range(1, len(available_entry) + 1):
    actual_choices.append(str(i))
print(actual_choices)
current_choices = "-"
transaction_pass = []

while current_choices != 0:
    if current_choices in actual_choices:
        print("Adding {}".format(current_choices))
        index = int(current_choices) - 1
        chosen_method = available_entry[index]
        transaction_pass.append(chosen_method)
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_entry):
            print("{0}: {1}".format(number + 1, part))

    current_choices = input("What Are the Preferences: " + "_______")

print(transaction_pass + "Comeback later, Tada!")