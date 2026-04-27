print("Bayes Theorem")
print("-------------")
pa = float(input("Enter P(A): "))
pbgna = float(input("Enter P(B|A): "))
pb = float(input("Enter P(B): "))

if pb == 0:
    print("Error: Division by zero is not possible.")
else:
    p_a_given_b = (pbgna * pa) / pb
    print(f"Result: P(A|B) = {p_a_given_b:.4f}")