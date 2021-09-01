Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #2
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a=20;
>>> a+=30;
>>> a%=3;
>>> a
2
>>> True * False
0
>>> True & False
False
>>> True and False
False
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False is 'False'
False
>>> ((True == False) or (False > True)) and (False <= True)
False
>>> 
>>> 
>>> #3
>>> s1 = "Nice to have it"
>>> s2 = "here"
>>> s1+s2
'Nice to have ithere'
>>> s1 = "Nice to have it "
>>> s1+s2
'Nice to have it here'
>>> 
>>> 
>>> #3
>>> #4
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
>>> a[3][1][2][0]
'hello'
>>> 
>>> #5
>>> a.insert(0, "s1")
>>> a
['s1', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
>>> a.insert(0, s1)
>>> a
['Nice to have it ', 's1', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
>>> a.append(s2)
>>> a
['Nice to have it ', 's1', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> 
>>> 
>>> 
>>> #6
>>> numbers = [386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,