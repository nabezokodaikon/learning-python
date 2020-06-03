from report import get_description as do_it

description = do_it()
print("Today's weather:", description)

import sys
for place in sys.path:
    print(place)
