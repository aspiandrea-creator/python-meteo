"""Primo script: scarica le temperature recenti di una città e ne calcola la media."""

import requests

URL = "https://api.open-meteo.com/v1/forecast"


def scarica_temperature(latitudine: float, longitudine: float, giorni: int = 7) -> dict:
    """Chiama l'API di Open-Meteo e restituisce i dati giornalieri."""
    parametri = {
        "latitude": latitudine,
        "longitude": longitudine,
        "daily": "temperature_2m_max,temperature_2m_min",
        "past_days": giorni,
        "forecast_days": 1,
        "timezone": "auto",
    }
    risposta = requests.get(URL, params=parametri, timeout=10)
    risposta.raise_for_status()  # si ferma con un errore se la chiamata fallisce
    return risposta.json()["daily"]


def calcola_media(valori: list[float | None]) -> float:
    """Media dei valori, ignorando quelli mancanti (None)."""
    validi = [v for v in valori if v is not None]
    if not validi:
        raise ValueError("Nessun valore valido")
    return sum(validi) / len(validi)


def calcola_minima(valori: list[float | None]) -> float:
    """Temperatura minima, ignorando i valori null"""
    validi_min = [v for v in valori if v is not None]
    if not validi_min:
        raise ValueError("Nessun valore valido per il calcolo della temp minima")
    return min(validi_min)

def righe_giornaliere(dati: dict) -> list[dict]:
    """Restituisce una lista di dizionari, uno per ogni giorno, con le temperature massime e minime."""
    return [
        {"giorno": giorno, "temp_max": temp_max, "temp_min": temp_min}
        for giorno, temp_max, temp_min in zip(
            dati["time"], dati["temperature_2m_max"], dati["temperature_2m_min"]
        )
    ]

def giorno_piu_caldo(righe: list[dict]) -> dict:
    """Restituisce il record del giorno con la temperatura massima più alta."""
    # escludo i record con temperatura massima mancante
    validi = [r for r in righe if r["temp_max"] is not None]
    if not validi:
        raise ValueError("Nessuna temperatura massima valida")
    # lambda serve a specificare che il criterio di confronto è la temperatura massima
    # in particolare è una funzione usa e getta che prende un record e restituisce il valore massimo
    return max(validi, key=lambda r: r["temp_max"])

def giorni_sotto_soglia(righe: list[dict], soglia: float) -> list[str]:
    """Restituisce le date dei giorni con temperatura minima sotto la soglia."""
    return [
        r["giorno"]
        for r in righe
        # and valuta la seconda condizione solo se la prima è vera
        # quindi se temp_min è None il confronto non viene eseguito e non c'è errore
        if r["temp_min"] is not None and r["temp_min"] < soglia
    ]

def main() -> None:
    dati = scarica_temperature(41.89, 12.48)  # Roma
    media_max = calcola_media(dati["temperature_2m_max"])
    media_min = calcola_media(dati["temperature_2m_min"])
    temp_min = calcola_minima(dati["temperature_2m_min"])
    righe = righe_giornaliere(dati)
    piu_caldo = giorno_piu_caldo(righe)
    giorni_freddi = giorni_sotto_soglia(righe, 10.0)
    
    print(f"Giorni scaricati: {len(righe)}")
    print(f"Temperature massime scaricate: {dati['temperature_2m_max']} °C")
    print(f"Temperature minime scaricate: {dati['temperature_2m_min']} °C")
    print(f"Media massime: {media_max:.1f} °C")
    print(f"Media minime: {media_min:.1f} °C")
    print(f"Temperatura minima del periodo: {temp_min:.1f} °C")
    print(f"Giorno più caldo: {piu_caldo['giorno']} ({piu_caldo['temp_max']:.1f} °C)")
    print(f"Giorni con minima sotto 10 °C: {', '.join(giorni_freddi) or 'nessuno'}")

if __name__ == "__main__":
    main()
