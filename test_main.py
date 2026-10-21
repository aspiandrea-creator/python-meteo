import pytest

from main import calcola_media
from main import calcola_minima


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
