import random

def loadingsequece():
    print("Windows 98 Key Generator")
    print("Loading...")

loadingsequece()

keys = int(input("How many keys do you want to generate? "))
generated_keys = []  # List to store generated keys

for _ in range(keys):
    # Create the first key part (xxx)
    key_part1 = random.randint(1, 366)
    # Check if the number is less than 100 add 0's at the start
    if key_part1 < 100:
        if key_part1 < 10:
            key_part1 = "00" + str(key_part1)
        else:
            key_part1 = "0" + str(key_part1)

    # Create the second key part (yy)
    
    years = [95, 96, 97, 98, 99, 0, 1, 2, 3]
    key_part2 = random.choice(years)
    if key_part2 <= 3:
        key_part2 = "0" + str(key_part2)

    while True:
        # Create the third key part (NNNNN)
        random_numbers = random.sample(range(10), 5)  # Use unique single-digit random numbers
        sum_digits = sum(random_numbers)
        if sum_digits % 7 == 0:
            key_part3 = "".join(map(str, random_numbers))
            key_part3 = f"{key_part3:05}"  # Format to 5 digits without leading zeros
            break
        
    # Create the fourth key part (zzzzz)
    key_part4 = "".join(str(random.randint(0, 9)) for _ in range(5))


    # Print the key
    final_key = f"{key_part1}{key_part2}-OEM-00{key_part3}-{key_part4}"
    generated_keys.append(final_key)

for key in generated_keys:
    print(key)