import collections


class Solution:
    def calcEquations(self, equations, values, queries):
        ## build pre_posts hashmap and pre_post_value hashmap
        pre_post = collections.defaultdict(list)
        pre_post_value = {}
        for i, [pre, post] in enumerate(equations):
            pre_post[pre].append(post)
            pre_post[post].append(pre)
            pre_post_value[(pre, post)] = values[i]
            pre_post_value[(post, pre)] = 1 / values[i]
        res = [-1] * len(queries)
        for i, [pre, post] in enumerate(queries):
            # print('enumerate:', i, pre, post)
            # found, value = self.dfs(pre_post, pre_post_value, pre, post)
            # if found: res[i] = value
            if (pre, post) in pre_post_value:
                res[i] = pre_post_value[(pre, post)]
            else:
                visited = set()
                visited.add((pre, post))
                res[i] = self.dfs(pre_post, pre_post_value, pre, post, visited)
        return res

    def dfs(self, pre_post, pre_post_value, pre, post, visited):
        if pre not in pre_post or post not in pre_post:
            return -1
        if (pre, post) in pre_post_value:
            return pre_post_value[(pre, post)]
        for cur_post in pre_post[pre]:
            pre_cur_post_value = pre_post_value[(pre, cur_post)]
            if (cur_post, post) in pre_post_value:
                return pre_cur_post_value * pre_post_value[(cur_post, post)]
            else:
                if (cur_post, post) in visited:
                    continue
                visited.add((cur_post, post))
                cur_post_post_value = self.dfs(pre_post, pre_post_value, cur_post, post, visited)
                if cur_post_post_value != -1:
                    pre_post[cur_post].append(post)
                    pre_post[post].append(cur_post)
                    pre_post_value[(cur_post, post)] = cur_post_post_value
                    pre_post_value[(post, cur_post)] = 1 / cur_post_post_value
                    return pre_cur_post_value * cur_post_post_value
        return -1

''' Test algorithm'''
testSolution = Solution()
print(testSolution.calcEquations([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]))
input_1 = [[["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]]
output_1 = [360.0, 0.008333333333333333, 20.0, 1.0, -1, -1]
assert testSolution.calcEquations(*input_1) == output_1