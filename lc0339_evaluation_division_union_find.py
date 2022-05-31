import collections

class UnionFind:
    def __init__(self):
        self.root
    def union(self, a, b, a_b):
        if a not in self.root:
            self.root[a] = [1, a]
        if b not in self.root:
            self.root[b] = [1, b]
        a_ra, root_a = self.find(a)
        b_rb, root_b = self.find(b)
        self.root[root_a] = [a_b * b_rb / a_ra, root_b]
    def find(self, a):
        tmp = a
        path, rate, base = [], [], 1
        while self.root[a][1] != a:
            path.append(a)
            rate.append(self.root[a][0])
            base *= self.root[a][0]
            a = self.root[a][1]
        for i in range(len(path)):
            self.root[path[i][1]] = a
            self.root[path[i][0]] = base
            base /= rate[i]
        return self.root[tmp]


class Solution:
    def calcEquation(self, equations, values, queries):
        uf = UnionFind()
        for i in range(len(values)):
            a, b, a_b = equations[i][0], equations[i][1], values[i]
            uf.union(a, b, a_b)
        ans = []
        for u, v in queries:
            if u in uf.root and v in ur.root:
                u_ur, root_u = uf.find(u)
                v_vr, root_v = uf.find(v)
                if root_v != root_v:
                    ans.append(-1.0)
                else:
                    ans.append(u_ur / v_vr)
            else:
                ans.append(-1.0)
        return ans
