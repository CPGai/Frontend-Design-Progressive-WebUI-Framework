# Frontend-Design & Progressive WebUI Framework

Un framework y ecosistema unificado de ingeniería de software frontend para diseñar, maquetar, estructurar y auditar interfaces web accesibles, hermosas y cognitivamente ergonómicas.

Diseñado específicamente para mitigar el antipatrón de **"Backend Variable Dumping"** (volcado de variables de backend) y eliminar los clichés de diseño generados por IA, integrando las mejores prácticas de **Anthropic**, **Vercel Labs**, **shadcn/ui** y **using-agent-skills**.

---

## 1. Arquitectura y Procedencia de Fuentes

| Fuente Oficial | Repositorio / Origen | Rol en el Framework |
| :--- | :--- | :--- |
| **Anthropic** | `anthropics/skills/skills/frontend-design` | **Aesthetic Restraint:** Dirección de arte en 2 pases, paletas semánticas de 4–6 tokens hex, tipografía disciplinada y copywriting en lenguaje humano. |
| **Vercel Labs** | `vercel-labs/web-interface-guidelines` & `agent-skills` | **Hard Rules & Ergonomics:** Más de 100 reglas estrictas de accesibilidad, focus rings, interacción táctil, rendimiento, animación GPU y contraste APCA. |
| **shadcn/ui** | `shadcn-ui/ui/skills/shadcn` (vía `skills.sh`) | **Semantic Primitives:** Composición estricta (`FieldGroup`, `ToggleGroup`, `SheetTitle`), tokens semánticos y sincronización CLI con dry-run y smart merge. |
| **Google Antigravity** | `agent-skills` (`using-agent-skills`, `browser-testing`) | **Triaje y Verificación:** Triaje cognitivo previo, orquestación de subagentes y verificación empírica en navegador Chromium real. |

---

## 2. Estructura del Repositorio

```text
Frontend-Design_WebUI/
├── reference-repos/                    # Fuentes originales intactas sin headers de scraping
│   ├── anthropic-frontend-design/      # SKILL.md oficial y LICENSE.txt (Apache 2.0)
│   ├── vercel-web-interface-guidelines/# README.md, AGENTS.md, command.md, SKILL.md
│   └── shadcn-ui-skill/                # SKILL.md, CLI, personalización, reglas de composición
├── agents/
│   └── frontend-design-agent.md        # Subagente auditor y diseñador UI/UX especializado
├── skills/
│   └── progressive-webui-workflow/     # Flujo maestro secuencial de 5 compuertas
│       └── SKILL.md
├── templates/
│   └── PROGRESSIVE_UI_RULE_TEMPLATE.md # Directiva para CLAUDE.md / GEMINI.md de cualquier repo
└── tests/
    ├── test_repos_and_install.py       # Pruebas de ingestión y paridad de repositorios
    └── test_framework_integration.py   # Pruebas de integración del framework y skills globales
```

---

## 3. La Arquitectura de Divulgación Progresiva (Hick's Law)

Para evitar la parálisis cognitiva del usuario, toda pantalla o componente se descompone en tres estratos:

1. **Estrato 1 (Vista Principal Esencial):**
   - Máximo **3 a 4 controles directos** y **1 acción primaria dominante (CTA)**.
   - Cero parámetros de calibración numérica en la vista inicial.
2. **Estrato 2 (Modos y Perfiles Semánticos):**
   - Agrupación de variables técnicas en selectores semánticos intuitivos (`ToggleGroup`, `Select`, `Tabs`) con perfiles predefinidos (ej. *"Modo Silencioso"*, *"Equilibrado"*, *"Máximo Rendimiento"*).
3. **Estrato 3 (Cajón de Parámetros Avanzados):**
   - El 10% de ajustes avanzados o de diagnóstico se aísla en paneles laterales deslizantes (`Sheet`, `<dialog id="adv-drawer">`) o acordeones colapsados (`Accordion`, `<details>`), accesibles mediante un disparador sutil *"Ajustes avanzados…"*.

---

## 4. Las 5 Compuertas del Workflow Secuencial

```text
[Compuerta 1: Triaje Cognitivo] ──> [Compuerta 2: Dirección de Arte] ──> [Compuerta 3: Ensamblaje Estructural]
                                                                                        │
                                    [Compuerta 5: Verificación Browser] <── [Compuerta 4: Auditoría Estática]
```

1. **Compuerta 1 — Triaje Cognitivo (`using-agent-skills`):** Matriz markdown clasificando cada variable del backend en Estrato 1, 2, 3 o Interno.
2. **Compuerta 2 — Dirección de Arte en 2 Pases (`frontend-design`):** Definición de paleta de 4–6 hex tokens, escala tipográfica, wireframe ASCII de los 3 estratos, erradicación de clichés IA y reescritura de etiquetas técnicas.
3. **Compuerta 3 — Ensamblaje Estructural (`shadcn` + fallbacks nativos):** Implementación con primitivas accesibles (`FieldGroup`, `ToggleGroup`, `<Sheet>` o equivalentes HTML5 `<dialog>`/`<details>`), estados obligatorios (`Empty`, `Skeleton`, `Error`).
4. **Compuerta 4 — Auditoría Estática (`frontend-design-agent`):** Revisión automatizada contra >100 reglas de accesibilidad, targets $\ge 24\text{px}$ ($44\text{px}$ móvil), `prefers-reduced-motion`, `tabular-nums` y formato `file:line`.
5. **Compuerta 5 — Verificación Visual en Chromium Real (`browser-testing-with-devtools`):** Auditoría en breakpoints (320px, 768px, 1024px, 1440px), validación de cero scroll horizontal y apertura fluida del cajón de Estrato 3.

---

## 5. Guía Rápida de Uso

### En Google Antigravity 2.0

1. **Instalación Global:** Los skills y agentes ya quedan activos en tu perfil global de Antigravity:
   - `~/.gemini/config/skills/frontend-design/`
   - `~/.gemini/config/skills/shadcn/`
   - `~/.gemini/config/skills/progressive-webui-workflow/`
   - `~/.gemini/config/plugins/agent-skills/agents/frontend-design-agent.md`
2. **Invocar el Agente de Diseño en Chat:**
   ```text
   Invoca al subagente frontend-design-agent para auditar la interfaz en src/components/Dashboard.tsx
   ```
3. **Aplicar el Workflow Completo a una Nueva Interfaz:**
   ```text
   Activa el skill progressive-webui-workflow para diseñar la interfaz del gestor de tareas siguiendo las 5 compuertas.
   ```

### En Cualquier Repositorio de Trabajo
Copia el bloque de [`templates/PROGRESSIVE_UI_RULE_TEMPLATE.md`](./templates/PROGRESSIVE_UI_RULE_TEMPLATE.md) directamente en el archivo `AGENTS.md`, `CLAUDE.md` o `GEMINI.md` de tu proyecto. El asistente respetará automáticamente la Divulgación Progresiva y el límite de 4 controles en la vista inicial.

---

## 6. Verificación de la Suite de Pruebas

Ejecuta el conjunto completo de pruebas con pytest:

```bash
python -m pytest "a:/Google Drive CPG/AI_projects_VIBE-Coding/CarlosPG-Skills/skills-CPG/Frontend-Design_WebUI/tests" -v
```
