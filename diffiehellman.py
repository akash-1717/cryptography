def generate_symmetric_key(g, p, x, y):
    A = pow(g, x, p)
    B = pow(g, y, p)

    symmetric_key_a = pow(B, x, p)
    symmetric_key_b = pow(A, y, p)

    assert symmetric_key_a == symmetric_key_b

    return symmetric_key_a

g = 2
p = 23
x = 6
y = 15

symmetric_key = generate_symmetric_key(g, p, x, y)
 
print("Symmetric Key:", symmetric_key)

# Output:
# Symmetric Key: 19
