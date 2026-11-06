# Recibir actividades y guardar tu juego

Cada alumno trabaja en un repositorio individual privado. El canal común entrega las actividades preparadas por el profesor. El historial inicial es compartido para poder integrar actualizaciones con Git.

## Preparación inicial

1. En GitHub crea un repositorio privado para tu juego. Déjalo vacío al crearlo, con README, .gitignore y licencia desactivados.
2. En una terminal situada en tu carpeta de proyectos, clona la distribución. Cambia MiJuego por el nombre que quieras usar para la carpeta local.

```bash
git clone https://github.com/devInClass/Motores-1-Alumnos.git MiJuego
cd MiJuego
git remote rename origin curso
```

3. Copia la URL HTTPS de tu repositorio privado. Sustituye TU_USUARIO y TU_REPOSITORIO en el comando siguiente por los datos reales.

```bash
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
git push -u origin main
git remote -v
```

Origin debe apuntar a tu repositorio individual y curso a devInClass/Motores-1-Alumnos. Abre en Unity Hub la carpeta ProyectoUnity dentro de tu clon.

## Guardar una actividad

Guarda las escenas, sal de Play y cierra Unity. Desde la raíz del clon revisa git status --short. Para registrar el trabajo de U01 situado en Assets/Alumno, prepara la carpeta y su .meta.

```bash
git add ProyectoUnity/Assets/Alumno.meta ProyectoUnity/Assets/Alumno
git diff --cached --stat
git commit -m "Guardar mi actividad de U01"
git push origin main
```

Revisa la lista de archivos antes del commit. Los cambios propios del juego van en Assets/Alumno. Si necesitas modificar configuraciones adicionales, revísalas con el profesor y registra también esos cambios en tu repositorio.

## Recibir una actividad liberada

Guarda y registra tu trabajo antes de actualizar. Cierra Unity y ejecuta los comandos desde la raíz del clon.

```bash
git status --short
git fetch curso
git log --oneline HEAD..curso/main
git diff --stat HEAD...curso/main
```

Fetch descarga las novedades del canal. Los comandos siguientes a fetch muestran sus commits y archivos desde el punto de partida compartido. Cuando el profesor indique que se integra la entrega, ejecuta lo siguiente.

```bash
git merge --no-edit curso/main
git push origin main
```

Abre de nuevo ProyectoUnity y sigue la actividad liberada. Si Git informa un conflicto, conserva el mensaje y pide apoyo para revisar los archivos implicados.

## Comprobar el resultado

- El commit nuevo del curso aparece en tu historial.
- La actividad liberada aparece en la carpeta indicada por el profesor.
- Tus escenas y scripts en Assets/Alumno conservan su contenido y archivos .meta.
- Origin recibe tu progreso y curso sigue apuntando al canal común.

Si usas GitHub Desktop para guardar avances, agrega tu clon como repositorio local. Fetch origin consulta tu repositorio individual. La actualización desde curso se realiza con los comandos anteriores en la terminal.
