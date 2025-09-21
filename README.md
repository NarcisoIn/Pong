# Proyecto Pong en Python
Este proyecto consiste en una **versión del juego clásico Pong** desarrollada en **Python** utilizando la biblioteca **Pygame**. Fue creado como proyecto educativo y de práctica en programación de videojuegos simples.

## Descripción
El juego permite que **dos jugadores** compitan en la misma computadora controlando cada uno su paleta para evitar que la pelota salga de su lado de la pantalla. Incluye sonidos, marcadores visibles y una pantalla de ganador con opción de reiniciar.

## Funcionalidades
- Control de paletas:
  - **Jugador 1:** `W` (arriba) / `S` (abajo)
  - **Jugador 2:** `Flecha Arriba` / `Flecha Abajo`
- Pantalla de selección de meta de puntos: 5, 10 o 15.
- Marcadores visibles durante el juego.
- Sonidos al:
  - Golpear paleta
  - Rebotar en pared
  - Anotar punto
- Pantalla de ganador con opción de **volver a jugar** o **cerrar el juego**.
- Icono personalizado en la ventana del juego.
- Ejecutable `.exe` disponible para Windows.

## Requisitos
- Python 3.8 o superior
- Pygame
Instalación de Pygame:

```bash
pip install pygame
```

## Cómo ejecutar
1. Ejecuta el script pong.py con Python: ``` python pong.py ``` o abre el archivo .exe si ya generaste el ejecutable.
2. Selecciona la meta de puntos en el menú principal.
3. Controla las paletas según el jugador.
4. El primer jugador en alcanzar la meta de puntos gana.
5. En la pantalla de ganador, presiona:
    s para volver a jugar
    n para salir del juego

## Generar archivo ejecutable (.exe)
Se puede generar un ejecutable en Windows usando PyInstaller:
```
  pip install pyinstaller
  pyinstaller --onefile --windowed --icon=pong.ico pong.py
```
El ejecutable se generará dentro de la carpeta dist.

## Créditos
Juego desarrollado por Iván Narciso Guzmán Hernández como práctica académica y personal para el aprendizaje de programación en Python, desarrollo de videojuegos con Pygame y manejo de recursos multimedia. Este proyecto permite practicar conceptos de lógica de programación, manejo de eventos, colisiones y creación de interfaces gráficas interactivas.
Icono y sonidos incluidos para mejorar la experiencia de juego.
