def list_to_hex(crazy_list):
    out = ""
    return "0x" + out.join(crazy_list)

def hex_to_list(our_hex):
    crazy_list = list(our_hex.upper())
    crazy_list.pop(0)
    crazy_list.pop(0)
    return crazy_list

first_entered_hex = input("Enter please your first hex number:")
first_entered_hex = list(first_entered_hex)

second_entered_hex = input("Enter please your second hex number:")
second = list(first_entered_hex)


sum = (hex(int(list_to_hex(first_entered_hex), 16) + int(list_to_hex(second_entered_hex),16)))
product = (hex(int(list_to_hex(first_entered_hex), 16) * int(list_to_hex(second_entered_hex),16)))

print("\nSum of two entered hex is:")
print(hex_to_list(sum))

print("\nProduct of two entered hex is:")
print(hex_to_list(product))
