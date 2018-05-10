#coding=utf-8
edward = ['Edward Gumby',42]
john = ['John Smith',50]
database = [edward,john]
print database

greeting = 'Hello World!'
print greeting[0]
print greeting[0:-1]
print greeting[1:2]
print greeting[0:3]
print greeting[:3]
print greeting[:]
print greeting[0:-1:2]
print greeting[::2]
print greeting[::-2]
num = list('12345678910')
print num[:]
print num[5::-2]
print num[:5:-2]
string = num + list('greeting')
print string
print 'sadf'*2

print 'H' in greeting
print 'h' in greeting

database = [
    ['xxx','123'],
    ['aaa','234']
]

# username = raw_input('User name:')
# PIN = raw_input('PIN code :')
#
# if [username,PIN] in database : print 'Access granted'
# else : print 'ssssss'
# list add data
list=list("adfjadlf");
# list.append("asdf");
print(list);

num=list.count("a");
print(num)
list.reverse()    #reverse
print(list)
list.sort() #sort
print list


print("---------------------------------")
xxx=[1,678,23,879,345,546,2,67,3]
xxx.sort()
print xxx
