def heap_sort_k(A, K):
    cnt = 0
    n = len(A)

    # heapify (min-heap)
    def heapify(A, n, i):
        nonlocal cnt

        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and A[left] < A[smallest]:
            smallest = left
        if right < n and A[right] < A[smallest]:
            smallest = right

        if smallest != i:
            A[i], A[smallest] = A[smallest], A[i]
            cnt += 1

            if cnt == K:
                print(*A)
                exit()

            heapify(A, n, smallest)

    # 1. min-heap 구성
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)

    # 2. heap sort 진행
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        cnt += 1

        if cnt == K:
            print(*A)
            return

        heapify(A, i, 0)
    print(-1)

N, K = map(int, input().split())
A = list(map(int, input().split()))

heap_sort_k(A, K)