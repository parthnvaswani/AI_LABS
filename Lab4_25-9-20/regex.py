# email: r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]{2,3}$"
# pincode: r"^[1-9][0-9]{5}$"
# phone: r"^[0-9]{10}$"
# password: r"^(?=.*\d+)(?=.*[A-Z]+)(?=.*[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+)(?!.*\s).{4,8}$"

import re


def check_email(email):
    regex = re.compile(r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]{2,3}$")
    return "valid email" if regex.match(email) else "invalid email"


print(check_email("parthnvaswanigmail.com"))
print(check_email("parthnvaswani@gmail.com"))


def check_pincode(pincode):
    regex = re.compile(r"^[1-9][0-9]{5}$")
    return "valid pincode" if regex.match(pincode) else "invalid pincode"


print(check_pincode("39000"))
print(check_pincode("390002"))


def check_phone(phone):
    regex = re.compile(r"^[0-9]{10}$")
    return "valid phone number" if regex.match(phone) else "invalid phone number"


print(check_phone("123456789"))
print(check_phone("1234567890"))


def check_password(password):
    regex = re.compile(
        r"^(?=.*\d+)(?=.*[A-Z]+)(?=.*[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]+)(?!.*\s).{8,}$"
    )
    return "valid password" if regex.match(password) else "invalid password"


print(check_password("A123Bazy"))
print(check_password("A123$Bazy_"))
