# T=n,S=n
def main(mapping):
    start = None
    sources = mapping.keys()
    destinations = set(mapping.values())
    for source in sources:
        if source not in destinations:
            start = source
            break
    while start in mapping:
        print(start, mapping[start])
        start = mapping[start]


for mapping in [
    {
        'Chennai': 'Bangalore',
        'Bombay': 'Delhi',
        'Goa': 'Chennai',
        'Delhi': 'Goa'
    }
]:
    main(mapping)
