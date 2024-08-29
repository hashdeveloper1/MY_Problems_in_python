# ===============================
#          -- Input --
# ===============================
# ===============================
name = input("Enter Your Name : ").strip().capitalize()
email = input("Enter Your Email : ").strip()
user_name = email[0:email.find('@')]
domin = email[email.find('@') + 1:]
print(f"Hello {name} \nYour UserName is : {user_name} \nDomin Name is : {domin}")