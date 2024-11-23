file_1 = open("КурсинАндрейАнатольевич_У-244_vvod.txt", "r")
file_2 = open("КурсинАндрейАнатольевич_У-244_vivod.txt", "w")
file_2.write(file_1.read())