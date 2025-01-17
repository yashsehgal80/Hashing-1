class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap = dict()
        tMap = dict()
        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]
            if sChar in sMap:
                if sMap[sChar] != tChar:
                    return False
            else:
                sMap[sChar] = tChar
            if tChar in tMap:
                if tMap[tChar] != sChar:
                    return False
            else:
                tMap[tChar] = sChar
            
        return True
        
        
  