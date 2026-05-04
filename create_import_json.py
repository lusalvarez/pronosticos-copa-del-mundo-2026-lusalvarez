import json

# Lire le fichier source
with open('matches-phase-groupes-2026.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Créer le format attendu par l'application
export_data = {
    "matches": []
}

for match in data['matches']:
    export_data["matches"].append({
        "homeTeam": match['equipe_domicile'],
        "awayTeam": match['equipe_exterieur'],
        "date": f"{match['date']}T{match['heure']}",
        "stage": f"Fase de grupos - Grupo {match['groupe']}"
    })

# Sauvegarder dans un nouveau fichier pour l'import
with open('matches-import-espanol.json', 'w', encoding='utf-8') as f:
    json.dump(export_data, f, ensure_ascii=False, indent=2)

print(f'OK - Fichier matches-import-espanol.json cree avec {len(export_data["matches"])} matchs')
print('Utilisez ce fichier pour importer dans l\'interface admin')

# Made with Bob
