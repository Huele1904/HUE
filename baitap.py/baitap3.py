# 1. In ra các số chẵn từ 0 đến 10
for i in range(11):
    if i % 2 == 0:
        print(i)

# 2. Tìm số lớn nhất trong danh sách không dùng hàm có sẵn
def find_max(lst):
    if not lst:
        return None
    max_num = lst[0]
    for num in lst[1:]:
        if num > max_num:
            max_num = num
    return max_num

numbers = [3, 1, 9, 7, 2, 8]
print("Số lớn nhất:", find_max(numbers))

# 3. Chương trình Quản lý sinh viên
class Student:
    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score
    
    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.score}"

class StudentManagement:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def display_students(self):
        for student in self.students:
            print(student)
    
    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def sort_by_score(self):
        self.students.sort(key=lambda s: s.score, reverse=True)
    
    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]

# Chạy chương trình
def main():
    sm = StudentManagement()
    sm.add_student(Student("SV001", "An", 85))
    sm.add_student(Student("SV002", "Bình", 90))
    sm.add_student(Student("SV003", "Chi", 78))
    
    print("Danh sách sinh viên:")
    sm.display_students()
    
    print("\nTìm kiếm sinh viên SV002:")
    print(sm.search_student("SV002"))
    
    print("\nDanh sách sau khi sắp xếp theo điểm:")
    sm.sort_by_score()
    sm.display_students()
    
    print("\nXóa sinh viên SV001")
    sm.remove_student("SV001")
    sm.display_students()

if __name__ == "__main__":
    main()
