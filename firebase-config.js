// Configuration Firebase pour l'application de pronósticos
// Ce fichier contient les clés d'accès à votre base de données Firebase

const firebaseConfig = {
  apiKey: "AIzaSyC8GDye6ADmlKxtlF9UdNegLC7pMgSg3OU",
  authDomain: "pronostico-copa-del-mundo-2026.firebaseapp.com",
  databaseURL: "https://pronostico-copa-del-mundo-2026-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "pronostico-copa-del-mundo-2026",
  storageBucket: "pronostico-copa-del-mundo-2026.firebasestorage.app",
  messagingSenderId: "380632905205",
  appId: "1:380632905205:web:ecbe47471dca7ddb16dcbc"
};

// Initialiser Firebase
firebase.initializeApp(firebaseConfig);
const database = firebase.database();

console.log("✅ Firebase inicializado correctamente");

// Made with Bob
