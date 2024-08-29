#######################################################
#    -- Admin System Login as Admin --                #
#    -- BY Hashem Ahmed Mahmoud EL Mahdi --           #
#######################################################
# Message to Start Program
print('#'*40)
print(' [ Start Program ] '.center(40, '#'))
print('#'*40)
# Admin List
admins = ['Hashem', 'Ali', 'Abdo']
# Take Username By Input Method
name = input("Enter Your Name : ").strip().capitalize()

# If Name is in Admins
if name in admins:
    print(f"Hello {name} Welcome Back")
    option = input('Delete or Update | [D,U] Your Name : ').strip().capitalize()
    # Update Option
    if option == 'Update' or option == 'U':
        new_name = input('Please Enter New Name : ').strip().capitalize()
        admins[admins.index(name)] = new_name
        print("Your Name updated")
        print(admins)
    # Delete Option
    elif option == 'Delete' or option == 'D':
        admins.remove(name)
        print("Your Name Deleted")
        print(admins)
    # wrong Option
    else:
        print("Please Enter Valid Option")
# If Name is not found in Admins
else:
    # To Add or not
    status = input("You Is not Admin , To Add You Enter [ Y or N ]: ").strip().capitalize()
    if status == 'Yes' or status == 'Y':
        print("You is been added")
        admins.append(name)
        print(admins)
    else:
        print("You Are Not Added.")

# This Design To End Program
print('#'*40)
print(' [ End Program ] '.center(40, '#'))
print('#'*40)