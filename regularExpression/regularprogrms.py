#regular expression....for pattern matching

#step 1
#package not in bultins.py it is in re

import re
matcher=re.finditer("ab","abababababaabbababbab")
#                         0 2 4 6 8  11 14 16 19
cnt=0
for match in matcher:
    print(match.start())
    cnt+=1
print(cnt)
    