import re
def canUpdate(newUsername, curUsername, isChanged, users):
	newUsername = newUsername.lower()
	not_allowed = [c for c in re.split('[a-z0-9_]+',newUsername,flags=re.IGNORECASE) if c != '']
	if not_allowed == []:
		curUsername = curUsername.lower()
		users = [user.lower() for user in users]
		if newUsername not in users and curUsername in users and not isChanged:
			return True
		elif newUsername == curUsername and curUsername in users:
			return True

	return False
print canUpdate('Aaron', 'aaron', False, ['aaron','Cymor','NEMENO'])

print canUpdate('Aaron', 'aaron', False, ['Snake','the_boss','NEMENO'])