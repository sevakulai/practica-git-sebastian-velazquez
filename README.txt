Marcos Sebastián Velázquez Hernández

2630013

Creación y sincronización de repositorios con Git y GitHub

Crear un repositorio local utilizando Git, sincronizarlo con un repositorio remoto en GitHub y comprobar el flujo de trabajo en ambos sentidos

Descripción: Utilicé primeramente mi terminal PowerShell para realizar la configuración del lado local para inicializar de manera correcta y siguiendo las instrucciones un git, a continuación sincronicé mi trabajo local con GitHub para hacer la siguiente parte del trabajo, utilicé los comandos previamente aprendidos en las clases de Metodologías de la programación así como la guía que venía en la asignatura.

Comando	Función
git init	           Inicializa un repositorio Git nuevo dentro de la carpeta actual.
git branch -M main	   Renombra la rama principal a main.
git status	           Muestra el estado actual del repositorio: qué archivos están modificados, agregados o sin seguimiento.
git add .	           Agrega todos los archivos modificados o nuevos al área de preparación (Staging Area).
git commit -m "mensaje"	   Guarda los cambios que están en el Staging Area como una nueva versión (commit) en el historial local, con un mensaje descriptivo.
git remote add origin URL  Vincula el repositorio local con un repositorio remoto en GitHub, asignándole el nombre origin.
git remote -v	           Muestra las URLs de los repositorios remotos vinculados, para verificar que la conexión sea correcta.
git push -u origin main	   Envía los commits locales al repositorio remoto por primera vez y establece origin main como destino predeterminado para futuros push.
git pull origin main	   Descarga los cambios más recientes del repositorio remoto y los combina con el repositorio local.
git push	           Envía los commits locales nuevos al repositorio remoto ya vinculado.

El repositorio local se creó dentro de una carpeta nueva, usando git init para convertirla en un repositorio Git. Esto genera una carpeta oculta .git donde Git guarda todo el historial de versiones. Después configuré la rama principal como main, que es el nombre estándar recomendado actualmente, y añadí los archivos base del proyecto.

Para vincular el repositorio local con GitHub, primero creé un repositorio vacío en GitHub (sin archivos iniciales) y copié su URL. Con el comando git remote add origin URL_DEL_REPOSITORIO le indiqué a Git que ese repositorio remoto se llamaría origin y sería el destino de mis futuros envíos de cambios. Confirmé la vinculación con git remote -v, que muestra las direcciones configuradas para fetch y push.

Cuando hago cambios en mi computadora, primero los guardo con git add y git commit en el repositorio local. Después, uso git push para enviar esos commits al repositorio remoto en GitHub, de modo que los cambios queden reflejados también ahí y disponibles para cualquier persona que consulte el repositorio.

Cuando un cambio se realiza directamente en GitHub (por ejemplo, editando un archivo desde el navegador y haciendo un commit ahí), ese cambio existe en el repositorio remoto pero no en mi computadora. Para traerlo, uso git pull origin main, que descarga los commits nuevos del repositorio remoto y los combina con mi repositorio local, actualizando los archivos en mi computadora.

README.md: documento que explica el objetivo, el procedimiento y los comandos utilizados en esta práctica.
datos.txt: archivo de prueba utilizado para comprobar la sincronización de cambios entre el repositorio local y GitHub, tanto en un sentido como en el otro.

Con esta práctica aprendí a usar Git para crear un repositorio local, registrar cambios con add y commit, y sincronizarlo con GitHub usando push y pull. Entendí la diferencia entre trabajar en el repositorio local y el remoto, y cómo mantenerlos actualizados en ambos sentidos: subiendo mis cambios con push y descargando los hechos en GitHub con pull. En general, la práctica me ayudó a perder el miedo a usar Git desde la terminal y a entender el flujo básico de trabajo con control de versiones.