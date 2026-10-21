import pytest

from main import calcola_media, calcola_minima, giorni_sotto_soglia, giorno_piu_caldo, righe_giornaliere

DATI_FINTI = {
    "time": ["2026-10-01", "2026-10-02", "2026-10-03"],
    "temperature_2m_max": [20.0, 25.0, 18.0],
    "temperature_2m_min": [12.0, 8.0, 9.5],
}

def test_media_semplice():
    assert calcola_media([10, 20, 30]) == 20

def test_ignora_valori_mancanti():
    assert calcola_media([10, None, 30]) == 20

def test_lista_vuota_solleva_errore():
    with pytest.raises(ValueError):
        calcola_media([])

def test_tutti_mancanti_media():
    with pytest.raises(ValueError):
        calcola_media([None, None])

def test_tutti_mancanti_minima():
    with pytest.raises(ValueError):
        calcola_minima([None, None])

def test_minima_semplice():
    assert calcola_minima([10, 20, 30]) == 10

def test_minima_valori_mancanti():
    assert calcola_minima([10, None, 20]) == 10

def test_righe_giornaliere():
    righe = righe_giornaliere(DATI_FINTI)
    assert len(righe) == 3
    assert righe[0] == {"giorno": "2026-10-01", "temp_max": 20.0, "temp_min": 12.0}

def test_giorno_piu_caldo():
    righe = righe_giornaliere(DATI_FINTI)
    assert giorno_piu_caldo(righe)["giorno"] == "2026-10-02"

def test_giorno_piu_caldo_ignora_none():
    righe = [
        {"giorno": "2026-10-01", "temp_max": None, "temp_min": 5.0},
        {"giorno": "2026-10-02", "temp_max": 15.0, "temp_min": 5.0},
    ]
    assert giorno_piu_caldo(righe)["giorno"] == "2026-10-02"

def test_giorno_piu_caldo_tutti_none_solleva_errore():
    righe = [{"giorno": "2026-10-01", "temp_max": None, "temp_min": 5.0}]
    with pytest.raises(ValueError):
        giorno_piu_caldo(righe)

def test_giorni_sotto_soglia():
    righe = righe_giornaliere(DATI_FINTI)
    assert giorni_sotto_soglia(righe, 10.0) == ["2026-10-02", "2026-10-03"]

def test_giorni_sotto_soglia_ignora_none():
    righe = [
        {"giorno": "2026-10-01", "temp_max": 15.0, "temp_min": None},
        {"giorno": "2026-10-02", "temp_max": 15.0, "temp_min": 5.0},
    ]
    assert giorni_sotto_soglia(righe, 10.0) == ["2026-10-02"]