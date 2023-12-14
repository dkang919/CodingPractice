class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        sheet = ""

        for let in magazine:
            if let in ransomNote:
                ransomNote = ransomNote.replace(let,"",1)
        
        return ransomNote == ""