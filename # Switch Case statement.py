# Switch Case statement

from typing import *
import math
def areaSwitchCase(ch: int, a: List[float]):
    # Write your code here
    if ch==1:
        r=a[0]
        return format(math.pi*r*r, ".5f")
    elif ch==2:
        return format(a[0]*a[1], ".5f")
    pass