# Shalom (versión 2)

> Un algoritmo de cifrado simétrico que se translada a una simple librería

## Instalación

```
git clone https://github.com/DtxdF/Shalom.git
cd Shalom
python3
```

## Uso

```
from shalom_v2 import Shalom
shalom = Shalom(index=-6)
text = shalom.encrypt('Hola!', [-4, 9, 15, -7, -5])
print('Encrypt: ' + str(text))
Encrypt: [(74, 10), (126, -3), (129, -9), (96, 13), (34, 11)]
print('Decrypt: ' + shalom.decrypt(text))
Decrypt: Hola!
```

*Shalom acepta tres parámetros iniciales*

```
Shalom(password=..., index=..., rest=...)
```

**Nota: ** Una ayuda extra puede ser help(...) de Python.

~ DtxdF (DtxdF@protonmail.com)
