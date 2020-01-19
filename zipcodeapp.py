import urllib.request
def find_name(line):
    start = 9
    stop = line.index(' ZIP')
    name = line[start: stop + 1]
    return name


def find_pop(line):
    start = line.index('Total population</dt><dd>') + 25
    c = 0
    population = ''
    while line[c + start] != '<':
        char = line[c + start]
        if char.isdigit() or char == ',':
            population += char
        c += 1
    return population


def main():
    in_zip = input('Please enter your zip code: ')
    zip_url = 'http://www.uszip.com/zip/{}'.format(in_zip)
    zip_url = urllib.request.urlopen(zip_url)
    for line in zip_url:
        line = str(line)
        if "b'<title>" in line:
            name = find_name(line)
        elif 'Total population' in line:
            population = find_pop(line)
    print('Name: {1}\nPopulation: {0}'.format(population, name))


if __name__ == '__main__':
    try:
        main()
    except:
        print('Something went wrong')
