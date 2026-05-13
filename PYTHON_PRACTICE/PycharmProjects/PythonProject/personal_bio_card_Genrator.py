def generate_bio():
    data = {
        "Name"  :  input("Enter your full name:"),
        "Age"   :  int(input("Enter your age:")),
        "City"  :  input("Enter your city:"),
        "Role"  :  input("Enter your dream role:"),
        "Skills":  input("Enter your Top 3skills:"),
        "Github":  input("Enter your Github username:")
        }
    # Format skills into list
    skills_list = [skills.strip() for skills in data["Skills"].split(",")]

    # Create bio card
    print("\n" + "="*40)
    print("        🚀 PERSONAL BIO CARD")
    print("="*40)
    print(f"👤 Name      : {data['Name']}")
    print(f"🎂 Age       : {data['Age']}")
    print(f"📍 City      : {data['City']}")
    print(f"💼 Goal      : {data['Role']}")
    print(f"🛠️ Skills    : {', '.join(skills_list)}")
    print(f"🌐 GitHub    : https://github.com/{data['Github']}")
    print("=" * 40)


generate_bio()