content = ['houssein loves liverpool', 'neji is the best caracter of all motherfucking time','houssein will be the greatest software enginerier ever.']
filenames =['presentation.txt','information.txt', 'icespice_pussy.txt']
for cont, filename in zip(content, filenames):
   file = open(f'files/{filename}','w')
   file.write(cont)
