# Galactic Rescue

**Galactic Rescue** es un juego arcade hecho con **Python** y **Pygame**. 

## Requisitos
- Python 3.8+
- Pygame (instalar con `pip install pygame`)

## Archivos
- `main.py` — código fuente del juego
- `bullet` — Lógica de las balas (velocidad, dirección, colisiones)
- `enemy` — Contiene la clase Enemy y su comportamiento
- `player` — Contiene la clase Player y sus funciones
- `utils` — Funciones auxiliares (cargar imágenes, texto, etc.)
- `README.md` — este archivo

## Cómo ejecutar
1. Clona o descarga los archivos.
2. Instala Pygame si no lo tienes.
3. ejecuta.


## Controles
- Mover: Flechas izquierda/derecha o A/D
- Disparar: Espacio
- Pausa: P
- Volver/Salir: Esc

## Características
- Menú principal con opciones: Start, Settings, Instructions, Quit.
- Pantalla de pausa y Game Over.
- Múltiples tipos de enemigos ("basic", "zigzag", "big") con comportamientos distintos.
- Sistema de oleadas que incrementa la dificultad.
- HUD con puntaje, vidas y nivel.
- Código organizado con funciones personalizadas:
- `draw_text()`, `spawn_enemy()`, `handle_collisions()`, `show_main_menu()`, `show_settings()`, etc.

## Entregables 
**Funciones personalizadas**: el proyecto usa varias funciones reutilizables (por ejemplo `spawn_enemy`, `handle_collisions`, `draw_text`).
**Menús y varias funciones**: menús principal, instrucciones, settings y pausa implementados.
**Enemigos**: al menos 3 tipos con comportamientos distintos.
**README.md**: contiene descripción, instrucciones y controles.

## Posibles mejoras (opciones para el estudiante)
- Añadir imágenes/sonidos externos.
- Implementar enemigos que disparen.
- Añadir power-ups, tabla de highscores guardada en archivo.
- Sistema de niveles con mapas prefijados.
- Guardar configuración de settings en un archivo JSON.


