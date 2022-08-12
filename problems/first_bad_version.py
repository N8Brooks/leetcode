import bisect

BAD_VERSION: int


def set_bad_version(bad_version: int) -> None:
    """Set bad version for testing"""
    global BAD_VERSION  # pylint: disable=global-statement
    BAD_VERSION = bad_version


def is_bad_version(version: int) -> bool:
    return version >= BAD_VERSION


def first_bad_version(n: int) -> int:
    return bisect.bisect_left(range(n), True, key=is_bad_version)
