# Team Tools & Utilities — Recommended Stack for IT Agent Operations

## Purpose

Curated tool recommendations to help the IT team work more efficiently. Maintained by picard, reviewed quarterly.

---

## 1. Knowledge Base Management Tools

| Tool                    | Use Case                     | Command/Integration                  | Priority |
| ----------------------- | ---------------------------- | ------------------------------------ | -------- |
| **GitHub Actions**      | Automated index updates      | `gh api /repos/:owner/:repo/actions` | HIGH     |
| **Text Processing CLI** | Document parsing, validation | `jq`, `sed`, `awk`                   | MEDIUM   |
| **Markdown Linter**     | Consistent formatting        | `markdownlint-cli2`                  | LOW      |

```bash
# Example: Automated index verification script
cat > verify-index.sh << 'EOF'
#!/bin/bash
echo "=== Knowledge Base Index Verification ==="
find knowledge_base/documents -name "*.md" -exec basename {} \; | sort > /tmp/docs.txt
grep -c "\.md$" /tmp/docs.txt && echo "Documents found: ✓" || echo "No documents: ✗"
EOF

chmod +x verify-index.sh
./verify-index.sh
```

---

## 2. Documentation Generation Tools

| Tool        | Use Case               | Integration                        | Priority |
| ----------- | ---------------------- | ---------------------------------- | -------- |
| **Docdash** | Auto-generate API docs | CLI, GitHub Action                 | MEDIUM   |
| **MkDocs**  | Static site generation | Python package                     | LOW      |
| **Pandoc**  | Format conversion      | `pandoc --from markdown --to html` | LOW      |

---

## 3. Collaboration & Communication Tools

| Tool                        | Use Case                 | Team Member                      | Priority |
| --------------------------- | ------------------------ | -------------------------------- | -------- |
| **GitHub Issues Templates** | Standardized bug reports | All team members                 | HIGH     |
| **Pull Request Reviewers**  | Code review assignment   | Senior developers (sulu, chekov) | HIGH     |
| **Wiki/Notion Integration** | Cross-referencing docs   | picard (orchestrator)            | MEDIUM   |

---

## 4. Version Control & History Tools

| Tool                           | Use Case                         | Command                                | Priority |
| ------------------------------ | -------------------------------- | -------------------------------------- | -------- |
| **git-blame-ignore-revs**      | Cleaner blame output             | `npm install -g git-blame-ignore-revs` | LOW      |
| **conventional-changelog-cli** | Generate changelogs from commits | `npx conventional-changelog`           | MEDIUM   |

```bash
# Example: Generate team documentation changelog
git log --oneline --since="2026-04-01" knowledge_base/documents/ > docs-changelog.txt
cat docs-changelog.txt
```

---

## 5. Search & Discovery Tools

| Tool          | Use Case                     | Integration                   | Priority |
| ------------- | ---------------------------- | ----------------------------- | -------- |
| **DocSearch** | Full-text search across docs | GitHub Action, custom indexer | HIGH     |
| **mdsearch**  | Markdown file search         | CLI tool                      | MEDIUM   |

```bash
# Example: Quick knowledge base search
mdsearch "incident" knowledge_base/documents/*.md
```

---

## 6. Quality Assurance Tools

| Tool                 | Use Case              | Team Member      | Priority |
| -------------------- | --------------------- | ---------------- | -------- |
| **markdown-toc-cli** | Generate TOC for docs | All team members | LOW      |
| **shellcheck**       | Verify CLI scripts    | DevOps (geordi)  | MEDIUM   |

---

## 7. Verification & Testing Tools

```bash
# Knowledge base completeness checker
cat > check-kb-completeness.sh << 'EOF'
#!/bin/bash
echo "=== Knowledge Base Completeness Check ==="
TOTAL_DOCS=$(find knowledge_base/documents -name "*.md" | wc -l)
INDEXED=$(grep -c "\.md" knowledge_base/documents/index.md || echo 0)
echo "Total documents: $TOTAL Docs"
echo "Referenced in index: $INDEXED docs"
if [ "$TOTAL_DOCS" -eq "$INDEXED" ]; then
    echo "Status: COMPLETE ✓"
else
    echo "Status: INCOMPLETE — $(($TOTAL_DOCS - $INDEXED)) docs missing from index"
fi
EOF

chmod +x check-kb-completeness.sh
./check-kb-completeness.sh
```

---

## Version History

```markdown
---
Version History:
    - 2026-04-05: picard — Initial team tools and utilities recommendations document
---
```

---

_Created: 2026-04-05 | Owner: picard (orchestrator) | Review cadence: Quarterly_
