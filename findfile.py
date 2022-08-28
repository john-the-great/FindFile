import os

def search(file_data, dir):
    try:
        files = os.listdir(dir)
        for file_name in files:
            if not '.' in file_name and not file_name == 'OneDrive':
                #open folder and search
                new_dir = dir + f'{file_name}/'
                file_data['found_file'] = search(file_data, new_dir)
            elif file_name == file_data['files']['ffile_name']:
                new_dir = dir + f'{file_name}'
                print(f'Found File!\ndir: {new_dir}')
                file_data['found_file'] = True
                return file_data['found_file']
            else:
                continue
    except: pass
    return file_data['found_file']

def menu():
    user_input = str(input('{dir//} {file name (with ext)}: '))
    user_input = user_input.split()
    drive = user_input[0]
    file_name = user_input[1]
    file_data = {
        'drive':drive, 'files':{
                'ffile_name':file_name},
        'found_file':False
        }
    found_file = search(file_data, file_data['drive'])
    if not found_file:
        print('Could not find file.\nTry retyping the file name.')

while 1:
    menu()