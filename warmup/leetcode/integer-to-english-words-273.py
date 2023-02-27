def main(num):
    below20 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
               'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    if not num:
        return 'Zero'

    def helper(num):
        if num < 20:
            res = below20[num]
        elif num < 100:
            res = tens[num // 10] + ' ' + helper(num % 10)
        elif num < 1000:
            res = helper(num // 100) + ' Hundred ' + helper(num % 100)
        elif num < 1000000:
            res = helper(num // 1000) + ' Thousand ' + helper(num % 1000)
        elif num < 1000000000:
            res = helper(num // 1000000) + ' Million ' + helper(num % 1000000)
        else:
            res = helper(num // 1000000000) + ' Billion ' + helper(num % 1000000000)
        return res.rstrip()

    return helper(num)


for num in [
    0, 10, 20, 100, 1000, 1000000, 1000000000,
    4, 9, 62, 84, 257, 972, 1452, 12345,
    1234567, 1234567891, 54868,
    50868, 500689
]:
    print(main(num))
