from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class CitationReadyChunk:
    document_id: str
    chunk_id: int
    semantic_identifier: str
    blurb: str
    link: str | None
    metadata: dict[str, str]


@dataclass(frozen=True)
class CitationReadySourceDoc:
    document_id: str
    chunk_ind: int
    semantic_identifier: str
    blurb: str
    link: str | None
    metadata: dict[str, str]


def filter_authorized_chunks(
    chunks: Sequence[CitationReadyChunk],
    authorization_decisions: dict[str, bool],
) -> list[CitationReadyChunk]:
    return [chunk for chunk in chunks if authorization_decisions.get(chunk.document_id, False)]


def build_source_docs_and_citations(
    chunks: Sequence[CitationReadyChunk],
    authorization_decisions: dict[str, bool],
) -> tuple[list[CitationReadySourceDoc], dict[int, str]]:
    allowed_chunks = filter_authorized_chunks(chunks, authorization_decisions)
    source_docs = [
        CitationReadySourceDoc(
            document_id=chunk.document_id,
            chunk_ind=chunk.chunk_id,
            semantic_identifier=chunk.semantic_identifier,
            blurb=chunk.blurb,
            link=chunk.link,
            metadata=chunk.metadata,
        )
        for chunk in allowed_chunks
    ]
    citation_mapping = {i: doc.document_id for i, doc in enumerate(source_docs, start=1)}
    return source_docs, citation_mapping
