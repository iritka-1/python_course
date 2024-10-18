# TODO Найдите количество книг, которое можно разместить на дискете
disket_bite=1.44*1024*1024
symbols_in_book=100*50*25
bite_per_book=symbols_in_book*4







print("Количество книг, помещающихся на дискету:", int(disket_bite//bite_per_book))
