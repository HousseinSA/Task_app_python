# import glob
# glob_files= glob.glob('files/*.txt')
# for file in glob_files:
#     with open(file, 'r') as local_file:
#         print(local_file.read())

# import csv
# with open('files/weather.csv','r') as file_local:
#     csv_file =list(csv.reader(file_local))
# city_name = input('please enter the city name: ')
# for item in csv_file:
#     if item[0] == city_name:
#        temperature = item[1]
#        print(int(temperature))
#
#
# import webbrowser
# user_term = input('Enter a search term: ')
# webbrowser.open(f'https://google.com/search?q={user_term}')

import shutil
zip =  shutil.make_archive('neji','zip', 'files')
print(zip)