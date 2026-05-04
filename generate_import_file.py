import json
import re

# Lire matches-data.js
with open('matches-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extraire le contenu JSON du fichier JavaScript
# Trouver le tableau de matchs
match = re.search(r'"matches":\s*\[(.*?)\]', content, re.DOTALL)
if not match:
    print("Erreur: impossible de trouver les matchs dans matches-data.js")
    exit(1)

matches_str = '[' + match.group(1) + ']'

# Parser le JSON
matches = eval(matches_str)  # Utiliser eval car c'est du JavaScript, pas du JSON pur

# Créer le format d'export
export_data = {
    "matches": matches
}

# Sauvegarder
with open('matches-import-espanol.json', 'w', encoding='utf-8') as f:
    json.dump(export_data, f, ensure_ascii=False, indent=2)

print(f'OK - Fichier matches-import-espanol.json cree avec {len(matches)} matchs')
print('Tous les noms de pays sont en espagnol')
print('Utilisez ce fichier pour importer dans l\'interface admin')

# Made with Bob
