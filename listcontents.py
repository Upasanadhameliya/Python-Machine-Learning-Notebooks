import os

# Get current directory file path
current_directory = os.getcwd()

# List the contents of the 
for *_, files in os.walk(current_directory):
	data = "\n".join(files)
	out_file_name = f"{os.path.split(current_directory)[1]}_files_list.txt"
	with open(out_file_name,'w',encoding='utf-8') as f:
		f.write(data)
	break
