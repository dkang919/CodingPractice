class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        s_ = s.replace("-","").upper()
        key = ""
        piece = ""

        for i in range(len(s_)-1, -1, -1):
            
            if len(piece) != k:
                piece = s_[i] + piece 
            
            else:
                key = piece + "-" + key
                piece = s_[i]

        if piece != "":
            key = piece + "-" + key

        return key[:-1]


----------------------------------------------------------

class Solution:
  def licenseKeyFormatting(self, s: str, k: int) -> str:
    key = s.replace("-", "").upper()
    
    formatted = []
    i = len(key)-k
    while i >= 0:
        formatted.append(key[i:i+k])
        i -= k
        
    if i != -k:
        formatted.append(key[:i + k])
        
    formatted = formatted[::-1]
    
    return "-".join(formatted)
        