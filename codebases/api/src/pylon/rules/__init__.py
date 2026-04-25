"""Beacon rule implementations.

Each rule is a module exporting a single ``check(diff: Diff) -> list[Finding]``
function. Modules are imported by name from ``pylon.analyzer`` and registered
in the rule dispatch table there.

Adding a rule:
1. Create ``pylon/rules/<rule_name>.py`` with a ``check`` function.
2. Add a customer-facing docs page at ``pylon.dev/docs/rules/<rule-id>``.
3. Register it in ``pylon.analyzer._RULES``.
4. Write tests under ``tests/rules/test_<rule_name>.py``.
5. Calibrate severity vs. false-positive rate against the customer corpus
   (see ``docs/architecture.md`` for the calibration process).

The rule modules in this package are deliberately small — one file per
rule, terse implementations. The complexity in real rule design lives in
the test corpus and the calibration data, not in the detection code.
"""
