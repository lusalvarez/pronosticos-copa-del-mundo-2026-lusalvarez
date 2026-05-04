# 🌐 Comment lancer un serveur web local

## ⚠️ Pourquoi un serveur local est nécessaire ?

Quand vous ouvrez `participant.html` **directement** depuis l'explorateur de fichiers (double-clic), le navigateur applique des **restrictions de sécurité** qui empêchent le chargement de fichiers JSON locaux.

**Erreur typique :**
```
Access to fetch at 'file:///C:/Users/.../matches-mundial-2026-completo.json' 
from origin 'null' has been blocked by CORS policy
```

---

## ✅ Solution : Utiliser un serveur web local

Un serveur local permet au navigateur de charger les fichiers correctement.

---

## 🚀 Méthode 1 : Python (RECOMMANDÉ)

### Si vous avez Python installé :

1. **Ouvrez PowerShell ou CMD**
2. **Allez dans le dossier du projet** :
   ```bash
   cd C:\Users\059758706\Desktop\pronostics-coupe-du-monde
   ```

3. **Lancez le serveur** :
   
   **Python 3 :**
   ```bash
   python -m http.server 8000
   ```
   
   **Python 2 :**
   ```bash
   python -m SimpleHTTPServer 8000
   ```

4. **Ouvrez votre navigateur** et allez sur :
   ```
   http://localhost:8000/participant.html
   ```

5. ✅ **Ça fonctionne !** Les matchs se chargent automatiquement

---

## 🚀 Méthode 2 : Extension VS Code (FACILE)

Si vous utilisez Visual Studio Code :

1. **Installez l'extension "Live Server"**
   - Ouvrez VS Code
   - Allez dans Extensions (Ctrl+Shift+X)
   - Cherchez "Live Server"
   - Installez-la

2. **Clic droit sur `participant.html`**
3. **Sélectionnez "Open with Live Server"**
4. ✅ Le navigateur s'ouvre automatiquement avec le serveur local

---

## 🚀 Méthode 3 : Node.js (http-server)

Si vous avez Node.js installé :

1. **Installez http-server** (une seule fois) :
   ```bash
   npm install -g http-server
   ```

2. **Allez dans le dossier** :
   ```bash
   cd C:\Users\059758706\Desktop\pronostics-coupe-du-monde
   ```

3. **Lancez le serveur** :
   ```bash
   http-server -p 8000
   ```

4. **Ouvrez** :
   ```
   http://localhost:8000/participant.html
   ```

---

## 🚀 Méthode 4 : Serveur IIS (Windows)

Si vous avez Windows Pro :

1. Activez IIS dans "Fonctionnalités Windows"
2. Copiez le dossier dans `C:\inetpub\wwwroot\`
3. Accédez via `http://localhost/pronostics-coupe-du-monde/participant.html`

---

## 📋 Vérification

Une fois le serveur lancé, vous devriez voir dans la console du navigateur (F12) :

```
📡 Chargement des matchs depuis ./matches-mundial-2026-completo.json...
✅ 48 partidos cargados
```

---

## 🆘 Dépannage

### Erreur : "python n'est pas reconnu"
➡️ Installez Python depuis https://www.python.org/downloads/

### Erreur : "Port 8000 déjà utilisé"
➡️ Utilisez un autre port : `python -m http.server 8001`

### Erreur : "Fichier non trouvé"
➡️ Vérifiez que vous êtes dans le bon dossier avec `dir` (Windows) ou `ls` (Mac/Linux)

---

## 💡 Astuce pour le déploiement

Pour partager avec vos participants :

1. **Déployez sur GitHub Pages** (gratuit, voir GUIDE-DEPLOIEMENT.md)
2. **Ou utilisez Netlify/Vercel** (gratuit aussi)
3. Les participants accèdent via une URL : `https://votre-site.github.io/participant.html`
4. ✅ Pas besoin de serveur local pour eux !

---

## 📝 Commandes rapides

```bash
# Aller dans le dossier
cd C:\Users\059758706\Desktop\pronostics-coupe-du-monde

# Lancer le serveur Python
python -m http.server 8000

# Ouvrir dans le navigateur
# http://localhost:8000/participant.html
```

---

**Une fois le serveur lancé, tout fonctionne parfaitement ! 🎉**