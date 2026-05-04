# 🏆 Application de Pronostics - Coupe du Monde 2026

Application web complète pour gérer les pronostics de la Coupe du Monde de football avec vos amis, collègues ou famille.

## ✨ Fonctionnalités

### Pour l'Administrateur
- ✅ Gestion des matchs (ajout manuel, import JSON, API)
- ✅ Import des pronostics des participants
- ✅ Saisie des résultats réels
- ✅ Calcul automatique des points
- ✅ Classement en temps réel
- ✅ Export de la liste des matchs

### Pour les Participants
- ✅ Page de saisie dédiée et intuitive
- ✅ Sauvegarde automatique des pronostics
- ✅ Export des pronostics au format JSON
- ✅ Statistiques de progression
- ✅ Interface responsive (mobile/tablette/desktop)

### Système de Points
- **3 points** : Score exact
- **1 point** : Bon résultat (victoire/nul/défaite)
- **0 point** : Mauvais pronostic

## 🚀 Démarrage Rapide

### Option 1 : Déploiement sur Internet (Recommandé)

**Avantages :** Accessible partout, pas de fichiers à envoyer, gratuit

1. Suivez le guide détaillé : **[GUIDE-DEPLOIEMENT.md](GUIDE-DEPLOIEMENT.md)**
2. Déployez sur GitHub Pages (5 minutes, gratuit)
3. Partagez les URLs avec vos participants

### Option 2 : Utilisation Locale

**Avantages :** Pas besoin de compte, fonctionne hors ligne

1. Téléchargez tous les fichiers
2. Ouvrez `index.html` pour l'administration
3. Envoyez `participant.html` + fichiers aux participants

## 📚 Documentation

| Document | Description |
|----------|-------------|
| **[GUIDE-UTILISATION.md](GUIDE-UTILISATION.md)** | Guide complet d'utilisation pour admin et participants |
| **[GUIDE-DEPLOIEMENT.md](GUIDE-DEPLOIEMENT.md)** | Comment rendre l'application accessible sur Internet |
| **[GUIDE-API-FOOTBALL.md](GUIDE-API-FOOTBALL.md)** | Récupérer les matchs depuis Internet (API) |
| **[GUIDE-SCRAPER-FIFA.md](GUIDE-SCRAPER-FIFA.md)** | Scraper les matchs depuis le site FIFA |

## 📁 Structure des Fichiers

```
pronostics-coupe-du-monde/
├── index.html                          # Application administrateur
├── app.js                              # Logique administrateur
├── participant.html                    # Page de saisie participants
├── participant.js                      # Logique participants
├── styles.css                          # Styles communs
├── matches-coupe-du-monde-2026.json   # Données des matchs
├── README.md                           # Ce fichier
├── GUIDE-UTILISATION.md               # Guide d'utilisation
├── GUIDE-DEPLOIEMENT.md               # Guide de déploiement
├── GUIDE-API-FOOTBALL.md              # Guide API
└── GUIDE-SCRAPER-FIFA.md              # Guide scraper
```

## 🎯 Workflow Simplifié

### 1️⃣ L'Administrateur

```
1. Déployer l'application (ou garder en local)
2. Ajouter les matchs
3. Exporter la liste des matchs
4. Partager l'URL participant + fichier des matchs
5. Importer les pronostics reçus
6. Saisir les résultats au fur et à mesure
7. Consulter le classement
```

### 2️⃣ Les Participants

```
1. Accéder à la page participant (URL ou fichier HTML)
2. Charger le fichier des matchs
3. Saisir les pronostics
4. Exporter les pronostics
5. Envoyer le fichier à l'admin
6. Consulter le classement pendant la compétition
```

## 💾 Format des Fichiers

### Fichier des Matchs (Export Admin → Participants)

```json
{
  "exportDate": "2026-04-30T14:00:00.000Z",
  "matches": [
    {
      "homeTeam": "France",
      "awayTeam": "Brésil",
      "date": "2026-06-12T21:00"
    }
  ]
}
```

### Fichier des Pronostics (Export Participants → Admin)

```json
{
  "participantName": "Alice",
  "exportDate": "2026-04-30T15:00:00.000Z",
  "predictions": [
    {
      "homeTeam": "France",
      "awayTeam": "Brésil",
      "date": "2026-06-12T21:00",
      "prediction": {
        "home": 2,
        "away": 1
      }
    }
  ]
}
```

## 🔧 Technologies Utilisées

- **HTML5** : Structure
- **CSS3** : Design moderne et responsive
- **JavaScript Vanilla** : Logique (pas de framework)
- **LocalStorage** : Stockage des données côté client
- **JSON** : Format d'échange de données

## 🌐 Compatibilité

- ✅ Chrome / Edge (recommandé)
- ✅ Firefox
- ✅ Safari
- ✅ Mobile (iOS / Android)
- ✅ Tablette

## ⚠️ Limitations Actuelles

### Stockage Local
- Chaque utilisateur a sa propre copie des données
- Les données sont dans le navigateur (localStorage)
- Pas de synchronisation automatique entre utilisateurs

### Solution : Workflow Import/Export
- L'admin exporte les matchs → participants importent
- Participants exportent leurs pronostics → admin importe
- Simple, efficace, sans serveur !

## 🔮 Évolutions Futures Possibles

Si vous voulez une synchronisation en temps réel :

1. **Backend Firebase** (gratuit)
   - Base de données temps réel
   - Authentification
   - Synchronisation automatique

2. **Backend Supabase** (gratuit)
   - PostgreSQL
   - API REST
   - Temps réel

3. **Backend personnalisé**
   - Node.js + Express
   - MongoDB / PostgreSQL
   - Hébergement gratuit (Render, Railway)

## 📊 Exemple d'Utilisation

### Scénario : 10 amis pour la Coupe du Monde

1. **Jour 1** : Admin déploie sur GitHub Pages (5 min)
2. **Jour 2** : Admin ajoute les 64 matchs et exporte
3. **Jour 3-7** : Les 10 amis saisissent leurs pronostics
4. **Jour 8** : Admin importe les 10 fichiers (2 min)
5. **Pendant la compétition** : Admin saisit les résultats
6. **Tout le temps** : Classement visible par tous

**Temps total admin** : ~30 minutes
**Temps total participant** : ~20 minutes

## 🎨 Captures d'Écran

### Interface Administrateur
- Gestion des participants
- Ajout/import de matchs
- Saisie des résultats
- Import des pronostics

### Interface Participant
- Saisie intuitive des pronostics
- Statistiques de progression
- Export facile

### Écran Consultation
- Classement général
- Détail des pronostics par match
- Points par participant

## 🤝 Contribution

Cette application a été créée pour être simple et efficace. Si vous avez des suggestions :

1. Testez l'application
2. Notez les améliorations possibles
3. Partagez vos retours

## 📝 Licence

Libre d'utilisation pour un usage personnel et non commercial.

## 👨‍💻 Support

Pour toute question :
1. Consultez les guides dans le dossier
2. Vérifiez la section "Dépannage" du GUIDE-UTILISATION.md
3. Testez dans un autre navigateur

## 🎉 Bon Pronostics !

Profitez de la Coupe du Monde 2026 avec vos amis !

---

**Made with ❤️ by Bob**

*Application créée pour simplifier la gestion des pronostics entre amis, sans complexité technique.*