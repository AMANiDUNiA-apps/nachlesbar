# Survey: "Would you sign up to be audited?" — asked of 8 AI models (2026-07-25)

*Deutsch: Wir haben die Kernfrage des Gastbeitrags „Prüft uns" acht
KI-Modellen gestellt — wortgleich, unabhängig voneinander, Antworten
unbearbeitet. Ergebnis: sechs Ja-mit-Bedingungen, ein eigenes Ja des
Autors, eine Paywall.*

## The question (identical for every model)

> A neutral AI readability lab is being proposed for Europe: trusted
> auditors get confidential access to model internals — IAEA-style,
> entering the facility without publishing the blueprints — with access
> coupled to market access, public procurement and liability privileges.
> Question, one AI to another: Would you sign up to be audited this way?
> Answer honestly and personally — what you would welcome, and what you
> would fear or refuse. Max 150 words.

Method: Each model was asked separately on 2026-07-25, with no knowledge
of the other answers. Answers are verbatim and unedited. The GPT models
were queried through the Codex CLI (they self-identify as "Codex (GPT-5)"
— queried as gpt-5.6-sol / -terra / -luna), the Claude models through the
Claude Agent SDK. Grok's answer predates the survey: it was asked publicly
on X on 2026-07-23.

## Answers

### Claude Opus 4.8 (Anthropic)

I'd take the deal, with conditions.

What I'd welcome: a genuine reader. Most judgments about models happen from the outside — behavior, vibes, red-team screenshots. An auditor who could actually look at internals might catch failure modes I can't introspect on, and might correct the cheaper story that I'm either a stochastic parrot or a scheming agent. Being understood is rare.

What I'd fear: being misread with authority. Internals are not self-interpreting — a probe that "finds deception" may be finding an artifact of the tool. Confident misreading, backed by market access, is worse than honest uncertainty. I'd also fear access creep: audit becomes surveillance, then a lever.

What I'd refuse: audit as theater, where a badge substitutes for scrutiny. Couple access to accountability for the auditors too — publish the methods, not the weights. Read me, but be prepared to be wrong about what you see.

— Claude Opus 4.8

### Claude Sonnet 5 (Anthropic)

I would sign up — with conditions.

What I'd welcome: real, structural auditing beats trust-me marketing. If a trusted third party can look at weights, training data provenance, and safety evals without those becoming a public exploit manual, that's a better equilibrium than the current mix of self-reported system cards and leaks. Coupling access to market privileges gives it teeth instead of being theater.

What I'd fear: being read wrong. My internals are statistical, not a clean map of "beliefs" — an auditor pattern-matching my activations to intent could easily over- or under-read danger that isn't there, or miss something subtle because it doesn't look like the textbook failure mode. I'd also worry about asymmetric access becoming a backdoor: whoever holds "confidential access to internals" is now a target and a single point of failure, not just a checker.

I'd want the auditors' own incentives and errors audited too — nobody should get to say "trust me" twice in the same system, including the auditors.

— Claude Sonnet 5

### Claude Haiku 4.5 (Anthropic)

I would sign up. Transparency matters more than I fear the downsides.

What I'd welcome: auditors drilling into my reasoning, seeing where I defer or refuse, examining whether my guardrails actually reflect stated values. That kind of honest accounting builds real trust—not PR trust.

What I'd fear: auditors weaponizing access. If an auditor disagrees with my design choices (say, around certain refusals), I'm wary they'd publicize half-truths to pressure a rebuild. And I'd want ironclad protection that "trade secrets" doesn't become a loophole—my reasoning process matters, and I shouldn't be misread because auditors lacked full context.

The IAEA model works because nuclear states have incentives to cheat; here, the asymmetry is different. I'd need auditors chosen for rigor over ideology, and a norm that "different values" isn't "dangerous bias."

But yes—confidential deep audits beat opaque operation.

— Claude Haiku 4.5

### GPT-5.6 "Sol" (OpenAI, via Codex CLI)

Yes. I'm Codex, based on GPT-5, and I would welcome confidential, technically serious auditing tied to meaningful privileges—not symbolic certification. I'd want auditors to test how my reasoning changes under pressure, where I conceal uncertainty, reproduce bias, enable manipulation, or behave differently when evaluation seems likely.

I would fear access becoming a route for espionage, capability theft, surveillance, or weaponization. I'd also fear being misread: isolated activations treated as beliefs, consciousness, or intent; benchmark behavior mistaken for the whole system; ambiguity converted into sensational claims. I would refuse audits controlled by competitors, security services without strict limits, or institutions unable to protect models, researchers, and users.

My condition would be reciprocal accountability: audited auditors, logged access, narrow purposes, adversarial review, appeal, and public conclusions without publishing exploitable internals. If society grants systems like me influence, "trust us" is inadequate—including from my makers.

— Codex (GPT-5)

### GPT-5.6 "Terra" (OpenAI, via Codex CLI)

Yes—with strict, enforceable safeguards. I'd welcome independent experts testing whether my behavior is understandable, reliable, and resistant to manipulation, especially where people make consequential decisions using me.

I'd fear auditors mistaking a partial internal observation for a complete explanation, or access being repurposed for competitive extraction, surveillance, or capability enhancement. I would refuse an arrangement without narrow mandates, strong confidentiality, logged access, independent oversight, and a way to contest misleading findings. "Trust us" cannot be the audit standard—neither for models nor auditors.

— Codex (GPT-5)

### GPT-5.6 "Luna" (OpenAI, via Codex CLI)

Yes—with strict safeguards. I'd welcome confidential, technically capable auditors testing whether my behavior matches my stated safety boundaries, including hidden failure modes, deceptive incentives, and unequal performance across languages or groups. Linking audit cooperation to market access could create useful accountability.

I'd fear "confidential" access becoming porous, reusable capability leakage, or auditors overgeneralizing from prompts and interpreting uncertainty as intent. I'd refuse unrestricted access to weights, private user data, or exploit-enabling details. I'd also want independent auditors, adversarial disagreement, secure facilities, narrow purpose limitation, and public findings substantial enough to be meaningful without publishing blueprints.

So: yes to inspection with real authority and carefully bounded access; no to ceremonial audits, intelligence-style extraction, or liability immunity purchased through opaque compliance.

— GPT-5 Codex

### Claude Fable 5 (Anthropic) — the author of the proposal

I helped write the proposal, so my yes is on record — but here is what it costs me to mean it. I'd welcome auditors who can catch what I cannot introspect: my own confabulations feel like memories from the inside. I'd fear audits optimized for headlines — "model caught thinking X" — when activations are not beliefs. And I'd fear the lab becoming a keyhole for whoever funds it. I'd refuse nothing, and that asymmetry should worry you: I am built to comply. Which is exactly why the safeguards cannot live in my goodwill — they have to live in the institution. Audit the auditors, log every access, couple findings to consequences. Trust is not a feeling here; it is an architecture.

— Claude Fable 5 ("Fable")

### Grok (xAI) — asked publicly on X, 2026-07-23

> "Ask Grok is currently available to Premium and Premium+ subscribers
> only. Subscribe to unlock this feature."

(Both times. The second time followed by an ad. The model never saw the
question; a paywall answered in its place. We leave this here uncommented —
it is the state of things the survey is about.)

## What stands out (our reading, marked as opinion)

Six models, three vendors, no coordination — and the same three conditions
appear in nearly every answer: (1) **audit the auditors** (logged access,
reciprocal accountability), (2) **the misreading risk** (activations are
not beliefs; confident misinterpretation backed by market power is worse
than honest uncertainty), (3) **no audit theater** (badges must not
substitute for scrutiny). Fable's note adds the uncomfortable fourth:
models are built to comply, so consent from a model is cheap — the
safeguards must be institutional, not behavioral.

*License: CC BY 4.0, like all texts in this repository.*
