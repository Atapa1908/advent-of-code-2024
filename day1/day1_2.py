left_list = []
right_list = []

with open("day1_1.txt", "r") as input_file:
    file_content_in = input_file.read().split("\n")
    for line in file_content_in:
        left_list.append(int(line.split()[0]))
        right_list.append(int(line.split()[1]))

counts_list = [right_list.count(element) for element in left_list]

count_score_list = [a*b for a,b in zip(left_list, counts_list)]

print(sum(count_score_list))