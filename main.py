#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mods.calculadora import Calculadora10

if __name__ == '__main__':
    while True:
        try:
            print("ingrese un valor para poder calcular su 10%:")
            total = int(input())
            calculadora = Calculadora10(total)
            print("el 10%% de %s es: " % str(total))
            print(calculadora.valor10)
            break
        except ValueError:
            print("Lo sentimos, debe ingresar un numero.")  
            continue
        except Exception:
            print("Lo sentimos, tenemos un problema, intentelo mas tarde.")  
            break