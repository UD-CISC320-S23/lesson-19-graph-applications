####we need a function to sort our data in the json file
searchtext=","
replace="\n"
with open('data.txt','r') as text_file:
    data=text_file.read()
    data=data.replace(searchtext,replace)

with open('data.txt','w') as text_file:
    text_file.write(data)

## we need to sort by hierarchy of pages 
##we can do this by amount of slashes in the url


main_pages=[]
secondary_pages=[]
third=[]
fourth=[]
fifth=[]
with open('data.txt') as text_file:
    for line in text_file:
        if line.count("/") ==3:
            main_pages.append(line)
        if line.count("/") ==4:
            secondary_pages.append(line)
        if line.count("/") ==5:
            third.append(line)
        if line.count("/") ==6:
            fourth.append(line)
        if line.count("/") ==7:
            fifth.append(line)
with open('orderedPages.txt','a') as new_text:
    for i in main_pages:
        new_text.write(i)
        new_text.write("\n")
    for i in secondary_pages:
        new_text.write(i)
        new_text.write("\n")
    for i in third:
        new_text.write(i)
        new_text.write("\n")
    for i in fourth:
        new_text.write(i)
        new_text.write("\n")

    






