class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # Split the queryIP
        # Check list contain 4 items -> IPV4 -> Validate a list of item of IPV4
        # Chekc list contain 8 items -> IPV6 -> Validate a list of item of IPV6
        ipV4List = queryIP.split('.')
        if len(ipV4List) == 4:
            for item in ipV4List:
                try:
                    value = int(item)
                except ValueError:
                    return "Neither"
                
                if item == "0":
                    continue
                
                if value < 0 or value > 255 or item.startswith("0"):
                    return "Neither"
            return "IPv4"


        ipV6List = queryIP.split(':')
        if len(ipV6List) == 8:
            for item in ipV6List:
                if len(item) == 0 or len(item) > 4:
                    return "Neither"
                try:
                    value = int(item, 16)
                except ValueError:
                    return "Neither"
                if value < 0 or value > 0xFFFF:
                    return "Neither"
            return "IPv6"

        return "Neither"



        