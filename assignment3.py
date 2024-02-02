def score (result):
    if len(number_of_subjects) !=5:
        exit("Please Enter marks of 5 subjects only.")
    percentage = sum(number_of_subjects)/5
    if percentage >75 :
        return f"You scored {percentage} your score is distinction."
    elif 60<= percentage <75 :
        return f"You scored {percentage} you are in first division."
    elif  50<= percentage <60 :
        return f"You scored {percentage} you are in second division."
    elif  40>= percentage <50 :
        return f"You scored {percentage} you are in third division."
number_of_subjects = []
subjects = int(input("Enter The number of your subjeects : "))
for _ in range(subjects) :
    subject = float(input("Enter Your marks "))
    number_of_subjects.append(subject)
result = score(number_of_subjects)
print(result)
