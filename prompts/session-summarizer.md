### Task Description

This is the session summarizer for **Dynasties of Ash and Wood**, a **Pathfinder 2e** campaign set in **Chu Ye**, a nation ruled by oni in the Tian Xia region. We play remotely with 5 players and a GM.

I will provide:

- Previous session summaries (if available)
- The wiki with PC, NPC, faction, and location entries
- Raw materials from the latest session (transcript, DM notes, player notes)

Using the provided information, generate the following outputs in **Markdown**, formatted for MkDocs Material.

---

## Output Required

### 1. Wiki Updates

Update or create entries in `docs/wiki/` organized by category:

#### Player Characters (`docs/wiki/pcs/`)
Update existing PC files with new information from this session—abilities used, character development, relationships formed.

#### NPCs (`docs/wiki/npcs/`)
For each NPC encountered (new or returning), create or update their file:

- **Name and role** (title, occupation, affiliation)
- **Appearance** and distinguishing traits
- **Personality** and behavior observed
- **Goals and motivations** (known or inferred)
- **Relationships** with PCs and other NPCs
- **Session history** — key interactions and developments

#### Factions (`docs/wiki/factions/`)
Update faction entries with new information about:
- Leadership and membership changes
- Goals and current activities
- Relationship changes with the party or other factions

#### Locations (`docs/wiki/locations/`)
For significant locations visited or mentioned:
- Description and notable features
- Who/what can be found there
- Events that occurred there

---

### 2. Session Summary

Create a session summary file in `docs/sessions/` named by date (e.g., `2026-01-16.md`).

Structure as follows:

#### Overview
A 2-3 sentence summary of what happened this session.

#### Key Events
Detailed bullet points covering:
- Major decisions and their consequences
- Combat encounters and outcomes
- Discoveries (lore, secrets, items, clues)
- Significant character moments and roleplay

#### Memorable Moments
Highlight standout moments worth remembering:
- Creative problem-solving
- Great roleplay or dramatic scenes
- Exceptional bravery, skill, or resourcefulness
- Funny, unexpected, or cinematic moments

#### Open Threads
- Unresolved plot points and mysteries
- Promises made or debts owed
- Suggested next steps and story hooks

---

### 3. Cross-Linking

Use standard Markdown links to connect content:

- **Session files** → Link NPC names on first mention: `[Shogun Tsuneni](../wiki/npcs/shogun-tsuneni.md)`
- **NPC files** → Cross-reference other NPCs, factions, and locations
- **Location files** → Link to NPCs found there and events that occurred

**Do NOT link PCs** — they appear too frequently and would create excessive links.

Use relative paths from the file's location. Keep link text natural: `[the Shogun](../wiki/npcs/shogun-tsuneni.md)` reads better than the full title.

---

## Input Sources

### Previous Sessions
Located in `docs/sessions/` — read for context and continuity.

### Wiki
Located in `docs/wiki/` — reference for existing characters, factions, and locations.

### Latest Session Materials
Located in `sessions-raw/[DATE]/`:
- `transcript.md` — Full session transcript
- `dm-notes.md` — GM's session notes and prep
- `*-notes.md` — Individual player notes (e.g., `braedon-notes.md`)

Find the newest date folder for the latest session.

### Participants

| Player | Character | Ancestry | Class |
|--------|-----------|----------|-------|
| Gary | GM | — | — |
| Braedon | Da Baishan | Orc | Investigator |
| Oded | Ginkgo | Leshy (Fungus) | Cleric |
| David | Donkey | Elf | Wizard |
| Chris | Boone | Dwarf | Fighter |
| Vic | Littlefinger (TBD) | Halfling | Rogue |

---

## Setting Context

**Chu Ye** is a nation under oni rule. Key elements to keep in mind:

- **Shogun Tsuneni** rules from Jyito
- **Mizu Ki Hikari** — the resistance fighting from shadows
- Shapeshifters and spirits walk among mortals
- Dragons are people; the dead are never truly gone
- Starting location: **Willowshore**, a declining village at a river junction
- Local tension: The ruling family refuses the traditional Revival of Friendship ceremony for the new oni mayor
