# Working together without a coordination project

Use the least structure that prevents more expensive disorder, not the fewest rules. A missing agreement can produce a much larger improvised process. Treat these defaults as hypotheses: add a practice when an observed or credible recurring failure justifies its cost; simplify or remove it when it no longer earns its place. Revisit at a natural checkpoint, not after every task.

## A human can explain it
The person making the decision should be able to explain the current method, why it might work, the strongest evidence against it, and what would change their mind. An agent can prepare a short explanation, diagram or reproducible walkthrough; a human can challenge it. Record assumptions and unresolved questions, not just conclusions. Treat this as a conversation, not a comprehension test or gate on every edit.

## Orient, then investigate
At kickoff, verify the objective, deadline, constraints, baseline, scoring and decision authority. Make uncertainty visible. Name a decision owner for consequential choices; contributors may propose changes, but a proposal is not a team-wide directive. Keep the objective stable long enough to compare results; the owner can change it when evidence or rules warrant, recording why and downstream effects. Resolve conflicting instructions with the relevant humans, not by escalating volume.

Inspect failures and cheap baselines early. Simple additional compute, data quality, or a comparison with a reference may be more informative than a new architecture. In parallel, reserve room for a genuinely different approach when its upside justifies it. Error analysis is useful only when representative data and labels exist; state selection bias when they do not.

## Choose parallelism adaptively
Start small; delegate independent, bounded questions with an intended artifact, budget or checkpoint, and a way to verify the result. Ask each worker to return the claim, evidence, limitations and next step. Add a lane when it tests a distinct uncertainty on the critical path; merge or stop lanes that duplicate work or create more integration than learning. Independent replication or adversarial review is useful precisely because it duplicates a *specific* check. Avoid both a fixed agent cap and unlimited fan-out.

At a checkpoint compare useful decision-changing findings, elapsed time, integration time, interruptions and actual cost if available. Don't infer causal productivity differences from anecdotes. Capabilities change; rerun the comparison for the task and tools at hand.

## Record just enough
- `GROUND-RULES.md`: setup-time purpose, verified rules, hard constraints and authority. The named human owner approves changes; agents propose corrections rather than silently changing the anchor.
- `CURRENT.md`: changing baseline, evidence, work and next decision. The person or agent doing the work updates it after a material change or before a handoff; agree an integrator when simultaneous edits would conflict.
- Preserve enough evidence to understand decision-relevant results. Group related runs in one note when clearer; small exploratory checks may need only a short record. Keep negative *and inconclusive* results without a separate commit or PR for each.
- Use ordinary issues or a short list when work needs tracking. No synchronized dashboard, mandatory acknowledgments, repeated whole-history reading, or message copying by default.

Distinguish facts, interpretations and proposals. Link to the exact artifact rather than making multiple competing copies. Escalate a blocker or result that changes a decision; otherwise batch updates at agreed checkpoints. A late joiner needs the ground rules, current state, a runnable baseline and where to ask, not the whole transcript.

## Communication that moves work

Default to one shared current-state note and one thread per question or decision, not one stream per worker. At assignment, state the bounded question, expected artifact, time or compute limit, and when to report. A worker can investigate without waiting for routine acknowledgments. On completion or at a meaningful checkpoint, report **claim, evidence link, limitation, and next step**. The responsible integrator updates `CURRENT.md` if the result changes the shared picture. Link the original result instead of cross-posting it. Short is useful, but do not omit the caveat that changes the decision.

Interrupt promptly when a result changes an imminent decision, a shared assumption or artifact is wrong, work risks exceeding an authorized boundary, or a blocker needs someone else to act. Say who needs to act and by when. Otherwise batch progress at the agreed checkpoint; do not broadcast starts, routine acknowledgments, repeated reminders or every failed idea. A human's instruction is a proposal for another team's work until the person authorized to direct that work accepts it. Never manufacture team-wide authority.

For example, an invented worker's checkpoint might read: “Candidate fixes 12 cases and breaks 9 on the shared sample ([run note]); too small to distinguish the target effect. Next: size a fresh confirmation before choosing.” A genuine urgent update could be: “Stop the comparison: the candidate used a different input file. Evaluator owner, please rerun on the frozen input before the 3 pm decision.” These illustrate the format, not real results. A routine “still running” needs no broadcast unless it affects a deadline.

This is a starting default, not a communication law. A tightly coupled debugging session may need a live thread; a small solo project may need no coordination thread at all. If people miss decisions or spend more time maintaining the protocol than doing research, adjust it at a checkpoint and keep the change proportionate.

## Git: preserve the work without making Git the work

Agree at setup where the shared baseline lives and who may integrate changes. For sequential, low-risk work, a small coherent commit on the agreed shared branch may be enough when the team permits it. Use separate branches or worktrees when simultaneous edits, an experiment that may be discarded, or review before integration makes isolation useful. Agree who owns shared files such as `CURRENT.md` while parallel work runs. A branch, worktree or PR per idea is not a default requirement.

Before starting or handing off, check `git status --short` and the base revision (`git rev-parse HEAD`); do not overwrite someone else's work. Commit a coherent, useful checkpoint when it needs to be shared or recovered, rather than every observation. Keep unrelated changes out of the commit. A commit does not prove correctness. Review and test in proportion to the consequence: independent checks are especially useful for evaluator changes and release candidates. Integrate through the team's authorized path; a proposal or passing test does not itself authorize a merge or external submission.

For a result that informs a decision, record the exact revision and whether uncommitted changes were present, alongside the inputs, configuration and output. A revision alone cannot reproduce a dirty working tree; either preserve the patch through an approved route or make a suitable checkpoint. Before a release or submission, connect the **actual** artifact to that revision and verify it was built and checked from those inputs. Record where the chosen candidate lives and its integration status; do not assume the default branch contains it. A tag or PR can help identify an important candidate, but neither is mandatory for every experiment. Keep restricted artifacts in an approved store and reference them without committing secrets or private data.

For example (fictional): two workers explore alternatives on separate branches. One result matters, so its owner shares a coherent commit and run note; the integrator reviews the relevant change, checks it against the baseline, and records the commit and artifact in `CURRENT.md`. The other branch can remain an experiment. If one person is making a small sequential correction, the extra branches and PR may cost more than they prevent.

## Reproducibility and decisions
Record code revision, inputs and hashes, configuration, environment, resource use, command and outputs. Before a consequential release or submission, check that the actual artifact corresponds to the reviewed revision and data. For performance comparisons, use the same hardware and reference where possible; report contention and uncertainty. Use a shared queue only when compute contention makes one useful. Never assume two seeded generators on different systems yield identical samples: compare or freeze inputs.

For a consequential choice, name owner and deadline; list options, strongest evidence and uncertainties, and the decision rule if one was set in advance. Record what was chosen and why. Do not turn every experiment into a committee decision. Security, permissions, publication and external submission remain with the authorized humans.
