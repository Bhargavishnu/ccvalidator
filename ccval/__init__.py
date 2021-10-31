def startwith(credit_card_number):
    return credit_card_number.startswith('4', '5', '6', '37', '34', '35')

def luhn_check(credit_card_number):
    validation_sum = 0
    credit_card_number_length = len(credit_card_number)
    for i in range(credit_card_number_length):
        digit = int(credit_card_number[i])
        if i % 2 == 0:
            digit *= 2
            if digit > 9:
                digit %= 10
                digit += 1
        validation_sum += digit

    return validation_sum % 10 == 0


def main():
    credit_card_number = str(input("Enter a credit card number"))
    error_message = "Invalid credit card number given "
    if not credit_card_number.isdigit():
        print(error_message + "Hint: Contains alphabets or special characters")
        return False
    if not (13 <= len(credit_card_number) <= 16):
        print(error_message + "Hint:Check Number Length")
        return False
    if not startwith(credit_card_number):
        print(error_message + "Hint:Check starting number")
        return False
    if not luhn_check(credit_card_number):
        print(error_message)
        return False

    print("Given number is a valid credit card number")
    return True

