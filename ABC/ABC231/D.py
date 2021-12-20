from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

class UnionFind():
    def __init__(self, n):
        self.par = [-1] * n     #par[x]:要素xの親頂点の番号（自身が根の場合は-1）
        self.rank = [0] * n     #rank[x]:要素xが属する根付き木の高さ
        self.siz = [1] * n    #siz[x]:要素xが属する根付き木に含まれる頂点数
    
    #根を求める
    def root(self, x):
        if self.par[x] == -1:   #xが根の場合はxを返す
            return x
        else:
            self.par[x] = self.root(self.par[x])    #経路圧縮
            return self.par[x]
    
    #xとyが同じグループに属するか（根が一致するか）
    def issame(self, x, y):
        return self.root(x) == self.root(y)
    
    #xを含むグループとyを含むグループを併合する
    def unite(self, x, y):
        #x側とy側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False    #すでに同じグループのときは何もしない
        #union by size
        if self.rank[rx] > self.rank[ry]:   #ry側のrankが小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx   #ryをrxの子とする
        if self.rank[rx] == self.rank[ry]:  #rx側のrankを調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]    #rx側のsizを調整する
        return True
    
    #xを含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]


N, M = map(int, input().split())
uf = UnionFind(N)
cnt = defaultdict(int)

for i in range(M):
    a, b = map(int, input().split())
    if uf.issame(a-1, b-1):
        print("No")
        exit()
    else:
        uf.unite(a-1, b-1)
        cnt[a-1] += 1
        cnt[b-1] += 1

for i in range(N):
    if cnt[i] >= 3:
        print("No")
        exit()

print("Yes")