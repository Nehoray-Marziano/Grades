from plumbum.cmd import sort, wc, uniq, sed, awk

def print_num_of_students():
    print((awk['{print $1}', 'lab10 _grades']| wc["-l"]()))

def print_list_of_students():
    print(awk['{print $1}','lab10_grades'])
	
def print_error_list():
	print ((awk['{print $2}', 'lab10_grades'] | 
                awk['{split($0,a,"|"); for (i=1;i<=NR;i++) print a[i]}'] |
                awk['-F', ':', '{print $1}'] |
                sed['/^$/d'] |
                sort|
                uniq['-c'] |
                sed ['s/^[ \t]*//;s/[ \t]*$//'])())
                    
def print_error_count():
    print ((awk['{print $2}', 'lab10_grades'] | 
                awk['{split($0,a,"|"); for (i=1;i<=NR;i++) print a[i]}'] |
                awk['-F', ':', '{print $1}'] |
                sed['/^$/d'] |
                sort|
                uniq['-c'] |
                sed ['s/^[ \t]*//;s/[ \t]*$//'] |
                wc["-l"])())

	
if __name__ == '__main__':
    print_list_of_students()
    print_num_of_students
    print_error_list()
    print_error_count()
