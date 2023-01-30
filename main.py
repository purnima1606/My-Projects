import all_methods
import my_db
from config import database_info


class Main:
    def is_aadhar_card(self, aadhar_file):
        if aadhar_file:
            aadhar_dict = all_methods.aadhar_card(aadhar_file)
            # return aadhar_dict
        else:
            aadhar_dict = {"Name": None, "Guardian": None,
                           "DOB": None, "Gender": None, "Aadhar no": None}
        return aadhar_dict

    def is_passport(self, passport_file):
        if passport_file:
            pass_dict = all_methods.passport(passport_file)
            # return pass_dict
        else:
            pass_dict = {"Passport No": None}
            # return pass_dict
        return pass_dict

    def is_pancard(self, pancard_file):
        if pancard_file:
            pan_data = all_methods.pancard(pancard_file)
            # return pan_data
        else:
            pan_data = {"Pancard No": None}
            # return pan_data
        return pan_data

    def insert_data_db(self, database_info, details_dict):
        my_db.insert_data(database_info, details_dict)
        print()
        print("Data inserted successfully!")
        print()
        return

    def get_data_db(self, database_info):
        data = my_db.get_data(database_info)
        return data


if __name__ == "__main__":
    aadhar_file = "Adhar.jpg"
    passport_file = "Passport.png"
    pancard_file = "Pancard.jpg"

    obj = Main()

    aadhar_data = obj.is_aadhar_card(aadhar_file)
    passport_data = obj.is_passport(passport_file)
    pancard_data = obj.is_pancard(pancard_file)

    details_dict = {}
    details_dict.update(aadhar_data)
    details_dict.update(passport_data)
    details_dict.update(pancard_data)
    print("--------------------------------------------------------------------------------------------------------------------------")
    print(details_dict)
    print()
    user_input = input("Do you want to add the result in database y/n: ")
    if user_input in "yY":
        obj.insert_data_db(database_info, details_dict)
    else:
        pass

    user_input = input("Want to fetch value from the database table y/n: ")
    print()
    if user_input in "yY":
        get_data = obj.get_data_db(database_info)
        for row in get_data:
            print(row)
        print("--------------------------------------------------------------------------------------------------------------------------")
    else:
        pass
