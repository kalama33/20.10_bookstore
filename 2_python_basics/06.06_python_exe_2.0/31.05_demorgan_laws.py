def demorgans_law_1(p, q):
    left_side = not (p and q)
    right_side = (not p) or (not q)
    return left_side == right_side

def demorgans_law_2(p, q):
    left_side = not (p or q)
    right_side = (not p) and (not q)
    return left_side == right_side

# Given values
p = True
q = True

# Check the validity of De Morgan's Laws
law_1_valid = demorgans_law_1(p, q)
law_2_valid = demorgans_law_2(p, q)

print(f"De Morgan's Law 1 is valid: {law_1_valid}")
print(f"De Morgan's Law 2 is valid: {law_2_valid}")

