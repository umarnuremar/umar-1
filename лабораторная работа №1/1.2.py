2
#описание книги
pages = 100           #колво страниц
linesperpage = 50   # колво строк на странице
symbperline = 25   #колво символов в строке
bytespersymb = 4    #байты для одного символа
#одна книга в байтах
booksize_bytes = pages * linesperpage * symbperline * bytespersymb
disksize_mb = 1.44
disksize_bytes = disksize_mb * 1024 * 1024  #в байты переводим
#колво книг на дискете
numbooks = int(disksize_bytes // booksize_bytes)
print("Количество книг, помещающихся на дискету:", numbooks)

