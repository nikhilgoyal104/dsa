# T=n,S=n
def main(mapping):
    start, sources, destinations = None, mapping.keys(), set(mapping.values())
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
