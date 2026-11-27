def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # الشرط 1: الطول بين 2 و 6 أحرف
    if not (2 <= len(s) <= 6):
        return False

    # الشرط 2: الأحرف والأرقام فقط، بدون رموز أو مسافات
    if not s.isalnum():
        return False

    # الشرط 3: يجب أن يبدأ بحرفين على الأقل
    if not s[:2].isalpha():
        return False

    # الشرط 4 و 5: الأرقام تأتي في النهاية، ولا يبدأ الرقم بالصفر
    for i, char in enumerate(s):
        if char.isdigit():
            if not s[i:].isdigit():
                return False
            if char == "0":
                return False
            break

    return True

main()
