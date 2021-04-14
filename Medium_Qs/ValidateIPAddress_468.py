import re

class Solution:
    def validIPAddress(self, IP: str) -> str:
        try: 
            if "." in IP:
                strIp = IP.split(".")
                if len(strIp) != 4:  # 4 octets
                    return "Neither"
                for strI in strIp:   # 192.169.1.1
                    if len(strI) > 3:
                        return "Neither"
                    if int(strI) >=0 and int(strI) <= 255:
                        if len(strI) == 2:
                            if int(strI) < 10:
                                return "Neither"
                        if len(strI) == 3:
                            if int(strI) < 100:
                                return "Neither"
                    else:
                        return "Neither"
                return "IPv4"   # all false statements are cleared off.
            if ":" in IP:
                strIp = IP.split(":")
                if len(strIp) != 8:  # 8 octets
                    return "Neither"
                for strI in strIp:   # 2001:0db8:85a3:0000:0000:8a2e:0370:7334
                    if len(strI) > 4 or len(strI) < 1:
                        return "Neither"
                    numDec = int(strI, 16)  # converting Hex to Decimal
                    if numDec <0 and numDec > 65535:
                        return "Neither"
                return "IPv6"   # all false statements are cleared off.           
            else:
                return "Neither"
        except Exception:
            return "Neither"  # int() failed with inappropraite chars
			
			
			
			
*********************************************************************************

Optimised solution
			
class Solution:
    def validIPAddress(self, IP: str) -> str:
        def checkIPV4(IP):
            nums = IP.split('.')
            
            for num in nums:
                if len(num) == 0 or len(num)>3:
                    return "Neither"
                
                if num[0] == '0' and len(num)!= 1 or not num.isdigit()  or int(num) > 255:
                    return "Neither"
            
            return "IPv4"
        
        def checkIPV6(IP):
            nums = IP.split(':')
            hexaDecimal = "abcdefABCDEF0123456789"
            
            for num in nums:
                if len(num) == 0 or len(num)>4 or not all(c in hexaDecimal for c in num):
                    return "Neither"
                
            return "IPv6"
                
        
        
        if IP.count('.') == 3:
            return checkIPV4(IP)
        elif IP.count(':') == 7:
            return checkIPV6(IP)
        
        return "Neither"			