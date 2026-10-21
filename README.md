I due file (main & test_main) presenti in questa cartella permettono di effettuare dei calcoli sulle temperature, prendendo i dati direttamente da una open source tramite api.

git switch main && git pull                # parti sempre da main aggiornato
git switch -c tipo/nome-breve              # nuovo branch
# ...modifiche...
uv run pytest -v                           # prima testo
git add . && git commit -m "messaggio"
git push -u origin tipo/nome-breve
gh pr create --fill
gh pr merge --merge --delete-branch
git switch main && git pull