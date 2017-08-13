# Task 3
import Queue


def read_pockets(n):
    return [raw_input() for pocket in range(n)]

def pocket_simulator(buffer_size, pockets):
    buffer = Queue.Queue(buffer_size)
    times = ''
    buffer_status = False

    for current_pocket in pockets:
        current_time = current_pocket[0]
        print('current_time = {}'.format(current_time))
        times += str(current_time)

    return times
'''
buffer_size, n = map(int, raw_input().split(' '))
pockets = read_pockets(n)
print('buffer_size={}, pockets={}'.format(buffer_size, pockets))
pocket_simulator(buffer_size, pockets)
'''

buffer_size = 1
pockets = [(0, 1), (2, 3)]
t = pocket_simulator(buffer_size, pockets)
print(t)
