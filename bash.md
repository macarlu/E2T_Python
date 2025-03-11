# 💻 BÁSICOS BASH: GUÍA VISUAL PARA PRINCIPIANTES

## 🎨 1. Conceptos Fundamentales

### 🔍 Comodines del Terminal
- **`?`** ➡️ Un solo carácter cualquiera.
- **`*`** ➡️ Desde nada hasta cualquier cantidad de caracteres.
- **`[1-5]`** ➡️ Cualquier carácter dentro del rango.
- **`[!1-5]`** ➡️ Cualquier carácter que *NO* esté en el rango.
- **`{}`** ➡️ Lista de valores. Ejemplo: `cp {archivo1,archivo2} destino/`
- **`\`** ➡️ Escape de carácteres especiales.

### ⏯️ Atajos del Terminal
- **`./`** ➡️ Ejecuta un archivo en el directorio actual.
- **`Ctrl + R`** ➡️ Buscar en el historial.
- **`!!`** ➡️ Ejecuta el último comando.
- **`!$`** ➡️ Usa el último argumento del comando anterior.

### ⛓️ Concatenación de Comandos
- **`;`** ➡️ Ejecuta comandos en secuencia, sin importar si fallan.
- **`&&`** ➡️ Ejecuta el segundo comando solo si el primero es exitoso.
- **`||`** ➡️ Ejecuta el segundo comando solo si el primero falla.

### ➡️ Redirecciones
- **`>`** ➡️ Guarda la salida en un archivo (sobrescribe).
- **`>>`** ➡️ Agrega la salida al final del archivo.
- **`2>`** ➡️ Guarda los errores en un archivo.
- **`&>`** ➡️ Guarda salida y errores en un archivo.

### ◼️ Tuberías (Pipes)
- **`|`** ➡️ Usa la salida de un comando como entrada de otro.
- Ejemplo:
  ```bash
  ls | grep "archivo"
  ```

---

## 📁 2. Ficheros del Sistema

- **`/etc/environment`** ➡️ Variables de entorno globales.
- **`/boot/grub/grub.cfg`** ➡️ Configuración del GRUB.
- **`/etc/default/grub`** ➡️ Configuración personalizable del arranque.

---

## ⚙️ 3. Comandos Esenciales

### 📖 Documentación y Ayuda
- **`man comando`** ➡️ Manual de usuario.
- **`info comando`** ➡️ Información más detallada.
- **`help comando`** ➡️ Ayuda breve.
- **`whatis comando`** ➡️ Resumen del comando.

### 🛠️ Administración
- **`su`** ➡️ Cambiar a usuario root.
- **`sudo comando`** ➡️ Ejecutar comando como superusuario.
- **`sudo -l`** ➡️ Lista comandos permitidos.

### 📊 Información del Sistema
- **`uptime`** ➡️ Tiempo encendido y carga del sistema.
- **`uname -a`** ➡️ Información del kernel.
- **`hostname`** ➡️ Nombre de la máquina.

### 📃 Historial y Alias
- **`history`** ➡️ Ver comandos anteriores.
- **`alias nuevo='comando'`** ➡️ Crear un alias.
  ```bash
  alias listar='ls -la'
  ```

### ⌨️ Entrada y Salida
- **`echo "texto"`** ➡️ Mostrar texto en la terminal.
- **`read variable`** ➡️ Leer entrada del usuario.
- **`which comando`** ➡️ Ubicación de un comando.
- **`clear`** ➡️ Limpiar la terminal.

### ⏳ Control del Sistema
- **`sleep 5`** ➡️ Esperar 5 segundos.
- **`exit`** ➡️ Salir de la sesión actual.
- **`reboot`** ➡️ Reiniciar el sistema.
- **`shutdown -h now`** ➡️ Apagar el sistema.

---

📚 **Consejos para Memorizar**
- 🌟 Usa **alias** para simplificar comandos largos.
- 📕 Practica **tuberías** y **redirecciones** para combinar comandos.
- ✅ Experimenta en un entorno seguro para evitar daños en el sistema.
- 🎨 Usa colores y resaltado en tu terminal para identificar comandos.

💪🏻 ¡Sigue practicando y dominarás Bash rápidamente! 🌟

