CC=g++ # Note that this is g++ 11.2 for C++17
CFLAGS=-c -Wall
PROG=a.out

all: two_sum add_two_nums lswrc palindrome_number zigzag atoi most_water roman roman_int 3sum 4sum nth_node

two_sum: two_sum.o
	$(CC) two_sum.o -o two_sum/$(PROG)

two_sum.o: two_sum/two_sum.cpp
	$(CC) $(CFLAGS) two_sum/two_sum.cpp

add_two_nums: add_two_nums.o
	$(CC) add_two_nums.o -o add_two_nums/$(PROG)

add_two_nums.o:	lib/list_node.h add_two_nums/add_two_nums.cpp
	$(CC) $(CFLAGS) add_two_nums/add_two_nums.cpp

lswrc: lswrc/lswrc.o
	$(CC) lswrc/lswrc.o -o lswrc/$(PROG)

lswrc/lswrc.o: lswrc/lswrc.cpp
	$(CC) $(CFLAGS) lswrc/lswrc.cpp -o lswrc/lswrc.o

palindrome: palindrome_number/palindrome_number.o
	$(CC) palindrome_number/palindrome_number.o -o palindrome_number/$(PROG)

palindrome_number/palindrome_number.o: palindrome_number/palindrome_number.cpp
	$(CC) $(CFLAGS) palindrome_number/palindrome_number.cpp -o palindrome_number/palindrome_number.o

zigzag: zigzag/zigzag.o
	$(CC) zigzag/zigzag.o -o zigzag/$(PROG)

zigzag/zigzag.o: zigzag/zigzag.cpp
	$(CC) $(CFLAGS) zigzag/zigzag.cpp -o zigzag/zigzag.o

atoi: atoi/atoi.o
	$(CC) atoi/atoi.o -o atoi/$(PROG)

atoi/atoi.o: atoi/atoi.cpp
	$(CC) $(CFLAGS) atoi/atoi.cpp -o atoi/atoi.o

most_water: most_water/most_water.o
	$(CC) most_water/most_water.o -o most_water/$(PROG)

most_water/most_water.o: most_water/most_water.cpp
	$(CC) $(CFLAGS) most_water/most_water.cpp -o most_water/most_water.o

roman: int_roman/int_roman.o
	$(CC) int_roman/int_roman.o -o int_roman/$(PROG)

int_roman/int_roman.o: int_roman/int_roman.cpp
	$(CC) $(CFLAGS) int_roman/int_roman.cpp -o int_roman/int_roman.o

roman_int: roman_int/roman_int.o
	$(CC) roman_int/roman_int.o -o roman_int/$(PROG)

roman_int/roman_int.o: roman_int/roman_int.cpp
	$(CC) $(CFLAGS) roman_int/roman_int.cpp -o roman_int/roman_int.o

common_prefix: common_prefix/common_prefix.o
	$(CC) common_prefix/common_prefix.o -o common_prefix/$(PROG)

common_prefix/common_prefix.o: common_prefix/common_prefix.cpp
	$(CC) $(CFLAGS) common_prefix/common_prefix.cpp -o common_prefix/common_prefix.o

3sum: 3sum/3sum.o
	$(CC) 3sum/3sum.o -o 3sum/$(PROG)

3sum/3sum.o: 3sum/3sum.cpp
	$(CC) $(CFLAGS) 3sum/3sum.cpp -o 3sum/3sum.o

3sum_close: 3sum_closest/3sum_closest.o
	$(CC) 3sum_closest/3sum_closest.o -o 3sum_closest/$(PROG)

3sum_closest/3sum_closest.o: 3sum_closest/3sum_closest.cpp
	$(CC) $(CFLAGS) 3sum_closest/3sum_closest.cpp -o 3sum_closest/3sum_closest.o

phone: letter_phone/phone.o
	$(CC) letter_phone/phone.o -o letter_phone/$(PROG)

letter_phone/phone.o: letter_phone/phone.cpp
	$(CC) $(CFLAGS) letter_phone/phone.cpp -o letter_phone/phone.o

4sum: 4sum/4sum.o
	$(CC) 4sum/4sum.o -o 4sum/$(PROG)

4sum/4sum.o: 4sum/4sum.cpp
	$(CC) $(CFLAGS) 4sum/4sum.cpp -o 4sum/4sum.o

nth_node: nth_node/nth_node.o
	$(CC) nth_node/nth_node.o -o nth_node/$(PROG)

nth_node/nth_node.o: nth_node/nth_node.cpp lib/list_node.h
	$(CC) $(CFLAGS) nth_node/nth_node.cpp -o nth_node/nth_node.o

clean:
	rm */*.o
	rm */a.out
