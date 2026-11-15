"""ノートのコードを上から順に実行して確かめる。

- `raises-exception` の印があるセルは、エラーになることを確かめる
- それ以外のセルは、エラーなく動くことを確かめる
- `input` は決まった値を返すように差し替える

使い方: py -I tools/check.py
"""
import builtins
import contextlib
import io
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def fake_input(prompt=""):
    if "年" in prompt:
        return "2007"
    if "段" in prompt or "数" in prompt:
        return "7"
    return "山田 太郎"


def run(path):
    nb = json.loads(path.read_text(encoding="utf-8"))
    ns = {"__name__": "__main__"}
    problems = []
    n = 0
    for i, cell in enumerate(nb["cells"]):
        if cell["cell_type"] != "code":
            continue
        n += 1
        src = "".join(cell["source"])
        expect_error = "raises-exception" in cell.get("metadata", {}).get("tags", [])
        out = io.StringIO()
        err = None
        try:
            with contextlib.redirect_stdout(out):
                exec(compile(src, f"<cell {i}>", "exec"), ns)
        except Exception as e:  # noqa: BLE001
            err = f"{type(e).__name__}: {e}"
        if expect_error and err is None:
            problems.append(f"  セル {i}: エラーになるはずが動いた")
        if not expect_error and err is not None:
            problems.append(f"  セル {i}: {err}")
    return n, problems


def main():
    builtins.input = fake_input
    bad = 0
    for folder in ["notebooks", "solutions"]:
        for path in sorted((ROOT / folder).glob("*.ipynb")):
            n, problems = run(path)
            mark = "OK " if not problems else "NG "
            print(f"{mark}{folder}/{path.name} (コード {n} セル)")
            for p in problems:
                print(p)
            bad += len(problems)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
