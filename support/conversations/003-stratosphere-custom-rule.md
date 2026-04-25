---
id: 003
account: acct_strato
customer_user: user_strato_002
pylon_agent: emp_033
channel: chat
status: resolved
opened_at: 2026-02-04T14:22:00Z
closed_at: 2026-02-04T17:11:00Z
category: [help, beacon, rules, custom-rules]
---

**Customer (Annika Sjöblom):**

Trying to write a custom rule that flags any function call to our internal `unsafe_subprocess()` helper. PRL syntax for matching a function call is...?

---

**Bridget:**

Annika — easy one.

```yaml
- id: stratosphere.unsafe-subprocess
  message: "unsafe_subprocess() called — use safe_subprocess() instead unless you have a specific reason."
  severity: medium
  match:
    language: python
    query: |
      (call function: (identifier) @name (#eq? @name "unsafe_subprocess"))
```

Drop that into your `pylon.yaml` under `custom_rules:`. The query is tree-sitter syntax; the `@name` capture and the `#eq?` predicate are standard.

---

**Customer:**

Works. Three findings on the first PR I tested it against (preview mode). Two are real; one is in a test fixture.

How do I scope it the same way python.bare-except does (default-skip tests)?

---

**Bridget:**

Add a `paths.exclude` block:

```yaml
- id: stratosphere.unsafe-subprocess
  message: ...
  severity: medium
  paths:
    exclude:
      - tests/**
      - "**/test_*.py"
      - "**/*_test.py"
      - "**/conftest.py"
  match:
    language: python
    query: ...
```

That's the same exclusion pattern Beacon uses for python.bare-except by default.

---

**Customer:**

That worked. Going to ship this rule into shadow mode for a week, then promote to default-on if FP rate is reasonable.

When the Marketplace launches, can I publish this rule? It feels like other teams using subprocess wrappers might want it.

---

**Bridget:**

Yes — you'll be able to publish from the dashboard once Marketplace public preview launches in March (PYL-100 if you're tracking our roadmap). Feel free to ping me when you're ready and I'll walk you through the publishing flow.

---

**Customer:**

Will do. Thanks Bridget.
