# my solution - re assigning two strings to unique number representation and compare if the images match

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(set(s)) != len(set(t)):
            return False
        
        s_ = {}
        t_ = {}
        c1,c2 = 1,1

        smap = ""
        tmap = ""

        for sitem in s:
            if sitem not in s_:
                s_[sitem] = str(c1)
                c1 += 1
                smap += str(c1)

            else:
                smap += s_[sitem]
            
        for titem in t:
            if titem not in t_:
                t_[titem] = str(c2)
                c2 += 1
                tmap += str(c2)

            else:
                tmap += t_[titem]

        return smap == tmap


# best runtime solution 

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        zipped = set(zip(s, t))
        return len(zipped)==len(set(s))== len(set(t))


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        zipped = set(zip(s, t))
        if len(zipped)==len(set(s))== len(set(t)):
            return True
        else:
            return False
        

# very interesting to see the runtime and memory difference by using if-else statement vs return 
# if-else makes it faster , assuming that if statement checks if any condition fails or not
# where as, the return method needs to execute entire line before returning value