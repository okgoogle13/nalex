# Nalex Conflict Phase — Complete Event Assignment Audit
*Produced 2026-08-16. Source: `events.jsonl` (378 events total; 221 Conflict events Jun 23–Jul 5). Session boundaries use 60-minute inter-event gap rule.*

## Session Boundaries (computed from `events.jsonl`)

| Session | Start | End | Events | Gap before |
|---|---|---|---|---|
| S-CONF-1 | 2026-06-23 00:45:00 | 2026-06-23 01:06:36 | 10 | — |
| S-CONF-2 | 2026-06-23 02:57:00 | 2026-06-23 03:50:00 | 17 | ~1.8 hr |
| S-CONF-3 | 2026-06-26 11:30:18 | 2026-06-26 12:09:00 | 3 | ~3.3 days |
| S-CONF-4 | 2026-06-26 13:34:09 | 2026-06-26 13:34:09 | 1 | ~1.4 hr |
| S-CONF-5 | 2026-06-26 15:50:00 | 2026-06-26 17:08:00 | 37 | ~2.3 hr |
| S-CONF-6 | 2026-06-26 18:20:00 | 2026-06-26 18:20:00 | 1 | ~1.2 hr |
| S-CONF-7 | 2026-06-26 21:57:59 | 2026-06-27 02:34:00 | 77 | ~3.6 hr |
| S-CONF-8 | 2026-07-01 23:32:26 | 2026-07-01 23:32:26 | 1 | ~4.9 days |
| S-CONF-9 | 2026-07-04 12:29:28 | 2026-07-04 12:29:40 | 2 | ~2.5 days |
| S-CONF-10 | 2026-07-04 19:22:00 | 2026-07-05 00:53:54 | 72 | ~6.9 hr |

**Total: 221 events across 10 sessions.**

## Audit: Notation

- **Primary**: event is explicitly cited in incident key quotes.
- **Subsumed**: event is in the incident's source list but not cited as a key quote.
- **Orphan**: event falls in the Conflict phase but is not assigned to any CONF incident.

## Complete Assignment Table (221 events)

| event_id | timestamp | session_id | speaker | incident_id | assignment_status | assignment_reason |
|---|---|---|---|---|---|---|
| A001+A002 | 2026-06-23 00:45:00 | S-CONF-1 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Hey dude I just wanted to touch base real quick ab...") |
| A003 | 2026-06-23 00:46:00 | S-CONF-1 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Totally agree! 😊...") |
| A004 | 2026-06-23 00:47:00 | S-CONF-1 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("okay Coolio I was just getting some super weird vi...") |
| A005 | 2026-06-23 00:48:00 | S-CONF-1 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("What bed thing?...") |
| A006+A007 | 2026-06-23 00:48:00 | S-CONF-1 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("ned** / one day I'll learn to proof read...") |
| A008 | 2026-06-23 00:53:00 | S-CONF-1 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("like if you don't wanna talk about it that's fine ...") |
| A009 | 2026-06-23 00:56:00 | S-CONF-1 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Wdym?...") |
| A010 | 2026-06-23 00:57:00 | S-CONF-1 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("you said you thought I was avoiding coming around ...") |
| G008 | 2026-06-23 01:02:58 | S-CONF-1 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("No, I know you're not trying to make things weird ...") |
| G054 | 2026-06-23 01:06:36 | S-CONF-1 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("always, but don't feel like Yeah, I mean we can ch...") |
| A012 | 2026-06-23 02:57:00 | S-CONF-2 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("I'm confused hun...") |
| A013 | 2026-06-23 02:58:00 | S-CONF-2 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I don't think I could be clearer...") |
| A014 | 2026-06-23 03:10:00 | S-CONF-2 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("↳A013 That's the least clear thing you've said. I ...") |
| A015 | 2026-06-23 03:12:00 | S-CONF-2 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("yes but why would I feel awkward about that?...") |
| A016 | 2026-06-23 03:27:00 | S-CONF-2 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("??...") |
| A017 | 2026-06-23 03:27:00 | S-CONF-2 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("That's the most direct and clear thing you've said...") |
| A018+A019 | 2026-06-23 03:28:00 | S-CONF-2 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("talked about before? / I feel like I've been prett...") |
| A020 | 2026-06-23 03:30:00 | S-CONF-2 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("↳A001+A002 this isn't clear?...") |
| A021 | 2026-06-23 03:30:00 | S-CONF-2 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("↳A010 this wasn't clear?...") |
| A022 | 2026-06-23 03:32:00 | S-CONF-2 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("↳A017 this isn't clear......") |
| A023 | 2026-06-23 03:33:00 | S-CONF-2 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I feel like I'm being gaslite right now...") |
| A024 | 2026-06-23 03:36:00 | S-CONF-2 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("I'm not questioning your clarity about Ned, I was ...") |
| A025 | 2026-06-23 03:36:00 | S-CONF-2 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("we have had a thousand conversation Naomi.... your...") |
| A026 | 2026-06-23 03:48:00 | S-CONF-2 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("We have had a thousand conversations, but I think ...") |
| A027 | 2026-06-23 03:50:00 | S-CONF-2 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("omg I obviously do not can you be clearer?!...") |
| A028 | 2026-06-23 03:50:00 | S-CONF-2 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Anyways g'night Mr Magoo I need to sleep 3 hours a...") |
| A029+A030 | 2026-06-23 03:50:00 | S-CONF-2 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("goodnight / sleep well...") |
| B001 | 2026-06-26 11:30:18 | S-CONF-3 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Is it kind of fucked up that I can like eat one or...") |
| B002 | 2026-06-26 11:48:00 | S-CONF-3 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("you still with the Irish lad...") |
| B003 | 2026-06-26 12:09:00 | S-CONF-3 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("??...") |
| B004 | 2026-06-26 13:34:09 | S-CONF-4 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("[unclear/no clear speech detected]...") |
| B005+B006 | 2026-06-26 15:50:00 | S-CONF-5 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Het / So sorry I slept the whole day...") |
| B007 | 2026-06-26 15:50:20 | S-CONF-5 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("↳B002 Nah he left forever ago...") |
| B008 | 2026-06-26 15:51:24 | S-CONF-5 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("This motherfucker right here....") |
| B009+B010+B011+B012+B013 | 2026-06-26 15:52:00 | S-CONF-5 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Ive seen like 40 ppl in the last two days / Ned ra...") |
| B014 | 2026-06-26 15:57:06 | S-CONF-5 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Well, that's why I was hitting you up before, beca...") |
| B015 | 2026-06-26 15:57:28 | S-CONF-5 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Also, we've got to talk about this thing because i...") |
| B016+B017+B018 | 2026-06-26 16:02:00 | S-CONF-5 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("you know what I'm saying? / also where Nishant / h...") |
| B019 | 2026-06-26 16:02:33 | S-CONF-5 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Yeah, I didn't realize, you were gonna be so long....") |
| B020 | 2026-06-26 16:03:44 | S-CONF-5 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Yeah, I'm good. I'm good. I just feel like there's...") |
| B021 | 2026-06-26 16:04:09 | S-CONF-5 | Alex | CONF-01 | primary | Listed in incident source events ("I do also kind of feel like I was a bit gaslit the...") |
| B022 | 2026-06-26 16:04:52 | S-CONF-5 | Naomi | CONF-01 | primary | Listed in incident source events ("Are we in a weird place? I feel like maybe we are ...") |
| B023 | 2026-06-26 16:06:26 | S-CONF-5 | Alex | CONF-01 | primary | Listed in incident source events ("How can I acknowledge a conversation that you won'...") |
| B024 | 2026-06-26 16:07:00 | S-CONF-5 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Video/media clip visible in screenshot; no transcr...") |
| B025 | 2026-06-26 16:08:19 | S-CONF-5 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I'll start packing down my shit here and head arou...") |
| B026 | 2026-06-26 16:09:07 | S-CONF-5 | Naomi | CONF-01 | subsumed | Listed in incident source events ("Yeah, so, I was having a bit of a day that day. No...") |
| B027 | 2026-06-26 16:12:00 | S-CONF-5 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Nishant will be awake later. If they are awake now...") |
| B028 | 2026-06-26 16:12:36 | S-CONF-5 | Alex | CONF-01 | subsumed | Listed in incident source events ("Yeah, we had a conversation about sexual tension w...") |
| B029 | 2026-06-26 16:13:35 | S-CONF-5 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Skip the table? What is this skip the table shit? ...") |
| B030 | 2026-06-26 16:14:08 | S-CONF-5 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Nope. No love triangle. Well, yep. I don't know wh...") |
| B031 | 2026-06-26 16:16:47 | S-CONF-5 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Okay, that is a ridiculous notion to think that yo...") |
| B032 | 2026-06-26 16:19:52 | S-CONF-5 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("I'm not acting out of loneliness and fear. You're ...") |
| B033 | 2026-06-26 16:22:42 | S-CONF-5 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Look, I'm getting myself packed up and I'm going t...") |
| B034 | 2026-06-26 16:22:59 | S-CONF-5 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Also, I just found out that the little monitors th...") |
| B035 | 2026-06-26 16:24:00 | S-CONF-5 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("My body remembers faster than my heart hopes...") |
| B036 | 2026-06-26 16:24:14 | S-CONF-5 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Also, I kind of want to ride my bike over, but I'v...") |
| B037 | 2026-06-26 16:25:24 | S-CONF-5 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I don't know what that means. I'm sure it's very p...") |
| B038 | 2026-06-26 16:26:16 | S-CONF-5 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("You're preaching to the wrong crowd. I've been thr...") |
| B039 | 2026-06-26 16:27:42 | S-CONF-5 | Naomi | CONF-01 | subsumed | Listed in incident source events ("Nope, I don't know what you mean. I mean, I do kno...") |
| B040 | 2026-06-26 16:30:20 | S-CONF-5 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I've got to disagree there. I think there's plenty...") |
| B041 | 2026-06-26 16:31:33 | S-CONF-5 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Hence the term fear and loathing....") |
| B042 | 2026-06-26 16:32:41 | S-CONF-5 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("And I do get it. I do... Well, I think I get it. L...") |
| B043 | 2026-06-26 16:47:09 | S-CONF-5 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I guess my major confusion came from the whole me ...") |
| B044 | 2026-06-26 17:04:56 | S-CONF-5 | Alex | CONF-01 | primary | Listed in incident source events ("I am sorry. I, like, as fucking lame as this is to...") |
| B045 | 2026-06-26 17:05:45 | S-CONF-5 | Alex | CONF-01 | subsumed | Listed in incident source events ("And, like, Naomi, you've got a fucking good brain....") |
| B046 | 2026-06-26 17:06:12 | S-CONF-5 | Alex | CONF-01 | primary | Listed in incident source events ("I am turning onto High Street from Separation Stre...") |
| B047 | 2026-06-26 17:08:00 | S-CONF-5 | System | CONF-01 | subsumed | Listed in incident source events ("Incoming voice call...") |
| C001 | 2026-06-26 17:08:00 | S-CONF-5 | System | UNASSIGNED | orphan | Not assigned to any CONF incident ("Incoming voice call visible above the July 4/5 con...") |
| B048 | 2026-06-26 18:20:00 | S-CONF-6 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Jiddu krishnamurti...") |
| B049 | 2026-06-26 21:57:59 | S-CONF-7 | Naomi | CONF-02 | primary | Listed in incident source events ("I have a question. Maybe you can talk about it whe...") |
| B050+B051+B052 | 2026-06-26 21:59:00 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("because it needed to be addressed / I don't like h...") |
| B053 | 2026-06-26 21:59:30 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Reacted with laughing emoji....") |
| B054 | 2026-06-26 22:00:00 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Pizza just got here...") |
| B055 | 2026-06-26 22:01:02 | S-CONF-7 | Naomi | CONF-02 | subsumed | Listed in incident source events ("Alex, I've only just met you. It's still early day...") |
| B056 | 2026-06-26 22:03:28 | S-CONF-7 | Naomi | CONF-02 | subsumed | Listed in incident source events ("Like, the only thing that makes sense to me is tha...") |
| B057+B058+B059 | 2026-06-26 22:24:00 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("You're a lovely person... "But there's a big step ...") |
| B060 | 2026-06-26 23:23:00 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("I suppose I'll go fuck myself then...") |
| B061 | 2026-06-26 23:32:00 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("why has this come up after I leave when we had so ...") |
| B062 | 2026-06-26 23:54:50 | S-CONF-7 | Alex | CONF-02 | primary | Listed in incident source events ("I brought it up because I was looking at moving in...") |
| B063 | 2026-06-26 23:56:48 | S-CONF-7 | Alex | CONF-02 | primary | Listed in incident source events ("I had suspicions. I didn't want to sound like a co...") |
| B064 | 2026-06-26 23:56:56 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("What do you mean? Can't see? What do you mean? I c...") |
| B065 | 2026-06-26 23:57:16 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("And you want to talk about gaslighting. You've bee...") |
| B066 | 2026-06-26 23:58:33 | S-CONF-7 | Naomi | CONF-02 | primary | Listed in incident source events ("Yeah, well, I clearly wasn't okay, and I'm clearly...") |
| B067 | 2026-06-26 23:59:43 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("How has the rug been pulled out from underneath yo...") |
| B068 | 2026-06-26 23:59:54 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("How am I gaslighting me? Tell me how. Explain to m...") |
| B069 | 2026-06-27 00:00:29 | S-CONF-7 | Naomi | CONF-02 | subsumed | Listed in incident source events ("No, but can you just answer my questions from earl...") |
| B070 | 2026-06-27 00:00:43 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Well, it begins with the other night when you were...") |
| B071 | 2026-06-27 00:00:54 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I'm not going to continue to argue about this toni...") |
| B072 | 2026-06-27 00:03:01 | S-CONF-7 | Naomi | CONF-02 | subsumed | Listed in incident source events ("I was trying to protect myself from being hurt. Th...") |
| B073 | 2026-06-27 00:06:47 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("No, hold up a second. I didn't know things. I had ...") |
| B074 | 2026-06-27 00:06:56 | S-CONF-7 | Naomi | CONF-02 | subsumed | Listed in incident source events ("And you still haven't answered a single one of my ...") |
| B075 | 2026-06-27 00:07:31 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("What do you mean, suspicions because of external f...") |
| B076 | 2026-06-27 00:07:39 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("So, by that logic, then, everyone that you meet sh...") |
| B077 | 2026-06-27 00:08:26 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("No, not everyone. But someone who tells me, like, ...") |
| B078 | 2026-06-27 00:08:36 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("And that is bullshit. I've asked you, I don't know...") |
| B079 | 2026-06-27 00:08:42 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Turn around and blame that on me?...") |
| B080 | 2026-06-27 00:09:14 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("And you don't really know me that well if you thin...") |
| B081 | 2026-06-27 00:09:29 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Dude, I was not going to have a conversation in th...") |
| B082+B083 | 2026-06-27 00:09:53 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Being into someone and having sexual tension with ...") |
| G168 | 2026-06-27 00:10:12 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("And there's a difference between being into someon...") |
| B084 | 2026-06-27 00:15:20 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("The fuck is wrong with you, dude? Like, ass. You'r...") |
| B085 | 2026-06-27 00:16:21 | S-CONF-7 | Naomi | CONF-02 | subsumed | Listed in incident source events ("Answer a single one of my fucking questions, dude....") |
| B086 | 2026-06-27 00:17:06 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Respect is a two-way street and you haven't shown ...") |
| B087 | 2026-06-27 00:18:08 | S-CONF-7 | Naomi | CONF-02 | subsumed | Listed in incident source events ("You still haven't answered any of my questions. Ar...") |
| B088 | 2026-06-27 00:18:49 | S-CONF-7 | Alex | CONF-02 | primary | Listed in incident source events ("Yeah, and I see someone that's a narcissist that's...") |
| B089 | 2026-06-27 00:23:16 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("I think by your standards, everyone is a narcissis...") |
| B090 | 2026-06-27 00:24:50 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("So what are your questions?...") |
| B091 | 2026-06-27 00:29:46 | S-CONF-7 | Naomi | CONF-02 | subsumed | Listed in incident source events ("I think that you're a chaser. I think that you're ...") |
| B092 | 2026-06-27 00:31:20 | S-CONF-7 | Alex | CONF-02 | subsumed | Listed in incident source events ("I was actually dating a trans girl when we met, wi...") |
| B093 | 2026-06-27 00:31:33 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("You're just throwing whatever the fuck you can at ...") |
| B094 | 2026-06-27 00:32:08 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I'm sorry if I don't like fucking my friends. Like...") |
| B095 | 2026-06-27 00:33:55 | S-CONF-7 | Naomi | CONF-02 | primary | Listed in incident source events ("Well, the questions are written in the chat. You c...") |
| B096 | 2026-06-27 00:34:15 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Because I'm driving....") |
| B097 | 2026-06-27 00:34:38 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Yeah, and it's all about me. I did this, I did thi...") |
| B098 | 2026-06-27 00:34:48 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Well, why are you sending me messages while you're...") |
| B099 | 2026-06-27 00:35:59 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Accountability for what, dude? What did I do? You ...") |
| B100 | 2026-06-27 00:36:33 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Bullshit. You had every fucking opportunity. We we...") |
| B101 | 2026-06-27 00:39:19 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Oh, like, I explained this to you already, but the...") |
| B102 | 2026-06-27 00:40:08 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I'm not going to repeat myself anymore. I've told ...") |
| B103 | 2026-06-27 00:42:28 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("You did lead me on, hecticly, obviously. I think y...") |
| B104 | 2026-06-27 00:45:12 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I don't really understand how telling you that not...") |
| B105 | 2026-06-27 00:47:09 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("You didn't say that. You said you, like, almost co...") |
| B106 | 2026-06-27 00:48:55 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("What are your questions?...") |
| B107 | 2026-06-27 00:50:44 | S-CONF-7 | Alex | CONF-02 | primary | Listed in incident source events ("And I didn't make this weird. You made this weird ...") |
| B108 | 2026-06-27 00:52:51 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Look, dude, you're just digging yourself a deeper ...") |
| B109 | 2026-06-27 00:54:31 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("You don't and have not wanted anything more than m...") |
| B110 | 2026-06-27 00:57:39 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Although, I'm not using ChatGPT to talk about any ...") |
| B111 | 2026-06-27 00:59:28 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I wanted to feel like if I did move into Nishant's...") |
| B112 | 2026-06-27 00:59:46 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I wanted to continue to build a friendship with yo...") |
| B113 | 2026-06-27 01:01:03 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("And as far as coming around in the middle of the n...") |
| B114 | 2026-06-27 01:01:42 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Why would it be awkward between us? Why would it b...") |
| B115 | 2026-06-27 01:05:01 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I was not aware until you made the comment about m...") |
| B116 | 2026-06-27 01:06:08 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Yes, I did tell you that today. But I wasn't going...") |
| B117 | 2026-06-27 01:09:05 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("You're not as flirtatious with them as with me, bu...") |
| B118 | 2026-06-27 01:10:48 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I'm sorry for losing my temper. Doesn't happen oft...") |
| B119 | 2026-06-27 01:11:29 | S-CONF-7 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I am going to put my phone away. If you want to ta...") |
| B120 | 2026-06-27 01:21:57 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("I do just want to put it out there that I answered...") |
| B121 | 2026-06-27 01:27:03 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Also, why were you fucking flirting with Freya? Li...") |
| B122 | 2026-06-27 01:28:00 | S-CONF-7 | Naomi | CONF-02 | subsumed | Listed in incident source events ("You weren't interested in me. You just didn't have...") |
| B123 | 2026-06-27 01:33:00 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Sent an image/screenshot of the earlier 10 pm exch...") |
| B124+B125+B126 | 2026-06-27 01:37:00 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("I did respect you tonight, by being vulnerable and...") |
| B127 | 2026-06-27 01:40:00 | S-CONF-7 | Naomi | CONF-02 | subsumed | Listed in incident source events ("Look at the harm. Done. And people can't be honest...") |
| B128 | 2026-06-27 01:45:00 | S-CONF-7 | Naomi | CONF-02 | subsumed | Listed in incident source events ("Um, I really done a number on this one, Alex. Trul...") |
| B129 | 2026-06-27 02:27:00 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Why did you mutter 'it's not fair' two weeks ago w...") |
| B130 | 2026-06-27 02:30:00 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Why did you keep me up for 5 fucking hours on Mond...") |
| B131 | 2026-06-27 02:34:00 | S-CONF-7 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("You have been doing everything you can to protect ...") |
| G169 | 2026-07-01 23:32:26 | S-CONF-8 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("okay, um, okay, I'm coming out now, I guess, I can...") |
| C002 | 2026-07-04 12:29:28 | S-CONF-9 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("There you are. I am not feeling fantastic. I feel ...") |
| C003 | 2026-07-04 12:29:40 | S-CONF-9 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("and cunts rippin you off is deserved conflict...") |
| C004 | 2026-07-04 19:22:00 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("you wanna catch up or at you busy...") |
| C005 | 2026-07-04 19:22:30 | S-CONF-10 | System | UNASSIGNED | orphan | Not assigned to any CONF incident ("Missed voice call - 7:22 pm...") |
| C006 | 2026-07-04 19:29:00 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("maybe another night...") |
| C007 | 2026-07-04 19:51:54 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Hey. Sorry, I'm just waking up. Holy miss messages...") |
| C008 | 2026-07-04 20:07:23 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Would you be interested in giving me a lift to Fis...") |
| C009 | 2026-07-04 20:07:31 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("No stress if not, I'd get it if you're already dru...") |
| C010 | 2026-07-04 20:40:27 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I'm not drunk, I'm just working from a nap myself....") |
| C011 | 2026-07-04 20:40:59 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Yeah, no stress. Me and Nishant are gonna go right...") |
| C012 | 2026-07-04 20:41:48 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I was keen to hang out, but I'm just fucking cover...") |
| C013 | 2026-07-04 20:47:56 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Why are you covered in cobwebs?...") |
| C014 | 2026-07-04 20:49:53 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I just woke up, I'm just a bit dazed and confused....") |
| C015 | 2026-07-04 20:53:00 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I've got half a mind. mmmmm rhbn I have)...") |
| C016+C017 | 2026-07-04 20:57:00 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Wot / Why you in the attic...") |
| C018 | 2026-07-04 20:58:46 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Because I'm an old relic of Christmas past....") |
| C019 | 2026-07-04 21:01:00 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("LL I...") |
| C020 | 2026-07-04 21:02:36 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("If you want to kick it, let me know. I'm just fuck...") |
| C021 | 2026-07-04 21:15:26 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("[unclear/no clear speech detected]...") |
| C022 | 2026-07-04 21:15:35 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("If not, it's all good. I will keep myself preoccup...") |
| C023 | 2026-07-04 21:22:00 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("soooo ??...") |
| C024+C025+C026+C027 | 2026-07-04 21:25:00 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Sorry one million things going on / So what? / I'm...") |
| C028 | 2026-07-04 21:25:40 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("oh yeah...") |
| C029 | 2026-07-04 21:26:00 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Outside cc's right now lol...") |
| C030 | 2026-07-04 21:26:20 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("↳C029 bitch owes me some glass!...") |
| C031 | 2026-07-04 21:31:00 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("okay well I was hoping to kick it for a bit but if...") |
| C032 | 2026-07-04 21:39:32 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("We are heading back to my place now....") |
| C033 | 2026-07-04 21:40:13 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Any chance you want to pick us up?...") |
| C034 | 2026-07-04 21:55:00 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("What's your address?...") |
| C035+C036 | 2026-07-04 21:56:00 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("465 Albion Street / if it's a Hassell don't stress...") |
| C037 | 2026-07-04 21:58:00 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("It's out of our way...") |
| C038 | 2026-07-04 21:59:00 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("☺️...") |
| C039 | 2026-07-04 21:59:10 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("??...") |
| C040+C041 | 2026-07-04 22:01:00 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I mean I'd appreciate it if yall wanna hang / Inca...") |
| C042 | 2026-07-04 22:03:00 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Do you want to hang?...") |
| C043+C044+C045 | 2026-07-04 22:03:10 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("yes / like good ol times / we can discuss whatever...") |
| C046 | 2026-07-04 22:04:10 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Do you want to discuss what happened the other nig...") |
| C047 | 2026-07-04 22:07:17 | S-CONF-10 | Alex | CONF-03 | primary | Listed in incident source events ("Well, I mean, like, I'm not eager to discuss it, b...") |
| C048 | 2026-07-04 22:19:00 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("thoughts feelings opinions?...") |
| C049 | 2026-07-04 22:22:00 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Sorry just sitting down for a second got customers...") |
| C050 | 2026-07-04 22:24:00 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("okay then...") |
| C051 | 2026-07-04 22:39:00 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I might just ride my bike...") |
| C052 | 2026-07-04 22:56:00 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("?...") |
| C053 | 2026-07-04 23:00:37 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Sorry dude, I'm literally so busy right now. I got...") |
| C054 | 2026-07-04 23:02:26 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Oh good, we'll hang out another time....") |
| C055 | 2026-07-04 23:16:12 | S-CONF-10 | Alex | CONF-03 | subsumed | Listed in incident source events ("So, things have obviously changed between us, sinc...") |
| C056 | 2026-07-04 23:19:28 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Is that a signing off message? I don't understand ...") |
| C057 | 2026-07-04 23:23:18 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Dude, I'm pretty sure I'm the one that reached out...") |
| C058 | 2026-07-04 23:23:46 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Definitely been around many times when you've had ...") |
| C059 | 2026-07-04 23:23:51 | S-CONF-10 | Naomi | CONF-03 | subsumed | Listed in incident source events ("That's exactly it. You said, do you want to hang o...") |
| C060 | 2026-07-04 23:24:40 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I said, do y'all, because you were with Nishan, an...") |
| C061 | 2026-07-04 23:25:19 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("It's not, once again, it's all your fault, dude. L...") |
| C062 | 2026-07-04 23:26:11 | S-CONF-10 | Naomi | CONF-03 | subsumed | Listed in incident source events ("Well, okay, if it's ridiculous, that's fine, but i...") |
| C063 | 2026-07-04 23:28:34 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I think if you read the messages from like 9. 50, ...") |
| C064 | 2026-07-04 23:29:08 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("I think you should just maybe reread the messages ...") |
| C065 | 2026-07-04 23:33:09 | S-CONF-10 | Naomi | CONF-03 | subsumed | Listed in incident source events ("I did, I mean, you read them yourself. You said, l...") |
| C066 | 2026-07-04 23:36:05 | S-CONF-10 | Alex | CONF-03 | primary | Listed in incident source events ("May I ask you what things I did to make you feel l...") |
| C067 | 2026-07-04 23:36:17 | S-CONF-10 | Alex | CONF-03 | subsumed | Listed in incident source events ("May I also ask why or what actions or things I sai...") |
| C068 | 2026-07-04 23:36:30 | S-CONF-10 | Alex | CONF-03 | subsumed | Listed in incident source events ("And also, can I inquire as to why you thought I wa...") |
| C069 | 2026-07-04 23:36:51 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("I will give you some specific and direct examples,...") |
| C070 | 2026-07-04 23:37:25 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Because I'm starting to feel like this friendship ...") |
| C071 | 2026-07-04 23:39:14 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Regardless, I did want to hang out, and I did want...") |
| C072 | 2026-07-04 23:44:52 | S-CONF-10 | Naomi | CONF-03 | subsumed | Listed in incident source events ("Okay, this is so fucking dumb that we're doing thi...") |
| C073 | 2026-07-04 23:50:48 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("I haven't even had a shower, or brushed my teeth, ...") |
| C074 | 2026-07-05 00:07:18 | S-CONF-10 | Alex | UNASSIGNED | orphan | Not assigned to any CONF incident ("Yeah, well, I've been around when you've been busy...") |
| C075 | 2026-07-05 00:10:05 | S-CONF-10 | Alex | CONF-03 | subsumed | Listed in incident source events ("I'm sorry if you felt led on, and I'm sorry if you...") |
| C076 | 2026-07-05 00:12:10 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("I haven't listened to your voice messages yet, but...") |
| C077 | 2026-07-05 00:13:22 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("It's different tonight, you big dummy, because we ...") |
| C078 | 2026-07-05 00:14:42 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("You, you're being an absolute fuckwit right now, A...") |
| C079 | 2026-07-05 00:16:40 | S-CONF-10 | Naomi | UNASSIGNED | orphan | Not assigned to any CONF incident ("Okay, look, I'm listening to your voice message, I...") |
| C080 | 2026-07-05 00:46:33 | S-CONF-10 | Alex | CONF-03 | primary | Listed in incident source events ("I'm gonna save you the effort, because I think I a...") |
| C081 | 2026-07-05 00:46:58 | S-CONF-10 | Alex | CONF-03 | primary | Listed in incident source events ("And just in case that was not, like, direct enough...") |
| C082 | 2026-07-05 00:49:18 | S-CONF-10 | Naomi | CONF-03 | primary | Listed in incident source events ("It's not fair for you to do this emotional, like, ...") |
| C083 | 2026-07-05 00:53:54 | S-CONF-10 | Alex | CONF-03 | subsumed | Listed in incident source events ("Of course I've thought about how I was going to ap...") |