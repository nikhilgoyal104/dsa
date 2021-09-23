from collections import Counter


# T=n,S=n
def main(cpdomains):
    freq = Counter()
    for cpdomain in cpdomains:
        count, domain = cpdomain.split(' ')
        subdomains = domain.split('.')
        for i in range(len(subdomains)):
            freq['.'.join(subdomains[i:])] += int(count)
    return [str(count) + ' ' + subdomain for subdomain, count in freq.items()]


for cpdomains in [
    ['9001 discuss.leetcode.com'],
    ['900 google.mail.com', '50 yahoo.com', '1 intel.mail.com', '5 wiki.org']
]:
    print(main(cpdomains))
