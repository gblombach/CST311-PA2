def file_distribution():
    F = 7000
    N = 5
    Us = 99
    u_arr = [16, 21, 13, 11, 24]
    d_arr = [35, 39, 23, 26, 30]

    Dcs = max(((N * F) / Us), F / min(d_arr))
    print('Dcs', round(Dcs, 2))

    Dp2p = max((F / Us), (F / min(d_arr)), (N * F) / (Us + sum(u_arr)))
    print('Dp2p', round(Dp2p, 2))


def rtt_equation():
    samples = [30,40,100,40,50]
    EstimatedRTT = 100
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


def checksum():
    num1 = '1001100110111100'
    num2 = '0100010100111101'
    inverted = ''

    sum = bin(int(num1,2) + int(num2,2))
    print('Sum', sum)

    if len(sum) > len(num1) + 2:
        sum = bin(int(sum,2) + int('1', 2))

    for char in sum:
        inverted += '1' if char == '0' else '0'

    print('CheckSum is ', inverted)


file_distribution()
# rtt_equation()
# checksum()
