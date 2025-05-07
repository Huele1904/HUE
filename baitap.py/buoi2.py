import math

# Bài 1: Hình tròn
r = 30
print("Diện tích hình tròn:", math.pi * r * r)
print("Chu vi hình tròn:", 2 * math.pi * r)

r_input = float(input("Nhập bán kính: "))
print("Diện tích với bán kính bạn nhập:", math.pi * r_input * r_input)

# Bài 2: Số lớn nhất trong danh sách
numbers = [5, 12, 3, 25, 8]
print("Số lớn nhất:", max(numbers))

# Bài 3: Số nhỏ nhất trong danh sách
print("Số nhỏ nhất:", min(numbers))

# Bài 4: Độ dài câu
sentence = "Tôi là một sinh viênDAU"
print("Độ dài câu:", len(sentence))

# Bài 5: Số từ trong câu
print("Số từ trong câu:", len(sentence.split()))
