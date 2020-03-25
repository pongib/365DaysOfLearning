import helpers

name = "Sittipong SripaisaRnMonGKoL"
print(f"Lower is {helpers.extract_lower_sorted(name)}")
print(f"Upper is {helpers.extract_upper_sorted_reversed(name)}")

print(f"From Name var Lower is {helpers.extract_lower_sorted(helpers.my_name)}")