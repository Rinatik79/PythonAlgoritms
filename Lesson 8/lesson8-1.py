import hashlib
s = "papa u vasi silen v matematike"
list = []
#hush_obj1 = hashlib.sha1(s.encode('utf-8')).hexdigest()

counter = -1

for i in range(len(s)):

    for j in range(i, len(s) + 1):
        current_substring = s[i:j]
        current_hash_obj = hashlib.md5(current_substring.encode('utf-8')).hexdigest()
        if list.count(current_hash_obj) == 0:
            list.append(current_hash_obj)
            counter += 1
            print("'" + s[i:j] + "'")


print("We have " + str(counter) + " substrings totally.")
