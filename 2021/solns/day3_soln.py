# Advent of Code Day 3

# Imports
import numpy as np

# Get data
report = np.loadtxt('../data/day3_data.txt', dtype=str)

# Intialize counter array
gam_count = [0]*len(report[0])

# Scan each string and increment/decrement counter array as appropriate
for entry in report:
    for i, bit in enumerate(entry):
        if int(bit) == 1:
            gam_count[i] = gam_count[i] + 1 # Increment if 1
        else:
            gam_count[i] = gam_count[i] - 1 # Decrement if 0

# Based on parity of each element, transform gam_count into binary number
gam = [0]*len(gam_count)
for i in range(len(gam_count)):
    if (gam_count[i]) >= 0: # 1 most common bit
        gam[i] = 1
    else: # 0 most common bit
        gam[i] = 0

# Generate epsilon based on complement of gamma:
eps = [0]*len(gam)
for i in range(len(gam)):
    eps[i] = int(not gam[i])

# Transform from binary to decimal
gam_dec = 0
eps_dec = 0
for i in range(len(gam)):
    gam_dec = gam_dec + gam[-1-i]*2**i
    eps_dec = eps_dec + eps[-1-i]*2**i

# Get product and print
print(gam_dec * eps_dec)

##### PART 2 #####

# Start with all indices valid
idc = np.arange(len(report))
ido = np.arange(len(report))

# Initialize placeholders for winning numbers
cnum = 0
onum = 0

# Scan entries for most common bits
for i in range(len(report[0])):
    gam_count = 0
    # Get most frequent value
    for j in ido:
        if int(report[j][i]) == 1:
            gam_count = gam_count + 1
        else:
            gam_count = gam_count - 1
    # Assign most bits according to rules
    if gam_count >= 0:
        gam = 1
    else:
        gam = 0
    # Remove all noncompliant indices:
    for j in range(len(report)):
        if int(report[j][i]) != gam:
            ido = ido[ido != j]
    if len(ido) == 1:
        onum = int(report[ido])
        break

# Scan entries for least common bits
for i in range(len(report[0])):
    eps_count = 0
    # Get most frequent value
    for j in idc:
        if int(report[j][i]) == 1:
            eps_count = eps_count + 1
        else:
            eps_count = eps_count - 1
    # Assign least bits according to rules
    if eps_count >= 0:
        eps = 0
    else:
        eps = 1
    # Remove all noncompliant indices:
    for j in range(len(report)):
        if int(report[j][i]) != eps:
            idc = idc[idc != j]
    if len(idc) == 1:
        cnum = int(report[idc])
        break

# Convert to decimal
onum = int(str(onum), 2)
cnum = int(str(cnum), 2)

# Print life support number
print(onum*cnum)
