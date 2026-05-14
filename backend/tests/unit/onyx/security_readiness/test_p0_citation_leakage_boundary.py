from onyx.security_readiness.citation_filter import CitationReadyChunk
from onyx.security_readiness.citation_filter import build_source_docs_and_citations


def test_restricted_citations_are_filtered() -> None:
    chunks = [
        CitationReadyChunk("doc-allowed", 1, "Allowed", "ok", None, {"class": "internal"}),
        CitationReadyChunk("doc-restricted", 2, "Restricted", "no", None, {"class": "secret"}),
    ]

    source_docs, citations = build_source_docs_and_citations(
        chunks,
        {"doc-allowed": True, "doc-restricted": False},
    )

    assert [d.document_id for d in source_docs] == ["doc-allowed"]
    assert citations == {1: "doc-allowed"}
