inputs = [
    [3, 1, 2, 4],
    [11, 81, 94, 43, 3],
    [71, 55, 82, 55],
    [1, 26734, 27943, 524, 4612, 26421, 17122, 2570, 15674, 24112, 7796, 12767, 22132, 11774, 127, 8546, 16572, 20639,
     12467, 9527, 21142, 29257, 26006, 14806, 3832, 19818, 6304, 6811, 18841, 6696, 21366, 15128, 12996, 24112, 13873,
     21626, 18587, 22330, 26768, 6413, 20338, 134, 6480, 22239, 9226, 6521, 16723, 26628, 16225, 6394, 8797, 3890, 9928,
     1510, 19621, 15927, 3333, 1407, 4406, 25824, 28889, 9153, 13234, 5720, 21808, 15276, 370, 6999, 241, 13129, 26136,
     26421, 18083, 28788, 27343, 15316, 11801, 9463, 5007, 16524, 14216, 303, 1016, 6518, 7794, 13498, 27069, 27709,
     8094, 20357, 16684, 27007, 9076, 13325, 17847, 12585, 12545, 6018, 22253, 24412, 19540, 16884, 26412, 25804, 595,
     20374, 619, 12213, 6028, 6150, 13070, 1374, 21737, 14743, 26182, 8197, 29022, 28890, 11486, 4630, 3753, 2065, 1266,
     26052, 10924, 14024, 13081, 24058, 12033, 10712, 20360, 11513, 19732, 13744, 17048, 12078, 7601, 28306, 17662,
     19083, 8598, 19081, 16580, 17442, 16174, 7725, 19634, 2423, 9330, 9109, 13032, 83, 6140, 25620, 23759, 399, 18202,
     15453, 2923, 22252, 10867, 11467, 10976, 18250, 25012, 25274, 9378, 26928, 1760, 18689, 21015, 28673, 12517, 12439,
     18831, 10206, 29060, 10435, 4407, 10186, 7638, 29956, 26649, 22021, 8227, 8451, 4557, 17543, 6623, 3137, 27029,
     8073, 18781, 3882, 8540, 4153, 8282, 283, 10854, 28166, 18778, 28476, 13539, 1786, 4607, 14617, 6838, 2750, 7880,
     14047, 12619, 22485, 28217, 16297, 2729, 3523, 12101, 2577, 16300, 21286, 8692, 15655, 29373, 4995, 27883, 12444,
     26411, 11217, 27545, 26438, 24921, 9880, 7779, 2952, 23384, 12011, 13948, 2861, 2080, 25248, 16760, 4958, 5683,
     10805, 7975, 4095, 228, 28656, 13329, 19839, 16967, 21051, 26723, 9871, 19712, 446, 8902, 785, 13306, 25710, 26796,
     20127, 25379, 14185, 2470, 13950, 21548, 6757, 3837, 29541, 13392, 19450, 29769, 20946, 12424, 16208, 14892, 13533,
     17031, 9274, 3443, 28888, 27114, 20631, 13237, 26711, 13961, 19286, 27760, 5348, 22970, 28016, 12336, 16832, 9929,
     27933, 10067, 7299, 11762, 2905, 4781, 2907, 21345, 9963, 1122, 20727, 8969, 24317, 27537, 17559, 27963, 27693,
     11783, 21382, 597, 18981, 29057, 17087, 8911, 16192, 11459, 8862, 13471, 6762, 14218, 7155, 542, 667, 12711, 8956,
     1177, 24497, 2943, 9246, 24671, 22054, 12855, 23007, 7784, 12656, 24346, 9349, 24116, 13108, 21107, 5379, 13641,
     4024, 16904, 3876, 28277, 27679, 8311, 9504, 129, 29864, 17304, 9540, 29879, 7995, 19549, 12824, 3605, 7710, 21160,
     6952, 9415, 5398, 1122, 1573, 5864, 2842, 20614, 26538, 14855, 9197, 15134, 21477, 18952, 4796, 23187, 26967,
     15075, 20832, 17450, 4983, 11540, 28922, 1610, 22931, 18562, 17063, 14785, 4502, 18292, 28325, 15236, 25468, 20536,
     5171, 24635, 5080, 28281, 4809, 12344, 24793, 10820, 18493, 19894, 8710, 12153, 17553, 15020, 28136, 21718, 2574,
     20550, 17769, 15794, 9741, 23319, 27271, 9729, 14512, 21493, 22829, 8479, 17237, 26257, 2140, 24820, 21046, 24817,
     26657, 22319, 19981, 2843, 17138, 1021, 13102, 2534, 18248, 980, 22097, 19994, 2527, 3932, 23203, 22344, 27247,
     10538, 6211, 28642, 14194, 16995, 2726, 24200, 6693, 28511, 13888, 4740, 18100, 7500, 3396, 14583, 15123, 21341,
     27012, 6520, 24756, 13607, 3780, 22530, 11582, 16806, 97, 7420, 17375, 929, 3947, 15740, 6615, 21130, 26780, 4939,
     11151, 2149, 28188, 21372, 4316, 6977, 18419, 8974, 4727, 25056, 8278, 21028, 11911, 7157, 25944, 21102, 12394,
     18811, 4104, 29252, 22555, 24702, 6187, 25190, 9541, 10214, 20026, 26214, 20475, 8709, 24737, 4049, 28281, 21172,
     16847, 6271, 13823, 12712, 15869, 22958, 24708, 14471, 18466, 24381, 21432, 17951, 12072, 1861, 24954, 6074, 17079,
     6331, 114, 12098, 16224, 7819, 1519, 23126, 14510, 1629, 4123, 21076, 29558, 28140, 28849, 13690, 19769, 2512,
     17645, 22132, 26930, 2479, 12416, 8147, 3462, 7032, 24018, 16654, 16425, 6922, 24768, 14537, 25037, 13152, 53,
     6801, 18268, 5006, 14536, 17943, 11720, 857, 1860, 24287, 14852, 2857, 6151, 9639, 1657, 18210, 15024, 23337,
     14297, 16336, 24118, 24812, 9792, 2931, 26927, 23127, 589, 1801, 25909, 12099, 164, 16978, 29889, 29502, 7328,
     22146, 5565, 24589, 18452, 24505, 20623, 24941, 4125, 8109, 5605, 3712, 6662, 2502, 13479, 10357, 267, 5866, 21070,
     1303, 558, 25697, 27452, 1109, 7796, 10753, 17430, 18818, 28933, 8112, 12049, 11286, 25158, 5795, 27279, 19863,
     14677, 21586, 5902, 1322, 25964, 10701, 26204, 18703, 17464, 26479, 9116, 11497, 25344, 27224, 23574, 27569, 16514,
     5199, 25448, 26500, 9126, 20005, 565, 27784, 10415, 16918, 20524, 24704, 21210, 9811, 27920, 6688, 22408, 15214,
     7604, 15383, 9448, 15626, 6257, 7933, 7339, 25848, 11747, 25708, 11363, 9614, 19924, 12137, 24562, 19416, 20995,
     29095, 25348, 10250, 13783, 25981, 26784, 16167, 16371, 2499, 6383, 3550, 9760, 478, 15232, 18, 10791, 3064, 7295,
     19924, 7935, 174, 24768, 16171, 26478, 8057, 9595, 926, 15229, 26843, 54, 17326, 7211, 20606, 27764, 14531, 26303,
     11572, 6531, 12681, 19759, 24071, 20310, 2156, 23865, 3976, 3452, 6371, 5227, 5795, 6016, 16059, 25810, 15763,
     19722, 23469, 29704, 8229, 28262, 5867, 5784, 23877, 2369, 27037, 27094, 21064, 20899, 14387, 2123, 10375, 22822,
     17631, 9176, 5166, 6320, 16026, 21001, 28329, 23419, 21184, 18985, 29941, 18285, 23450, 12063, 4181, 11016, 23771,
     15244, 14867, 6242, 10874, 22482, 12516, 5270, 28765, 27993, 25818, 14679, 29602, 2140, 19648, 964, 10335, 16796,
     14490, 13093, 28122, 26502, 26719, 23403, 6047, 19838, 11099, 26666, 10332, 17904, 24809, 9866, 3640, 10706, 8112,
     10532, 29303, 25785, 17537, 25197, 15164, 27938, 7598, 27027, 16923, 3328, 14196, 9432, 6643, 23609, 5050, 18760,
     16607, 16440, 5614, 21039, 14198, 16742, 27851, 29810, 18292, 15071, 29333, 994, 4933, 21146, 9431, 14933, 18688,
     12098, 17732, 9535, 4794, 19142, 4892, 5064, 25497, 23264, 2997, 22093, 24692, 24767, 18692, 16140, 18291, 9612,
     17404, 23691, 13337, 3256, 25168, 8774, 13258, 19752, 24109, 19197, 11583, 3190, 29030, 14925, 13253, 22870, 22237,
     21134, 29393, 24969, 18838, 3846, 24903, 15472, 17549, 16708, 6666, 16702, 14095, 26914, 28233, 29491, 15880, 8739,
     2833, 639, 8295, 1187, 21528, 14341, 24595, 25013, 14181, 14455, 15906, 19653, 14279, 28796, 8268, 1144, 29159,
     2630, 5642, 8217, 25230, 9486, 19678, 25389, 16300, 6843, 15402, 687, 10985, 5406, 12066, 1804, 20103, 20680,
     24203, 17878, 3700, 4368, 29528, 20875, 19874, 14623, 9713, 25504, 28192, 7492, 10315, 9551, 29553, 17279, 22274,
     10006, 9801, 22347, 24460, 4289, 26264, 19552, 9117, 5864, 28404, 15654, 13176, 9174, 19810, 268, 27341, 18487, 19,
     1851, 18000, 7218, 9944, 26207, 23598, 15463, 26305, 17452, 8408, 29282, 1780, 2070, 26883, 16527, 26288, 23803,
     21979, 28682, 10338, 18774, 27184, 7380, 183, 16370, 12834, 11925, 11541, 20281, 15800, 13256, 20365, 10770, 14711,
     10041]
]


# T=n³,S=1
def main(nums):
    n = len(nums)
    res = 0
    for i in range(n):
        for j in range(i, n):
            res += min(nums[i:j + 1])
    return res % (10 ** 9 + 7)


for nums in inputs:
    print(main(nums), end=' ')

print()


# T=n²,S=1
def main(nums):
    n = len(nums)
    res = 0
    for i in range(n):
        minVal = nums[i]
        for j in range(i, n):
            minVal = min(minVal, nums[j])
            res += minVal
    return res % (10 ** 9 + 7)


for nums in inputs:
    print(main(nums), end=' ')

print()


# T=n,S=n
# left[i] = index of first smaller element on left of nums[i]
# right[i] = index of first smaller element on right of nums[i]
def main(nums):
    n = len(nums)
    left = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)
    right = [n] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            right[stack.pop()] = i
        stack.append(i)
    res = 0
    for i in range(n):
        subarrays = (i - left[i]) * (right[i] - i)
        res += subarrays * nums[i]
    return res % (10 ** 9 + 7)


for nums in inputs:
    print(main(nums), end=' ')
