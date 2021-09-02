try:
    fo=open('file4','r');
    print(fo)
except IOError:
    print('The file is not found')
else:
    print("Written content successfully")
