### MK calculation of alpha for genes with frequencies > .5 within the given population

import csv

### create initial variables, separate frequencies, test for above desired threshold
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
                # working with particular dataset in strings, could have converted to numeric, and used a single if statement (if value > .5)
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










