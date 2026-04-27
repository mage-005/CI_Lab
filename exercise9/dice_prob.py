def dice_probability():
    t = int(input("Enter target sum: "))
    total_outcomes = 36
    favorable = []
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == t:
                favorable.append((i, j))

    p = len(favorable) / total_outcomes
    print(f"Outcomes: {favorable}")
    print(f"Sample space (n): {len(favorable)}")
    print(f" P = P(A) / S(n)")
    #print(f"Calculation: {len(favorable)} / {total_outcomes}")
    print(f"Probability = {p:.4f}")

dice_probability()