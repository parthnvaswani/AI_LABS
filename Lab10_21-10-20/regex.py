# Write a Python program to test the first character of a string is uppercase or not.
import re


def check_uppercase(input):
    regex = re.compile(r"^[A-Z]")
    return "valid input" if regex.match(input) else "invalid input"


print(check_uppercase("Parth"))
print(check_uppercase("PArth"))
print(check_uppercase("parth"))

# Write a Python program to search a date within a string.
def check_date(input):
    regex = re.compile(r"^\d{2}[-/]\d{2}[-/]\d{4}$")
    return "valid input" if regex.match(input) else "invalid input"


print(check_date("01/11/2000"))

# Write a Python program to check whether a given value is IP value or not.
def check_IP(input):
    regex = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    return "valid input" if regex.match(input) else "invalid input"


print(check_IP("20.122.253.10"))

# Write a Python program to check whether a given value is an valid url or not.
def check_URL(input):
    regex = re.compile(r"^https?://(www.)?[a-zA-z0-9$-_.+!*'(),]+\.[a-z]{1,3}(/.*)?$")
    return "valid input" if regex.match(input) else "invalid input"


print(check_URL("https://parthnvaswani.com"))

# Write a Python program to check whether a given value is alpha numeric or not.
def check_alpha(input):
    regex = re.compile(r"^\w+$")
    return "valid input" if regex.match(input) else "invalid input"


print(check_alpha("Parth1234"))

# Write a Python program to check whether a given value is time string or not.
def check_time(input):
    regex = re.compile(r"^([01]?[0-9]|2[0-3]):[0-5][0-9]$")
    return "valid input" if regex.match(input) else "invalid input"


print(check_time("12:30"))

# Write a Python program to check whether a given value is hexcolor value or not.
def check_hexcolor(input):
    regex = re.compile(r"^#([0-9a-fA-F]{3}){1,2}$")
    return "valid input" if regex.match(input) else "invalid input"


print(check_hexcolor("#fff"))

# Write a Python program to extract year, month and date from an url.


def extract_date(url):
    return re.findall(r"/(\d{4})/(\d{1,2})/(\d{1,2})/", url)


print(extract_date("https://www.parthnvaswani.com/birth/2000/11/20/"))
