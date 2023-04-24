class Student(Person):
    pass

s1 = Student('Arthur', 'Curry', 33, 'England', 'London')
s2 = Student('Emily', 'Carter', 28, 'England', 'Manchester')
print(s1.person_info())
s1.add_skill('HTML')
s1.add_skill('CSS')
s1.add_skill('JavaScript')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)