# Lab_2: Find the number of books that can be placed on a floppy disk

# Initial data
inf_mb = 1.44
pages = 100
str_on_page = 50
chars_in_str = 25
symbol_b = 4

# Megabytes -> bytes
inf_b = inf_mb * (1024 ** 2)

# How much space does 1 book take in bytes:
book_in_b = pages * str_on_page * chars_in_str * symbol_b
# How many books will fit on a disk:
books_on_disk = inf_b // book_in_b
books_on_disk_int = int(books_on_disk) # convert result to int value

print("Количество книг, помещающихся на дискету:", books_on_disk_int)
