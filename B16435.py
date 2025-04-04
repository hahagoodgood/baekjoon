#input the number of ropes
import sys

N = int(sys.stdin.readline())
#input the maximum weight of the ropes
ropes_max_w = []
for i in range(N): ropes_max_w.append(int(sys.stdin.readline()))
ropes_max_w.sort()
# determination if it is the maximum weight
max_w =0
for i in range(N):
    if ropes_max_w[i] * (N-i) > max_w:
        max_w = ropes_max_w[i] * (N-i)

sys.stdout.write(f"{max_w}")
