import heapq

n = 3

#define the state of disk around the rod
initial_state = (
    (3,2,1),
    (),
    ()
)

goal_state = (
    (),
    (),
    (3,2,1)
)
# untuk perkiraan seberapa jauh state skrng dari goal
def heuristic(state):
    return n - len(state[2])

# untuk mencari semua state yang mungkin terjadi setelah 1 langkah perpindahan
def get_successors(state):
    successors = []

    gagang = [list(gagang) for gagang in state]

    for i in range(3):

        if not gagang[i]:
            continue

        disk = gagang[i][-1]

        for j in range(3):
            if i == j:
                continue

            if not gagang[j] or gagang[j][-1] > disk:

                new_gagang = [list(gagang) for gagang in gagang]
                new_gagang[i].pop()
                new_gagang[j].append(disk)

                successors.append(tuple(tuple(gagang)for gagang in new_gagang))

    return successors

# A* search
def astar_search():
    pq = []
    heapq.heappush(pq, (0, initial_state))

    visited = set()

    while pq:
        f, state = heapq.heappop(pq)

        if state == goal_state:
            return state

        if state in visited:
            continue
        visited.add(state)

        for next_state in get_successors(state):

            cost = heuristic(next_state)

            heapq.heappush(
                pq, (cost, next_state)
            )
    return None

result = astar_search()

print("Disk sudah berpindah ke gagang yang sesuai.")
print(result)





