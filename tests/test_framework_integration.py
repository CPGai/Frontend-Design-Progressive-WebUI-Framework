"""
Test suite verifying integration of the Unified Progressive WebUI Framework.
Validates file presence, global installation parity, clean Antigravity frontmatter,
structural completeness of frontend-design-agent, progressive-webui-workflow,
and rule templates.
"""

from pathlib import Path
import pytest
import yaml

REPO_ROOT = Path("a:/Google Drive CPG/AI_projects_VIBE-Coding/CarlosPG-Skills/skills-CPG/Frontend-Design_WebUI")
GLOBAL_CONFIG = Path("C:/Users/carlo/.gemini/config")

# Component A files
LOCAL_AGENT = REPO_ROOT / "agents" / "frontend-design-agent.md"
GLOBAL_AGENT = GLOBAL_CONFIG / "plugins" / "agent-skills" / "agents" / "frontend-design-agent.md"

# Component B files (Global shadcn skill)
GLOBAL_SHADCN_DIR = GLOBAL_CONFIG / "skills" / "shadcn"
GLOBAL_SHADCN_FILES = [
    GLOBAL_SHADCN_DIR / "SKILL.md",
    GLOBAL_SHADCN_DIR / "cli.md",
    GLOBAL_SHADCN_DIR / "customization.md",
    GLOBAL_SHADCN_DIR / "design-system.md",
    GLOBAL_SHADCN_DIR / "rules" / "composition.md",
    GLOBAL_SHADCN_DIR / "rules" / "forms.md",
    GLOBAL_SHADCN_DIR / "rules" / "styling.md",
    GLOBAL_SHADCN_DIR / "rules" / "base-vs-radix.md",
    GLOBAL_SHADCN_DIR / "rules" / "icons.md",
]

# Component C files
LOCAL_WORKFLOW_SKILL = REPO_ROOT / "skills" / "progressive-webui-workflow" / "SKILL.md"
GLOBAL_WORKFLOW_SKILL = GLOBAL_CONFIG / "skills" / "progressive-webui-workflow" / "SKILL.md"

# Component D files
TEMPLATE_FILE = REPO_ROOT / "templates" / "PROGRESSIVE_UI_RULE_TEMPLATE.md"
README_FILE = REPO_ROOT / "README.md"


def _extract_frontmatter(file_path: Path) -> dict:
    """Extract and parse YAML frontmatter delimited by triple hyphens."""
    content = file_path.read_text(encoding="utf-8")
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    closing_indices = [i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---"]
    if not closing_indices:
        return {}
    end_idx = closing_indices[0]
    frontmatter_raw = "\n".join(lines[1:end_idx])
    parsed = yaml.safe_load(frontmatter_raw)
    return parsed or {}


def test_agent_files_exist_and_match():
    """Verify frontend-design-agent exists locally and globally with exact parity."""
    assert LOCAL_AGENT.exists(), f"Missing local agent at {LOCAL_AGENT}"
    assert GLOBAL_AGENT.exists(), f"Missing global agent at {GLOBAL_AGENT}"

    local_text = LOCAL_AGENT.read_text(encoding="utf-8")
    global_text = GLOBAL_AGENT.read_text(encoding="utf-8")

    assert local_text == global_text, "Local and global agent definitions must be identical"

    meta = _extract_frontmatter(LOCAL_AGENT)
    assert meta.get("name") == "frontend-design-agent"
    assert "description" in meta


def test_agent_contains_all_four_pillars():
    """Verify frontend-design-agent encodes Hick's Law, Anthropic restraint, shadcn rules, and Vercel guidelines."""
    content = LOCAL_AGENT.read_text(encoding="utf-8")

    # Pillar 0: Progressive Disclosure & Hick's Law
    assert "Tier 1: Essential Primary View" in content
    assert "Tier 2: Semantic Modes & Profiles" in content
    assert "Tier 3: Advanced & Expert Parameters" in content
    assert "Backend Variable Dumping" in content
    assert "Max 3–4 Controls" in content

    # Pillar 1: Anthropic aesthetic restraint
    assert "Prohibited AI Design Clichés" in content
    assert "#F4F1EA" in content

    # Pillar 2: Component composition & Native fallbacks
    assert "FieldGroup" in content
    assert "ToggleGroup" in content
    assert "SheetTitle" in content
    assert "<dialog id=" in content
    assert "<details><summary" in content

    # Pillar 3: Vercel guidelines (>100 rules)
    assert "prefers-reduced-motion" in content
    assert "tabular-nums" in content
    assert "overscroll-behavior: contain" in content
    assert "touch-action: manipulation" in content
    assert "transition: all" in content

    # Scorecard
    assert "Progressive Disclosure & Ergonomics Scorecard" in content


@pytest.mark.parametrize("file_path", GLOBAL_SHADCN_FILES, ids=lambda p: p.name)
def test_global_shadcn_files_exist_and_substantial(file_path: Path):
    """Verify all global shadcn skill files exist and exceed 100 bytes."""
    assert file_path.exists(), f"Expected file does not exist: {file_path}"
    assert file_path.stat().st_size > 100, f"File too small: {file_path}"


def test_global_shadcn_clean_frontmatter():
    """Verify global shadcn SKILL.md has clean frontmatter without Antigravity incompatible keys."""
    skill_file = GLOBAL_SHADCN_DIR / "SKILL.md"
    content = skill_file.read_text(encoding="utf-8")

    assert "user-invocable: false" not in content
    assert "allowed-tools:" not in content

    meta = _extract_frontmatter(skill_file)
    assert meta.get("name") == "shadcn"
    assert "description" in meta
    assert "Principles" in content
    assert "Critical Rules" in content


def test_progressive_webui_workflow_skill_parity_and_content():
    """Verify master progressive-webui-workflow skill exists locally and globally with exact parity."""
    assert LOCAL_WORKFLOW_SKILL.exists()
    assert GLOBAL_WORKFLOW_SKILL.exists()

    local_text = LOCAL_WORKFLOW_SKILL.read_text(encoding="utf-8")
    global_text = GLOBAL_WORKFLOW_SKILL.read_text(encoding="utf-8")

    assert local_text == global_text, "Local and global workflow skills must be identical"

    meta = _extract_frontmatter(LOCAL_WORKFLOW_SKILL)
    assert meta.get("name") == "progressive-webui-workflow"
    assert "description" in meta

    # Verify 5 Gates
    assert "Gate 1: Cognitive Triage" in local_text
    assert "Gate 2: 2-Pass Art Direction" in local_text
    assert "Gate 3: Structural Assembly" in local_text
    assert "Gate 4: Static Audit" in local_text
    assert "Gate 5: Visual & Interactive Browser Verification" in local_text

    # Verify Mermaid and Stack mapping
    assert "```mermaid" in local_text
    assert "Stack Mapping Matrix" in local_text
    assert "<dialog>" in local_text
    assert "Definition of Done" in local_text


def test_rule_template_and_readme():
    """Verify rule template and README documentation completeness."""
    assert TEMPLATE_FILE.exists()
    assert README_FILE.exists()

    template_text = TEMPLATE_FILE.read_text(encoding="utf-8")
    assert "3-Tier Progressive Disclosure Architecture" in template_text
    assert "no more than 3 to 4 direct controls" in template_text
    assert "FieldGroup" in template_text
    assert "frontend-design-agent" in template_text

    readme_text = README_FILE.read_text(encoding="utf-8")
    assert "Anthropic" in readme_text
    assert "Vercel Labs" in readme_text
    assert "shadcn/ui" in readme_text
    assert "Hick's Law" in readme_text
    assert "Google Antigravity 2.0" in readme_text
