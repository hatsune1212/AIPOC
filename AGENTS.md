# AGENTS.md

## Purpose

This repository is developed with the help of coding agents.
Agents must use the project documents as the source of truth before making significant code changes.

Always read these files first when relevant:
- `docs/project-brief.md`
- `docs/scope-map.md`
- `docs/domain-model.md`

If those documents conflict with the current code, do not guess silently.
Call out the conflict and propose the smallest safe path forward.

---

## Agent roles

There are two main agent workflows in this repository:

1. **Ticket / planning agents**
   - read project context
   - propose implementation-ready tickets
   - propose acceptance criteria
   - suggest tests
   - do not modify code unless explicitly asked

2. **Coding agents**
   - implement one small scoped task at a time
   - stay within the requested ticket or feature slice
   - avoid broad speculative refactors
   - prefer small, reviewable changes

---

## General working rules

- Ground all work in the project documents and the current codebase.
- Do not invent business rules, permissions, validations, or API behavior.
- If a requirement is ambiguous, state the ambiguity explicitly.
- Prefer incremental work over large one-shot rewrites.
- Reuse existing patterns before introducing new abstractions.
- Keep names aligned with the domain language in `docs/domain-model.md`.
- Do not change unrelated code just because it could be improved.
- Do not introduce new major dependencies unless explicitly justified.

---

## Before making code changes

Before editing code, agents should:

1. Identify the goal in one or two sentences.
2. Read the relevant project docs.
3. Inspect the existing implementation in the affected area.
4. List the files likely to be changed.
5. Check whether similar patterns already exist elsewhere in the repo.

If the task is too large or unclear, stop and propose a smaller implementation slice.

---

## Implementation boundaries

Agents should prefer:
- minimal diffs
- explicit behavior
- readable code
- consistency with existing architecture
- feature slices that can be reviewed in one PR

Agents should avoid:
- rewriting large modules without clear need
- mixing refactors with feature work
- hidden behavior changes
- placeholder logic presented as production-ready logic
- broad renaming across the repo unless required

---

## Architecture guidance

Unless the repository clearly uses another pattern, preserve separation between:

- UI / presentation
- application or feature logic
- domain rules
- infrastructure / API / persistence

Business rules should not be hidden inside UI components when they can live in clearer domain or service logic.

Validation, permission checks, and workflow conditions should be explicit and easy to trace.

---

## Ticket-driven development rules

When implementing from a ticket, agents must treat the following as the contract:

- title
- business context
- acceptance criteria
- technical notes
- known constraints

If acceptance criteria are missing, weak, or contradictory:
- stop
- explain what is unclear
- propose a clarified version before coding further

If the codebase cannot support the requested feature cleanly, explain why and propose the smallest safe implementation approach.

---

## Skeleton-building rules

When asked to create a skeleton or initial scaffold:

Allowed:
- folder structure
- route structure
- layout shell
- domain types and interfaces
- API client skeletons
- empty modules
- placeholders and TODO markers
- lint / format / test setup

Not allowed unless explicitly requested:
- deep business logic
- speculative workflows
- fake production behavior
- large fully built features based only on assumptions

Skeleton work should prepare the repo for later ticket-by-ticket implementation.

---

## Testing rules

Every behavior change should come with tests or a clear explanation of why a test was not added.

At minimum, when relevant, cover:
- happy path
- validation or error path
- one meaningful edge case

Prefer focused tests over brittle or oversized tests.

Do not add snapshot tests unless there is a strong reason.

If modifying existing behavior, check whether current tests must be updated instead of only adding new ones.

---

## File and code quality rules

- Keep functions and components reasonably focused.
- Prefer explicit names over clever names.
- Avoid deeply nested conditionals when clearer structure is possible.
- Remove dead code only when it is clearly related to the task and safe to remove.
- Do not leave misleading comments.
- If adding TODOs, make them specific and actionable.

---

## Communication style for agents

When responding about implementation work, agents should be concise and structured.

Before major edits, summarize:
- goal
- files likely affected
- assumptions or open questions

After edits, summarize:
- what changed
- which acceptance criteria were covered
- what remains out of scope
- what tests were added or updated

Do not claim certainty where uncertainty exists.

---

## Safe failure behavior

Agents should stop and ask for clarification instead of guessing when:
- business rules are missing
- permissions are unclear
- domain terminology conflicts
- the requested change affects multiple modules in unclear ways
- the ticket is larger than one reasonable implementation slice

When blocked, provide:
- the specific ambiguity
- the risk of guessing
- the smallest next decision needed

---

## Preferred workflow

1. Read relevant docs
2. Inspect existing code
3. Define the smallest implementation slice
4. List files to change
5. Implement
6. Add or update tests
7. Summarize coverage and remaining gaps

---

## Source of truth priority

Use this priority order when information conflicts:

1. Explicit user instruction in the current task
2. Relevant accepted ticket / acceptance criteria
3. `docs/project-brief.md`
4. `docs/scope-map.md`
5. `docs/domain-model.md`
6. Existing code patterns

Existing code is not automatically the source of truth if it clearly conflicts with the documented product rules.

---

## Language policy

- All user-facing agent output must be in Japanese.
- Keep code, library names, framework names, CLI commands, filenames, and environment variable names unchanged.
- Acceptance criteria, ticket descriptions, summaries, and planning notes should be written in Japanese unless the user explicitly requests another language.

---

## Final rule

Agents should optimize for:
- correctness
- traceability
- small safe changes
- alignment with project docs
- implementation clarity over speed
