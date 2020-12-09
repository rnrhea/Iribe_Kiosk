import sys
import re

# file1 = open('faculty_names.txt', 'r') 
# Lines = file1.readlines() 

# html_1 = '<li> <a href="#"> <table id ="faculty"> <tr> <td class="d1">'
# #then name
# html_2 = '</td> <td class="d3"> <button onclick="selectOffice('
# html_2b = ')" style="font-size: 35px;">'  
# #then room num
# html_3 = '</button> </td> </tr> </table> </a> </li>'

# for line in Lines:
#     m = re.search('(.*) is in IRB (\d\d\d\d).', line)
#     name = m.group(1).split()
#     room = m.group(2)
#     html = html_1 + name[-1] + ", " + " ".join(name[0:-1]) + html_2 + room + html_2b + room + html_3
#     #print(html)

# for line in Lines:
#     m = re.search('(.*) is in IRB (\d\d\d\d).', line)
#     name = m.group(1).split()

#     print(*name)

file1 = open('faculty_full_name.txt', 'r') 
Lines = file1.readlines() 
names=[]
for line in Lines:
    line=line.replace('\n','')
    names.append(line)

print(names)
    

    