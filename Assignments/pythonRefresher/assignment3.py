"""
Lists Assignment
- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals
"""

zoo = ["lion", "tiger", "bear", "elephant", "giraffe"]
zoo.pop(3)
zoo.append("zebra")
zoo.pop(0)
print("All animals in the zoo:", zoo)
print("First three animals in the zoo:", zoo[:3])