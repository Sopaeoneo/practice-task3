import re
filename = (r"\cyrillic_unicode.txt")
infile = open('text_for_task.txt', 'r')
lines = infile.readlines()
result = ''
for i in lines:
    if re.match(r"^(\w{4,5})(\s)(.*)$", i):
        i = re.sub(r"^(\w{4,5})(\s)(.*)$", r"\\x{\1}", i)
        result += i.strip()
    if re.match(r"^(\w{4,5})(..)(\w{4,5})(.*)$", i):
        i = re.sub(r"^(\w{4,5})(..)(\w{4,5})(.*)$", r"\\x{\1}-\\x{\3}", i)
        result += i.strip()
result = re.sub(r'(.+)', r"[\1]", result)
print(result) 