infile = open("C:/Users/Aravind S/Desktop/DSAL/week-5/lecture-pgms/input.txt", "r")
outfile = open("C:/Users/Aravind S/Desktop/DSAL/week-5/lecture-pgms/output.txt", "w")

# contents = infile.readlines()
# for i in contents:
#     outfile.write(i)

outfile.writelines(infile.readlines())

infile.close()
outfile.close()