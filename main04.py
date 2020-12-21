import string

###### PART 1 ######

REQUIRED = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def main():
	with open("data04.txt", "r") as f:
		c = 0
		r = f.readline()
		details = r
		while r != "":
			r = f.readline()
			details += r

			if r == "\n":
				passport = dict()
				fields = details.split()

				for field in fields:
					n = field.split(":")
					passport[n[0]] = n[1]

				if(all(x in passport for x in REQUIRED)):

					cond = check(
						passport['byr'],
						passport['iyr'],
						passport['eyr'],
						passport['hgt'],
						passport['hcl'],
						passport['ecl'],
						passport['pid']
						)

					if cond == True:
						c += 1

				#print(passport)
				details = ""
				continue

	print(c)


###### PART 2 ######

def check(byr, iyr, eyr, hgt, hcl, ecl, pid):
	c = 0
	if len(byr) == 4 and (int(byr) >= 1920 and int(byr) <= 2002):
		c += 1
	
	if len(iyr) == 4 and (int(iyr) >= 2010 and int(iyr) <= 2020):
		c += 1
	if len(eyr) == 4 and (int(eyr) >= 2020 and int(eyr) <= 2030):
		c += 1
	
	if hgt[-2:] == "cm":
		if int(hgt[:-2]) >= 150 and int(hgt[:-2]) <= 193:
			c += 1
	elif hgt[-2:] == "in":
		if int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76:
			c += 1
	else:
		return False
	
	if hcl[0] == "#":
		hcl = hcl[1:]
		hex = all(c in string.hexdigits for c in hcl)
		if hex == True:
			c += 1
	
	
	eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	if ecl in eye_colors:
		c += 1
	
	if len(pid) == 9:
		c += 1

	if c == 7:
		return True


main()