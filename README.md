# La Terre, à l’épreuve des mesures — version autonome

Copie du dossier XXXI et de ses dépendances locales : expériences Three.js/HDR, texture NASA, illustrations, polices, KaTeX, formules survolables, audit scientifique et licences.

## Lancer

```sh
python3 serve.py
```

Ouvrir http://localhost:8766/ ; Ctrl+C arrête le serveur. Pour changer le port : `python3 serve.py --port 9000`. Python 3 suffit ; aucune installation npm ni compilation nécessaire. Le fichier HTML doit être servi en HTTP pour charger les modules JavaScript.

La page est dans `provoxys/terre-sphere/index.html`. Les dépendances partagées sont dans `assets/` et le logo dans `ymir-lalie/assets/`. Toutes les ressources nécessaires au rendu sont locales. Les références scientifiques externes et l’accueil du collectif restent des liens Internet.

Adaptations pour la copie autonome : entrée à la racine ; liens vers l’accueil et le dossier Lumière orientés vers le site d’origine ; appareil critique orienté vers l’audit local ; compteur de visites retiré car le service API n’est pas inclus. Textes scientifiques et expériences conservés. Le dépôt Git préexistant est préservé. Copie effectuée le 1er octobre 2026.
