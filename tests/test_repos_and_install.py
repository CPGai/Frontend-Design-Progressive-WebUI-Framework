"""
Test suite verifying UI/UX reference repository ingestion and global installation.
Validates file presence, minimum size thresholds, absence of scraper headers,
exact content parity between local and global skills, and YAML frontmatter schemas.
"""

from pathlib import Path
import pytest
import yaml

REPO_BASE = Path("a:/Google Drive CPG/AI_projects_VIBE-Coding/CarlosPG-Skills/skills-CPG/Frontend-Design_WebUI/reference-repos")
GLOBAL_SKILL_DIR = Path("C:/Users/carlo/.gemini/config/skills/frontend-design")

ALL_MANAGED_FILES = [
    REPO_BASE / "anthropic-frontend-design" / "SKILL.md",
    REPO_BASE / "anthropic-frontend-design" / "LICENSE.txt",
    REPO_BASE / "vercel-web-interface-guidelines" / "README.md",
    REPO_BASE / "vercel-web-interface-guidelines" / "AGENTS.md",
    REPO_BASE / "vercel-web-interface-guidelines" / "command.md",
    REPO_BASE / "vercel-web-interface-guidelines" / "SKILL.md",
    REPO_BASE / "shadcn-ui-skill" / "SKILL.md",
    REPO_BASE / "shadcn-ui-skill" / "cli.md",
    REPO_BASE / "shadcn-ui-skill" / "customization.md",
    REPO_BASE / "shadcn-ui-skill" / "design-system.md",
    REPO_BASE / "shadcn-ui-skill" / "rules" / "composition.md",
    REPO_BASE / "shadcn-ui-skill" / "rules" / "forms.md",
    REPO_BASE / "shadcn-ui-skill" / "rules" / "styling.md",
    REPO_BASE / "shadcn-ui-skill" / "rules" / "base-vs-radix.md",
    REPO_BASE / "shadcn-ui-skill" / "rules" / "icons.md",
    GLOBAL_SKILL_DIR / "SKILL.md",
    GLOBAL_SKILL_DIR / "LICENSE.txt",
]


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


@pytest.mark.parametrize("file_path", ALL_MANAGED_FILES, ids=lambda p: p.name)
def test_file_exists_and_meets_size_threshold(file_path: Path):
    """Ensure every managed file exists on disk and has substantial content (>100 bytes)."""
    assert file_path.exists(), f"Expected file does not exist: {file_path}"
    assert file_path.is_file(), f"Path is not a regular file: {file_path}"
    size = file_path.stat().st_size
    assert size > 100, f"File {file_path} is too small ({size} bytes)"


@pytest.mark.parametrize("file_path", ALL_MANAGED_FILES, ids=lambda p: p.name)
def test_no_download_tell_header(file_path: Path):
    """Ensure downloaded files do not include the raw GitHub scraper header line."""
    content = file_path.read_text(encoding="utf-8")
    assert "successfully downloaded text file" not in content, (
        f"Scraper header detected in {file_path}"
    )


def test_anthropic_frontend_design_parity_and_frontmatter():
    """Verify local and global Anthropic frontend-design files are identical and have valid frontmatter."""
    local_skill = REPO_BASE / "anthropic-frontend-design" / "SKILL.md"
    global_skill = GLOBAL_SKILL_DIR / "SKILL.md"
    local_license = REPO_BASE / "anthropic-frontend-design" / "LICENSE.txt"
    global_license = GLOBAL_SKILL_DIR / "LICENSE.txt"

    # Exact content parity
    assert local_skill.read_text(encoding="utf-8") == global_skill.read_text(encoding="utf-8")
    assert local_license.read_text(encoding="utf-8") == global_license.read_text(encoding="utf-8")

    # Frontmatter validation
    meta_local = _extract_frontmatter(local_skill)
    meta_global = _extract_frontmatter(global_skill)

    assert meta_local.get("name") == "frontend-design"
    assert meta_global.get("name") == "frontend-design"
    assert "description" in meta_local
    assert "Apache License" in local_license.read_text(encoding="utf-8")


def test_shadcn_skill_frontmatter_and_content():
    """Verify shadcn SKILL.md frontmatter schema and key architectural sections."""
    skill_file = REPO_BASE / "shadcn-ui-skill" / "SKILL.md"
    meta = _extract_frontmatter(skill_file)

    assert meta.get("name") == "shadcn"
    assert "description" in meta

    content = skill_file.read_text(encoding="utf-8")
    assert "## Principles" in content
    assert "## Critical Rules" in content
    assert "## Component Selection" in content
    assert "## Updating Components" in content


def test_shadcn_submodules_content():
    """Verify auxiliary shadcn documentation rules files contain required domain guidelines."""
    cli_doc = (REPO_BASE / "shadcn-ui-skill" / "cli.md").read_text(encoding="utf-8")
    assert "init" in cli_doc and "apply" in cli_doc and "add" in cli_doc

    styling_doc = (REPO_BASE / "shadcn-ui-skill" / "rules" / "styling.md").read_text(encoding="utf-8")
    assert "Semantic colors" in styling_doc
    assert "size-*" in styling_doc

    forms_doc = (REPO_BASE / "shadcn-ui-skill" / "rules" / "forms.md").read_text(encoding="utf-8")
    assert "FieldGroup" in forms_doc
    assert "InputGroup" in forms_doc

    composition_doc = (REPO_BASE / "shadcn-ui-skill" / "rules" / "composition.md").read_text(encoding="utf-8")
    assert "SelectGroup" in composition_doc
    assert "Alert" in composition_doc


def test_vercel_guidelines_integrity():
    """Verify Vercel web-interface-guidelines documentation and AGENTS.md rules."""
    agents_file = REPO_BASE / "vercel-web-interface-guidelines" / "AGENTS.md"
    content = agents_file.read_text(encoding="utf-8")

    assert "## Interactions" in content
    assert "## Layout" in content
    assert "## Animation" in content
    assert "## Performance" in content

    command_file = REPO_BASE / "vercel-web-interface-guidelines" / "command.md"
    cmd_meta = _extract_frontmatter(command_file)
    assert "description" in cmd_meta

    skill_file = REPO_BASE / "vercel-web-interface-guidelines" / "SKILL.md"
    skill_meta = _extract_frontmatter(skill_file)
    assert skill_meta.get("name") == "web-design-guidelines"
