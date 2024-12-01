input_file = "Input_Puzzle_1.md"
list1 = []
list2 = []

with open(input_file, "r") as file:
    for line in file:
        a, b = map(int, line.split())
        list1.append(a)
        list2.append(b)

list1.sort()
list2.sort()

total_distance=0
for i in range (len(list1)):
    total_distance+= abs(list1[i]-list2[i])

print(f"total distance: {total_distance}")

similarity_score = 0
for i in range(len(list1)):
    m = 0
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            m += 1
    similarity_score += list1[i] * m 

print("Similarity Score:", similarity_score)
