#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de récupération des matchs de la Coupe du Monde 2026 depuis le site FIFA
Génère un fichier JSON compatible avec l'application de pronostics
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import sys

def scrape_fifa_matches():
    """
    Récupère les matchs depuis le site FIFA
    """
    print("🌐 Connexion au site FIFA...")
    
    # URL du calendrier de la Coupe du Monde 2026
    # Note: Cette URL devra être mise à jour avec l'URL réelle une fois disponible
    url = "https://www.fifa.com/fifaplus/en/tournaments/mens/worldcup/canadamexicousa2026/matches"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        print("✅ Connexion réussie !")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de connexion: {e}")
        print("\n💡 Le site FIFA n'est peut-être pas encore disponible pour la Coupe du Monde 2026.")
        print("   Utilisation des données de démonstration à la place...\n")
        return generate_demo_data()
    
    print("📄 Analyse de la page...")
    soup = BeautifulSoup(response.content, 'html.parser')
    
    matches = []
    
    # Recherche des matchs dans la page
    # Note: Les sélecteurs CSS devront être ajustés selon la structure réelle du site FIFA
    match_elements = soup.find_all('div', class_='match-card')  # À ajuster
    
    if not match_elements:
        print("⚠️  Aucun match trouvé avec les sélecteurs actuels.")
        print("   Le site FIFA a peut-être changé de structure.")
        print("   Utilisation des données de démonstration...\n")
        return generate_demo_data()
    
    for match_elem in match_elements:
        try:
            # Extraction des informations (à ajuster selon la structure HTML réelle)
            home_team = match_elem.find('span', class_='home-team').text.strip()
            away_team = match_elem.find('span', class_='away-team').text.strip()
            date_str = match_elem.find('time', class_='match-date')['datetime']
            stage = match_elem.find('span', class_='match-stage').text.strip()
            
            # Conversion de la date au format requis
            date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            formatted_date = date_obj.strftime('%Y-%m-%dT%H:%M')
            
            matches.append({
                'homeTeam': home_team,
                'awayTeam': away_team,
                'date': formatted_date,
                'stage': stage
            })
            
        except Exception as e:
            print(f"⚠️  Erreur lors de l'extraction d'un match: {e}")
            continue
    
    if matches:
        print(f"✅ {len(matches)} match(s) récupéré(s) !")
    else:
        print("⚠️  Aucun match extrait. Utilisation des données de démonstration...")
        return generate_demo_data()
    
    return matches


def generate_demo_data():
    """
    Génère des données de démonstration basées sur le format attendu de la Coupe du Monde 2026
    """
    print("📋 Génération de données de démonstration...")
    
    matches = [
        {
            "homeTeam": "Mexique",
            "awayTeam": "Canada",
            "date": "2026-06-11T18:00",
            "stage": "Match d'ouverture - Groupe A"
        },
        {
            "homeTeam": "États-Unis",
            "awayTeam": "Pays de Galles",
            "date": "2026-06-11T21:00",
            "stage": "Phase de groupes - Groupe A"
        },
        {
            "homeTeam": "Argentine",
            "awayTeam": "Australie",
            "date": "2026-06-12T15:00",
            "stage": "Phase de groupes - Groupe B"
        },
        {
            "homeTeam": "France",
            "awayTeam": "Danemark",
            "date": "2026-06-12T18:00",
            "stage": "Phase de groupes - Groupe C"
        },
        {
            "homeTeam": "Brésil",
            "awayTeam": "Serbie",
            "date": "2026-06-12T21:00",
            "stage": "Phase de groupes - Groupe C"
        },
        {
            "homeTeam": "Espagne",
            "awayTeam": "Croatie",
            "date": "2026-06-13T15:00",
            "stage": "Phase de groupes - Groupe D"
        },
        {
            "homeTeam": "Allemagne",
            "awayTeam": "Japon",
            "date": "2026-06-13T18:00",
            "stage": "Phase de groupes - Groupe D"
        },
        {
            "homeTeam": "Angleterre",
            "awayTeam": "Iran",
            "date": "2026-06-13T21:00",
            "stage": "Phase de groupes - Groupe E"
        },
        {
            "homeTeam": "Pays-Bas",
            "awayTeam": "Sénégal",
            "date": "2026-06-14T15:00",
            "stage": "Phase de groupes - Groupe E"
        },
        {
            "homeTeam": "Portugal",
            "awayTeam": "Ghana",
            "date": "2026-06-14T18:00",
            "stage": "Phase de groupes - Groupe F"
        },
        {
            "homeTeam": "Belgique",
            "awayTeam": "Suisse",
            "date": "2026-06-14T21:00",
            "stage": "Phase de groupes - Groupe F"
        },
        {
            "homeTeam": "Uruguay",
            "awayTeam": "Corée du Sud",
            "date": "2026-06-15T15:00",
            "stage": "Phase de groupes - Groupe G"
        },
        {
            "homeTeam": "Pologne",
            "awayTeam": "Arabie Saoudite",
            "date": "2026-06-15T18:00",
            "stage": "Phase de groupes - Groupe G"
        },
        {
            "homeTeam": "Italie",
            "awayTeam": "Cameroun",
            "date": "2026-06-15T21:00",
            "stage": "Phase de groupes - Groupe H"
        },
        {
            "homeTeam": "Colombie",
            "awayTeam": "Tunisie",
            "date": "2026-06-16T15:00",
            "stage": "Phase de groupes - Groupe H"
        }
    ]
    
    print(f"✅ {len(matches)} matchs de démonstration générés")
    return matches


def save_to_json(matches, filename='matches-fifa-2026.json'):
    """
    Sauvegarde les matchs dans un fichier JSON
    """
    data = {
        'tournament': 'Coupe du Monde FIFA 2026',
        'source': 'FIFA.com',
        'generated_at': datetime.now().isoformat(),
        'matches': matches
    }
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"\n✅ Fichier '{filename}' créé avec succès !")
        print(f"📊 {len(matches)} match(s) sauvegardé(s)")
        return True
    except Exception as e:
        print(f"\n❌ Erreur lors de la sauvegarde: {e}")
        return False


def main():
    """
    Fonction principale
    """
    print("=" * 60)
    print("🏆 SCRAPER FIFA - COUPE DU MONDE 2026")
    print("=" * 60)
    print()
    
    # Récupération des matchs
    matches = scrape_fifa_matches()
    
    if not matches:
        print("\n❌ Aucun match à sauvegarder.")
        sys.exit(1)
    
    # Sauvegarde dans un fichier JSON
    success = save_to_json(matches)
    
    if success:
        print("\n" + "=" * 60)
        print("✅ TERMINÉ !")
        print("=" * 60)
        print("\n📝 Prochaines étapes :")
        print("   1. Ouvrez votre application de pronostics")
        print("   2. Cliquez sur '📥 Importer depuis un fichier JSON'")
        print("   3. Sélectionnez le fichier 'matches-fifa-2026.json'")
        print("   4. Confirmez l'import")
        print("\n🎉 Vos matchs seront importés automatiquement !")
        print()
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()

# Made with Bob
