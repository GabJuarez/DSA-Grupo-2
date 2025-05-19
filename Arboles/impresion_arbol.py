#modulo para reutilizar en los ejericios
#permite imprimir los arboles de manera mas legible


def imprimir_arbol(nodo, prefijo="", es_ultimo=True, es_raiz=True):
#se imprime un arbol de manera jerarquica
    if nodo is None:
        return

    if es_raiz:
        print(nodo.empleado.nombre)
    else:
        rama = "└── " if es_ultimo else "├── "
        print(prefijo + rama + nodo.empleado.nombre)

    nuevo_prefijo = prefijo + ("    " if not es_raiz and es_ultimo else "│   ") if not es_raiz else ""
    total_subordinados = len(nodo.subordinados)

    for i, sub in enumerate(nodo.subordinados):
        es_ultimo_hijo = (i == total_subordinados - 1)
        imprimir_arbol(sub, nuevo_prefijo, es_ultimo_hijo, es_raiz=False)