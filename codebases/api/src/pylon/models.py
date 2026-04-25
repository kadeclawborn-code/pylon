"""Pydantic models — request/response schemas, internal events."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field, model_validator


class Severity(str, Enum):
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    BLOCKING = "blocking"


class FileChange(BaseModel):
    """A single file's changes within a PR diff."""

    path: str
    language: str | None = None
    added: int = Field(ge=0)
    removed: int = Field(ge=0)
    patch: str
    """Unified diff text. Empty for binary/skipped files."""

    @model_validator(mode="after")
    def _patch_required_for_text(self) -> FileChange:
        # Binary files have empty patch; text files must have a patch.
        if self.language and not self.patch:
            raise ValueError(f"text file {self.path} must have a patch")
        return self


class Diff(BaseModel):
    """A PR's full diff."""

    pr_id: str
    base_sha: str
    head_sha: str
    files: list[FileChange]


class Finding(BaseModel):
    """A single analyzer finding to surface as a PR comment."""

    rule_id: str
    """e.g. 'python.bare-except'."""
    severity: Severity
    file_path: str
    line: int = Field(ge=1)
    """1-indexed line number in the *new* file."""
    message: str
    """Customer-facing message. Should fit one short paragraph."""
    suggestion: str | None = None
    """Optional fix suggestion. None for rules where suggestion isn't grounded enough yet."""

    @property
    def as_comment_body(self) -> str:
        """Render for posting as a PR comment."""
        body = f"**[{self.rule_id}]** {self.message}"
        if self.suggestion:
            body += f"\n\n_Suggestion:_ {self.suggestion}"
        return body


class AnalyzeRequest(BaseModel):
    """Request body for POST /analyze."""

    diff: Diff
    enabled_rules: list[str] | None = None
    """If None, run all default rules."""


class AnalyzeResponse(BaseModel):
    pr_id: str
    findings: list[Finding]
    rules_run: list[str]
    duration_ms: int


class WebhookEvent(BaseModel):
    """Normalized webhook event after signature verification.

    All upstream vendor differences are resolved into this shape before
    downstream services touch it. See the Switchyard adapter layer for the
    GitHub/GitLab/Bitbucket → ``WebhookEvent`` mapping.
    """

    vendor: Literal["github", "gitlab", "bitbucket"]
    event_type: Literal["pr_opened", "pr_updated", "pr_closed", "comment", "approval", "ping"]
    repo_full_name: str
    pr_number: int | None = None
    """None for events not tied to a PR (e.g. ``ping``)."""
    actor_login: str
    received_at: datetime
    raw_payload_size_bytes: int
