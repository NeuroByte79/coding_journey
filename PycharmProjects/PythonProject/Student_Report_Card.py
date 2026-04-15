def student_report_card():
    print("\n📊 STUDENT REPORT CARD\n")

    subjects = ["Math", "Science", "English", "History", "Computer"]
    marks = []

    # Input marks
    for sub in subjects:
        m = float(input(f"Enter marks for {sub}: "))
        marks.append(m)

    total = sum(marks)
    average = total / len(subjects)
    percentage = (total / 500) * 100  # assuming each subject is out of 100

    # Grade logic
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "F"

    # Pass/Fail logic
    result = "PASS ✅" if all(m >= 33 for m in marks) else "FAIL ❌"

    # Output formatting
    print("\n" + "="*40)
    print("        🎓 REPORT CARD")
    print("="*40)

    for sub, m in zip(subjects, marks):
        print(f"{sub:<15}: {m:>6.2f}")

    print("-"*40)
    print(f"{'Total':<15}: {total:>6.2f}")
    print(f"{'Average':<15}: {average:>6.2f}")
    print(f"{'Percentage':<15}: {percentage:>6.2f}%")
    print(f"{'Grade':<15}: {grade}")
    print(f"{'Result':<15}: {result}")
    print("="*40)


student_report_card()