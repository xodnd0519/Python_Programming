           # True
print(isinstance(t, SchoolMember))              # True
print(isinstance(s, Student))                   # True
print(isinstance(t, Teacher))                   # True

print(issubclass(Student, SchoolMember))        # True
print(issubclass(Teacher, SchoolMember))        # True
print(issubclass(Student, Teacher))     