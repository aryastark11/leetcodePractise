class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 0:
            dupList = []
            closeStr = { '(':')', '{':'}', '[':']' }
            key_list = list(closeStr.keys())
            val_list = list(closeStr.values())
            for i in range(0, len(s)):
                if s[i] not in val_list:
                    dupList.append(s[i])
                else:
                    # get the key associated with the close brace.
                    if dupList: # there is a openBrace for this closeBrace
                        openBrace = key_list[val_list.index(s[i])]
                        if dupList[-1] == openBrace:
                            dupList.pop()
                        else:  # the last added brace is not its openBrace
                            return False
                    else: # there is no openBrace for this closeBrace
                        return False
            if not dupList:
                return True
        return False
                
                
                
            
            
        
