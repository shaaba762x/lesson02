name_ = 'Lora'
age_ = [104, 101, 212]
length_ = 49.5
is_student_ = (age_[0] > length_)
immutable_var = name_, age_, length_, is_student_
print(immutable_var)
immutable_var [1][0] = (12)
is_student_ = (age_[0] > length_)
print(immutable_var)
mutable_list = [name_, is_student_, age_, length_]
print(mutable_list)
mutable_list [0] = 'Palmer'
mutable_list [2][0] = (42)
print(mutable_list)
