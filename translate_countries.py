import re

# Dictionnaire de traduction français -> espagnol
translations = {
    "France": "Francia",
    "Allemagne": "Alemania",
    "Angleterre": "Inglaterra",
    "Espagne": "España",
    "Italie": "Italia",
    "Pays-Bas": "Países Bajos",
    "Belgique": "Bélgica",
    "Portugal": "Portugal",
    "Croatie": "Croacia",
    "Suisse": "Suiza",
    "Danemark": "Dinamarca",
    "Suède": "Suecia",
    "Norvège": "Noruega",
    "Autriche": "Austria",
    "République Tchèque": "República Checa",
    "Tchéquie": "Chequia",
    "Pologne": "Polonia",
    "Serbie": "Serbia",
    "Slovénie": "Eslovenia",
    "Bosnie-Herzégovine": "Bosnia y Herzegovina",
    "Finlande": "Finlandia",
    "Écosse": "Escocia",
    "Irlande": "Irlanda",
    "Brésil": "Brasil",
    "Argentine": "Argentina",
    "Uruguay": "Uruguay",
    "Colombie": "Colombia",
    "Chili": "Chile",
    "Paraguay": "Paraguay",
    "Équateur": "Ecuador",
    "Pérou": "Perú",
    "Mexique": "México",
    "États-Unis": "Estados Unidos",
    "Canada": "Canadá",
    "Costa Rica": "Costa Rica",
    "Panama": "Panamá",
    "Jamaïque": "Jamaica",
    "Trinidad et Tobago": "Trinidad y Tobago",
    "Haïti": "Haití",
    "Maroc": "Marruecos",
    "Sénégal": "Senegal",
    "Tunisie": "Túnez",
    "Algérie": "Argelia",
    "Égypte": "Egipto",
    "Ghana": "Ghana",
    "Nigeria": "Nigeria",
    "Cameroun": "Camerún",
    "Côte d'Ivoire": "Costa de Marfil",
    "Afrique du Sud": "Sudáfrica",
    "RD Congo": "RD Congo",
    "Japon": "Japón",
    "Corée du Sud": "Corea del Sur",
    "Australie": "Australia",
    "Iran": "Irán",
    "Arabie Saoudite": "Arabia Saudita",
    "Irak": "Irak",
    "Jordanie": "Jordania",
    "Ouzbékistan": "Uzbekistán",
    "Turquie": "Turquía",
    "Qatar": "Catar",
    "Nouvelle-Zélande": "Nueva Zelanda",
    "Curaçao": "Curazao",
    "Cap-Vert": "Cabo Verde"
}

# Lire le fichier
with open('matches-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Remplacer chaque pays
for french, spanish in translations.items():
    # Remplacer dans les chaînes entre guillemets
    content = content.replace(f'"{french}"', f'"{spanish}"')

# Écrire le fichier modifié
with open('matches-data.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK - Traduction terminee: tous les pays sont maintenant en espagnol")

# Made with Bob
