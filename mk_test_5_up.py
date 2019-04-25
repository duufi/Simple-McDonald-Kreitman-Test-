### MK calculation of alpha for genes with frequencies > .5 within the population
### 3-21-19, for Enard Lab, MKData2017.txt for data

import csv

### create initial variables, separate frequencies, test for above desired
def calculation(file_name):
    with open(file_name, "r") as csv_file:
        D_s = 0
        D_n = 0
        P_n = 0
        P_s = 0
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for line in csv_reader:
            line_spaced = (line[2].split(","))
            for i in line_spaced:
            # could set a variable count then run through i = integer input then subtract input to get frequency range
                if i != "" and (i.find (".5") >= 1 or i.find (".6") >= 1 or i.find('.7') >= 1 or i.find('.8') >= 1 or i.find('.9') >= 1):
                    P_n += 1
            line_spaced2 = (line[4].split(','))
            for i in line_spaced2:
                if i != "" and (i.find(".5") >= 1 or i.find(".6") >= 1 or i.find('.7') >= 1 or i.find('.8') >= 1 or i.find('.9') >= 1):
                    P_s += 1
            D_s += int(line[6])
            D_n += int(line[5])
        print("P_n: " + str(P_n), "P_s: " + str(P_s),"D_s: " + str(D_s),"D_n: " +  str(D_n))
        print("	α = " + str(1 - (P_n * D_s) / (D_n * P_s)))

def main():
    file_in = input("Specify file to be read [case sensitive, include file extension .txt/.csv etc]: ")
    calculation(file_in)

main()


### does not suggest that there is more positive selection within the plasmodium interacting proteins as opposed to thte entire human proteome
### however, it is good to show that there is at east some selection
### test poly DFE

### not much directional selection
### balancing selection, could not have been intereacting for that much time
### could test for the expression levels in the PIPs, compare the levels of expression between the Northern European population, compare it to the African Pop
### poly DFE for the difference, suggest what could be done to find out more
### kstart to think about the hyppotheses that could potentially explain



### when comparing the GO ontologies, you would want to take one of the categories then compare it to the rest of the genome, or
### you would want to ensure that the GC content is the same, the length is the same, but they are not in the same family or in the same functionality


"""        ### added to ensure the correct values are obtained for non frequency specified traits (total calculated correctly)
        if count1 > 0 and count2 > 0:
            D_s += int(line[6])
            D_n += int(line[5])
        elif count1 > 0 and count2 <= 0:
            D_s += int(line[6])
            D_n += int(line[5])
        elif count1 <= 0 and count2 > 0:
            D_s += int(line[6])
            D_n += int(line[5])
        else:
            continue
"""
### variable output and alpha calculation
#print("P_n = " + str(P_n))
#print("P_s = " + str(P_s))
#print("D_s = " + str(D_s))
#print("D_n = " + str(D_n))
#num = int(P_n * D_s)
#den = int(P_s * D_n)
#print(1-(num/den))

#alpha = (1 - ((int(P_n) * int(D_s)) / (int(P_s) * int(D_n))))
#print(str(alpha))







