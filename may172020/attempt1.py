# Implement an autocomplete system. That is, given a query string s 
# and a set of all possible query strings, return all strings in the set 
# that have s as a prefix.

# For example, given the query string de 
# and the set of strings [dog, deer, deal], return [deer, deal].


def autoComplete(s, possible):
	length = len(s)
	allowed = []
	for string in possible:
		if s == string[:length]:
			allowed.append(string)
	return allowed

assert autoComplete("de", ["dog", "deer", "deal"]) == ["deer", "deal"]
assert autoComplete("al", ["allowed", "allowance", "helpful", "wrong", 
					"test", "altercation", "champ", "alternate"]) == ["allowed", "allowance", "altercation", "alternate"]