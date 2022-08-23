options_list = [

# pehle question ke liye options
["Four", "Nine", "Seven", "Eight"],
#second question ke liye options
["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#third question ke liye options
["Software Engineering", "Counseling", "Tourism", "Agriculture"]]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1]

question_list = ["How many continents are there?", "What is the capital of India?","NG mei kaun se course padhaya jaata hai?"]
option_list=[["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
fiftyfifty=[["Seven", "Eight"],["Chennai", "Delhi"],["Software Engineering", "Counseling"]]
answer_list = [3, 4, 1]
i=0
while i<len(question_list):
    print(i+1,question_list[i])
    j=0
    while j<=len(option_list):
        print(j+1,option_list[i][j])
        j+=1
    user=int(input("enter the number:"))
    if user==answer_list[i]:
        print("congratulation")
    else:
        print("sorry your answer is wrong")
    i+=1





