samples = [250, 300, 150, 200, 5]
EstimatedRTT = 175
DevRTT = 0
ALPHA = 0.125
BETA = 0.25

print(list(samples))
print("========================")

for sampleRTT in samples:
    EstimatedRTT = (1 - ALPHA) * EstimatedRTT + ALPHA * sampleRTT;
    DevRTT = (1 - 0.25) * DevRTT + 0.25 * abs(sampleRTT - EstimatedRTT)
    print('EstimatedRTT', round(EstimatedRTT, 3))
    print("DevRTT", round(DevRTT, 3))
    print("========================")

Timout = EstimatedRTT + 4 * DevRTT
print('TimeoutInterval', round(Timout, 3))