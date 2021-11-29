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

graph = [[] for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    graph[a-1].append(b-1)

uf = UnionFind(N)
ans = [0]
cnt = 0

for v in reversed(range(N)):
    cnt += 1
    for u in graph[v]:
        if uf.issame(v, u):
            continue
        else:
            uf.unite(v, u)
            cnt -= 1
    ans.append(cnt)

for i in range(N):
    print(ans[-(i+2)])