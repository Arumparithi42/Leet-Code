class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        if (len(s) != len(t)):
            return False
        for i in range(0,len(s)):
            dic1.update({s[i]: dic1.get(s[i])+1 if dic1.get(s[i])!=None else 0})
            dic2.update({t[i]: dic2.get(t[i])+1 if dic2.get(t[i])!=None else 0})
        return (dic1 == dic2)
