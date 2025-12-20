def love_calculator(name1, name2):
    # Convert names to lowercase and remove spaces
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    # Combine names
    combined_names = name1 + name2

    # Count letters in the word "love"
    score = 0
    for char in "love":
        score += combined_names.count(char)

    # Generate percentage
    love_percentage = (score * 10) % 101

    return love_percentage


print("❤️ Welcome to Love Calculator ❤️")

person1 = input("Enter first name: ")
person2 = input("Enter second name: ")

result = love_calculator(person1, person2)

print(f"\n💖 Love Percentage between {person1} and {person2} is: {result}%")

if result > 80:
    print("💍 Perfect match!")
elif result > 50:
    print("😊 Good relationship!")
elif result > 30:
    print("🙂 Can work with effort.")
else:
    print("💔 Better stay friends.")
