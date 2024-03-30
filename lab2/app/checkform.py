def phonecheck(phone: str) -> str:
    
    for char in '()-.+ ':
        phone = phone.replace(char, "")

    if not phone.isdigit():
        return "Недопустимый ввод. В номере телефона встречаются недопустимые символы."

    if not (10 <= len(phone) <= 11):
        return "Недопустимый ввод. Неверное количество цифр."
    
    return ""

def phoneformat(phone: str) -> str:
    phone = ''.join(filter(str.isdigit, phone))

    if phone.startswith("7"):
        phone = phone[1:]

    elif phone.startswith("8"):
        phone = phone[1:]

    return f"8-{phone[:3]}-{phone[3:6]}-{phone[6:8]}-{phone[8:10]}"