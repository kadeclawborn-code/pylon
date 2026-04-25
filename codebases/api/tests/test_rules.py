"""Rule-level tests. One section per rule."""

from __future__ import annotations

from pylon.analyzer import run_analyzer
from tests.conftest import make_diff


# ---- python.bare-except ---------------------------------------------------


def test_bare_except_flags_bare() -> None:
    d = make_diff("svc/handler.py", added=["    try:", "        do()", "    except:", "        pass"])
    f = run_analyzer(diff=d, enabled_rules=["python.bare-except"])
    assert len(f) == 1
    assert "Bare `except:`" in f[0].message


def test_bare_except_skips_typed_except() -> None:
    d = make_diff("svc/handler.py", added=["    try:", "        do()", "    except Exception:", "        pass"])
    assert run_analyzer(diff=d, enabled_rules=["python.bare-except"]) == []


def test_bare_except_skips_test_paths() -> None:
    """PYL-302 — Arcola Studios reported false positives on tests with intentional bare-except."""
    d = make_diff("tests/test_x.py", added=["    except:", "        pass"])
    assert run_analyzer(diff=d, enabled_rules=["python.bare-except"]) == []


# ---- python.print-in-prod -------------------------------------------------


def test_print_in_prod_flags_print() -> None:
    d = make_diff("svc/handler.py", added=["    print('hi')"])
    f = run_analyzer(diff=d, enabled_rules=["python.print-in-prod"])
    assert len(f) == 1


def test_print_in_prod_skips_test_paths() -> None:
    d = make_diff("tests/test_x.py", added=["    print('hi')"])
    assert run_analyzer(diff=d, enabled_rules=["python.print-in-prod"]) == []


# ---- python.todo-without-author -------------------------------------------


def test_todo_without_author_flags() -> None:
    d = make_diff("svc/handler.py", added=["    # TODO: handle this case"])
    f = run_analyzer(diff=d, enabled_rules=["python.todo-without-author"])
    assert len(f) == 1


def test_todo_with_author_passes() -> None:
    d = make_diff("svc/handler.py", added=["    # TODO @hugo: handle this case"])
    assert run_analyzer(diff=d, enabled_rules=["python.todo-without-author"]) == []


def test_fixme_also_flagged() -> None:
    d = make_diff("svc/handler.py", added=["    # FIXME this leaks"])
    f = run_analyzer(diff=d, enabled_rules=["python.todo-without-author"])
    assert len(f) == 1
    assert "FIXME" in f[0].message


# ---- python.bare-mutex ----------------------------------------------------


def test_bare_mutex_flags_lock() -> None:
    d = make_diff("svc/handler.py", added=["lock = threading.Lock()", "lock.acquire()"])
    f = run_analyzer(diff=d, enabled_rules=["python.bare-mutex"])
    assert len(f) == 1


def test_with_lock_passes() -> None:
    d = make_diff("svc/handler.py", added=["with threading.Lock() as lock:", "    do()"])
    assert run_analyzer(diff=d, enabled_rules=["python.bare-mutex"]) == []


# ---- python.async-without-await -------------------------------------------


def test_async_without_await_flags() -> None:
    d = make_diff(
        "svc/handler.py",
        added=["async def fetch():", "    return 1"],
    )
    f = run_analyzer(diff=d, enabled_rules=["python.async-without-await"])
    assert len(f) == 1


def test_async_with_await_passes() -> None:
    d = make_diff(
        "svc/handler.py",
        added=["async def fetch():", "    x = await client.get('/')", "    return x"],
    )
    assert run_analyzer(diff=d, enabled_rules=["python.async-without-await"]) == []


def test_async_with_yield_passes() -> None:
    """Async generators that yield without awaiting are accepted (documented FP corner)."""
    d = make_diff(
        "svc/handler.py",
        added=["async def gen():", "    yield 1", "    yield 2"],
    )
    assert run_analyzer(diff=d, enabled_rules=["python.async-without-await"]) == []
