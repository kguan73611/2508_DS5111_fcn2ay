import sys
sys.path.append('.')
import platform
import bin.normalize as nm

def test_of_pytest():
     assert True

def test_python_version():
    # GIVEN Python is available
    major, minor = sys.version_info[:2]

    # WHEN we check the python version
    version_str = f"{major}.{minor}"

    # THEN the python version should be a supported version >=3.9
    assert major == 3 and minor >= 9, f"Expected Python >= 3.9, got {version_str}"

def test_os_version():
    # GIVEN the system is running
    system = platform.system()
    release = platform.release()

    # WHEN we check the os
    version_info = f"{system} {release}"

    # THEN it should be Linux
    assert system == "Linux", f"Expected Linux, got {system}"

def test_os():
    is_linux = sys.platform.startswith("linux") or platform.system() == "Linux"
    assert is_linux, f"Expected Linux, got sys.platform={sys.platform}, platform.system()={platform.system()}"

def test_python_desired_version():
    allowed = {(3, 12), (3, 13)}
    current = (sys.version_info.major, sys.version_info.minor)
    assert current in allowed, f"Python {current[0]}.{current[1]} is not allowed; expected one of: {sorted(allowed)}"
