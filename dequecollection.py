from collections import deque

# Initialize 
d = deque()

# Append right
d.append(1)
d.append(2)
d.append(3)

# Append left
d.appendleft(0)
d.appendleft(-1)

# Remove right
right_pop = d.pop()

# Remove left
left_pop = d.popleft()
# Print the deque
print(d)
#popped elements left right
print(f'Popped from right: {right_pop}')
print(f'Popped from left: {left_pop}')

# Access with index
print(d[0])  # First element
print(d[-1]) # Last element


d.extend([9,5,2])
d.extendleft([-5, -7])

print(d)

