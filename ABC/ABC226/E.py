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
        self.par[ry] = rx   #ryをrxの子とする
        if self.rank[rx] == self.rank[ry]:  #rx側のrankを調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]    #rx側のsizを調整する
        return True
    
    #xを含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]

N, M = map(int, input().split())
cnt = 0
uf = UnionFind(N)
mod = 998244353
cnt = [0 for i in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    if uf.issame(x-1, y-1):
        cnt[uf.root(x-1)] += 1
    else:
        cnt[uf.root(x-1)] += cnt[uf.root(y-1)] + 1
        uf.unite(x-1, y-1)

ans = 0

for i in range(N):
    if uf.par[i] == -1:
        if uf.siz[i] == cnt[i]:
            ans += 1
        else:
            ans = 0
            break

if ans == 0:
    print(0)
else:
    print(pow(2, ans) % mod)