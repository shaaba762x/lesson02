name_ = 'Lora'
age_ = [104, 101, 212]
length_ = 49.5
is_student_ = True
immutable_var = name_, age_, length_, is_student_
print(immutable_var)
immutable_var [1][1] = (69)
print(immutable_var)
mutable_list = [name_, is_student_, age_, length_]
print(mutable_list)
mutable_list [name_] = 'Palmer'
mutable_list [2][0] = (42)
print(mutable_list)
