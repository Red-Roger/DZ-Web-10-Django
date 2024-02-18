import os

path_html = os.getcwd() + '\\Web_2_10_2\\quotes\\quoteapp\\templates\\quoteapp\\main.html'
path_start = os.getcwd() + '\\Web_2_10_2\\quotes\\quoteapp\\start_page'
path_end = os.getcwd() + '\\Web_2_10_2\\quotes\\quoteapp\\end_page'

def imp_html():

    with open(path_start, 'r') as file1:
        data1 = file1.read()
        print (data1)
    with open(path_end, 'r') as file2:
        data2 = file2.read()
    data3 = data1+data2
    with open(path_html, 'w') as file3:
        file3.write(data3)