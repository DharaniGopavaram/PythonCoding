"""
The below program shows the way to interact with packages.
This is a perfect example of how packages help us to resolve naming conflicts
"""

import Practice_Package.module1 as pack1
import com.module1 as cm
from com.dharani.module2 import f1
print('calling the f1 function in module1 file in Practice_Package')
pack1.f1()
print('calling the f1 function in module1 file in com package')
cm.f1()
print('calling the f1 function in module2 file in com/dharani package')
f1()



