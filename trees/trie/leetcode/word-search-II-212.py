inputs = [
    (
        [
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['i', 'f', 'l', 'v']
        ],
        ['oath', 'pea', 'eat', 'rain']
    ),
    (
        [

            ['a', 'b'],
            ['c', 'd']
        ],
        ['abcb']
    ),
    (
        [
            ['o', 'a', 'b', 'n'],
            ['o', 't', 'a', 'e'],
            ['a', 'h', 'k', 'r'],
            ['a', 'f', 'l', 'v']
        ], ['oa', 'oaa']
    ),
    (
        [
            ['a', 'b', 'c', 'e'],
            ['x', 'x', 'c', 'd'],
            ['x', 'x', 'b', 'a']
        ], ['abc', 'abcd']
    ),
    (
        [
            ['a', 'b', 'c'],
            ['a', 'e', 'd'],
            ['a', 'f', 'g']
        ], ['abcdefg', 'gfedcbaaa', 'eaabcdgfa', 'befa', 'dgc', 'ade']
    )
]


# T=N3ᴸ,S=L
def main(grid, words):
    m, n = len(grid), len(grid[0])
    offsets = (0, 1), (0, -1), (-1, 0), (1, 0)

    def dfs(ri, ci, word, vis):
        if not word:
            return True
        if ri in [-1, m] or ci in [-1, n] or (ri, ci) in vis or word[0] != grid[ri][ci]:
            return False
        vis.add((ri, ci))
        for i, j in offsets:
            if dfs(ri + i, ci + j, word[1:], vis):
                return True
        vis.remove((ri, ci))
        return False

    res = set()
    for word in words:
        for ri in range(m):
            for ci in range(n):
                if word[0] == grid[ri][ci] and dfs(ri, ci, word, set()):
                    res.add(word)
    return res


for grid, words in inputs:
    print(main(grid, words))

print()

inputs += [
    (
        [
            ['b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a'],
            ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'],
            ['b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a'],
            ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'],
            ['b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a'],
            ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'],
            ['b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a'],
            ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'],
            ['b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a'],
            ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
        ],
        [
            'ababababaa', 'ababababab', 'ababababac', 'ababababad', 'ababababae', 'ababababaf', 'ababababag',
            'ababababah', 'ababababai', 'ababababaj', 'ababababak', 'ababababal', 'ababababam', 'ababababan',
            'ababababao', 'ababababap', 'ababababaq', 'ababababar', 'ababababas', 'ababababat', 'ababababau',
            'ababababav', 'ababababaw', 'ababababax', 'ababababay', 'ababababaz', 'ababababba', 'ababababbb',
            'ababababbc', 'ababababbd', 'ababababbe', 'ababababbf', 'ababababbg', 'ababababbh', 'ababababbi',
            'ababababbj', 'ababababbk', 'ababababbl', 'ababababbm', 'ababababbn', 'ababababbo', 'ababababbp',
            'ababababbq', 'ababababbr', 'ababababbs', 'ababababbt', 'ababababbu', 'ababababbv', 'ababababbw',
            'ababababbx', 'ababababby', 'ababababbz', 'ababababca', 'ababababcb', 'ababababcc', 'ababababcd',
            'ababababce', 'ababababcf', 'ababababcg', 'ababababch', 'ababababci', 'ababababcj', 'ababababck',
            'ababababcl', 'ababababcm', 'ababababcn', 'ababababco', 'ababababcp', 'ababababcq', 'ababababcr',
            'ababababcs', 'ababababct', 'ababababcu', 'ababababcv', 'ababababcw', 'ababababcx', 'ababababcy',
            'ababababcz', 'ababababda', 'ababababdb', 'ababababdc', 'ababababdd', 'ababababde', 'ababababdf',
            'ababababdg', 'ababababdh', 'ababababdi', 'ababababdj', 'ababababdk', 'ababababdl', 'ababababdm',
            'ababababdn', 'ababababdo', 'ababababdp', 'ababababdq', 'ababababdr', 'ababababds', 'ababababdt',
            'ababababdu', 'ababababdv', 'ababababdw', 'ababababdx', 'ababababdy', 'ababababdz', 'ababababea',
            'ababababeb', 'ababababec', 'ababababed', 'ababababee', 'ababababef', 'ababababeg', 'ababababeh',
            'ababababei', 'ababababej', 'ababababek', 'ababababel', 'ababababem', 'ababababen', 'ababababeo',
            'ababababep', 'ababababeq', 'ababababer', 'ababababes', 'ababababet', 'ababababeu', 'ababababev',
            'ababababew', 'ababababex', 'ababababey', 'ababababez', 'ababababfa', 'ababababfb', 'ababababfc',
            'ababababfd', 'ababababfe', 'ababababff', 'ababababfg', 'ababababfh', 'ababababfi', 'ababababfj',
            'ababababfk', 'ababababfl', 'ababababfm', 'ababababfn', 'ababababfo', 'ababababfp', 'ababababfq',
            'ababababfr', 'ababababfs', 'ababababft', 'ababababfu', 'ababababfv', 'ababababfw', 'ababababfx',
            'ababababfy', 'ababababfz', 'ababababga', 'ababababgb', 'ababababgc', 'ababababgd', 'ababababge',
            'ababababgf', 'ababababgg', 'ababababgh', 'ababababgi', 'ababababgj', 'ababababgk', 'ababababgl',
            'ababababgm', 'ababababgn', 'ababababgo', 'ababababgp', 'ababababgq', 'ababababgr', 'ababababgs',
            'ababababgt', 'ababababgu', 'ababababgv', 'ababababgw', 'ababababgx', 'ababababgy', 'ababababgz',
            'ababababha', 'ababababhb', 'ababababhc', 'ababababhd', 'ababababhe', 'ababababhf', 'ababababhg',
            'ababababhh', 'ababababhi', 'ababababhj', 'ababababhk', 'ababababhl', 'ababababhm', 'ababababhn',
            'ababababho', 'ababababhp', 'ababababhq', 'ababababhr', 'ababababhs', 'ababababht', 'ababababhu',
            'ababababhv', 'ababababhw', 'ababababhx', 'ababababhy', 'ababababhz', 'ababababia', 'ababababib',
            'ababababic', 'ababababid', 'ababababie', 'ababababif', 'ababababig', 'ababababih', 'ababababii',
            'ababababij', 'ababababik', 'ababababil', 'ababababim', 'ababababin', 'ababababio', 'ababababip',
            'ababababiq', 'ababababir', 'ababababis', 'ababababit', 'ababababiu', 'ababababiv', 'ababababiw',
            'ababababix', 'ababababiy', 'ababababiz', 'ababababja', 'ababababjb', 'ababababjc', 'ababababjd',
            'ababababje', 'ababababjf', 'ababababjg', 'ababababjh', 'ababababji', 'ababababjj', 'ababababjk',
            'ababababjl', 'ababababjm', 'ababababjn', 'ababababjo', 'ababababjp', 'ababababjq', 'ababababjr',
            'ababababjs', 'ababababjt', 'ababababju', 'ababababjv', 'ababababjw', 'ababababjx', 'ababababjy',
            'ababababjz', 'ababababka', 'ababababkb', 'ababababkc', 'ababababkd', 'ababababke', 'ababababkf',
            'ababababkg', 'ababababkh', 'ababababki', 'ababababkj', 'ababababkk', 'ababababkl', 'ababababkm',
            'ababababkn', 'ababababko', 'ababababkp', 'ababababkq', 'ababababkr', 'ababababks', 'ababababkt',
            'ababababku', 'ababababkv', 'ababababkw', 'ababababkx', 'ababababky', 'ababababkz', 'ababababla',
            'abababablb', 'abababablc', 'ababababld', 'abababable', 'abababablf', 'abababablg', 'abababablh',
            'ababababli', 'abababablj', 'abababablk', 'ababababll', 'abababablm', 'ababababln', 'abababablo',
            'abababablp', 'abababablq', 'abababablr', 'ababababls', 'abababablt', 'abababablu', 'abababablv',
            'abababablw', 'abababablx', 'abababably', 'abababablz', 'ababababma', 'ababababmb', 'ababababmc',
            'ababababmd', 'ababababme', 'ababababmf', 'ababababmg', 'ababababmh', 'ababababmi', 'ababababmj',
            'ababababmk', 'ababababml', 'ababababmm', 'ababababmn', 'ababababmo', 'ababababmp', 'ababababmq',
            'ababababmr', 'ababababms', 'ababababmt', 'ababababmu', 'ababababmv', 'ababababmw', 'ababababmx',
            'ababababmy', 'ababababmz', 'ababababna', 'ababababnb', 'ababababnc', 'ababababnd', 'ababababne',
            'ababababnf', 'ababababng', 'ababababnh', 'ababababni', 'ababababnj', 'ababababnk', 'ababababnl',
            'ababababnm', 'ababababnn', 'ababababno', 'ababababnp', 'ababababnq', 'ababababnr', 'ababababns',
            'ababababnt', 'ababababnu', 'ababababnv', 'ababababnw', 'ababababnx', 'ababababny', 'ababababnz',
            'ababababoa', 'ababababob', 'ababababoc', 'ababababod', 'ababababoe', 'ababababof', 'ababababog',
            'ababababoh', 'ababababoi', 'ababababoj', 'ababababok', 'ababababol', 'ababababom', 'ababababon',
            'ababababoo', 'ababababop', 'ababababoq', 'ababababor', 'ababababos', 'ababababot', 'ababababou',
            'ababababov', 'ababababow', 'ababababox', 'ababababoy', 'ababababoz', 'ababababpa', 'ababababpb',
            'ababababpc', 'ababababpd', 'ababababpe', 'ababababpf', 'ababababpg', 'ababababph', 'ababababpi',
            'ababababpj', 'ababababpk', 'ababababpl', 'ababababpm', 'ababababpn', 'ababababpo', 'ababababpp',
            'ababababpq', 'ababababpr', 'ababababps', 'ababababpt', 'ababababpu', 'ababababpv', 'ababababpw',
            'ababababpx', 'ababababpy', 'ababababpz', 'ababababqa', 'ababababqb', 'ababababqc', 'ababababqd',
            'ababababqe', 'ababababqf', 'ababababqg', 'ababababqh', 'ababababqi', 'ababababqj', 'ababababqk',
            'ababababql', 'ababababqm', 'ababababqn', 'ababababqo', 'ababababqp', 'ababababqq', 'ababababqr',
            'ababababqs', 'ababababqt', 'ababababqu', 'ababababqv', 'ababababqw', 'ababababqx', 'ababababqy',
            'ababababqz', 'ababababra', 'ababababrb', 'ababababrc', 'ababababrd', 'ababababre', 'ababababrf',
            'ababababrg', 'ababababrh', 'ababababri', 'ababababrj', 'ababababrk', 'ababababrl', 'ababababrm',
            'ababababrn', 'ababababro', 'ababababrp', 'ababababrq', 'ababababrr', 'ababababrs', 'ababababrt',
            'ababababru', 'ababababrv', 'ababababrw', 'ababababrx', 'ababababry', 'ababababrz', 'ababababsa',
            'ababababsb', 'ababababsc', 'ababababsd', 'ababababse', 'ababababsf', 'ababababsg', 'ababababsh',
            'ababababsi', 'ababababsj', 'ababababsk', 'ababababsl', 'ababababsm', 'ababababsn', 'ababababso',
            'ababababsp', 'ababababsq', 'ababababsr', 'ababababss', 'ababababst', 'ababababsu', 'ababababsv',
            'ababababsw', 'ababababsx', 'ababababsy', 'ababababsz', 'ababababta', 'ababababtb', 'ababababtc',
            'ababababtd', 'ababababte', 'ababababtf', 'ababababtg', 'ababababth', 'ababababti', 'ababababtj',
            'ababababtk', 'ababababtl', 'ababababtm', 'ababababtn', 'ababababto', 'ababababtp', 'ababababtq',
            'ababababtr', 'ababababts', 'ababababtt', 'ababababtu', 'ababababtv', 'ababababtw', 'ababababtx',
            'ababababty', 'ababababtz', 'ababababua', 'ababababub', 'ababababuc', 'ababababud', 'ababababue',
            'ababababuf', 'ababababug', 'ababababuh', 'ababababui', 'ababababuj', 'ababababuk', 'ababababul',
            'ababababum', 'ababababun', 'ababababuo', 'ababababup', 'ababababuq', 'ababababur', 'ababababus',
            'ababababut', 'ababababuu', 'ababababuv', 'ababababuw', 'ababababux', 'ababababuy', 'ababababuz',
            'ababababva', 'ababababvb', 'ababababvc', 'ababababvd', 'ababababve', 'ababababvf', 'ababababvg',
            'ababababvh', 'ababababvi', 'ababababvj', 'ababababvk', 'ababababvl', 'ababababvm', 'ababababvn',
            'ababababvo', 'ababababvp', 'ababababvq', 'ababababvr', 'ababababvs', 'ababababvt', 'ababababvu',
            'ababababvv', 'ababababvw', 'ababababvx', 'ababababvy', 'ababababvz', 'ababababwa', 'ababababwb',
            'ababababwc', 'ababababwd', 'ababababwe', 'ababababwf', 'ababababwg', 'ababababwh', 'ababababwi',
            'ababababwj', 'ababababwk', 'ababababwl', 'ababababwm', 'ababababwn', 'ababababwo', 'ababababwp',
            'ababababwq', 'ababababwr', 'ababababws', 'ababababwt', 'ababababwu', 'ababababwv', 'ababababww',
            'ababababwx', 'ababababwy', 'ababababwz', 'ababababxa', 'ababababxb', 'ababababxc', 'ababababxd',
            'ababababxe', 'ababababxf', 'ababababxg', 'ababababxh', 'ababababxi', 'ababababxj', 'ababababxk',
            'ababababxl', 'ababababxm', 'ababababxn', 'ababababxo', 'ababababxp', 'ababababxq', 'ababababxr',
            'ababababxs', 'ababababxt', 'ababababxu', 'ababababxv', 'ababababxw', 'ababababxx', 'ababababxy',
            'ababababxz', 'ababababya', 'ababababyb', 'ababababyc', 'ababababyd', 'ababababye', 'ababababyf',
            'ababababyg', 'ababababyh', 'ababababyi', 'ababababyj', 'ababababyk', 'ababababyl', 'ababababym',
            'ababababyn', 'ababababyo', 'ababababyp', 'ababababyq', 'ababababyr', 'ababababys', 'ababababyt',
            'ababababyu', 'ababababyv', 'ababababyw', 'ababababyx', 'ababababyy', 'ababababyz', 'ababababza',
            'ababababzb', 'ababababzc', 'ababababzd', 'ababababze', 'ababababzf', 'ababababzg', 'ababababzh',
            'ababababzi', 'ababababzj', 'ababababzk', 'ababababzl', 'ababababzm', 'ababababzn', 'ababababzo',
            'ababababzp', 'ababababzq', 'ababababzr', 'ababababzs', 'ababababzt', 'ababababzu', 'ababababzv',
            'ababababzw', 'ababababzx', 'ababababzy', 'ababababzz']
    ),
    (
        [
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
        ],
        ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']
    ),
    (
        [['b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a'], ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'],
         ['b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a'], ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'],
         ['b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a'], ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'],
         ['b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a'], ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'],
         ['b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a'], ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']],
        [
            'aababababa', 'abbabababa', 'acbabababa', 'adbabababa', 'aebabababa', 'afbabababa', 'agbabababa',
            'ahbabababa', 'aibabababa', 'ajbabababa', 'akbabababa', 'albabababa', 'ambabababa', 'anbabababa',
            'aobabababa', 'apbabababa', 'aqbabababa', 'arbabababa', 'asbabababa', 'atbabababa', 'aubabababa',
            'avbabababa', 'awbabababa', 'axbabababa', 'aybabababa', 'azbabababa', 'bababababa', 'bbbabababa',
            'bcbabababa', 'bdbabababa', 'bebabababa', 'bfbabababa', 'bgbabababa', 'bhbabababa', 'bibabababa',
            'bjbabababa', 'bkbabababa', 'blbabababa', 'bmbabababa', 'bnbabababa', 'bobabababa', 'bpbabababa',
            'bqbabababa', 'brbabababa', 'bsbabababa', 'btbabababa', 'bubabababa', 'bvbabababa', 'bwbabababa',
            'bxbabababa', 'bybabababa', 'bzbabababa', 'cababababa', 'cbbabababa', 'ccbabababa', 'cdbabababa',
            'cebabababa', 'cfbabababa', 'cgbabababa', 'chbabababa', 'cibabababa', 'cjbabababa', 'ckbabababa',
            'clbabababa', 'cmbabababa', 'cnbabababa', 'cobabababa', 'cpbabababa', 'cqbabababa', 'crbabababa',
            'csbabababa', 'ctbabababa', 'cubabababa', 'cvbabababa', 'cwbabababa', 'cxbabababa', 'cybabababa',
            'czbabababa', 'dababababa', 'dbbabababa', 'dcbabababa', 'ddbabababa', 'debabababa', 'dfbabababa',
            'dgbabababa', 'dhbabababa', 'dibabababa', 'djbabababa', 'dkbabababa', 'dlbabababa', 'dmbabababa',
            'dnbabababa', 'dobabababa', 'dpbabababa', 'dqbabababa', 'drbabababa', 'dsbabababa', 'dtbabababa',
            'dubabababa', 'dvbabababa', 'dwbabababa', 'dxbabababa', 'dybabababa', 'dzbabababa', 'eababababa',
            'ebbabababa', 'ecbabababa', 'edbabababa', 'eebabababa', 'efbabababa', 'egbabababa', 'ehbabababa',
            'eibabababa', 'ejbabababa', 'ekbabababa', 'elbabababa', 'embabababa', 'enbabababa', 'eobabababa',
            'epbabababa', 'eqbabababa', 'erbabababa', 'esbabababa', 'etbabababa', 'eubabababa', 'evbabababa',
            'ewbabababa', 'exbabababa', 'eybabababa', 'ezbabababa', 'fababababa', 'fbbabababa', 'fcbabababa',
            'fdbabababa', 'febabababa', 'ffbabababa', 'fgbabababa', 'fhbabababa', 'fibabababa', 'fjbabababa',
            'fkbabababa', 'flbabababa', 'fmbabababa', 'fnbabababa', 'fobabababa', 'fpbabababa', 'fqbabababa',
            'frbabababa', 'fsbabababa', 'ftbabababa', 'fubabababa', 'fvbabababa', 'fwbabababa', 'fxbabababa',
            'fybabababa', 'fzbabababa', 'gababababa', 'gbbabababa', 'gcbabababa', 'gdbabababa', 'gebabababa',
            'gfbabababa', 'ggbabababa', 'ghbabababa', 'gibabababa', 'gjbabababa', 'gkbabababa', 'glbabababa',
            'gmbabababa', 'gnbabababa', 'gobabababa', 'gpbabababa', 'gqbabababa', 'grbabababa', 'gsbabababa',
            'gtbabababa', 'gubabababa', 'gvbabababa', 'gwbabababa', 'gxbabababa', 'gybabababa', 'gzbabababa',
            'hababababa', 'hbbabababa', 'hcbabababa', 'hdbabababa', 'hebabababa', 'hfbabababa', 'hgbabababa',
            'hhbabababa', 'hibabababa', 'hjbabababa', 'hkbabababa', 'hlbabababa', 'hmbabababa', 'hnbabababa',
            'hobabababa', 'hpbabababa', 'hqbabababa', 'hrbabababa', 'hsbabababa', 'htbabababa', 'hubabababa',
            'hvbabababa', 'hwbabababa', 'hxbabababa', 'hybabababa', 'hzbabababa', 'iababababa', 'ibbabababa',
            'icbabababa', 'idbabababa', 'iebabababa', 'ifbabababa', 'igbabababa', 'ihbabababa', 'iibabababa',
            'ijbabababa', 'ikbabababa', 'ilbabababa', 'imbabababa', 'inbabababa', 'iobabababa', 'ipbabababa',
            'iqbabababa', 'irbabababa', 'isbabababa', 'itbabababa', 'iubabababa', 'ivbabababa', 'iwbabababa',
            'ixbabababa', 'iybabababa', 'izbabababa', 'jababababa', 'jbbabababa', 'jcbabababa', 'jdbabababa',
            'jebabababa', 'jfbabababa', 'jgbabababa', 'jhbabababa', 'jibabababa', 'jjbabababa', 'jkbabababa',
            'jlbabababa', 'jmbabababa', 'jnbabababa', 'jobabababa', 'jpbabababa', 'jqbabababa', 'jrbabababa',
            'jsbabababa', 'jtbabababa', 'jubabababa', 'jvbabababa', 'jwbabababa', 'jxbabababa', 'jybabababa',
            'jzbabababa', 'kababababa', 'kbbabababa', 'kcbabababa', 'kdbabababa', 'kebabababa', 'kfbabababa',
            'kgbabababa', 'khbabababa', 'kibabababa', 'kjbabababa', 'kkbabababa', 'klbabababa', 'kmbabababa',
            'knbabababa', 'kobabababa', 'kpbabababa', 'kqbabababa', 'krbabababa', 'ksbabababa', 'ktbabababa',
            'kubabababa', 'kvbabababa', 'kwbabababa', 'kxbabababa', 'kybabababa', 'kzbabababa', 'lababababa',
            'lbbabababa', 'lcbabababa', 'ldbabababa', 'lebabababa', 'lfbabababa', 'lgbabababa', 'lhbabababa',
            'libabababa', 'ljbabababa', 'lkbabababa', 'llbabababa', 'lmbabababa', 'lnbabababa', 'lobabababa',
            'lpbabababa', 'lqbabababa', 'lrbabababa', 'lsbabababa', 'ltbabababa', 'lubabababa', 'lvbabababa',
            'lwbabababa', 'lxbabababa', 'lybabababa', 'lzbabababa', 'mababababa', 'mbbabababa', 'mcbabababa',
            'mdbabababa', 'mebabababa', 'mfbabababa', 'mgbabababa', 'mhbabababa', 'mibabababa', 'mjbabababa',
            'mkbabababa', 'mlbabababa', 'mmbabababa', 'mnbabababa', 'mobabababa', 'mpbabababa', 'mqbabababa',
            'mrbabababa', 'msbabababa', 'mtbabababa', 'mubabababa', 'mvbabababa', 'mwbabababa', 'mxbabababa',
            'mybabababa', 'mzbabababa', 'nababababa', 'nbbabababa', 'ncbabababa', 'ndbabababa', 'nebabababa',
            'nfbabababa', 'ngbabababa', 'nhbabababa', 'nibabababa', 'njbabababa', 'nkbabababa', 'nlbabababa',
            'nmbabababa', 'nnbabababa', 'nobabababa', 'npbabababa', 'nqbabababa', 'nrbabababa', 'nsbabababa',
            'ntbabababa', 'nubabababa', 'nvbabababa', 'nwbabababa', 'nxbabababa', 'nybabababa', 'nzbabababa',
            'oababababa', 'obbabababa', 'ocbabababa', 'odbabababa', 'oebabababa', 'ofbabababa', 'ogbabababa',
            'ohbabababa', 'oibabababa', 'ojbabababa', 'okbabababa', 'olbabababa', 'ombabababa', 'onbabababa',
            'oobabababa', 'opbabababa', 'oqbabababa', 'orbabababa', 'osbabababa', 'otbabababa', 'oubabababa',
            'ovbabababa', 'owbabababa', 'oxbabababa', 'oybabababa', 'ozbabababa', 'pababababa', 'pbbabababa',
            'pcbabababa', 'pdbabababa', 'pebabababa', 'pfbabababa', 'pgbabababa', 'phbabababa', 'pibabababa',
            'pjbabababa', 'pkbabababa', 'plbabababa', 'pmbabababa', 'pnbabababa', 'pobabababa', 'ppbabababa',
            'pqbabababa', 'prbabababa', 'psbabababa', 'ptbabababa', 'pubabababa', 'pvbabababa', 'pwbabababa',
            'pxbabababa', 'pybabababa', 'pzbabababa', 'qababababa', 'qbbabababa', 'qcbabababa', 'qdbabababa',
            'qebabababa', 'qfbabababa', 'qgbabababa', 'qhbabababa', 'qibabababa', 'qjbabababa', 'qkbabababa',
            'qlbabababa', 'qmbabababa', 'qnbabababa', 'qobabababa', 'qpbabababa', 'qqbabababa', 'qrbabababa',
            'qsbabababa', 'qtbabababa', 'qubabababa', 'qvbabababa', 'qwbabababa', 'qxbabababa', 'qybabababa',
            'qzbabababa', 'rababababa', 'rbbabababa', 'rcbabababa', 'rdbabababa', 'rebabababa', 'rfbabababa',
            'rgbabababa', 'rhbabababa', 'ribabababa', 'rjbabababa', 'rkbabababa', 'rlbabababa', 'rmbabababa',
            'rnbabababa', 'robabababa', 'rpbabababa', 'rqbabababa', 'rrbabababa', 'rsbabababa', 'rtbabababa',
            'rubabababa', 'rvbabababa', 'rwbabababa', 'rxbabababa', 'rybabababa', 'rzbabababa', 'sababababa',
            'sbbabababa', 'scbabababa', 'sdbabababa', 'sebabababa', 'sfbabababa', 'sgbabababa', 'shbabababa',
            'sibabababa', 'sjbabababa', 'skbabababa', 'slbabababa', 'smbabababa', 'snbabababa', 'sobabababa',
            'spbabababa', 'sqbabababa', 'srbabababa', 'ssbabababa', 'stbabababa', 'subabababa', 'svbabababa',
            'swbabababa', 'sxbabababa', 'sybabababa', 'szbabababa', 'tababababa', 'tbbabababa', 'tcbabababa',
            'tdbabababa', 'tebabababa', 'tfbabababa', 'tgbabababa', 'thbabababa', 'tibabababa', 'tjbabababa',
            'tkbabababa', 'tlbabababa', 'tmbabababa', 'tnbabababa', 'tobabababa', 'tpbabababa', 'tqbabababa',
            'trbabababa', 'tsbabababa', 'ttbabababa', 'tubabababa', 'tvbabababa', 'twbabababa', 'txbabababa',
            'tybabababa', 'tzbabababa', 'uababababa', 'ubbabababa', 'ucbabababa', 'udbabababa', 'uebabababa',
            'ufbabababa', 'ugbabababa', 'uhbabababa', 'uibabababa', 'ujbabababa', 'ukbabababa', 'ulbabababa',
            'umbabababa', 'unbabababa', 'uobabababa', 'upbabababa', 'uqbabababa', 'urbabababa', 'usbabababa',
            'utbabababa', 'uubabababa', 'uvbabababa', 'uwbabababa', 'uxbabababa', 'uybabababa', 'uzbabababa',
            'vababababa', 'vbbabababa', 'vcbabababa', 'vdbabababa', 'vebabababa', 'vfbabababa', 'vgbabababa',
            'vhbabababa', 'vibabababa', 'vjbabababa', 'vkbabababa', 'vlbabababa', 'vmbabababa', 'vnbabababa',
            'vobabababa', 'vpbabababa', 'vqbabababa', 'vrbabababa', 'vsbabababa', 'vtbabababa', 'vubabababa',
            'vvbabababa', 'vwbabababa', 'vxbabababa', 'vybabababa', 'vzbabababa', 'wababababa', 'wbbabababa',
            'wcbabababa', 'wdbabababa', 'webabababa', 'wfbabababa', 'wgbabababa', 'whbabababa', 'wibabababa',
            'wjbabababa', 'wkbabababa', 'wlbabababa', 'wmbabababa', 'wnbabababa', 'wobabababa', 'wpbabababa',
            'wqbabababa', 'wrbabababa', 'wsbabababa', 'wtbabababa', 'wubabababa', 'wvbabababa', 'wwbabababa',
            'wxbabababa', 'wybabababa', 'wzbabababa', 'xababababa', 'xbbabababa', 'xcbabababa', 'xdbabababa',
            'xebabababa', 'xfbabababa', 'xgbabababa', 'xhbabababa', 'xibabababa', 'xjbabababa', 'xkbabababa',
            'xlbabababa', 'xmbabababa', 'xnbabababa', 'xobabababa', 'xpbabababa', 'xqbabababa', 'xrbabababa',
            'xsbabababa', 'xtbabababa', 'xubabababa', 'xvbabababa', 'xwbabababa', 'xxbabababa', 'xybabababa',
            'xzbabababa', 'yababababa', 'ybbabababa', 'ycbabababa', 'ydbabababa', 'yebabababa', 'yfbabababa',
            'ygbabababa', 'yhbabababa', 'yibabababa', 'yjbabababa', 'ykbabababa', 'ylbabababa', 'ymbabababa',
            'ynbabababa', 'yobabababa', 'ypbabababa', 'yqbabababa', 'yrbabababa', 'ysbabababa', 'ytbabababa',
            'yubabababa', 'yvbabababa', 'ywbabababa', 'yxbabababa', 'yybabababa', 'yzbabababa', 'zababababa',
            'zbbabababa', 'zcbabababa', 'zdbabababa', 'zebabababa', 'zfbabababa', 'zgbabababa', 'zhbabababa',
            'zibabababa', 'zjbabababa', 'zkbabababa', 'zlbabababa', 'zmbabababa', 'znbabababa', 'zobabababa',
            'zpbabababa', 'zqbabababa', 'zrbabababa', 'zsbabababa', 'ztbabababa', 'zubabababa', 'zvbabababa',
            'zwbabababa', 'zxbabababa', 'zybabababa', 'zzbabababa']
    )
]


class TrieNode:
    def __init__(self):
        self.word = ''
        self.children = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.word = word


# T=M3ᴸ,S=N
def main(grid, words):
    m, n = len(grid), len(grid[0])
    offsets = (0, 1), (0, -1), (-1, 0), (1, 0)
    res, trie = [], Trie()
    for word in words:
        trie.insert(word)

    def dfs(ri, ci, parent):
        if ri in [-1, m] or ci in [-1, n] or grid[ri][ci] == '1':
            return
        child = parent.children[ord(grid[ri][ci]) - ord('a')]
        if not child:
            return
        if child.word:
            res.append(child.word)
            child.word = ''
        char = grid[ri][ci]
        grid[ri][ci] = '1'
        for i, j in offsets:
            dfs(ri + i, ci + j, child)
        grid[ri][ci] = char

    for ri in range(m):
        for ci in range(n):
            dfs(ri, ci, trie.root)
    return res


for grid, words in inputs:
    print(main(grid, words))
