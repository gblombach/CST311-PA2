samples = [30, 40, 100, 100]
estimatedRTT = 80
DevRTT = 0
ALPHA = 0
BETA = 0


def rtt(samp):
    estimatedRTT = ((1 - ALPHA) * estimatedRTT) + (ALPHA * sampleRTT)
    DevRTT = (1 - 0.25) * DevRTT + 0.25 * Math.abs(sampleRTT - estimatedRTT)
    console.log('ertt', estimatedRTT)
    console.log('DevRTT', DevRTT)


print(list(map(rtt, samples)))


