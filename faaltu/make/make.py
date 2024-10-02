global num
for i in range(10): 
    num = i
    file = open('file_name'+ num,'w')
    file.write("helo world")

file.close()
