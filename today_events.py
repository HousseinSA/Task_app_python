today =input('hello, please enter the date here \n')
mood= input('rate your mood for today from 1 to 10\n')
discreption_of_the_day = input('how was your day? \n')
with open(f'events_of_the-day/{today}.txt','w') as file:
    file.writelines(f'rating-of-mood: {mood}\n description:{discreption_of_the_day} \n')

