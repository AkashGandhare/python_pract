
work_hours_list = [('Abbey', 400), ('Jose', 300), ('Shane',900), ('Jane',100)]
tup =();

def month_employee(workList):
	employee_name = ''
	max_hours = 0	

	for name,work_hours in work_hours_list:
		if work_hours > max_hours:
			max_hours = work_hours
			employee_name = name
		else:
			pass
	
	return(employee_name,max_hours)


tup = month_employee(work_hours_list)
employee, hours = month_employee(work_hours_list)
print(employee)
print(hours)
print(tup)
