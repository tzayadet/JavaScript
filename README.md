<p align="center">
  <img src="https://img.shields.io/badge/WEB_AUDIO-INTERACTIVE_EXPERIMENTS-101010?style=for-the-badge&labelColor=050805&color=00FF41" alt="Web Audio"/>
  <img src="https://img.shields.io/badge/JAVASCRIPT-BROWSER_APIS-101010?style=for-the-badge&logo=javascript&logoColor=00FF41" alt="JavaScript"/>
</p>

# Web Audio & Interactive Experiments

Collection of browser-based interfaces, real-time audio generators and small JavaScript automations. The repository keeps independent visual iterations and experiments rather than presenting them as one application.

<p align="center">
  <a href="https://tzayadet.github.io/JavaScript/"><strong>LIVE DEMO · WARRIOR'S BLOOD ANTHEM ↗</strong></a> ·
  <a href="https://github.com/tzayadet/JavaScript"><strong>SOURCE CODE</strong></a>
</p>

[![Static checks](https://github.com/tzayadet/JavaScript/actions/workflows/static-checks.yml/badge.svg)](https://github.com/tzayadet/JavaScript/actions/workflows/static-checks.yml)

## Main experience

- **Warrior's Blood Anthem** — [`index.html`](index.html): main audiovisual interface with animations, rhythm controls and sound generation through the Web Audio API.
- **Standalone version** — [`Warriors-Blood-Anthem.html`](Warriors-Blood-Anthem.html): independent version for opening or sharing directly.

## Web Audio and rhythm experiments

| File | Description |
|---|---|
| [HackerBeat.html](HackerBeat.html) | Audio interface with rhythm and terminal-inspired styling. |
| [Primal-Run-Anthem.html](Primal-Run-Anthem.html) | Running anthem at 180 BPM. |
| [Samurai-Run-Anthem.html](Samurai-Run-Anthem.html) | Japanese-themed variation with playback controls. |
| [Neural-Run-Anthem.html](Neural-Run-Anthem.html) | Cadence engine and audiovisual synthesis. |
| [Synthax-Engine.html](Synthax-Engine.html) | Real-time audio experiment with visualisation and interface telemetry. |
| [Extended-Hymn.html](Extended-Hymn.html) | Musical sequence generator using oscillators. |
| [Epic-Hymn.html](Epic-Hymn.html) | Chord and synthesis experiment using Web Audio API. |

## Interface and sound variations

- [Clan Operations Audio](Clan-Operations-Audio.html)
- [Extraction Point Audio](Extraction-Point-Audio.html)
- [Field Operations Audio](Field-Operations-Audio.html)
- [Hostile Zone Audio](Hostile-Zone-Audio.html)
- [Limits Cadence Audio](Limits-Cadence-Audio.html)
- [Movement Cadence Audio](Movement-Cadence-Audio.html)
- [Rain Cadence Audio](Rain-Cadence-Audio.html)
- [Dark Zone Audio](Dark-Zone-Audio.html)

These are independent visual or audio variations. Their names describe the theme, not a connection to real operational systems.

## JavaScript automation

- `Access-Request-Draft-Generator.gs`: Google Apps Script that locates access requests in Gmail and prepares response drafts. The configuration contains example values and must be adapted before use. It creates drafts; it does not send messages.

## Run locally

Open any `.html` file in a modern browser. To serve the directory locally:

```bash
python -m http.server 8000
```

Visit `http://localhost:8000` and open the experiment you want to try.

## Technology

- HTML5 and CSS3
- JavaScript
- Web Audio API
- Canvas and browser APIs
- Google Apps Script

## Notes

- Audio experiments may require explicit user interaction to start because of browser autoplay policies.
- HTML documents use the `.html` extension; the `.gs` file contains Google Apps Script automation.
- These are interface prototypes, not production applications.

## License

See [LICENSE](LICENSE).
