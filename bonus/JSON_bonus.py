import json
with open('questions.json', 'r') as file:
    data = file.read()
questions = json.loads(data)
correct_answer = ""
correct_answer_count = 0
options =[]
total_count =f"your score is {correct_answer_count}/{len(questions)}"
for question in questions:
    print(question['question'])
    correct_answer = question['correct_answer']
    try:
        for index,option in enumerate(question['options']):
            print(f'{index+1} - {option}')
            options = question['options']
        answer =(input('Enter the number of the correct answer: '))
        option_selected = options[int(answer)-1] or answer
        question['user_answer'] = answer
        if correct_answer == option_selected:
            print(f'{option_selected} is the right answer.')
            correct_answer_count = correct_answer_count + 1
        else:
            print(f'{option_selected} is wrong.')
    except IndexError:
        print('invalid index or data type.')
        continue
print(questions)
print('i love liverpool')
print(f'{correct_answer_count}/{len(questions)}')