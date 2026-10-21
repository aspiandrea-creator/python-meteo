import pytest

from main import calcola_media
from main import min_temp


def test_media_semplice():
    assert calcola_media([10, 20, 30]) == 20


def test_ignora_valori_mancanti():
    assert calcola_media([10, None, 30]) == 20


def test_lista_vuota_solleva_errore():
    with pytest.raises(ValueError):
        calcola_media([])


def test_tutti_mancanti_solleva_errore():
    with pytest.raises(ValueError):
        calcola_media([None, None])


def test_temperatura_minima():
    with pytest.raises(ValueError):
        min_temp([None,None])
