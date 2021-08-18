import hashlib
s = "papa u vasi silen v matematike"
#hush_obj1 = hashlib.sha1(s.encode('utf-8')).hexdigest()

counter = 0

for i in range(len(s)):

    for j in range(i, len(s) + 1):
        current_substring = s[i:j]
        current_hash_obj = hashlib.md5(current_substring.encode('utf-8')).hexdigest()

        if hashlib.md5(s[i:j].encode('utf-8')).hexdigest() == current_hash_obj and current_substring !="":
            counter += 1

print("We have " + str(counter - 1) + " substrings totally.")
