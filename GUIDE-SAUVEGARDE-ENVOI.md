# 📝 Guide : Sauvegarde Locale vs Envoi Firebase

## 🎯 Objectif

Ce guide explique la différence entre **sauvegarder localement** et **envoyer vers Firebase** dans l'application de pronostics.

---

## 🔄 Deux Actions Distinctes

### 1️⃣ **💾 Guardar mis pronósticos** (Sauvegarder localement)

**Fonction** : `saveData()`

**Ce qui se passe** :
- ✅ Sauvegarde vos pronostics dans le navigateur (localStorage)
- ✅ Permet de continuer plus tard sans perdre votre travail
- ✅ Fonctionne même sans connexion Internet
- ❌ **NE synchronise PAS** avec l'administrateur
- ❌ Les données restent uniquement sur votre ordinateur

**Message affiché** :
```
✅ ¡Tus pronósticos han sido guardados localmente!
```
(Fond vert)

**Quand l'utiliser** :
- Pendant que vous remplissez vos pronostics
- Pour faire une pause et revenir plus tard
- Pour sauvegarder régulièrement votre progression

---

### 2️⃣ **📤 Enviar mis pronósticos** (Envoyer vers Firebase)

**Fonction** : `sendToFirebase()`

**Ce qui se passe** :
- ✅ Sauvegarde d'abord localement (localStorage)
- ✅ **Envoie ensuite vers Firebase** (base de données cloud)
- ✅ L'administrateur reçoit vos pronostics en temps réel
- ✅ Synchronisation automatique avec l'application centrale
- ⚠️ Nécessite une connexion Internet

**Message affiché** :
```
🎉 ¡Tus pronósticos han sido enviados al administrador con éxito!
```
(Fond bleu)

**Quand l'utiliser** :
- Quand vous avez terminé tous vos pronostics
- Quand vous voulez que l'administrateur voie vos choix
- Pour mettre à jour vos pronostics déjà envoyés

---

## 📊 Workflow Recommandé

```
1. Remplir les pronostics
   ↓
2. Cliquer sur "💾 Guardar" régulièrement
   ↓
3. Continuer à remplir
   ↓
4. Une fois terminé, cliquer sur "📤 Enviar"
   ↓
5. Vérifier le message de confirmation bleu
```

---

## 🎨 Différences Visuelles

| Aspect | Guardar (Local) | Enviar (Firebase) |
|--------|----------------|-------------------|
| **Icône** | 💾 | 📤 |
| **Couleur du bouton** | Vert | Bleu |
| **Message** | "guardados localmente" | "enviados al administrador" |
| **Couleur du message** | Vert (#10b981) | Bleu (#3b82f6) |
| **Durée d'affichage** | 5 secondes | 5 secondes |

---

## 🔧 Détails Techniques

### Structure des Données Locales (localStorage)

```javascript
{
  participantName: "Juan Pérez",
  participantPassword: "hash_du_mot_de_passe",
  predictions: {
    0: { home: "2", away: "1" },
    1: { home: "3", away: "0" },
    // ...
  },
  lastSaved: "2026-06-11T14:30:00.000Z"
}
```

### Structure des Données Firebase

```javascript
{
  participantName: "Juan Pérez",
  passwordHash: "hash_du_mot_de_passe",
  lastUpdated: "2026-06-11T14:35:00.000Z",
  predictions: [
    {
      homeTeam: "Argentina",
      awayTeam: "Canada",
      date: "2026-06-11T21:00:00.000Z",
      stage: "Fase de grupos",
      prediction: { home: "2", away: "1" }
    },
    // ...
  ]
}
```

---

## ⚠️ Gestion des Erreurs

### Si Firebase n'est pas disponible

Lors du clic sur "📤 Enviar" :

```javascript
if (typeof firebase === 'undefined' || !firebase.database) {
  alert("❌ Firebase no está disponible.\n\n" +
        "No se pueden enviar los pronósticos al administrador.\n\n" +
        "Por favor, verifica tu conexión a Internet.");
  return;
}
```

**Message affiché** :
```
❌ Firebase no está disponible.

No se pueden enviar los pronósticos al administrador.

Por favor, verifica tu conexión a Internet.
```

### En cas d'erreur lors de l'envoi

```javascript
.catch((error) => {
  console.error("❌ Error al enviar a Firebase:", error);
  alert("❌ Error al enviar los pronósticos.\n\nPor favor, intenta de nuevo.");
});
```

---

## 🔐 Sécurité

- Le mot de passe est **haché** avant d'être stocké (local et Firebase)
- Fonction de hachage simple : `hashPassword(password)`
- Le mot de passe en clair n'est jamais stocké
- Vérification du mot de passe à chaque connexion

---

## 📱 Compatibilité

### Sauvegarde Locale (localStorage)
- ✅ Fonctionne hors ligne
- ✅ Tous les navigateurs modernes
- ⚠️ Limité à ~5-10 MB
- ⚠️ Peut être effacé si l'utilisateur vide le cache

### Envoi Firebase
- ❌ Nécessite Internet
- ✅ Stockage illimité (dans les limites du plan Firebase)
- ✅ Synchronisation en temps réel
- ✅ Accessible depuis n'importe quel appareil

---

## 🎯 Cas d'Usage

### Scénario 1 : Remplissage Progressif
```
Jour 1 : Remplir 10 matchs → Guardar
Jour 2 : Remplir 20 matchs → Guardar
Jour 3 : Remplir 18 matchs → Guardar → Enviar
```

### Scénario 2 : Modification Après Envoi
```
Envoi initial → Enviar
Changement d'avis → Modifier → Guardar → Enviar
```

### Scénario 3 : Travail Hors Ligne
```
Hors ligne : Remplir tous les matchs → Guardar
En ligne : Enviar
```

---

## 🚀 Avantages de Cette Approche

1. **Flexibilité** : L'utilisateur contrôle quand envoyer
2. **Sécurité** : Pas d'envoi accidentel
3. **Performance** : Moins de requêtes Firebase
4. **Clarté** : Distinction claire entre local et cloud
5. **Fiabilité** : Travail possible hors ligne

---

## 📞 Support

Si vous rencontrez des problèmes :

1. Vérifiez votre connexion Internet
2. Vérifiez que Firebase est configuré (firebase-config.js)
3. Consultez la console du navigateur (F12) pour les erreurs
4. Contactez l'administrateur

---

**Dernière mise à jour** : 1er mai 2026