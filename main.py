import openpyxl_section
import selenium_section


def main():
    user_info = get_user_info()
    spreadsheet_data = openpyxl_section.entrypoint()
    selenium_section.entrypoint(user_info, spreadsheet_data)
    print("Be sure to double check everything before submitting! Enter personal information and budget account number")


def get_user_info():
    print("Enter your full name: ")
    name = input()
    print("Enter your email: ")
    email = input()
    user_info = {'name': name, 'email': email}
    return user_info


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
