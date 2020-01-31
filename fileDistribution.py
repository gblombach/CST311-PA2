def file_distribution():
    F = 9000
    N = 6
    Us = 91
    u_arr = [13, 26, 29, 18, 12, 18]
    d_arr = [11, 19, 21, 31, 17, 27]

    Dcs = max(((N * F) / Us), F / min(d_arr))
    print('Dcs', round(Dcs, 2))

    Dp2p = max((F / Us), (F / min(d_arr)), (N * F) / (Us + sum(u_arr)))
    print('Dp2p', round(Dp2p, 2))

def rtt_equation():
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



# file_distribution()
# rtt_equation()
checksum()
