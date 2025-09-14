import subprocess

def test_harvest_cli():
    result = subprocess.run(
        ["python", "-m", "rightly_stage0.cli", "harvest", "demo_slug"],
        capture_output=True
    )
    assert result.returncode == 0
    assert "harvest called for: demo_slug" in result.stdout.decode()