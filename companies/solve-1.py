import requests

url = 'https://jsonmock.hackerrank.com/api/movies/search/?Title='


def main(substr):
    res, totalPages = [], requests.get(url + substr).json()['total_pages']
    for pageNumber in range(1, totalPages + 1):
        for response in requests.get(url + substr + '&page=' + str(pageNumber)).json()['data']:
            res.append(response['Title'])
    res.sort()
    return res


for substr in [
    'spiderman'
]:
    print(main(substr))
