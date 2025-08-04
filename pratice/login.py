# 'user_data.txt' ফাইলটি 'r' (read) মোডে খোলা হচ্ছে।
user_file = open('user_data.txt', 'r')

# ফাইলের সব লাইন একসাথে পড়া
all_users = user_file.readlines()

# ফাইলটি বন্ধ করে দেওয়া
user_file.close()

# লগইন করার জন্য ব্যবহারকারীর দেওয়া তথ্য
login_email = "rahim@example.com"
login_password = "asdf"

is_logged_in = False

# প্রতিটি লাইনের মধ্যে ব্যবহারকারীকে খোঁজা
for user_info in all_users:
    if login_email in user_info and login_password in user_info:
        is_logged_in = True
        break

if is_logged_in:
    print("Yes you are logged in")
else:
    print("You are not logged in")