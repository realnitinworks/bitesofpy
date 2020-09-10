def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    for old, new in zip(old_reqs.strip().splitlines(), new_reqs.strip().splitlines()):
        old_package, old_version = old.split("==")
        new_package, new_version = new.split("==")
        old_version = tuple(int(v) for v in old_version.split("."))
        new_version = tuple(int(v) for v in new_version.split("."))
        if new_version > old_version:
            yield new_package
