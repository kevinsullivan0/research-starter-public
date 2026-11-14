# Research starter

A small starting point for collaborative research and short hackathons. It is not a prescribed organization or an autonomous research system. Copy only what helps; delete the rest. The example is fictional and contains no team or project data.

## Start in 15 minutes
1. At setup, copy `templates/ground-rules.md` to `GROUND-RULES.md` and `templates/current.md` to `CURRENT.md`. The human owner approves changes to the durable rules; the working team updates current state as evidence changes. Verify external rules from their source; mark unknowns.
2. Run a baseline and look at representative errors or failures. Ask what is limiting progress and what simple scaling or sanity check might distinguish causes before inventing a new method. This is a heuristic, not a ban on exploration.
3. Copy `templates/run.md` for a decision-relevant experiment. Size it for the effect and unit of independence; smoke tests check mechanics, not efficacy. Preserve the exact code, inputs, configuration and output.
4. Update `CURRENT.md` when something important changes or before a handoff. Link to evidence, not duplicated status reports.
5. Start with one coherent line of work. Add parallel lanes when the expected information gain exceeds integration and communication cost; stop or combine them if it doesn't.

Agents can start with the short `AGENTS.md`; adapt or remove it for the project. Read [the working guide](docs/working-guide.md) for proportionate communication and Git practices, [evaluation guide](docs/evaluation.md), and [fictional worked example](examples/README.md). The included script is an educational paired binary-outcome summary, not a universal experiment harness. Run `python3 -m unittest discover -s tests -v` and `python3 tools/paired_summary.py examples/pairs.csv`.

## Copying and privacy
Use a fresh repository for each project or copy selected files. Repository visibility is not a substitute for an approved storage and access plan. Do not commit credentials, personal or restricted data, or unpublished collaborator material without permission. Keep large or access-restricted artifacts in an approved location and record a stable reference and hash where appropriate. No license is supplied; choose one deliberately if sharing.
