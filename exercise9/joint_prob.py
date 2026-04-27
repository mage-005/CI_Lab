import csv
print("Joint Probability")
p = {}


file_path = input("Enter CSV file path: ")

with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        a = int(row['A'])
        b = int(row['B'])
        c = int(row['C'])
        prob = float(row['P'])
        p[(a, b, c)] = prob

while True:
    print("\nMenu")
    print("1. Find Joint Probability")
    print("2. Find Marginal Probability ")
    print("3. Find Conditional Probability P(A|B,C)")
    print("4. Find Conditional Probability P(B | A,C)")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        ta, tb, tc = map(int, input("Enter values for A, B, C : ").split())
        print(f"Result: P(A={ta}, B={tb}, C={tc}) = {p[(ta, tb, tc)]}")

    elif choice == '2':
        var = input("Enter a variable(marginal probability) : ").upper()
        val = int(input(f"Value for {var} (0 or 1): "))

        if var == 'A':
            components = [p[(val, b, c)] for b in [0, 1] for c in [0, 1]]
            res = sum(components)
            detail_str = " + ".join([str(v) for v in components])
            print(f"\nWKT P(A={val}) = Summation P(A={val}, B, C)")
            print(f"{detail_str}")
        elif var == 'B':
            components = [p[(a, val, c)] for a in [0, 1] for c in [0, 1]]
            res = sum(components)
            detail_str = " + ".join([str(v) for v in components])
            print(f"\nWKT P(B={val}) = Summation P(A, B={val}, C)")
            print(f"{detail_str}")
        else:
            components = [p[(a, b, val)] for a in [0, 1] for b in [0, 1]]
            res = sum(components)
            detail_str = " + ".join([str(v) for v in components])
            print(f"\nWKT P(C={val}) = Summation P(A, B, C={val})")
            print(f"{detail_str}")

        print(f"Marginal P({var}={val}) = {res:.4f}")

    elif choice == '3':
        ta, tb, tc = map(int, input("Enter target A, B, C its values: ").split())
        p_abc = p[(ta, tb, tc)]
        v1, v2 = p[(0, tb, tc)], p[(1, tb, tc)]
        p_bc = v1 + v2

        print(f"\nWKT P(A|B,C) = P(A,B,C) / P(B,C)")
        print(f"P(A={ta}, B={tb}, C={tc}) = {p_abc}")
        print(f"P(B={tb}, C={tc}) = {v1} + {v2} = {p_bc}")
        print(f"{p_abc} / {p_bc}")
        print(f"P(A={ta}|B={tb},C={tc}) = {p_abc/p_bc if p_bc > 0 else 0:.4f}")

    elif choice == '4':
        ta, tb, tc = map(int, input("Enter values for A, B, C : ").split())
        p_abc = p[(ta, tb, tc)]
        v1, v2 = p[(ta, 0, tc)], p[(ta, 1, tc)]
        p_ac = v1 + v2

        print(f"\nWKT P(B|A,C) = P(A,B,C) / P(A,C)")
        print(f"P(A={ta}, B={tb}, C={tc}) = {p_abc}")
        print(f"P(A={ta}, C={tc}) = {v1} + {v2} = {p_ac}")
        print(f"{p_abc} / {p_ac}")
        print(f"P(B={tb}|A={ta},C={tc}) = {p_abc/p_ac if p_ac > 0 else 0:.4f}")

    elif choice == '5':
        print("Exit")
        break
    else:
        print("Invalid Choice!")