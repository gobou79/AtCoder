from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 9)

class UnionFind():
    def __init__(self, n):
        self.par = [-1] * n     #par[x]:要素xの親頂点の番号（自身が根の場合は-1）
        self.rank = [0] * n     #rank[x]:要素xが属する根付き木の高さ
        self.siz = [i for i in range(n)]    #siz[x]:要素xが属する根付き木に含まれる頂点数
    
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
        self.siz[rx] = max(self.siz[rx], self.siz[ry])    #rx側のsizを調整する
        return True
    
    #xを含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]


N = 2 ** 20

uf = UnionFind(N)

Q = int(input())
d = defaultdict(int)
seen = defaultdict(int)

for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        h = x % N
        if seen[h] != 0:
            a = uf.size(h)
            h = a+1
            if h == N:
                if seen[0] != 0:
                    a = uf.size(0)
                    h = a+1
                else:
                    h = 0
        d[h] = x
        seen[h] = 1
        if h+1 < N and seen[h+1] != 0:
            uf.unite(h, h+1)
        if h>0:
            if seen[h-1] != 0:
                uf.unite(h-1, h)
    
    elif t == 2:
        h = x % N
        if d[h] == 0 and seen[h] == 0:
            print(-1)
        else:
            print(d[h])