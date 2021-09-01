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
>>> numbers = [386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,599,826,248,866,950,248,866,950,626,950,626,949,687,217,815,67,104,58,512,24,892,894,767,553,81,379,483,831,445,742,717,958,743,527]
>>> numbers
[386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 599, 826, 248, 866, 950, 248, 866, 950, 626, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 483, 831, 445, 742, 717, 958, 743, 527]
>>> 
============================================================= RESTART: C:/Users/user/Desktop/assigment.py =============================================================
Traceback (most recent call last):
  File "C:/Users/user/Desktop/assigment.py", line 3, in <module>
    if x==237:
NameError: name 'x' is not defined
>>> 
============================================================= RESTART: C:/Users/user/Desktop/assigment.py =============================================================
386
462
418
344
236
566
978
328
162
758
918
237
>>> 
>>> 
>>> 
>>> #7
>>> 
============================================================= RESTART: C:/Users/user/Desktop/assigment.py =============================================================
386
Traceback (most recent call last):
  File "C:/Users/user/Desktop/assigment.py", line 13, in <module>
    print(color_list_1,difference(color_list_2))
NameError: name 'difference' is not defined
>>> 
============================================================= RESTART: C:/Users/user/Desktop/assigment.py =============================================================
386
Traceback (most recent call last):
  File "C:/Users/user/Desktop/assigment.py", line 14, in <module>
    print(color_list_1,difference(color_list_2))
NameError: name 'difference' is not defined
>>> 
============================================================= RESTART: C:/Users/user/Desktop/assigment.py =============================================================

============================================================= RESTART: C:/Users/user/Desktop/assigment.py =============================================================
{'white', 'black'}
>>> 

>>> #9
>>> 
>>> 