#define which sides of a display requires for each digit
#    1
#   ---				      - - -		         - - -
#  |   |				       |	|     | |
# 2|   |3				       |	|     | |          Each digit occupies exactly
#  | 4 |				       |	|     | | 	       size + 2 columns alld 2*size + 3 rows.				
#   ---					  - - -	     - - -   - - -      
#  |   |					   |		  |	      |	   size = 3 for this example (345)					
# 5|   |6					   |	   	  |	      |
#  |   |					   |		  |	      |
#   ---				      - - -		         - - - 
#    7

lcd_value=[[1,2,3,5,6,7],[3,6],[1,3,4,5,7],[1,3,4,6,7],[2,3,4,6],[1,2,4,6,7],[1,2,4,5,6,7],[1,3,6],[1,2,3,4,5,6,7],[1,2,3,4,6,7]]
def find_codes(display_codes, digit_values):
	
	for index in range (1,8):
		display_code = []
		for digit_value in digit_values:	
			digit_lcd_value = lcd_value[int(digit_value)]
			if index in digit_lcd_value:
				display_code.append(1)
			else:
				display_code.append(0)
		display_codes.append(display_code)
	
			

def draw_horizontal_bar(index, code, digit_size):
	#print index, code
	for value in code:
		if int(value) == 1:
			print_value = '-'
		else:
			print_value = ' '
		print '',
		for i in range(digit_size):
			print '%s' % print_value,
		print ' ',

	print '\n',

def draw_vertical_bar(index, code1, code2, digit_size):
	
	for i in range(digit_size):
		for value1,value2 in zip(code1,code2):
			
			if int(value1) == 1:
				print_value1 = '|'
			else:
				print_value1 = ' '
			
			if int(value2) == 1:
				print_value2 = '|'
			else:
				print_value2 = ' '
			
			print '%s' % print_value1,
			for j in range(digit_size-1):
				print ' ',
			print '%s ' % print_value2,
			

		print '\n',



def main():
	print'\n\t\t============================='
	print '\t\t\tLCD DISPLAY'
	print'\t\t============================='
	digit_size = digit_values = -1
	

	while( digit_size !=0 and digit_values != 0):
		display_codes = []
		try:
			print 'Enter the size of the digit ( 1 to 10) followed by digits...0 0 to end\n'
			print ' > ',
			character = raw_input()
			input_values = character.split(' ')
			digit_size = int(input_values[0])
			digit_values = input_values[1]
			if digit_size !=0 and digit_values != 0: 
				find_codes(display_codes, digit_values)
				for index, code in enumerate(display_codes):
					if index + 1 == 1 or index + 1 == 4 or index + 1 == 7:
					 	draw_horizontal_bar(index, code, digit_size)
					elif index + 1 == 2 or index + 1 == 5:
					 	draw_vertical_bar(index, code, display_codes[index + 1], digit_size)
					else:
						continue
		except:
			print 'Input Error'
if __name__ == '__main__':
	main()





    