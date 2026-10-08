# Documentation

Keep the README as the entry point.
Move detail here only when it improves understanding, execution or review.

## Create These Areas Only When Needed

- research/ — questions, sources, methods, findings and uncertainty.
- architecture/ — components, boundaries, interfaces or operating models.
- specifications/ — approved scope, requirements and acceptance criteria.
- decisions/ — consequential choices, alternatives and trade-offs.

Add links to actual documents as they are created.
Do not create empty directories or placeholder evidence.

## Reusable Patterns

The files in templates/ are blank authoring patterns, not project results.
Copy one only when a real question, specification or decision requires it.

Suggested destinations:
- research/[topic].md
- specifications/[milestone].md
- decisions/ADR-0001-[decision].md

Use sequential ADR numbers for architectural decisions.
For business, research or governance choices, "DEC-0001" is also appropriate.

Delete unused template files after initialization if they add no value.
Small projects may keep all useful documentation in the README.

## Status Model

- Historical — presented mainly as a record of an earlier stage.
- Research — investigating a question, without promising a product.
- Concept — a defined proposal without its principal functioning implementation.
- Prototype — a limited implementation or trial for testing an idea.
- Active — current work with a defined objective.
- Production — real operational use within a declared, evidenced scope.
- Archived — retained without intended maintenance.

Status is not a mandatory progression.
Use "Status: Active · Maturity: Prototype" when useful.
A research-only project need not become Production.
Historical does not mean technically archived.
Changing a label does not authorize changing repository settings.

## Evidence Boundaries

EXISTS NOW: available artifacts with a stated verification status.
EXPERIMENTAL: available work with unresolved validity or reliability.
PLANNED: work not yet implemented or completed.
HISTORICAL: earlier work whose current validity is not assumed.

Separate observations, interpretations and unknowns.
An absent result is not proof of failure; an untested result is not proof of success.

## Working Discipline

Problem → Evidence → Architecture → Specification → Decision
→ AI-assisted execution → Verification → Outcome

Use the parts that materially help the project.
Iterate when evidence requires it; keep important changes explicit.

Stop when further work is unlikely to materially improve the decision or outcome.
