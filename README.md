# Calculadora #

Este README contiene todos los pasos necesarios para ejecutar la aplicación.

## Folder Structure ##
```
.
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
├── mods
│   ├── __init__.py
│   └── calculadora.py
└── tests
    ├── __init__.py
    └── test_calculadora.py
```

## Installation ##

Esta aplicación es compatible con python2.7, python3.6, python3.7 y python3.8.

Por simplicidad, se toma python3.7 para el resto del documento.

### Setup ###

Crear ambiente virtual en su máquina para probar esta aplicación. No hay modulos externos a los que trae python para esta aplicación, si los tuviese en una versión futura deberá correr el siguiente script:

```shell
pip install -r requirements.txt
```

### Run tests ###

```shell
python -m unittest tests.test_calculadora -v
```

#### Resultado esperado ####

```shell
test_calculadora_correcta (tests.test_calculadora.TestCalculadora) ... ok
test_calculadora_incorrecta (tests.test_calculadora.TestCalculadora) ... ok
test_calculadora_no_enteros (tests.test_calculadora.TestCalculadora) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

## Run App ##

```shell
python main.py
```