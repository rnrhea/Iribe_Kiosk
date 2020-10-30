import sys
import re

file1 = open('faculty_names.txt', 'r') 
Lines = file1.readlines() 

html_1 = '<li> <a href="#"> <table> <tr> <td class="d1">'
#then name
html_2 = '</td> <td class="d3"> <button>'  
#then room num
html_3 = '</button> </td> </tr> </table> </a> </li>'


for line in Lines:
    m = re.search('(.*) is in IRB (\d\d\d\d).', line)
    name = m.group(1).split()
    room = m.group(2)
    html = html_1 + name[-1] + ", " + " ".join(name[0:-1]) + html_2 + room + html_3
    print(html)





    