# Web Audio & Interactive Experiments

**Live demo:** [Warrior's Blood Anthem](https://tzayadet.github.io/JavaScript/) · `index.html`

Colección de interfaces web experimentales, generadores de audio en tiempo real y pequeñas automatizaciones JavaScript. El repositorio conserva distintas iteraciones visuales y prototipos independientes.

## Aplicación principal

- **Warrior's Blood Anthem** — [`index.html`](index.html): interfaz audiovisual principal con animaciones, controles de ritmo y generación de audio mediante Web Audio API.
- **Warrior's Blood Anthem · Standalone** — [`Warriors-Blood-Anthem.html`](Warriors-Blood-Anthem.html): versión independiente para abrir o compartir sin depender del nombre de entrada del sitio.

## Web Audio & rhythm experiments

| Archivo | Descripción |
|---|---|
| [HackerBeat.html](HackerBeat.html) | Interfaz de audio con ritmo y estética terminal. |
| [Primal-Run-Anthem.html](Primal-Run-Anthem.html) | Anthem de carrera a 180 BPM. |
| [Samurai-Run-Anthem.html](Samurai-Run-Anthem.html) | Variante temática japonesa con controles de reproducción. |
| [Neural-Run-Anthem.html](Neural-Run-Anthem.html) | Motor de cadencia y síntesis audiovisual. |
| [Synthax-Engine.html](Synthax-Engine.html) | Experimento de audio en tiempo real con visualización y telemetría de interfaz. |
| [Extended-Hymn.html](Extended-Hymn.html) | Generador de secuencia musical mediante osciladores. |
| [Epic-Hymn.html](Epic-Hymn.html) | Experimento de acordes y síntesis con Web Audio API. |

## Interface & sound variants

- [Clan Operations Audio](Clan-Operations-Audio.html)
- [Extraction Point Audio](Extraction-Point-Audio.html)
- [Field Operations Audio](Field-Operations-Audio.html)
- [Hostile Zone Audio](Hostile-Zone-Audio.html)
- [Limits Cadence Audio](Limits-Cadence-Audio.html)
- [Movement Cadence Audio](Movement-Cadence-Audio.html)
- [Rain Cadence Audio](Rain-Cadence-Audio.html)
- [Dark Zone Audio](Dark-Zone-Audio.html)

Son prototipos independientes. Los nombres describen la variante visual o sonora, no una conexión con sistemas operativos reales.

## JavaScript automation

- `Access-Request-Draft-Generator.gs`: automatización de Google Apps Script para localizar solicitudes de acceso en Gmail y preparar borradores de respuesta. La configuración del archivo contiene valores de ejemplo; requiere adaptar permisos y datos antes de utilizarlo. El script está diseñado para crear borradores, no para enviar mensajes.

## Ejecución local

Abre cualquier archivo `.html` directamente en un navegador moderno. Para servir el directorio localmente:

```bash
python -m http.server 8000
```

Visita `http://localhost:8000` y abre el experimento que quieras probar.

## Tecnologías

- HTML5
- CSS3
- JavaScript
- Web Audio API
- Canvas y APIs del navegador
- Google Apps Script

## Notas

- Los experimentos de audio pueden requerir una interacción explícita para iniciar el sonido debido a las políticas de autoplay del navegador.
- Los documentos HTML están guardados con extensión `.html`; el único archivo `.gs` contiene la automatización de Google Apps Script.
- Los experimentos son prototipos de interfaz, no aplicaciones de producción.

## Licencia

Consulta [LICENSE](LICENSE).
