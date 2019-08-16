# Shalom

> Un algoritmo de cifrado hecho en Python usando saltos en un mapa de caracteres

## Instalación

```
git clone https://github.com/DtxdF/Shalom.git
cd Shalom
python
```

## Uso

```
from shalom import Shalom
shalom = Shalom()
text = shalom.encrypt(['H', 'o', 'l', 'a', '!'], [-4, 9, 15, -7, -5])
print('Encrypt: ' + text)
print('Decrypt: ' + shalom.decrypt(text))
```

*Shalom acepta dos parametros iniciales y dos de llamado*

```
Shalom(index=..., rest=...)
```

**Nota: ** Una ayuda extra puede ser help(...) de Python.
