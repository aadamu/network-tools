from cisco_decrypt import CiscoPassword

# Decode and return string using cisco_decrypt
def crack_cisco7(coded_string):
    cisco7_crack = CiscoPassword()

    decoded_string = cisco7_crack.decrypt(coded_string)

    return (decoded_string)
