import re
def is_valid_ethereum_address(address):
    # Ethereum address regular expression
    ethereum_address_pattern = re.compile(r'^0x[a-fA-F0-9]{40}$')

    # Check if the address matches the pattern
    return bool(ethereum_address_pattern.match(address))

# Example Ethereum address for testing
ethereum_address = input("enter your  ethereum")

# Check the validity of the Ethereum address
if is_valid_ethereum_address(ethereum_address):
    print("true")
else:
    print("false")