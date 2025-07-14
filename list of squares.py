def process_range(start: int, end: int):
    
    numbers = list(range(start, end + 1))
    squares = [n**2 for n in numbers]
    evens = [x for x in squares if x % 2 == 0]
    odds = [x for x in squares if x % 2 != 0]
    return squares, evens, odds
range1 = (1, 10)
range2 = (5, 15)

s1, even1, odd1 = process_range(*range1)
s2, even2, odd2 = process_range(*range2)

print(f"User 1 squares: {s1}")
print(f"  Even squares: {even1}")
print(f"  Odd squares: {odd1}")

print(f"\nUser 2 squares: {s2}")
print(f"  Even squares: {even2}")
print(f"  Odd squares: {odd2}")
