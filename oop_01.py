class AddmissionForm():

    merit_list = []

    def __init__(self, full_name, cnic, education):
        self.name = full_name
        self.cnic = cnic
        self.education = education

    def show_user_data(self):

        return f"Full Name: {self.name} - CNIC: {self.cnic} - Education: {self.education}"
    
    
    

class MeritList(AddmissionForm):

    def __init__(self, name):
        print("Merit List")
        self.name = name
    
    def add_into_merit_list(self):
        super().merit_list.append(self.name)


# user_full_name = input("Your Name: ")

# user_cnic = input("Your CNIC: ")

# user_education = input("Your Education: ")

# new_std = AddmissionForm(user_full_name, user_cnic, user_education)

new_std = MeritList("Jawad")



new_std.add_into_merit_list()



print(new_std.merit_list)




