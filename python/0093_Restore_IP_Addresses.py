class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        result = []
        path = [0] * 4

        def dfs(i, j, ip_val):

            if i == n:

                if j == 4:
                    a, b, c, _ = path
                    result.append(f"{s[:a]}.{s[a:b]}.{s[b:c]}.{s[c:]}")
                
                return
            
            if j == 4:
                return
            
            ip_val = ip_val * 10 + int(s[i])

            if ip_val > 255:
                return
            
            if ip_val > 0:
                dfs(i + 1, j, ip_val)
            
            path[j] = i + 1
            dfs(i + 1, j + 1, 0)
        
        dfs(0, 0, 0)

        return result
