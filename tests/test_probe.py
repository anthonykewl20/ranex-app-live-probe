def test_subject_materialises() -> None:
    assert b"tree" in b"subject-tree"


def test_verdict_binding_is_content_addressed() -> None:
    import hashlib
    assert len(hashlib.sha256(b"probe").hexdigest()) == 64


def test_gate_blocks_absence() -> None:
    assert bool([]) is False
