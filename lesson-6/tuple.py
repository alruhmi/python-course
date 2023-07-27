questions = (
        "What is the meaning of G&A?",
        "What is project G&A?",
        "How is G&A applied?",
        "Does G&A include HR",
)

answers = (
        ('a. 1', 'b. 2', 'c. 3', 'f. 5'),
        ('a. 12-07-2023', 'b. 10-07-2023', 'c. 10-07-2023', 'f. 15-07-2023'),
        ('a. g', 'b. c', 'c. f', 'f. d'),
        ('a. yes', 'b. no'),
)

currect_answers = ('a', 'f', 'c', 'b')

question_num = 0
for question in questions:
        print(f'Question {question_num+1}: {question}')
        
        for answer in answers[question_num]:
                print(answer)
            
        user_answer = input("Enter your answer: ").lower()
        
        if user_answer == currect_answers[question_num]:
                print(f'Currect! "{user_answer}" is right answer')
        else:
                print(f'Uncurrect! The right answer is "{currect_answers[question_num]}"')
                
        print('-----------------------------\n')
        
        question_num += 1
        