import ulid


def ulid_gen() -> str:
    return ulid.new().str
