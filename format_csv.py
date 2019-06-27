
from collections import OrderedDict
import os,bisect
from datetime import datetime
import sys

try:

	os.system("grep -v , '1530947027582 (1).csv' > cols.txt")
except:
	pass

sys.argv[1:]
dt = sys.argv[1]
file = sys.argv[2]
#dt = str(input())
date_out =datetime.strptime(str(dt), '%Y%m%d').strftime('%Y-%m-%d')
date_list = list(str(date_out).split('-'))
date_list.append(0)
date_list.append(0)
date_list = list(map(int, date_list))
date_tuple = tuple(date_list)

def get_pos(start_date):

	start=datetime.timestamp(datetime(start_date[0],start_date[1],start_date[2], start_date[3], start_date[4]))
	start_=str(int(start))+'000'
	pos1=bisect.bisect_left(li,start_)

	end=datetime.timestamp(datetime(start_date[0],start_date[1],start_date[2]+1, start_date[3], start_date[4]))
	end_=str(int(end))+'000'
	pos2=bisect.bisect_left(li,end_)
	return pos1,pos2



def get_cols():
	cols=[]
	for i in open("cols.txt"):
		cols.append(i[:-1])
	return cols	

def initializing_hours(filename,cols):
	c=-1
	data=OrderedDict()
	
	for i in open(filename):
		line=i.split(',')
		if len(line)==1:
			
			c+=1
		
		else:
			
			if c==0:

				try:
					data[line[0]]={}
					for col in cols:

						data[line[0]][col]=None

				except Exception as e:
					print(e,"sa")

			else:
				break				
	

	newdata=OrderedDict()
	hours_sorted=sorted(data)
	li=[]
	for hrs in hours_sorted:
		newdata[hrs]=data[hrs]
		li.append(hrs)
	del data	
	
	return newdata,li	
				

def put_into_data(data,cols,filename):



	c=-1
	
	for i in open(filename):
		line=i.split(',')

		if len(line)==1:
			c+=1

		else:
			try:

				data[line[0]][cols[c]]=line[1][:-1]


			except Exception as e:
				print(e)

	return data			
cols=get_cols()


data,li=initializing_hours(file,cols)

data=put_into_data(data,cols,file)


start,end=get_pos(date_tuple)

output_filename = file.split('.')[0]
#output_filename=''.join(str(i) for i in date_tuple)
# print(output_filename)

with open(output_filename+"_out.csv","w") as file:

	Len=len(cols)
	file.write("hours,")

	Len=len(cols)-1
	for i in cols:
		file.write(i+",")
	file.write('\n')
	
	
	for rows in range(start,end):
		file.write(li[rows]+',')
		for i,col in enumerate(cols):

			if i!=Len:

				file.write(data[li[rows]][col]+',')
			else:
				file.write(data[li[rows]][col]+'\n')


				
#1529125200000
