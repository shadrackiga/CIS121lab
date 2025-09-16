# create by Shadrack Iga
#2. In a) If boolean is not A code will not go to the next step it will automatically move to the next if unlike b) it has to first prove that the first statement is true for it to move to the next steps

light_color =(input('Enter the light color'))
if (light_color =="red"):
    print('stop')
elif (light_color == "yellow"):
    print ('yield')
elif (light_color == "green"):
    print('go')
else:
    print("Error")

