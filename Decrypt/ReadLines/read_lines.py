def read_lines(file):

    with open(file, 'r') as opened_file:
        lignes = opened_file.readlines()
    opened_file.close()

    return [ligne.strip() for ligne in lignes]
