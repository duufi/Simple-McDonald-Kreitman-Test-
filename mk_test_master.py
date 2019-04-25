### MK master uses polymorphism data for specified gene loci to calculate adaptation rates on the entire dataset 

import math
import csv

### function established polymorphism count, accepts data file as input 
def mk_testing(filename):
    with open(filename, "r") as csv_file:
        D_s = 0
        D_n = 0
        P_n = 0
        P_s = 0
        csv_reader = csv.reader(csv_file, delimiter='\t') 
        for line in csv_reader:
            P_n += int(str(line[1])) 
            D_s += int(str(line[6]))
            D_n += int(str(line[5]))
            P_s += int(str(line[3]))
        print("D_s =  " + str(D_s))
        print("D_n =  " + str(D_n))
        print("P_n =  " + str(P_n))
        print("P_s =  " + str(P_s))
        print("Numerator = " + str(int(D_s) * int(P_n)))
        print("Denominator = " + str(int(D_n) * int(P_s)))
        print("	α = " + str(1 - ((int(int(D_s) * int(P_n))) / (int(D_n) * int(P_s)))))


def main():
    file_name = input('Specify file to be read [case sensitive, include file extension .txt/.csv etc]:')
    mk_testing(file_name)

main()
