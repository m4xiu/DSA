class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        tree = [(0, [0] * k) for _ in range(4 * n)]

        def merge(a, b):
            p1, c1 = a
            p2, c2 = b

            cnt = c1[:]

            for r in range(k):
                cnt[(p1 * r) % k] += c2[r]

            return (p1 * p2 % k, cnt)

        def build(node, l, r):
            if l == r:
                x = nums[l] % k
                cnt = [0] * k
                cnt[x] = 1
                tree[node] = (x, cnt)
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, l, r, pos, val):
            if l == r:
                x = val % k
                cnt = [0] * k
                cnt[x] = 1
                tree[node] = (x, cnt)
                return

            mid = (l + r) // 2

            if pos <= mid:
                update(node * 2, l, mid, pos, val)
            else:
                update(node * 2 + 1, mid + 1, r, pos, val)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(
                query(node * 2, l, mid, ql, qr),
                query(node * 2 + 1, mid + 1, r, ql, qr)
            )

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)
            result = query(1, 0, n - 1, start, n - 1)
            ans.append(result[1][x])

        return ans