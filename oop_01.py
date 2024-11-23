class AddmissionForm():

    def __init__(self, full_name, cnic, education):
        self.name = full_name
        self.cnic = cnic
        self.education = education

    def show_user_data(self):

        return f"Full Name: {self.name} - CNIC: {self.cnic} - Education: {self.education}"


user_full_name = input("Your Name: ")

user_cnic = input("Your CNIC: ")

user_education = input("Your Education: ")



new_std = AddmissionForm(user_full_name, user_cnic, user_education)

result = new_std.show_user_data()


print(result)




