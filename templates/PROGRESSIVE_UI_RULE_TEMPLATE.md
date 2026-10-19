# Progressive WebUI & Cognitive Ergonomics Rule

> **Paste this block into your project's `CLAUDE.md`, `GEMINI.md`, or `AGENTS.md` to enforce human-centered design, cognitive ergonomics, and accessibility.**

```markdown
<!-- START: PROGRESSIVE_WEBUI_RULE -->
## Mandatory Web UI & UX Engineering Protocol (Hick's Law & Progressive Disclosure)

When designing, refactoring, or building user interfaces in this repository, you MUST adhere to the **3-Tier Progressive Disclosure Architecture**:

### 1. Prohibition of "Backend Variable Dumping"
- **NEVER** expose raw backend variables, hyperparameters, numerical tuning fields, or diagnostic timeouts directly on the primary viewport.
- **Strict Tier 1 Boundary:** The initial view MUST present **no more than 3 to 4 direct controls** and exactly **1 primary Call-to-Action (CTA)**.

### 2. The 3-Tier Hierarchy
1. **Tier 1 (Essential / Primary Path):** The primary input and primary CTA only. Clear, immediate visual feedback.
2. **Tier 2 (Semantic Modes & Presets):** Group technical complexity into high-level human profiles (e.g., *"Modo Silencioso"*, *"Equilibrado"*, *"Máximo Rendimiento"*) using composite selectors (`ToggleGroup`, `Select`, or `Tabs`).
3. **Tier 3 (Advanced & Expert Tuning):** Isolate specialized parameters inside slide-over drawers (`Sheet`, `<dialog id="adv-drawer">`) or collapsed accordions (`Accordion`, `<details>`). Provide an accessible trigger labeled *"Ajustes avanzados…"*.

### 3. Component & Ergonomics Standards
- **Component Primitives:** Use accessible primitives (`shadcn/ui` for React/Next.js/Vite, or native `<dialog>`/`<details>` and CSS custom properties for vanilla/Python stacks).
- **Form Layout:** Forms MUST use `FieldGroup` + `Field` with `gap-*`. NEVER use raw `div` with `space-y-*`.
- **Aesthetic Direction:** Avoid generic AI clichés (warm cream backgrounds `#F4F1EA`, identical SaaS cards, tracked ALL-CAPS subtitles). Build an intentional 4–6 hex token palette.
- **Human Copywriting:** Use active voice from the user's perspective (*"Guardar cambios"* instead of *"Submit"*; *"Notificaciones"* instead of *"Webhook config"*).
- **Accessibility & Vercel Guidelines:**
  - Visible focus rings (`:focus-visible`; `:focus-within`). Never `outline: none` without replacement.
  - Touch targets $\ge 24\text{px}$ (mobile $\ge 44\text{px}$). Input font size $\ge 16\text{px}$.
  - Honor `prefers-reduced-motion`; animate `transform`/`opacity` only; never `transition: all`.
  - Numeric comparisons must use `font-variant-numeric: tabular-nums`.
  - True ellipsis `…` (U+2026), never three periods `...`.
  - Modals and drawers must set `overscroll-behavior: contain`.

### 4. Mandatory Verification Gate
Before declaring any UI task complete:
- Perform an ergonomic review using the `frontend-design-agent` scorecard.
- Verify in a browser: Ensure zero horizontal overflow (`document.documentElement.scrollWidth <= innerWidth`) across mobile (320px), tablet (768px), and desktop (1280px+).
<!-- END: PROGRESSIVE_WEBUI_RULE -->
```
