import csv
with open('songs.csv', 'w+') as songsfile:
    fieldnames = ['Song', 'Year']
    writer = csv.DictWriter(songsfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Song': 'Colour and Shape',
                     'Year': 2000})
    writer.writerow({'Song': 'Long Distance Blues',
                     'Year': 2003})
    writer.writerow({'Song': 'Reconsider Baby',
                     'Year': 2004})
    writer.writerow({'Song': 'Your Funeral My Trial',
                     'Year': 2006})
    writer.writerow({'Song': 'Another Kind of Love',
                     'Year': 2007})
    writer.writerow({'Song': 'India / Mountain Time',
                     'Year': 2008})
with open('songs.csv') as songsfile:
    reader = csv.DictReader(songsfile)
    for heading in reader.fieldnames:
        print(heading, end=' ')
    print('\n')
    for row in reader:
        print(row['Song'], row['Year'])
