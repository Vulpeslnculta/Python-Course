from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0)  # differenting from get method, this adds key to dict.
print(f"beans: {beans_quantity}")

ketchup_quantity = pantry.get("ketchup", 0)
print(f"Ketchup: {ketchup_quantity}")

print()
print("`pantry` now contains...\n")

for key, value in sorted(pantry.items()):
    print(key, value)