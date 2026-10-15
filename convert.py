def binary_to_denary(binary):
    denary = 0

    for digit in binary:
        denary = denary * 2 + int(digit)

    return denary


def hex_to_denary(hexadecimal):
    digits = "0123456789ABCDEF"
    denary = 0

    for digit in hexadecimal.upper():
        denary = denary * 16 + digits.index(digit)

    return denary


def denary_to_binary(number):
    if number == 0:
        return "0"

    binary = ""

    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2

    return binary


def denary_to_hex(number):
    if number == 0:
        return "0"

    digits = "0123456789ABCDEF"
    hexadecimal = ""

    while number > 0:
        hexadecimal = digits[number % 16] + hexadecimal
        number = number // 16

    return hexadecimal


def to_twos_complement(number):
    if number < 0:
        number = 256 + number

    return denary_to_binary(number).zfill(8)


def to_sign_magnitude(number):
    if number < 0:
        sign = "1"
    else:
        sign = "0"

    magnitude = denary_to_binary(abs(number))

    return sign + magnitude.zfill(7)


def is_binary(value):
    for digit in value:
        if digit not in "01":
            return False
    return len(value) > 0

def is_denary(value):
    for digit in value:
        if digit not in "0123456789":
            return False
    return len(value) > 0


def is_hexadecimal(value):
    for digit in value.upper():
        if digit not in "0123456789ABCDEF":
            return False
    return len(value) > 0


def main():
    print("Number System Converter (8-bit maximum)")
    print("---------------------------------------")

    value = input("Enter a number: ").strip().upper()

    if value.startswith("0B"):
        system = "binary"
        value = value[2:]

    elif value.startswith("0X"):
        system = "hexadecimal"
        value = value[2:]

    else:
        if value.startswith("-"):
            system = "denary"

        elif is_binary(value):
            print("\nThis number could be:")
            print("1. Binary")
            print("2. Denary")
            print("3. Hexadecimal")

            choice = input("Choose the number system: ")

            if choice == "1":
                system = "binary"
            elif choice == "2":
                system = "denary"
            elif choice == "3":
                system = "hexadecimal"
            else:
                print("Invalid choice.")
                return

        elif is_hexadecimal(value):
            print("\nThis number could be:")
            print("1. Denary")
            print("2. Hexadecimal")

            choice = input("Choose the number system: ")

            if choice == "1":
                system = "denary"
            elif choice == "2":
                system = "hexadecimal"
            else:
                print("Invalid choice.")
                return

        else:
            print("Invalid number.")
            return

    if system == "binary":
        if not is_binary(value) or len(value) > 8:
            print("Binary must contain 1 to 8 bits.")
            return

        number = binary_to_denary(value)

        if value[0] == "1":
            print("\nHow should the binary number be interpreted?")
            print("1. Unsigned")
            print("2. Two's complement")
            print("3. Sign and magnitude")

            choice = input("Choose an interpretation: ")

            if choice == "2":
                if number >= 2 ** (len(value) - 1):
                    number = number - 2 ** len(value)

            elif choice == "3":
                magnitude = binary_to_denary(value[1:])
                number = -magnitude

            elif choice != "1":
                print("Invalid choice.")
                return

    elif system == "hexadecimal":
        if not is_hexadecimal(value) or len(value) > 2:
            print("Hexadecimal must contain 1 or 2 digits.")
            return

        number = hex_to_denary(value)

    else:
        try:
            number = int(value)
        except ValueError:
            print("Invalid denary number.")
            return

    if number < -128 or number > 255:
        print("Number is outside the 8-bit range.")
        return

    print("\nConversions")
    print("-----------")
    print("Denary:", number)

    if number >= 0:
        print("Unsigned binary:",
              denary_to_binary(number).zfill(8))
        print("Hexadecimal:",
              denary_to_hex(number).zfill(2))
    else:
        print("Binary magnitude: -",
              denary_to_binary(abs(number)), sep="")
        print("Hexadecimal magnitude: -",
              denary_to_hex(abs(number)), sep="")

    if -128 <= number <= 127:
        print("Two's complement:",
              to_twos_complement(number))

    if -127 <= number <= 127:
        print("Sign and magnitude:",
              to_sign_magnitude(number))


main()
