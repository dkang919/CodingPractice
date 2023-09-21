class Solution:
    def isValid(self, s: str) -> bool:
        
        stack_room = ""


        for item in s:
            if (item == "(") or (item == "{") or (item == "["):
                stack_room += item

            elif stack_room != "":
                if (item == ")"):
                    if stack_room[-1] == "(":
                        stack_room = stack_room[:-1]
                    else:
                        return False

                elif (item == "}"):
                    if stack_room[-1] == "{":
                        stack_room = stack_room[:-1]
                    else:
                        return False

                elif (item == "]"):
                    if stack_room[-1] == "[":
                        stack_room = stack_room[:-1]
                    else:
                        return False

            else:
                return False

        if stack_room != "":
            return False

        return True
