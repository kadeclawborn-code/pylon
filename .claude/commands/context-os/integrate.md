# Integrate: Auto-Generate Product Docs from Existing Codebase

Welcome! This command analyzes your existing codebase and automatically generates Context-OS product documentation, enabling instant adoption without manual product planning.

**What this command does:**
1. Analyzes your codebase to discover features, architecture, and tech stack
2. Auto-generates product documentation (mission, roadmap, tech-stack)
3. Creates integration guides for your next steps with Context-OS

This is perfect for established projects that want to adopt Context-OS without starting from scratch.

---

**IMPORTANT:** Ensure that your analysis and generated documentation IS ALIGNED and DOES NOT CONFLICT with any of user's preferred tech stack, coding conventions, or patterns as detailed in the following files:

@context-os/standards/backend/api.md
@context-os/standards/backend/migrations.md
@context-os/standards/backend/models.md
@context-os/standards/backend/queries.md
@context-os/standards/frontend/accessibility.md
@context-os/standards/frontend/components.md
@context-os/standards/frontend/css.md
@context-os/standards/frontend/responsive.md
@context-os/standards/global/coding-style.md
@context-os/standards/global/commenting.md
@context-os/standards/global/conventions.md
@context-os/standards/global/error-handling.md
@context-os/standards/global/tech-stack.md
@context-os/standards/global/validation.md
@context-os/standards/testing/test-writing.md

---

{{PHASE 0: @context-os/commands/integrate/0-integrate-intro.md}}

{{PHASE 1: @context-os/commands/integrate/1-analyze-codebase.md}}

{{PHASE 2: @context-os/commands/integrate/2-generate-product-docs.md}}

{{PHASE 3: @context-os/commands/integrate/3-validate-confirm.md}}

{{PHASE 4: @context-os/commands/integrate/4-verify-improve-standards.md}}

---

## Integration Complete! 🎉

You've successfully integrated Context-OS with your existing project.

**Final Documentation (clean, production-ready):**

📁 **Product Documentation:**
- ✅ `context-os/product/mission.md` - Product vision
- ✅ `context-os/product/roadmap.md` - Feature roadmap
- ✅ `context-os/product/tech-stack.md` - Technology stack

📁 **Standards Documentation:**
- ✅ `context-os/standards/global/README.md` - Master standards overview (300+ lines)
- ✅ `context-os/standards/global/core-rules.md` - Mandatory development rules
- ✅ `context-os/standards/global/architecture-principles.md` - Design principles
- ✅ `context-os/standards/global/coding-style.md` - Code style with real examples
- ✅ `context-os/standards/global/conventions.md` - Project conventions
- ✅ `context-os/standards/global/error-handling.md` - Error patterns
- ✅ `context-os/standards/global/tech-stack.md` - Technology reference
- ✅ `context-os/standards/testing/README.md` - Testing standards
- ✅ `context-os/standards/testing/tdd-process.md` - TDD process (if applicable)

📁 **Integration Guides:**
- ✅ `context-os/integration/integration-guide.md` - Your next steps guide
- ✅ `context-os/integration/feature-map.md` - Feature mapping

📁 **Configuration:**
- ✅ `context-os/config.yml` - Context-OS configuration

**Quality Assurance:**
5 specialized agents verified and improved your standards documentation in parallel:
- Structure Verifier → Ensured 300+ line README with all sections
- Code Examples Verifier → Replaced placeholders with real codebase examples
- Metrics Verifier → Corrected all statistics to match actual codebase
- Cross-Reference Verifier → Fixed all broken links and references
- Completeness Verifier → Added any missing content

**Cleanup Applied:**
Intermediate files (analysis data, validation reports) have been removed. Only essential, production-ready documentation remains.

**What to do next:**
1. **Review** the standards in `context-os/standards/global/README.md` - this is your anchor document
2. **Share** standards with your team for code review reference
3. **Create specs** for new features using `/shape-spec` or `/write-spec`
4. **Enforce** standards in CI/CD and code review processes

See `context-os/integration/integration-guide.md` for complete next steps!

