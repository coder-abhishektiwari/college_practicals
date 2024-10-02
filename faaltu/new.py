read_file = open('faaltu/read.txt', 'r')
write_file = open('faaltu/write.html', '+w')


html_code = read_file.read()  #reading read.txt file and saving into a variable
write_file.write(html_code)   #write saved variable content into write.html file


write_file.close()
read_file.close()