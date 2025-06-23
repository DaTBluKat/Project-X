sym_count = 0


while True:
    print("------ SUBNET CALCULATOR ------")
    print("1: CIDR to IP Range")
    print("2: IP Range to CIDR")
    calc_type = input("Enter here: ")
    if calc_type == "1" or calc_type == "2":
        break

if calc_type == "1":
    CIDR = input("Enter the CIDR: ")
    ip_verify(CIDR)

def ip_verify(CIDR):
    for symbol in CIDR:
        sym_count += 1
        if symbol == ".":
            if CIDR[sym_count - 1].isdigit:
                is_digit = True
            else:
                print("Invalid input!")
                return 1
                
            
