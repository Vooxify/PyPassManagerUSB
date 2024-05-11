from cryptography.fernet import Fernet
from Decrypt.ReadLines.datas_extraction import datas_extraction

# Récupérer le dictionnaire à partir de la fonction datas_extraction
dictionnaire = datas_extraction()


# Fonction pour déchiffrer un message à l'aide de la clé
def decrypt_message(key, encrypted_message):
    # Initialiser l'objet Fernet avec la clé
    f = Fernet(key)
    # Déchiffrer le message
    decrypted_message = f.decrypt(encrypted_message)
    # Retourner le message déchiffré sous forme de chaîne de caractères
    return decrypted_message.decode()


# Fonction pour déchiffrer le fichier
def decrypt_file():
    # Parcourir chaque paire clé-valeur dans le dictionnaire
    for key, value in dictionnaire.items():
        # Si la valeur est une liste
        if isinstance(value, list):
            # Initialiser une liste pour stocker les données déchiffrées
            decrypted_data_list = []
            # Parcourir chaque élément de la liste
            for item in value:
                # Déchiffrer chaque élément de la liste
                decrypted_data = decrypt_message(key, item.encode())
                # Ajouter les données déchiffrées à la liste
                decrypted_data_list.append(decrypted_data)
            # Afficher les résultats dans l'ordre Domain, Username, Password
            print(
                f"Domain: {decrypted_data_list[0]}\nUsername: {decrypted_data_list[1]}\nPassword: {decrypted_data_list[2]}\n----------------------------")
        else:
            continue


def run():
    decrypt_file()
