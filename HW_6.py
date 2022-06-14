class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if grade not in range(11):
                return 'Оценка не проставлена, поставьте от 0 до 10'
            elif course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    @staticmethod
    def find_avg(grades):
        val, count_ = 0, 0
        for v in grades.values():
            val += sum(v)
            count_ += len(v)
        return round(val / count_, 2)

    def __lt__(self, other):
        if isinstance(other, Reviewer):
            print('Нельзя сравнить с проверяющим!')
            return
        return self.find_avg(self.grades) < other.find_avg(other.grades)

    def __le__(self, other):
        if isinstance(other, Reviewer):
            print('Нельзя сравнить с проверяющим!')
            return
        return self.find_avg(self.grades) <= other.find_avg(other.grades)

    def __str__(self):
        return f'Имя: {self.name}' \
               f'\nФамилия: {self.surname}' \
               f'\nСредняя оценка за д/з: {self.find_avg(self.grades)}' \
               f'\nКурсы в процессе обучения: {", ".join(self.courses_in_progress)}' \
               f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lec_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lec_list.append(self)

    @staticmethod
    def find_avg(grades):
        val, count_ = 0, 0
        for v in grades.values():
            val += sum(v)
            count_ += len(v)
        return round(val / count_, 2)

    def __str__(self):
        return f'Имя: {self.name}' \
               f'\nФамилия: {self.surname}' \
               f'\nСредняя оценка за лекции: {self.find_avg(self.grades)}'

    def __lt__(self, other):
        if isinstance(other, Reviewer):
            print('Нельзя сравнить с проверяющим!')
            return
        return self.find_avg(self.grades) < other.find_avg(other.grades)

    def __le__(self, other):
        if isinstance(other, Reviewer):
            print('Нельзя сравнить с проверяющим!')
            return
        return self.find_avg(self.grades) <= other.find_avg(other.grades)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if grade not in range(11):
                return 'Оценка не проставлена, поставьте от 0 до 10'
            elif course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


def find_avg_rates(persons_list, course):
    res = {}
    sum_avg = 0
    for person in persons_list:
        if course in person.grades:
            avg_rate = round(sum(person.grades[course]) / len(person.grades[course]), 2)
            sum_avg += avg_rate
        else:
            avg_rate = 'no rates'
        res[f'{person.name} {person.surname}'] = avg_rate
    all_avg = round(sum_avg / len(res), 2)
    return res, course, all_avg


reviewer_1 = Reviewer('Mike', 'Myers')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Tom', 'Garfield')
reviewer_2.courses_attached += ['Java', 'Git']

student_1 = Student('Ruoy', 'Eman', 'm')
student_1.courses_in_progress += ['Python', 'Java', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Vasya', 'Ivanov', 'm')
student_2.courses_in_progress += ['Python', 'Java', 'Git']


lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('John', 'Smith')
lecturer_2.courses_attached += ['Java', 'Git']


reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_1, 'Java', 10)

reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Java', 9)

student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_2, 'Java', 7)
student_1.rate_lecturer(lecturer_2, 'Java', 10)
student_1.rate_lecturer(lecturer_2, 'Git', 10)
student_1.rate_lecturer(lecturer_2, 'Java', 9)

student_1.rate_lecturer(lecturer_2, 'Java', 7)
student_2.rate_lecturer(lecturer_1, 'Python', 5)
student_2.rate_lecturer(lecturer_1, 'Python', 7)
student_2.rate_lecturer(lecturer_2, 'Git', 4)

res1, course1, all_avg1 = find_avg_rates(Student.student_list, "Python")
res2, course2, all_avg2 = find_avg_rates(Lecturer.lec_list, 'Java')

print('\tПроверяющие:', reviewer_1, '', reviewer_2, sep='\n', end=2*'\n')
print('\tЛекторы:', lecturer_1, '', lecturer_2, sep='\n', end=2*'\n')
print('\tСтуденты:', student_1, '', student_2, sep='\n', end=2*'\n')

print(lecturer_1 > student_2)

print(f'Студент {student_1.name}:\n{student_1.grades}')
print(f'Студент {student_2.name}:\n{student_2.grades}')
print()
print(f'Лектор {lecturer_1.name} {lecturer_1.surname} прикреплен к курсам: {lecturer_1.courses_attached},'
      f'\nполучил оценки за лекции: {lecturer_1.grades}\n')

print(f'Лектор {lecturer_2.name} {lecturer_2.surname} прикреплен к курсам: {lecturer_2.courses_attached},'
      f'\nполучил оценки за лекции: {lecturer_2.grades}\n')

print(f'Средние оценки студентов по курсу {course1}:\n{res1}\n'
      f'Средняя оценка всех студентов: {all_avg1}\n')
print(f'Средние оценки лекторов по курсу {course2}:\n{res2}\n')
