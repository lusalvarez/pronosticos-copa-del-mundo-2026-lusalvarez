# 🚀 Comment récupérer les vrais matchs depuis le site FIFA

## ⚠️ Pourquoi Bob ne peut pas le faire directement ?

Bob (l'assistant IA) **n'a pas accès à Internet** depuis son environnement. Il peut créer des scripts, mais c'est **vous** qui devez les exécuter sur votre ordinateur.

---

## ✅ Solution : Exécuter le scraper Python

### Étape 1 : Vérifier que Python est installé

Ouvrez un terminal (PowerShell ou CMD) et tapez :

```bash
python --version
```

Si Python n'est pas installé, téléchargez-le depuis : https://www.python.org/downloads/

### Étape 2 : Installer les dépendances

Dans le dossier `pronostics-coupe-du-monde`, exécutez :

```bash
pip install requests beautifulsoup4
```

### Étape 3 : Exécuter le scraper

```bash
python scraper_fifa.py
```

Le script va :
1. Se connecter au site FIFA
2. Récupérer les matchs officiels
3. Créer un fichier JSON avec les vrais matchs

---

## 🔄 Alternative : Copier-coller manuel

Si Python ne fonctionne pas, vous pouvez :

### Option A : Copier depuis le site FIFA

1. Allez sur : https://www.fifa.com/fr/tournaments/mens/worldcup/canadamexicousa2026/scores-fixtures
2. Copiez les informations des matchs
3. Créez un fichier JSON manuellement
4. Importez-le dans l'application

### Option B : Utiliser les outils de développement du navigateur

1. Ouvrez le site FIFA
2. Appuyez sur F12 (outils de développement)
3. Allez dans l'onglet "Network" (Réseau)
4. Rechargez la page
5. Cherchez les requêtes API (souvent en JSON)
6. Copiez les données JSON
7. Sauvegardez dans un fichier

---

## 💡 Pourquoi les matchs créés sont "inventés" ?

Parce que Bob ne peut pas accéder au site FIFA en temps réel. Il a créé des matchs **hypothétiques** basés sur :
- Le format officiel 2026
- Les équipes probables
- Les dates approximatives

**Pour avoir les VRAIS matchs, vous devez exécuter le scraper Python vous-même.**

---

## 🆘 Besoin d'aide ?

Si vous avez des difficultés :

1. **Vérifiez votre connexion Internet**
2. **Installez Python** si ce n'est pas déjà fait
3. **Exécutez le scraper** depuis votre terminal
4. **Ou copiez manuellement** les matchs depuis le site FIFA

---

**En résumé : Bob crée les outils, mais c'est vous qui devez les exécuter pour accéder à Internet ! 🌐**