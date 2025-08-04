# 'user_data.txt' নামে একটি ফাইল খোলা হচ্ছে 'a' (append) মোডে।
# 'a' মোড ব্যবহার করলে ফাইলটি যদি আগে থেকেই থাকে, তাহলে নতুন তথ্য তার শেষে যুক্ত হবে।
# আর যদি না থাকে, তবে নতুন একটি ফাইল তৈরি হবে।
user_file = open('user_data.txt', 'a')

# নতুন ব্যবহারকারীর তথ্য
name = "Rahim Mia"
email = "rahim@example.com"
password = "password123"

# তথ্যের ফরম্যাট তৈরি করে ফাইলে লেখা
user_info = f"Name: {name}, Email: {email}, Password: {password}\n"
user_file.write(user_info)

# ফাইলটি বন্ধ করে দেওয়া
user_file.close()