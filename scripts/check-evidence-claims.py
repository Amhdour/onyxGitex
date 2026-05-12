#!/usr/bin/env python3
from pathlib import Path
import sys

ROOTS = [Path('security-readiness'), Path('agent-security-readiness'), Path('portfolio')]
EXTS = {'.md', '.txt', '.json'}
RISKY = ['safe to launch', 'fully verified', 'runtime verified', 'leakage prevented', 'tool authorization verified', 'PASS']
QUALIFIERS = ['NOT_ENOUGH_EVIDENCE', 'not verified', 'pending', 'example', 'template', 'required evidence', 'claims_not_allowed']

findings = []
for root in ROOTS:
    if not root.exists():
        continue
    for path in root.rglob('*'):
        if path.is_file() and path.suffix in EXTS:
            lines = path.read_text(encoding='utf-8', errors='ignore').splitlines()
            for idx, line in enumerate(lines, 1):
                lower = line.lower()
                for phrase in RISKY:
                    if phrase.lower() in lower:
                        window = ' '.join(lines[max(0, idx-2):min(len(lines), idx+1)]).lower()
                        if not any(q.lower() in window for q in QUALIFIERS):
                            findings.append((path, idx, phrase, line.strip()))

if findings:
    print('Forbidden claim findings:')
    for path, line_no, phrase, line in findings:
        print(f'{path}:{line_no} [{phrase}] {line}')
    sys.exit(1)

print('No clear forbidden claims found.')
