import datetime
output_file_name = "file.txt"
outputFile = open(output_file_name, 'w')
lis_ = []
inputFileName = "input.txt"
inputFile = open(inputFileName, 'r')
lines = inputFile.readlines()
lis = []
format = '%Y-%m-%d %H:%M:%S'
for l in lines:
   date = datetime.datetime.strptime(l[0:19],format)
   lis.append(date)
lis.sort()

for i in range(len(lis)):
   outputFile.writelines(str(lis[i])+'\n')
outputFile.close()