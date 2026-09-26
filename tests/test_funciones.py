import math
from fractions import Fraction

import pytest

import media
from media import (
    desviacion_estandar,
    desviacion_estandar_muestral,
    media as media_fn,
    mediana,
    moda,
    modas,
    varianza,
    varianza_muestral,
)

DATOS = [2, 4, 4, 4, 5, 5, 7, 9]


def test_version():
    assert media.__version__ == "0.3.0"


def test_ejemplo_del_readme():
    assert media_fn(DATOS) == 5.0
    assert mediana(DATOS) == 4.5
    assert moda(DATOS) == 4
    assert varianza(DATOS) == 4.0
    assert desviacion_estandar(DATOS) == 2.0


# --- media ---------------------------------------------------------------


def test_media_devuelve_float():
    resultado = media_fn([1, 2, 3])
    assert resultado == 2.0
    assert isinstance(resultado, float)


def test_media_precision_float():
    # sum() acumula error: sum([0.1] * 10) / 10 == 0.09999999999999999
    assert media_fn([0.1] * 10) == 0.1


def test_media_negativos_y_fracciones():
    assert media_fn([-1, 1]) == 0.0
    assert media_fn([Fraction(1, 2), Fraction(3, 2)]) == 1.0


# --- mediana -------------------------------------------------------------


def test_mediana_impar_y_par():
    assert mediana([3, 1, 2]) == 2
    assert mediana([4, 1, 3, 2]) == 2.5


def test_mediana_no_modifica_la_entrada():
    datos = [3, 1, 2]
    mediana(datos)
    assert datos == [3, 1, 2]


# --- moda / modas --------------------------------------------------------


def test_moda_empate_devuelve_el_primero():
    assert moda([3, 1, 1, 3]) == 3


def test_moda_admite_valores_no_numericos():
    assert moda(["rojo", "azul", "rojo"]) == "rojo"


def test_modas():
    assert modas([1, 2, 2, 3, 3]) == [2, 3]
    assert modas([5]) == [5]


# --- varianza y desviación -----------------------------------------------


def test_varianza_muestral():
    assert varianza_muestral(DATOS) == pytest.approx(32 / 7)
    assert desviacion_estandar_muestral(DATOS) == pytest.approx(math.sqrt(32 / 7))


def test_varianza_de_un_solo_dato():
    assert varianza([7]) == 0.0
    assert varianza_muestral([7]) == 0.0
    assert desviacion_estandar([7]) == 0.0


def test_varianza_datos_constantes():
    assert varianza([3.3] * 5) == 0.0


def test_varianza_coincide_con_statistics():
    import statistics

    datos = [1.5, 2.25, 3.0, 10.75, -4.5, 0.0]
    assert varianza(datos) == pytest.approx(statistics.pvariance(datos))
    assert varianza_muestral(datos) == pytest.approx(statistics.variance(datos))
    assert desviacion_estandar(datos) == pytest.approx(statistics.pstdev(datos))
    assert desviacion_estandar_muestral(datos) == pytest.approx(statistics.stdev(datos))


# --- entradas vacías -----------------------------------------------------


@pytest.mark.parametrize(
    "funcion",
    [
        media_fn,
        mediana,
        varianza,
        varianza_muestral,
        desviacion_estandar,
        desviacion_estandar_muestral,
    ],
)
def test_entrada_vacia_devuelve_cero(funcion):
    assert funcion([]) == 0.0


def test_moda_vacia():
    assert moda([]) is None
    assert modas([]) == []


# --- tipos de entrada ----------------------------------------------------


@pytest.mark.parametrize(
    "funcion, esperado",
    [
        (media_fn, 5.0),
        (mediana, 4.5),
        (moda, 4),
        (varianza, 4.0),
        (desviacion_estandar, 2.0),
    ],
)
def test_acepta_generadores_y_tuplas(funcion, esperado):
    assert funcion(x for x in DATOS) == esperado
    assert funcion(tuple(DATOS)) == esperado


@pytest.mark.parametrize(
    "funcion", [media_fn, mediana, varianza, desviacion_estandar]
)
@pytest.mark.parametrize("entrada", [[1, "2", 3], [1, None], "123", 5])
def test_rechaza_valores_no_numericos(funcion, entrada):
    with pytest.raises(TypeError):
        funcion(entrada)


# --- alias en inglés -----------------------------------------------------


def test_alias_en_ingles():
    assert media.mean is media.media
    assert media.median is media.mediana
    assert media.mode is media.moda
    assert media.multimode is media.modas
    assert media.variance is media.varianza
    assert media.sample_variance is media.varianza_muestral
    assert media.standard_deviation is media.desviacion_estandar
    assert media.sample_standard_deviation is media.desviacion_estandar_muestral


def test_import_desde_funciones_sigue_funcionando():
    from media.funciones import median, mode, standard_deviation, variance

    assert median(DATOS) == 4.5
    assert mode(DATOS) == 4
    assert variance(DATOS) == 4.0
    assert standard_deviation(DATOS) == 2.0


def test_all_exporta_nombres_existentes():
    for nombre in media.__all__:
        assert callable(getattr(media, nombre))
