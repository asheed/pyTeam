import re

num_list = range(1,500)

for num in num_list:
    s = re.search("[3|6|9]", str(num))
    if s is None:
        print num + ' '
