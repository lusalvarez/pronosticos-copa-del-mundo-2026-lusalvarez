# 📖 Guide d'Utilisation - Système de Pronostics Multi-Utilisateurs

Ce guide explique comment utiliser le système de pronostics avec plusieurs participants sans avoir besoin d'un serveur backend.

## 🌐 Prérequis : Rendre l'application accessible

### Option 1 : Déploiement sur Internet (RECOMMANDÉ)

**Avantages :**
- ✅ Les participants accèdent simplement via une URL
- ✅ Pas besoin d'envoyer des fichiers
- ✅ Mises à jour automatiques pour tous
- ✅ Accessible depuis n'importe quel appareil

**Comment faire :**

1. Suivez le guide `GUIDE-DEPLOIEMENT.md` pour déployer sur GitHub Pages, Netlify ou Vercel (gratuit)
2. Vous obtiendrez deux URLs :
   - `https://votre-site.com/index.html` → Pour l'administrateur
   - `https://votre-site.com/participant.html` → Pour les participants
3. Partagez l'URL `participant.html` avec tous les participants

**C'est la méthode la plus simple !**

### Option 2 : Utilisation locale (sans déploiement)

**Si vous ne voulez pas déployer sur Internet :**

1. **Envoyez les fichiers aux participants** :
   - Créez un dossier ZIP contenant :
     - `participant.html`
     - `participant.js`
     - `styles.css`
   - Envoyez ce ZIP à chaque participant par email/WhatsApp/etc.

2. **Instructions pour les participants** :
   - Décompresser le ZIP
   - Double-cliquer sur `participant.html`
   - Le fichier s'ouvre dans le navigateur

**Inconvénients :**
- ⚠️ Chaque participant doit télécharger les fichiers
- ⚠️ Si vous modifiez l'application, il faut renvoyer les fichiers
- ⚠️ Plus compliqué pour les utilisateurs non techniques

---

## 🎯 Vue d'ensemble du workflow

Le système fonctionne en 3 étapes simples :

1. **L'administrateur** crée les matchs et exporte la liste
2. **Les participants** saisissent leurs pronostics et exportent leurs fichiers
3. **L'administrateur** importe les pronostics de chaque participant

---

## 👨‍💼 Pour l'Administrateur

### Étape 0 : Déployer l'application (recommandé)

**Si vous choisissez le déploiement Internet :**

1. Suivez le `GUIDE-DEPLOIEMENT.md` (5 minutes)
2. Déployez sur GitHub Pages (gratuit et simple)
3. Notez vos deux URLs :
   - URL admin : `https://votre-nom.github.io/pronostics-coupe-du-monde/index.html`
   - URL participant : `https://votre-nom.github.io/pronostics-coupe-du-monde/participant.html`

**Si vous restez en local :**

1. Gardez tous les fichiers sur votre ordinateur
2. Préparez un ZIP avec `participant.html`, `participant.js`, `styles.css`

### Étape 1 : Configuration initiale

1. Ouvrez `index.html` dans votre navigateur (ou allez sur votre URL admin)
2. Vous êtes sur l'écran administrateur par défaut
3. Ajoutez les matchs de la Coupe du Monde :
   - **Option A** : Saisie manuelle
     - Remplissez le formulaire (équipe domicile, équipe extérieure, date)
     - Cliquez sur "Ajouter le match"
   - **Option B** : Import depuis un fichier JSON
     - Cliquez sur "📥 Importer des matchs (JSON)"
     - Sélectionnez votre fichier `matches-coupe-du-monde-2026.json`
   - **Option C** : Récupération depuis Internet
     - Cliquez sur "⚙️ Configurer l'API"
     - Entrez votre clé API-Football (gratuite)
     - Cliquez sur "🌐 Récupérer depuis Internet"

### Étape 2 : Partager avec les participants

**Si déployé sur Internet :**

Envoyez ce message à vos participants :

```
🏆 Pronostics Coupe du Monde 2026 🏆

Pour participer :
1. Allez sur : https://votre-site.com/participant.html
2. Téléchargez le fichier des matchs ci-joint
3. Suivez les instructions sur la page

Date limite : [DATE]
```

**Si en local :**

Envoyez ce message avec le ZIP en pièce jointe :

```
🏆 Pronostics Coupe du Monde 2026 🏆

Pour participer :
1. Décompressez le fichier ZIP ci-joint
2. Double-cliquez sur participant.html
3. Téléchargez le fichier des matchs ci-joint
4. Suivez les instructions

Date limite : [DATE]
```

### Étape 3 : Exporter la liste des matchs

1. Dans l'application admin, cliquez sur **"📤 Exporter la liste des matchs"**
2. Un fichier JSON sera téléchargé (ex: `matchs-coupe-du-monde-1234567890.json`)
3. **Envoyez ce fichier à tous les participants** par :
   - Email (en pièce jointe)
   - WhatsApp
   - Telegram
   - Drive partagé
   - Etc.

### Étape 4 : Importer les pronostics des participants

Quand un participant vous envoie son fichier de pronostics :

1. Cliquez sur **"👥 Importer les pronostics d'un participant"**
2. Sélectionnez le fichier reçu (ex: `pronostics-alice-1234567890.json`)
3. Le système va :
   - Créer automatiquement le participant s'il n'existe pas
   - Importer tous ses pronostics
   - Afficher un résumé de l'import

4. Répétez pour chaque participant

### Étape 5 : Saisir les résultats réels

Au fur et à mesure que les matchs sont joués :

1. Dans chaque carte de match, section "Résultat réel"
2. Entrez le score final (domicile et extérieur)
3. Cliquez sur "Enregistrer le résultat"
4. Les points sont calculés automatiquement

### Étape 6 : Consulter le classement

1. Cliquez sur l'onglet **"Écran consultation"**
2. Vous verrez :
   - Le classement général avec les points de chaque participant
   - Les pronostics de tous les participants pour chaque match
   - Les points gagnés par match

---

## 👥 Pour les Participants

### Étape 1 : Accéder à la page de saisie

**Si l'application est sur Internet :**
1. Cliquez sur le lien reçu de l'administrateur
2. La page s'ouvre directement dans votre navigateur
3. Passez à l'étape 2

**Si l'application est locale :**
1. Téléchargez le ZIP reçu de l'administrateur
2. Décompressez le ZIP
3. Double-cliquez sur `participant.html`
4. La page s'ouvre dans votre navigateur

### Étape 2 : Recevoir le fichier des matchs

L'administrateur vous envoie un fichier JSON contenant la liste des matchs.
Téléchargez-le et gardez-le accessible.

### Étape 3 : Charger les matchs

1. Sur la page de saisie, entrez votre nom (ex: "Alice")
2. Cliquez sur "Parcourir" et sélectionnez le fichier des matchs reçu
3. Cliquez sur "Commencer mes pronostics"

### Étape 4 : Saisir vos pronostics

1. Pour chaque match, entrez votre pronostic :
   - Score de l'équipe domicile
   - Score de l'équipe extérieure
2. Vos pronostics sont sauvegardés automatiquement dans votre navigateur
3. Vous pouvez revenir plus tard pour continuer

**💡 Conseil** : Cliquez régulièrement sur "💾 Sauvegarder mes pronostics" pour être sûr

### Étape 5 : Exporter vos pronostics

Une fois tous vos pronostics saisis :

1. Cliquez sur **"📤 Exporter mes pronostics"**
2. Un fichier JSON sera téléchargé (ex: `pronostics-alice-1234567890.json`)
3. **Envoyez ce fichier à l'administrateur** (email, WhatsApp, etc.)

### Étape 6 : Modifier vos pronostics (optionnel)

Si vous voulez modifier vos pronostics avant la date limite :

1. Retournez sur la page (URL ou fichier HTML)
2. Vos pronostics sont toujours là (sauvegardés dans le navigateur)
3. Modifiez les scores
4. Cliquez sur "💾 Sauvegarder mes pronostics"
5. Cliquez sur "📤 Exporter mes pronostics" pour générer un nouveau fichier
6. Envoyez le nouveau fichier à l'administrateur

---

## 🎮 Scénario d'utilisation complet

### Exemple avec 3 participants : Alice, Bruno et Chloé

#### Jour 1 - L'administrateur prépare

**Option Internet (recommandé) :**
1. L'admin déploie sur GitHub Pages (5 minutes)
2. Il obtient l'URL : `https://admin.github.io/pronostics/participant.html`
3. Il ouvre `index.html` et importe les 64 matchs
4. Il clique sur "📤 Exporter la liste des matchs"
5. Il envoie un message à Alice, Bruno et Chloé :
   ```
   🏆 Pronostics Coupe du Monde !
   
   Page de saisie : https://admin.github.io/pronostics/participant.html
   Fichier des matchs : [pièce jointe]
   Date limite : 10 juin 2026
   ```

**Option locale :**
1. L'admin crée un ZIP avec les fichiers participant
2. Il ouvre `index.html` et importe les 64 matchs
3. Il clique sur "📤 Exporter la liste des matchs"
4. Il envoie deux fichiers à Alice, Bruno et Chloé :
   - Le ZIP avec `participant.html`
   - Le fichier `matchs-coupe-du-monde.json`

#### Jour 2 - Les participants saisissent

**Alice :**
1. Clique sur le lien (ou ouvre le fichier HTML)
2. Entre son nom "Alice"
3. Charge le fichier `matchs-coupe-du-monde.json`
4. Saisit ses 64 pronostics
5. Clique sur "📤 Exporter mes pronostics"
6. Envoie `pronostics-alice.json` à l'admin par email

**Bruno et Chloé font de même**

#### Jour 3 - L'administrateur importe

1. L'admin reçoit les 3 fichiers par email
2. Il ouvre son application admin
3. Il clique 3 fois sur "👥 Importer les pronostics d'un participant"
4. Il sélectionne successivement :
   - `pronostics-alice.json`
   - `pronostics-bruno.json`
   - `pronostics-chloe.json`
5. Tous les pronostics sont maintenant dans l'application

#### Pendant la Coupe du Monde

1. Après chaque match, l'admin saisit le résultat réel
2. Les points sont calculés automatiquement
3. Le classement se met à jour en temps réel
4. Tout le monde peut consulter le classement :
   - **Si Internet** : Sur l'URL publique (onglet "Écran consultation")
   - **Si local** : L'admin partage des captures d'écran

---

## 📊 Système de points

- **3 points** : Score exact (ex: prédit 2-1, résultat 2-1)
- **1 point** : Bon résultat (ex: prédit 2-1, résultat 3-0 - les deux sont des victoires domicile)
- **0 point** : Mauvais pronostic

---

## 🔄 Cas d'usage avancés

### Participant en retard

Si un participant veut rejoindre après le début :

1. L'admin exporte à nouveau la liste des matchs
2. Le participant saisit ses pronostics pour les matchs restants
3. L'admin importe ses pronostics
4. Les matchs déjà joués comptent 0 point pour ce participant

### Modification de pronostics

**Avant la date limite :**
1. Le participant retourne sur la page (ses données sont sauvegardées)
2. Il modifie ses pronostics
3. Il exporte à nouveau
4. L'admin réimporte (écrase les anciens pronostics)

**Après la date limite :**
L'admin ne devrait plus accepter de modifications

### Sauvegarde et restauration

**Pour les participants :**
- Vos pronostics sont sauvegardés dans votre navigateur
- Pour les transférer sur un autre appareil :
  1. Cliquez sur "📤 Exporter mes pronostics"
  2. Sur le nouvel appareil, cliquez sur "📥 Importer mes pronostics sauvegardés"
  3. Sélectionnez votre fichier exporté

**Pour l'administrateur :**
- Toutes les données sont dans le localStorage du navigateur
- **Important** : Ne videz pas le cache de votre navigateur !
- Pour sauvegarder : Gardez les fichiers JSON des participants

---

## ⚠️ Points d'attention

### Pour l'administrateur

- ✅ **Déployez sur Internet** pour simplifier l'accès (recommandé)
- ✅ Exportez la liste des matchs **avant** que les participants commencent
- ✅ Ne modifiez pas les noms d'équipes après l'export
- ✅ Définissez une date limite claire pour la saisie des pronostics
- ✅ Gardez tous les fichiers JSON reçus (backup)

### Pour les participants

- ✅ Marquez l'URL en favori (si Internet) ou gardez le fichier HTML
- ✅ Gardez le fichier des matchs reçu
- ✅ Sauvegardez régulièrement pendant la saisie
- ✅ Vérifiez vos pronostics avant d'exporter
- ✅ Envoyez votre fichier avant la date limite
- ✅ Ne videz pas le cache de votre navigateur avant d'avoir exporté

---

## 🆘 Dépannage

### "Je ne trouve pas la page participant.html"

**Si Internet :**
- Vérifiez l'URL reçue
- Essayez de recharger la page (F5)

**Si local :**
- Vérifiez que vous avez bien décompressé le ZIP
- Cherchez le fichier `participant.html` dans le dossier décompressé
- Double-cliquez dessus

### "Format de fichier invalide"

**Cause :** Le fichier JSON est corrompu ou incorrect

**Solution :**
- Vérifiez que c'est bien un fichier .json
- Demandez à l'admin de réexporter
- Ne modifiez pas le fichier manuellement

### "Match non trouvé" lors de l'import

**Cause :** Les noms d'équipes ne correspondent pas

**Solution :**
- L'admin a peut-être modifié les noms après l'export
- Demandez un nouveau fichier de matchs
- Resaisissez vos pronostics

### "Mes pronostics ont disparu"

**Cause :** Cache du navigateur effacé

**Solution :**
- Si vous avez exporté : réimportez votre fichier
- Sinon : resaisissez vos pronostics
- **Prévention :** Exportez régulièrement !

### "Le fichier ne se télécharge pas"

**Solution :**
- Vérifiez les paramètres de téléchargement de votre navigateur
- Essayez un autre navigateur (Chrome, Firefox, Edge)
- Vérifiez que les pop-ups ne sont pas bloquées

---

## 📞 Support

Pour toute question ou problème :
1. Consultez ce guide
2. Vérifiez les fichiers JSON (format correct)
3. Essayez dans un autre navigateur
4. Contactez l'administrateur

---

## ✅ Checklist de démarrage

### Pour l'administrateur

- [ ] Choisir : Internet (recommandé) ou local
- [ ] Si Internet : Déployer sur GitHub Pages (voir GUIDE-DEPLOIEMENT.md)
- [ ] Si local : Préparer le ZIP pour les participants
- [ ] Ouvrir `index.html` (ou URL admin)
- [ ] Ajouter tous les matchs
- [ ] Exporter la liste des matchs
- [ ] Envoyer aux participants :
  - [ ] L'URL ou le ZIP
  - [ ] Le fichier des matchs
  - [ ] La date limite
- [ ] Attendre les fichiers des participants
- [ ] Importer tous les pronostics
- [ ] Saisir les résultats au fur et à mesure
- [ ] Partager le classement

### Pour les participants

- [ ] Recevoir l'URL ou le ZIP + fichier des matchs
- [ ] Accéder à la page de saisie
- [ ] Charger le fichier des matchs
- [ ] Saisir tous les pronostics
- [ ] Sauvegarder régulièrement
- [ ] Exporter les pronostics
- [ ] Envoyer le fichier à l'admin avant la date limite
- [ ] Consulter le classement pendant la compétition

---

## 🎉 Bon pronostics !

Profitez de la Coupe du Monde 2026 avec vos amis et que le meilleur gagne ! 🏆

**💡 Astuce finale :** Déployez sur Internet pour une expérience optimale. C'est gratuit, rapide (5 minutes) et beaucoup plus simple pour tout le monde !