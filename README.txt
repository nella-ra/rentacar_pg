
# Uputstvo za postavljanje sistema

1. **Instalacija Python okruženja**:
   - Preuzmite i instalirajte Python 3.9 ili noviji.

2. **Instalacija potrebnih paketa**:
   - Pokrenite sledeću komandu u terminalu:
     ```bash
     pip install flask requests
     ```

3. **Pokretanje backend-a**:
   - Pokrenite sledeću komandu iz direktorijuma gde je `app.py`:
     ```bash
     python app.py
     ```

4. **Otvaranje sajta**:
   - Otvorite fajl `index.html` u pregledaču i testirajte funkcionalnost rezervacija.

5. **Postavljanje Viber API ključa**:
   - Registrujte svoj bot na [Viber Partners](https://partners.viber.com/).
   - Zamenite `YOUR_VIBER_BOT_TOKEN_HERE` u fajlu `app.py` sa stvarnim tokenom.

6. **Testiranje rezervacija**:
   - Kada unesete podatke u formular, proverite da li dobijate obaveštenje na Viberu.
