import numpy as np
from IPython import embed

data = open('../data/day4_prob1.txt').read()
data = data.split('\n\n')

valid_passports = 0

for line in data:
    checks = 0
    
    if line.find('byr:') != -1:
        checks += 1
    if line.find('iyr:') != -1:
        checks += 1
    if line.find('eyr:') != -1:
        checks += 1
    if line.find('hgt:') != -1:
        checks += 1
    if line.find('hcl:') != -1:
        checks += 1
    if line.find('ecl:') != -1:
        checks += 1
    if line.find('pid:') != -1:
        checks += 1
    if checks == 7:
        valid_passports += 1

print(valid_passports)
