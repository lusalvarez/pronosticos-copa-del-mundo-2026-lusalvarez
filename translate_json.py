import json

# Dictionnaire de traduction
translations = {
    'France': 'Francia', 'Allemagne': 'Alemania', 'Angleterre': 'Inglaterra',
    'Espagne': 'España', 'Italie': 'Italia', 'Pays-Bas': 'Países Bajos',
    'Belgique': 'Bélgica', 'Portugal': 'Portugal', 'Croatie': 'Croacia',
    'Suisse': 'Suiza', 'Danemark': 'Dinamarca', 'Suède': 'Suecia',
    'Norvège': 'Noruega', 'Autriche': 'Austria', 'Tchéquie': 'Chequia',
    'Pologne': 'Polonia', 'Serbie': 'Serbia', 'Slovénie': 'Eslovenia',
    'Bosnie-Herzégovine': 'Bosnia y Herzegovina', 'Finlande': 'Finlandia',
    'Écosse': 'Escocia', 'Irlande': 'Irlanda', 'Brésil': 'Brasil',
    'Argentine': 'Argentina', 'Uruguay': 'Uruguay', 'Colombie': 'Colombia',
    'Chili': 'Chile', 'Paraguay': 'Paraguay', 'Équateur': 'Ecuador',
    'Pérou': 'Perú', 'Mexique': 'México', 'États-Unis': 'Estados Unidos',
    'Canada': 'Canadá', 'Costa Rica': 'Costa Rica', 'Panama': 'Panamá',
    'Jamaïque': 'Jamaica', 'Haïti': 'Haití', 'Maroc': 'Marruecos',
    'Sénégal': 'Senegal', 'Tunisie': 'Túnez', 'Algérie': 'Argelia',
    'Égypte': 'Egipto', 'Ghana': 'Ghana', 'Nigeria': 'Nigeria',
    'Cameroun': 'Camerún', "Côte d'Ivoire": 'Costa de Marfil',
    'Afrique du Sud': 'Sudáfrica', 'RD Congo': 'RD Congo',
    'Japon': 'Japón', 'Corée du Sud': 'Corea del Sur',
    'Australie': 'Australia', 'Iran': 'Irán', 'Arabie Saoudite': 'Arabia Saudita',
    'Irak': 'Irak', 'Jordanie': 'Jordania', 'Ouzbékistan': 'Uzbekistán',
    'Turquie': 'Turquía', 'Qatar': 'Catar', 'Nouvelle-Zélande': 'Nueva Zelanda',
    'Curaçao': 'Curazao', 'Cap-Vert': 'Cabo Verde'
}

# Lire le fichier JSON
with open('matches-phase-groupes-2026.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Traduire les noms d'équipes
count = 0
for match in data['matches']:
    if match['equipe_domicile'] in translations:
        match['equipe_domicile'] = translations[match['equipe_domicile']]
        count += 1
    if match['equipe_exterieur'] in translations:
        match['equipe_exterieur'] = translations[match['equipe_exterieur']]
        count += 1

# Sauvegarder
with open('matches-phase-groupes-2026.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'OK - JSON traduit: {count} noms de pays traduits en espagnol')

# Made with Bob
