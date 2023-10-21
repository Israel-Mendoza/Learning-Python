my_list = [1,2,3,3,0,4,3,3,3]

end_list = []

result = False

for num in my_list:
	if num == 3 and not end_list:
		end_list.append(num)
	elif num == 3 and len(end_list) == 1:
		end_list.append(num)
	elif num == 0 and len(end_list) == 2:
		result = True
	else:
		end_list == []

print(result)