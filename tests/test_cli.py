import subprocess
import os

def test_harvest_cli():
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.abspath("src")
    result = subprocess.run(
        ["python", "-m", "rightly_stage0.cli", "harvest", "demo_slug"],
        capture_output=True,
        env=env
    )
    assert result.returncode == 0
    assert "harvest called for: demo_slug" in result.stdout.decode()