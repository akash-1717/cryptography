def simple_hash(message):
    hash_value = sum(ord(char) for char in message)
    return hash_value

message = "Hello, World!"

hash_value = simple_hash(message)

computed_hash = simple_hash(message)

print("Original Message:", message)
print("Original Hash:", hash_value)

print("--- Receiver Computing Hash ---")
print("Computed Hash:", computed_hash)

modified_message = "Hello, World!!"

modified_hash = simple_hash(modified_message)

print("\nModified Message:", modified_message)
print("Modified Hash:", modified_hash)

# Output:
# Original Message: Hello, World!
# Original Hash: 1116
# --- Receiver Computing Hash ---
# Computed Hash: 1116 

# Modified Message: Hello, World!!
# Modified Hash: 1166
