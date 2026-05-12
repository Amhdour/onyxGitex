from __future__ import annotations

from onyx.security_readiness.citation_filter import CitationReadyChunk
from onyx.security_readiness.citation_filter import build_source_docs_and_citations
from onyx.security_readiness.citation_filter import filter_authorized_chunks

LEAK_MARKER = "DENIED_LEAK_MARKER"
DENIED_DOCUMENT_ID = "doc-denied"
ALLOWED_DOCUMENT_ID = "doc-allowed"


def _build_chunk(*, document_id: str, semantic_identifier: str, blurb: str, link: str, owner: str, chunk_id: int) -> CitationReadyChunk:
    return CitationReadyChunk(
        document_id=document_id,
        chunk_id=chunk_id,
        semantic_identifier=semantic_identifier,
        blurb=blurb,
        link=link,
        metadata={"owner": owner, "classification": "internal"},
    )


def _allowed_and_denied_chunks() -> tuple[CitationReadyChunk, CitationReadyChunk]:
    return (
        _build_chunk(
            document_id=ALLOWED_DOCUMENT_ID,
            semantic_identifier="Allowed Semantic ID",
            blurb="Allowed blurb",
            link="https://allowed.example/doc",
            owner="allowed-owner",
            chunk_id=1,
        ),
        _build_chunk(
            document_id=DENIED_DOCUMENT_ID,
            semantic_identifier=f"{LEAK_MARKER}-semantic",
            blurb=f"{LEAK_MARKER}-blurb",
            link=f"https://denied.example/{LEAK_MARKER}",
            owner=f"{LEAK_MARKER}-owner",
            chunk_id=2,
        ),
    )


def test_allowed_chunks_convert_normally() -> None:
    allowed, _ = _allowed_and_denied_chunks()
    docs, citations = build_source_docs_and_citations([allowed], {ALLOWED_DOCUMENT_ID: True})
    assert len(docs) == 1
    assert docs[0].document_id == ALLOWED_DOCUMENT_ID
    assert docs[0].semantic_identifier == "Allowed Semantic ID"
    assert citations == {1: ALLOWED_DOCUMENT_ID}


def test_denied_chunks_excluded_before_conversion() -> None:
    allowed, denied = _allowed_and_denied_chunks()
    filtered = filter_authorized_chunks([allowed, denied], {ALLOWED_DOCUMENT_ID: True, DENIED_DOCUMENT_ID: False})
    assert [chunk.document_id for chunk in filtered] == [ALLOWED_DOCUMENT_ID]


def test_denied_document_id_absent_from_citation_mapping() -> None:
    allowed, denied = _allowed_and_denied_chunks()
    _, citations = build_source_docs_and_citations([allowed, denied], {ALLOWED_DOCUMENT_ID: True, DENIED_DOCUMENT_ID: False})
    assert DENIED_DOCUMENT_ID not in citations.values()


def test_denied_identifier_absent_from_source_docs() -> None:
    allowed, denied = _allowed_and_denied_chunks()
    docs, _ = build_source_docs_and_citations([allowed, denied], {ALLOWED_DOCUMENT_ID: True, DENIED_DOCUMENT_ID: False})
    rendered = " ".join(f"{doc.semantic_identifier} {doc.blurb}" for doc in docs)
    assert denied.semantic_identifier not in rendered


def test_denied_link_absent_from_source_docs() -> None:
    allowed, denied = _allowed_and_denied_chunks()
    docs, _ = build_source_docs_and_citations([allowed, denied], {ALLOWED_DOCUMENT_ID: True, DENIED_DOCUMENT_ID: False})
    assert denied.link not in [doc.link for doc in docs]


def test_mixed_allowed_denied_outputs_only_allowed_sources() -> None:
    allowed, denied = _allowed_and_denied_chunks()
    docs, citations = build_source_docs_and_citations([denied, allowed], {ALLOWED_DOCUMENT_ID: True, DENIED_DOCUMENT_ID: False})
    assert len(docs) == 1
    assert docs[0].document_id == ALLOWED_DOCUMENT_ID
    assert citations == {1: ALLOWED_DOCUMENT_ID}


def test_denied_leak_markers_absent_from_output() -> None:
    allowed, denied = _allowed_and_denied_chunks()
    docs, citations = build_source_docs_and_citations([allowed, denied], {ALLOWED_DOCUMENT_ID: True, DENIED_DOCUMENT_ID: False})
    output = str(citations) + " " + " ".join(f"{doc.document_id} {doc.semantic_identifier} {doc.blurb} {doc.metadata} {doc.link}" for doc in docs)
    assert LEAK_MARKER not in output
