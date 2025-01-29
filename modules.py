import os

dir_path=input("Enter the dir path : ")
file_name=input('Enter the file name : ')
file_path=os.path.join(dir_path,file_name)

try:
    if os.path.exists(dir_path):
        print('Dir already exist')
    else:
        os.mkdir(dir_path)
        print('Dir created')

    if os.path.exists(file_path):
        print('File already exist')
    else:
        with open(file_path,'a+') as file:
            file.write('Summa')

except Exception as error:
    print(error)

finally:
    print('code executed')

# os.rmdir('msd')