import json

# Lire le fichier JSON
with open('matches-phase-groupes-2026.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Créer le contenu JavaScript
js_content = '''// Fichier de données partagé entre index.html et participant.html
// Les deux pages chargent ce fichier pour avoir les mêmes matchs

const MATCHES_DATA = {
  "tournament": "Copa del Mundo FIFA 2026",
  "format": "48 equipos, 12 grupos de 4 equipos",
  "totalMatches": 72,
  "matches": [
'''

# Convertir chaque match
for match in data['matches']:
    date_time = f"{match['date']}T{match['heure']}"
    js_content += f'''    {{
      "homeTeam": "{match['equipe_domicile']}",
      "awayTeam": "{match['equipe_exterieur']}",
      "date": "{date_time}",
      "stage": "Fase de grupos - Grupo {match['groupe']}",
      "group": "{match['groupe']}"
    }},
'''

# Enlever la dernière virgule et fermer
js_content = js_content.rstrip(',\n') + '\n  ]\n};\n\n// Made with Bob\n'

# Écrire le fichier
with open('matches-data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print('OK - matches-data.js mis a jour avec 72 matchs')

# Made with Bob
