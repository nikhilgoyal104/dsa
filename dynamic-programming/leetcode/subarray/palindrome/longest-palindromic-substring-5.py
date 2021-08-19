# T=n²,S=n²
# dp[i][j] = is s[i:j+1] a palindrome
def x(s):
    n = len(s)
    maxLen = start = end = 0
    dp = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            dp[i][j] = s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])
            if dp[i][j] and j - i + 1 > maxLen:
                maxLen, start, end = j - i + 1, i, j
    return s[start:end + 1]


# T=n²,S=1
def y(s):
    res, n = '', len(s)

    def expand(low, high):
        while low > -1 and high < n and s[low] == s[high]:
            low, high = low - 1, high + 1
        return s[low + 1:high]

    for i in range(n):
        res = max(res, expand(i, i), expand(i, i + 1), key=len)
    return res


# T=n²,S=1
def z(s):
    n = len(s)
    maxLen = start = end = 0

    def expand(low, high):
        while low > -1 and high < n and s[low] == s[high]:
            low, high = low - 1, high + 1
        return high - low - 1, low + 1, high - 1

    for i in range(n):
        currMaxLen, currStart, currEnd = expand(i, i)
        if currMaxLen > maxLen:
            maxLen, start, end = currMaxLen, currStart, currEnd
        currMaxLen, currStart, currEnd = expand(i, i + 1)
        if currMaxLen > maxLen:
            maxLen, start, end = currMaxLen, currStart, currEnd
    return s[start:end + 1]


for s in [
    'ccc',
    'xqpabbalps',
    'xqpacbcalps',
    'abba',
    'madam',
    'babad',
    'cbbd',
    'a',
    'ac',
    'glwhcebdjbdroiurzfxxrbhzibilmcfasshhtyngwrsnbdpzgjphujzuawbebyhvxfhtoozcitaqibvvowyluvdbvoqikgojxcefzpdgahujuxpiclrrmalncdrotsgkpnfyujgvmhydrzdpiudkfchtklsaprptkzhwxsgafsvkahkbsighlyhjvbburdfjdfvjbaiivqxdqwivsjzztzkzygcsyxlvvwlckbsmvwjvrhvqfewjxgefeowfhrcturolvfgxilqdqvitbcebuooclugypurlsbdfquzsqngbscqwlrdpxeahricvtfqpnrfwbyjvahrtosovsbzhxtutyfjwjbpkfujeoueykmbcjtluuxvmffwgqjgrtsxtdimsescgahnudmsmyfijtfrcbkibbypenxnpiozzrnljazjgrftitldcueswqitrcvjzvlhionutppppzxoepvtzhkzjetpfqsuirdcyqfjsqhdewswldawhdyijhpqtrwgyfmmyhhkrafisicstqxokdmynnnqxaekzcgygsuzfiguujyxowqdfylesbzhnpznayzlinerzdqjrylyfzndgqokovabhzuskwozuxcsmyclvfwkbimhkdmjacesnvorrrvdwcgfewchbsyzrkktsjxgyybgwbvktvxyurufsrdufcunnfswqddukqrxyrueienhccpeuqbkbumlpxnudmwqdkzvsqsozkifpznwapxaxdclxjxuciyulsbxvwdoiolgxkhlrytiwrpvtjdwsssahupoyyjveedgqsthefdyxvjweaimadykubntfqcpbjyqbtnunuxzyytxfedrycsdhkfymaykeubowvkszzwmbbjezrphqildkmllskfawmcohdqalgccffxursvbyikjoglnillapcbcjuhaxukfhalcslemluvornmijbeawxzokgnlzugxkshrpojrwaasgfmjvkghpdyxt',
    'busislnescsicxpvvysuqgcudefrfjbwwjcchtgqyajdfwvkypfwshnihjdztgmyuuljxgvhdiwphrweyfkbnjgerkmifbirubhseuhrugwrabnjafnbdfjnufdstjbkuwtnpflffaqmjbhssjlnqftgjiglvvequhapasarlkcvbmkwnkuvwktbgfoaxteprobdwswcdyddyvrehvmxrrjiiidatidlpihkbmmruysmhhsncmfdanafdrfpdtfgkglcqpwrrtvacuicohspkounojuziittugpqjyhhkwfnflozbispehrtrnizowrlzcuollagxwtznjwzcumvedjwokueuqktvvouwnsmpxqvvpuwprezrbobrpnwaccwljchdguubjulyilzvmandjjleitweybqkjttschrjjlebnmponvlktzzcdtuybugggcqffkcffpamauvxfbonjrobgpvlyzveiwemmtdvbjciaytvesnocnjrwodtcokgcuoiicxapmrzpkfphjniuvzjrhbnqndfshoduejyktebgdabidxlkstepuwvtrtgbxaeheylicvhrxddijshcvdadxzsccmainyfpfdhqdanfccqkzlmhsfilvoybqojlvbcixjzqpbngdvesuokbxhkomsiqfyukvspqthlzxdnlwthrgaxhtpjzhrugqbfokrdcyurivmzgtynoqfjbafboselxnfupnpqlryvlcxeksirvufepfwczosrrjpudbwqxwldgjyfjhzlzcojxyqjyxxiqvfhjdwtgoqbyeocffnyxhyyiqspnvrpxmrtcnviukrjvpavervvztoxajriuvxqveqsrttjqepvvahywuzwtmgyrzduxfqspeipimyoxmkadrvrdyefekjxcmsmzmtbugyckcbjsrymszftjyllfmoeoylzeahnrxlxpnlvlvzltwnmldi',
    'dumpyxybklgdwxbmhptxdckihigddiqzcyvhjhxdekozqxkwaiassrxalcnrlqjbakekgkbpsznmxfvdlhjuokdvzuetuoargsrrfboenozkrglrjnmlsntrxafvqfjniugdzxeutyjybdqfyqmqlkhgvryuwegoibobkstpirzdaspjyxddnyniaywgziqbmkwqaotxirlimlhiuxoyxwsnnmsyzpfxlatnpdqvbiafzqkfssetleiobwwpubzumgittqtrjzeioxkrujkdgzfykyypvnpsxnouxeeqmarjploacjntpixpglugxtiwycmeywhnjyqsmbgxchhtlpjesmhoaskatbfvqodtboozgwlpqclkigpqzvatavdzvgoibmygjsskynldvxevbprdxzpqcpuokyqyseyrekoiipoytftnwqawykfpcqriuazjoqucjkyknmcbiykqerpxxdkqlxvlijqegpexvylgkqygbgkicwmplnwubjwqnarulzlbrdftmzyrzhrmfqoiwzlncdreqaiipnqlwffxircopksnwizmyvzfphlqlvqpcsfjmyssrheczllgkvnretmtixoibncraddatreejidxilnplcrufhdgktvkzuaggcumykgklypodjrpdpjcneagjfxahtjeurotkufkmxsoelzpttfeugdculuxjddghlisdytyjwwnftjbvrwyntqwqjrwlfynczndjyiyaxozdlgdzjseyfumvxuclmszawzwiunwqouycmfgkpzgivsemxamnfjzcabkgkgxcruqhpbkzhpdrcexnioaxbjwxbuipnjbsujajpnqeckfgxyuydytrfhhwsxfjeahpiaoojdwkzstnxflxddljpbhfirteejbtcxpvwutsgrrjv'
]:
    print(x(s), end=' ')
    print(y(s), end=' ')
    print(z(s))
