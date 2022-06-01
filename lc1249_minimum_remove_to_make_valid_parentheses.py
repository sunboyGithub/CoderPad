class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''05/03/22 Time: O(N), Space: O(N)'''
        parent_stack = []
        parent_index = []
        for i in range(len(s)):
            char = s[i]
            if char != '(' and char != ')':
                continue
            elif char == '(':
                parent_stack.append('C')
                parent_index.append(i)
            else:
                if len(parent_stack) == 0 or parent_stack[-1] == ')':
                    parent_stack.append(')')
                    parent_index.append(i)
                else:
                    parent_stack.pop()
                    parent_index.pop()
        ## backwards
        for i in range(len(parent_index)-1, -1, -1):
            index = parent_index[i]
            s = s[:index] + s[index+1:]
        return s

test = Solution()
print(test.minRemoveToMakeValid("lee(t(c)o)de)"))