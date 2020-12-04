import re

data = open('../data/day4_prob1.txt').read()
data = data.split('\n\n')

valid_passports = 0
reg = re.compile('[^a-f0-9]')

for row in data:
    checks = 0
    key_value = ''
    line = row.replace('\n',' ')
    
    # For each line, check if the key is there, and if so, check if the value matches
    # the required regulations
    if line.find('byr:') != -1:
        key_value = line[line.find('byr:'):].split(' ')[0].split(':')[1]
        if int(key_value) <= 2002 and int(key_value) >= 1920:
            checks += 1

    if line.find('iyr:') != -1:
        key_value = line[line.find('iyr:'):].split(' ')[0].split(':')[1]
        if int(key_value) <= 2020 and int(key_value) >= 2010:
            checks += 1

    if line.find('eyr:') != -1:
        key_value = line[line.find('eyr:'):].split(' ')[0].split(':')[1]
        if int(key_value) <= 2030 and int(key_value) >= 2020:
            checks += 1

    if line.find('hgt:') != -1:
        key_value = line[line.find('hgt:'):].split(' ')[0].split(':')[1]
        if key_value[-2:] == 'cm':
            if int(key_value[:-2]) <= 193 and int(key_value[:-2]) >= 150:
                checks += 1
        elif key_value[-2:] == 'in':
            if int(key_value[:-2]) <= 76 and int(key_value[:-2]) >= 59:
                checks += 1

    if line.find('hcl:') != -1:
        key_value = line[line.find('hcl:'):].split(' ')[0].split(':')[1]
        if reg.search(key_value[1:]) == None and key_value[0] == '#':
            checks += 1

    if line.find('ecl:') != -1:
        key_value = line[line.find('ecl:'):].split(' ')[0].split(':')[1]
        if key_value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            checks += 1

    if line.find('pid:') != -1:
        key_value = line[line.find('pid:'):].split(' ')[0].split(':')[1]
        if len(key_value) == 9 and key_value.isnumeric():
            checks += 1

    if checks == 7:
        valid_passports += 1

print(valid_passports)
