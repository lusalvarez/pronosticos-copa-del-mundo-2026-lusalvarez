# 🐍 Guide : Utiliser le script Python pour récupérer les matchs FIFA

## 🎯 Objectif
Ce script Python récupère automatiquement les matchs de la Coupe du Monde 2026 depuis le site officiel FIFA et génère un fichier JSON prêt à être importé dans votre application.

---

## 📋 Prérequis

### 1. Installer Python
Si Python n'est pas installé sur votre ordinateur :

**Windows :**
1. Téléchargez Python depuis : https://www.python.org/downloads/
2. Lancez l'installeur
3. ⚠️ **IMPORTANT** : Cochez "Add Python to PATH"
4. Cliquez sur "Install Now"

**Vérifier l'installation :**
```bash
python --version
```
Vous devriez voir : `Python 3.x.x`

---

## 🚀 Installation et utilisation

### Étape 1 : Ouvrir un terminal dans le dossier

**Windows :**
1. Ouvrez l'explorateur de fichiers
2. Naviguez vers le dossier `pronostics-coupe-du-monde`
3. Dans la barre d'adresse, tapez `cmd` et appuyez sur Entrée
4. Un terminal s'ouvre dans le bon dossier

**Ou depuis VS Code :**
1. Ouvrez le dossier dans VS Code
2. Menu Terminal → New Terminal
3. Vous êtes déjà dans le bon dossier

---

### Étape 2 : Installer les dépendances

Dans le terminal, exécutez :

```bash
pip install -r requirements.txt
```

Cela installe :
- `requests` - Pour faire des requêtes HTTP
- `beautifulsoup4` - Pour analyser le HTML
- `lxml` - Parser HTML rapide

⏱️ Temps d'installation : ~30 secondes

---

### Étape 3 : Exécuter le script

Dans le terminal, exécutez :

```bash
python scraper_fifa.py
```

**Ce qui se passe :**
1. 🌐 Le script se connecte au site FIFA
2. 📄 Il analyse la page des matchs
3. 📊 Il extrait les informations (équipes, dates, phases)
4. 💾 Il génère le fichier `matches-fifa-2026.json`

---

## 📊 Résultat

Le script crée un fichier `matches-fifa-2026.json` avec ce format :

```json
{
  "tournament": "Coupe du Monde FIFA 2026",
  "source": "FIFA.com",
  "generated_at": "2026-04-30T15:30:00",
  "matches": [
    {
      "homeTeam": "Mexique",
      "awayTeam": "Canada",
      "date": "2026-06-11T18:00",
      "stage": "Match d'ouverture - Groupe A"
    }
  ]
}
```

---

## 📥 Importer dans l'application

1. Ouvrez votre application de pronostics
2. Allez dans l'**Écran administrateur**
3. Cliquez sur **"📥 Importer depuis un fichier JSON"**
4. Sélectionnez le fichier `matches-fifa-2026.json`
5. Confirmez l'import
6. ✅ Les matchs sont maintenant dans votre application !

---

## ⚠️ Notes importantes

### Si le site FIFA n'est pas encore disponible

Le script génère automatiquement des **données de démonstration** avec :
- 15 matchs de la phase de groupes
- Équipes qualifiées probables
- Dates réalistes (juin 2026)

**Pourquoi ?**
- La Coupe du Monde 2026 commence en juin 2026
- Le calendrier complet n'est peut-être pas encore publié
- Le tirage au sort n'a peut-être pas encore eu lieu

### Quand réexécuter le script ?

Réexécutez le script pour obtenir les données à jour :
- ✅ Après le tirage au sort officiel
- ✅ Quand le calendrier complet est publié
- ✅ Pour mettre à jour les horaires

---

## 🔧 Personnalisation du script

### Modifier l'URL source

Si l'URL du site FIFA change, modifiez la ligne 21 dans `scraper_fifa.py` :

```python
url = "https://www.fifa.com/fifaplus/en/tournaments/mens/worldcup/canadamexicousa2026/matches"
```

### Ajuster les sélecteurs CSS

Si la structure HTML du site FIFA change, ajustez les lignes 42-45 :

```python
home_team = match_elem.find('span', class_='home-team').text.strip()
away_team = match_elem.find('span', class_='away-team').text.strip()
```

**Comment trouver les bons sélecteurs ?**
1. Ouvrez le site FIFA dans Chrome/Firefox
2. Clic droit sur un match → "Inspecter"
3. Trouvez les classes CSS utilisées
4. Mettez à jour le script

---

## 🐛 Résolution de problèmes

### Erreur : `python` n'est pas reconnu

**Solution :** Python n'est pas dans le PATH
- Réinstallez Python en cochant "Add Python to PATH"
- Ou utilisez `py` au lieu de `python` :
  ```bash
  py scraper_fifa.py
  ```

### Erreur : `No module named 'requests'`

**Solution :** Les dépendances ne sont pas installées
```bash
pip install -r requirements.txt
```

### Erreur de connexion au site FIFA

**Causes possibles :**
- Pas de connexion Internet
- Le site FIFA est temporairement indisponible
- L'URL a changé

**Solution :** Le script génère automatiquement des données de démonstration

### Le script ne trouve aucun match

**Causes possibles :**
- La structure HTML du site a changé
- Les matchs ne sont pas encore publiés

**Solution :** 
1. Utilisez les données de démonstration générées
2. Ou ajustez les sélecteurs CSS (voir section Personnalisation)

---

## 💡 Conseils

### Automatiser l'exécution

**Windows - Créer un fichier .bat :**

Créez un fichier `lancer_scraper.bat` :
```batch
@echo off
cd /d "%~dp0"
python scraper_fifa.py
pause
```

Double-cliquez dessus pour exécuter le script facilement !

### Planifier l'exécution

**Windows - Planificateur de tâches :**
1. Ouvrez le Planificateur de tâches
2. Créez une nouvelle tâche
3. Action : Exécuter `python scraper_fifa.py`
4. Planifiez (ex: tous les jours à 8h)

---

## 📞 Besoin d'aide ?

### Vérifier que tout fonctionne

Test rapide :
```bash
python --version
pip --version
python scraper_fifa.py
```

Si tout fonctionne, vous verrez :
```
============================================================
🏆 SCRAPER FIFA - COUPE DU MONDE 2026
============================================================

🌐 Connexion au site FIFA...
✅ Connexion réussie !
📄 Analyse de la page...
✅ 15 match(s) récupéré(s) !

✅ Fichier 'matches-fifa-2026.json' créé avec succès !
📊 15 match(s) sauvegardé(s)

============================================================
✅ TERMINÉ !
============================================================
```

---

## 🔄 Alternatives

Si le script Python ne fonctionne pas pour vous :

1. **Import manuel** : Utilisez le fichier `matches-coupe-du-monde-2026.json` fourni
2. **API-Football** : Utilisez la fonctionnalité "🌐 Récupérer depuis Internet"
3. **Saisie manuelle** : Ajoutez les matchs un par un dans l'application

---

**Bon scraping ! 🐍⚽**