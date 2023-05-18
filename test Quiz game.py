print("wrong spelling considered as a wrong answered")
question_no = 0
score = 0
play = input("do you want to play game yes or no:- ").lower()
if play == 'yes':
    question_no += 1
    ques = input(f'\n{question_no}.what is full form of CPU? ').lower()
    if ques == 'central processing unit':
        score += 1
        print("you got 1 point as reward")
        
    else:
        print('incorrect! the correct answered is ')
        print('central processsing unit')
# question 2
    question_no += 1
    ques = input(f'\n{question_no}.what is full form of GPU? ').lower()
        
    if ques == 'graphics processing unit':
        score += 1
        print('you got 1 point as reward')
    else:
        print('incorrect! the correct answered is') 
        print('graphics processing unit')
#question 3
    question_no += 1
    ques = input(f'\n{question_no}.what is full form of RAM? ').lower()
    if ques == 'random access memory':
        score += 1
        print('you got 1 point as reward')
    else:
        print('incorrect! the correct answer is') 
        print('random access memory')
else:
    print('thank you. game is over')
    quit()
print(f'\n the number of question is {question_no}')
print(f'\n the score is {score}')
try:
    percentage = (score*100)/question_no
except ZeroDivisionError:
    print('0% answer is correct') 

print(f'\n {percentage}%.answered is correct ')           

                     
        
            







