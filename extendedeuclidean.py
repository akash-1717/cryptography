def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = extended_gcd(b % a, a)
    
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y

a = 35
b = 15

gcd, x, y = extended_gcd(a, b)

print("GCD:", gcd)
print("x:", x)
print("y:", y)

# Output:
# GCD: 5
# x: -1
# y: 3

