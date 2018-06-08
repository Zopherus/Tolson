import sys

class CString:
    def __init__(self, value, last):
        self.value = value
        self.last = last

    def __eq__(self, other):
        if other == None:
            return False
        s1 = self.value
        s2 = other.value
        if len(s1) != len(s2):
            return False
        s = s1 + s1
        val = s2 in s
        return val

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return sum(map(lambda c: int(c), self.value))

    def __len__(self):
        return len(self.value)

    def __getitem__(self, item):
        return self.value.__getitem__(item)

    def __str__(self):
        return self.value

    def count(self, val):
        return self.value.count(val)

    def replace(self, s1, s2):
        return self.value.replace(s1, s2)

def trans(s):
    length = len(s)
    l = set()

    #rule 4
    for i in range(length - 2):
        if s[i] == s[i + 2] and abs(int(s[i]) - int(s[i + 1])) == 1:
            l.add(s[0:i] + s[i + 1] + s[i] + s[i + 1] + s[i + 3:])

    if length >= 3:
        if s[length - 2] == s[0] and abs(int(s[0]) - int(s[length - 1])) == 1:
            l.add(s[length - 1] + s[1:length - 2] + s[length - 1] + s[0])

        if s[length - 1] == s[1] and abs(int(s[0]) - int(s[1])) == 1:
            l.add(s[1] + s[0] + s[2:length - 1] + s[0])


    #rule 3
    for i in range(length - 1):
        if abs(int(s[i]) - int(s[i + 1])) > 1:
            l.add(s[0:i] + s[i + 1] + s[i] + s[i + 2:])

    if length >= 2:
        if abs(int(s[0]) - int(s[length - 1])) > 1:
            l.add(s[length - 1] + s[1: length - 1] + s[0])

    #rule 1
    for i in range(length - 1):
        if s[i] == s[i + 1]:
            l.add(s[0:i] + s[i+2:])
    if length >= 2 and s[0] == s[length - 1]:
        l.add(s[1:length - 1])

    #rule 2
    minNum = 10
    minCount = 0
    maxNum = 0
    maxCount = 0
    for i in s:
        num = int(i)
        if num > maxNum:
            maxNum = num
            maxCount = 1
        elif num == maxNum:
            maxCount += 1
        elif num == minNum:
            minCount += 1
        elif num < minNum:
            minNum = num
            minCount = 1

    if minCount == 1:
        l.add(s.replace(str(minNum), ""))

    if maxCount == 1:
        l.add(s.replace(str(maxNum), ""))

    return list(map(lambda st: CString(st, s), l))

visited = set()

def reach(s1, s2):
    if s1 == s2:
        return True
    stack = [s1]
    visited.add(s1)
    while stack:
        sRot = stack.pop()
        for s in trans(sRot):
            if s == s2:
                while s.last != None:
                    print(s.last)
                    s = s.last
                return True
            if (not s in visited) and (len(s) >= len(s2)):
                stack.append(s)
                visited.add(s)
    return False

#s1, s2 = str(sys.argv[1]), str(sys.argv[2])
#sys.setrecursionlimit(2000)

print(reach(CString("123123123123123", None) , CString("222222222", None)))
