# Pylon — Org Chart

> Snapshot as of 2026-04-25. 71 employees total; 25 named in `employees.json` covering leadership, key managers, and ICs that future Pylon artifacts (tickets, PRs, support tickets, blog posts) will reference. The remaining 46 are unnamed seats; future POCs may flesh them out as needed.

```
                              Marcus Chen — CEO
                                    │
        ┌───────────────┬───────────┼───────────┬─────────────┬─────────────┬─────────────┐
        │               │           │           │             │             │             │
   Priya            Olivia       Dan Park    Sasha        Amir          Naomi
   Subramanian      Reyes        — CRO       Volkov       Hosseini      Brooks
   — CTO            — CPO        (Revenue)   — CMO        — VP Fin.     — VP People
   (Engineering)    (Product)                (Marketing)
        │               │           │           │
        │               │           │           │
   ┌────┴─────┐    ┌────┴─────┐ ┌───┴────┐ ┌────┴────┐
   Jordan     Wei  Anika      Kai Renata  Dave  Mei
   Mwangi     Chen Bhattach.  Tanaka     Cohen  Lin Park
   VP Eng,    Eng Dir,        Dir of     VP CS  VP Sales  Dir Mktg
   Platform   Beacon          Design
                              ──┬──
                                │
                              Felix Chen
                              Sr Designer

                                                         (under Renata)
                                                         ──┬──
                                                           │
                                                    ┌──────┴──────┐
                                                  Bridget         Tom
                                                  O'Sullivan      Whitfield
                                                  Dir Support     Sr CSM
                                                       │
                                                  Fatima
                                                  Al-Rashid
                                                  Sr Support Eng (T2)
```

```
ICs grouped by department (selected):

  Engineering (25 total; 6 named here):
    Tomás Herrera — Eng Dir, Product Surfaces (under Priya)
    Hugo Lefèvre — Sr Eng, Beacon (under Wei)
    Ravi Mehta — Staff Eng, Infrastructure (under Jordan)

  Product + Design (10 total; 4 named):
    Camille Dubois — Sr PM, Tower (under Anika)
    Felix Chen — Sr Designer (under Kai)

  Revenue (10 total; 3 named):
    Jake Patel — Sr SE (under Dave)

  Marketing (5 total; 4 named):
    Lila Reeves — Sr Content Marketer (under Mei)
    Esther Nakamura — DevRel (under Mei)

  Customer Success (10 total; 4 named — see Renata's tree above)
```

## Department headcounts

| Department | Headcount | Lead |
|---|---|---|
| Engineering | 25 | Priya Subramanian (CTO) |
| Product + Design | 10 | Olivia Reyes (CPO) |
| Customer Success | 10 | Renata Souza (VP CS) |
| Revenue (Sales + SE) | 10 | Daniel Park (CRO) |
| Marketing | 5 | Sasha Volkov (CMO) |
| Finance & Ops | 5 | Amir Hosseini (VP Finance) |
| People & Recruiting | 3 | Naomi Brooks (VP People) |
| Executive | 3 | (CEO + EA + Chief of Staff — last two unnamed) |
| **Total** | **71** | |

## Reporting peculiarities worth noting

- **Tomás Herrera** (Eng Director, Product Surfaces) reports to **Priya** directly, not to Jordan. This is intentional — Priya wanted dual-track engineering leadership: Jordan owns Platform (Beacon, Switchyard, infra), Tomás owns Product (frontend, billing, onboarding). Wei is a third Eng Director under Priya specifically for Beacon's algorithmic core.
- **Renata** (VP CS) reports to **Dan** (CRO), not to Marcus. This is a deliberate choice from Series A onward — Pylon treats Customer Success as a revenue function, not a "post-sale" function.
- **Naomi** (VP People) reports directly to **Marcus** despite the small org size, because pre-Series-C HR matters compound and Marcus wants the direct line.
- The Chief of Staff and CEO's EA are not named in this snapshot (placeholder seats). Future POCs may fill them in.

## What's not represented yet

- The full 46 unnamed engineers / ICs across Engineering and CS — these will be added as POCs need specific authors for tickets, PRs, support conversations, etc. When a POC needs a specific person, add them to `employees.json` with the right department and reports-to, and reference them consistently from there forward.
- Contractors who aren't headcount: writers, occasional designers, third-party legal. Pylon uses a notional 5-10 contractors at any given time; they're treated as off-org for this directory.
- Board members. The board is Marcus, Priya, Mike Volpi (Index Ventures), Aydin Senkut (Felicis), and one independent director (Susan Holcomb, ex-Stripe). They're not employees but appear in board materials.
