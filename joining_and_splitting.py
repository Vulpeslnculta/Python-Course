flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "lavender",
    "Sunflower",
    "Tiger Lily",
]

#  Joining section:

# for flower in flowers:
#     print(flower)

separator = " | "
output = separator.join(flowers)
print(output)

print(", ".join(flowers))

#  Splitting section:

panagram = """The quick brown
 fox jumps\t over
  the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,543,312,453"
print(sum(numbers.split(",")))