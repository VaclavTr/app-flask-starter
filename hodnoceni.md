# Hodnocení podle `ukoly.md`

Datum kontroly: 2026-05-07

## Přehled splnění úkolů

| Úkol | Stav | Poznámka |
|---|---|---|
| 1. Spuštění lokálně | 🟡 Částečně | Aplikace je spustitelná (`app.py`), formulář existuje. Běh jsem v této kontrole nespouštěl. |
| 2. Git a veřejný repozitář | ⚪ Nelze ověřit | Veřejnost repozitáře a minimální počet commitů nelze potvrdit pouze ze souborů. |
| 3. Nasazení na Render | ⚪ Nelze ověřit | `README.md` obsahuje správné instrukce, ale běžící URL není v projektu uvedena. |
| 4. Rozšíření o příjmení (GET) | ✅ Splněno | Ve `page.html` je `surname`, v `app.py` se čte `request.args.get(...)`, pozdrav má správný tvar. |
| 5. Přechod z GET na POST | ✅ Splněno | Route `/pozdrav-post`, šablona `pozdrav_post.html`, metoda POST a čtení přes `request.form` jsou hotové. |
| 6. Heslo a tajná informace | 🟡 Částečně | Heslo se ověřuje a vrací se zpráva o úspěchu/chybě, ale chybí samostatná „tajná informace“ dostupná jen po správném hesle. |
| 7. Validace vstupů | ✅ Splněno | Kontrola prázdných hodnot i limit 50 znaků je implementována, zobrazují se chybové hlášky. |
| 8. Oddělená chráněná stránka | ❌ Nesplněno | Chybí route `/tajne`, `session` i přesměrování nepřihlášeného uživatele. |
| 9. Záznam pokusů do souboru | ❌ Nesplněno | Nezapisuje se `logins.csv` (čas, jméno, výsledek). |
| 10. Vlastní 404 stránka | ❌ Nesplněno | Chybí `errorhandler(404)` i šablona `templates/404.html`. |

## Co je aktuálně dobře

- Základní Flask aplikace funguje se dvěma routami.
- GET i POST formulář jsou rozdělené přehledně.
- Proběhla základní validace vstupů (prázdné hodnoty, délka).

## Doporučení k dokončení

1. Dopsat úkol 8: `session`, `/tajne`, ochrana přístupu.
2. Dopsat úkol 9: zápis každého pokusu do `logins.csv`.
3. Dopsat úkol 10: vlastní 404 handler a šablonu.
4. U úkolu 6 upravit logiku tak, aby se po správném hesle zobrazila konkrétní tajná informace (ne jen obecné „Správné heslo!“).
5. Ověřit úkoly 1-3 v praxi: lokální běh, veřejné GitHub repo, veřejná Render URL.
