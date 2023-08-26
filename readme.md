## Descripción

PyScriptHandler es una herramienta CLI ultra-ligera diseñada para hacer que la gestión de scripts de Python sea tan simple y directa como sea posible.

La idea es que puedas tener una lista de scripts que funcionen en Windows, macOS, Linux y que puedas ejecutarlos desde cualquier lugar del sistema.

### Características clave:

- **Simplicidad**: Con menos de 150 líneas de código, PyScriptHandler es extremadamente fácil de entender y modificar según tus necesidades.
- **Portabilidad**: La idea es unificar la forma en que se ejecutan los scripts de Python en cualquier sistema operativo.
- **Cero Configuración**: No hay archivos de configuración para editar, no hay dependencias para instalar. Simplemente instala el script y empieza a usarlo.
- **Comandos Simples**: Los comandos son simples y fáciles de recordar. No hay necesidad de buscar en la documentación cada vez que quieras ejecutar un script.
- **Alias Friendly**: Puedes crear alias para los comandos y ejecutar tus scripts con un solo comando.

### ¿Por qué usar PyScriptHandler?
Este proyecto nació de mi propia necesidad de tener una herramienta simple donde poder almacenar y ejecutar mis scripts de Python, la cual fuera lo mas minimalista posible y que no requiriera de ninguna configuración adicional. Si te encuentras en una situación similar, entonces PyScriptHandler es para ti.

### Instalación

PyScriptHandler se puede instalar fácilmente clonando el repositorio y ejecutando el script de instalación:

```bash
git clone
cd pyscripthandler
python install.py
```
nota: Si estás en Linux o macOS, es posible que tengas que usar `python3` en lugar de `python`.

### Comandos

- `psh -h`: Muestra los comandos disponibles.
- `psh <script_name>`: Ejecuta un script.
- `psh list`: Lista todos los scripts disponibles.
- `psh add <script_path>`: Añade un nuevo script a la lista, el nombre del script será el nombre del archivo.
- `psh remove <script_name>`: Elimina un script de la lista.
- `psh find <script_name>`: Busca un script en la lista o varios scripts que contengan el nombre especificado.
- `psh pwd`: Muestra la ruta actual del directorio de scripts.

### Ejemplos

```bash
# Ejecuta un script
psh hello_world

# Lista todos los scripts
psh list

# Añade un nuevo script
psh add /path/to/script.py

# Elimina un script
psh remove hello_world

# Busca un script
psh find hello_world

# Muestra la ruta actual del directorio de scripts
psh pwd
```

### Licencia
[MIT](https://choosealicense.com/licenses/mit/)