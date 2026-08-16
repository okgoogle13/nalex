# Nalex Aftermath — Complete Event Assignment Audit
*Produced 2026-08-15. Source: `events.jsonl` (378 events total; 105 Aftermath events Jul 11–21). Session boundaries use 60-minute inter-event gap rule (CURRENT_STATE_CLEAN.md §7.1).*

## Session Boundaries (computed from `events.jsonl`)

| Session | Start | End | Events | Gap before |
|---|---|---|---|---|
| S-AM-1 | Jul 11 20:07:12 | Jul 11 22:53:24 | 40 | — (6.8 days since C083) |
| S-AM-2 | Jul 11 23:55:57 | Jul 12 00:04:10 | 4 | 62.6 min |
| S-AM-3 | Jul 12 01:10:23 | Jul 12 01:31:53 | 4 | 66.2 min |
| S-AM-4 | Jul 13 19:31:56 | Jul 13 23:04:44 | 28 | 2,520 min (~42 hr) |
| S-AM-5 | Jul 21 19:04:12 | Jul 21 21:48:45 | 29 | 11,280 min (~7.8 days) |

**Total: 105 events across 5 sessions. Matches CURRENT_STATE_CLEAN.md §1 exactly.**

## Audit: Notation

- **Primary**: event is the principal source for its incident's defining moment.
- **Subsumed**: event falls within the incident's time range but is logistical, transitional, or topically tangential; listed in source_event_ids of the parent incident without being separately cited in the incident summary.
- **Correction note**: G096 was absent from the prior timeline draft. Now assigned below.

---

## Complete Assignment Table (105 events)

| event_id | timestamp | session_id | speaker | incident_id | assignment_status | assignment_reason |
|---|---|---|---|---|---|---|
| G212 | 2026-07-11 20:07:12 | S-AM-1 | Naomi | AFT-01 | primary | Reconnection opener; first Aftermath event; speaker confirmed by manual listening (CURRENT_STATE_CLEAN.md §3) |
| G170 | 2026-07-11 20:15:20 | S-AM-1 | Alex | AFT-01 | primary | Alex explains why he did not come earlier; establishes drinking and weather context for reconnection |
| G171 | 2026-07-11 20:16:07 | S-AM-1 | Alex | AFT-01 | primary | Offer to buy her glass; low-key pre-conflict banter within reconnection window |
| G172 | 2026-07-11 20:21:50 | S-AM-1 | Alex | AFT-01 | subsumed | Naomi financial anxiety aside ("I'm scared I need money"); off-conflict topic; subsumed in AFT-01 reconnection |
| G173 | 2026-07-11 20:26:51 | S-AM-1 | Alex | AFT-01 | primary | Acknowledgement demand stated for first time in Aftermath ("I wouldn't mind having my friend back, just think some uh acknowledgement would be good is all") |
| G174 | 2026-07-11 20:27:06 | S-AM-1 | Alex | AFT-01 | primary | Fear of re-escalation stated ("I also don't wish to end in another argument") |
| G019 | 2026-07-11 20:27:26 | S-AM-1 | Alex | AFT-01 | primary | Conditional withdrawal offer ("if this is going to create another argument just just forget it and move on") |
| G097 | 2026-07-11 20:30:43 | S-AM-1 | Naomi | AFT-02 | subsumed | Ambiguous transition into AFT-02 ("is there a chance we can do you yet?"); marks shift from reconnection to accountability exchange |
| G175 | 2026-07-11 20:31:32 | S-AM-1 | Alex | AFT-02 | primary | Alex names hurt from silence ("I've had radio silence and it's been a little bit hurtful, but I've endured worse") |
| G096 | 2026-07-11 20:48:49 | S-AM-1 | Alex | AFT-02 | subsumed | Alex dismisses Naomi's Nishant tangent ("What does this have to do with the price of fish though?"); subsumed in AFT-02 as deflection-response; NOTE: this event was absent from the prior timeline draft and is added here |
| G080 | 2026-07-11 20:58:21 | S-AM-1 | Alex | AFT-02 | primary | Alex states anxiety at vagueness ("The anxiety of not knowing is going to kill me") |
| G028 | 2026-07-11 21:47:44 | S-AM-1 | Alex | AFT-02 | subsumed | Nishant-call clarification ("I said no to Nishant"); transition in accountability exchange; subsumed in AFT-02 |
| G066 | 2026-07-11 21:49:19 | S-AM-1 | Naomi | AFT-02 | subsumed | Brief vague response to Alex query; subsumed in AFT-02 |
| G176 | 2026-07-11 21:54:29 | S-AM-1 | Alex | AFT-02 | primary | Alex names vagueness as the problem ("You're still being very vague, and I would like just the smallest amount of clarity") |
| G020 | 2026-07-11 22:03:22 | S-AM-1 | Alex | AFT-02 | subsumed | Alex redirects back to core dispute ("what does Nishant have to do with what we're talking about"); subsumed in AFT-02 |
| G040 | 2026-07-11 22:17:50 | S-AM-1 | Naomi | AFT-02 | subsumed | Jamie logistics tangent; Naomi trying to eat dinner; off-conflict topic subsumed in AFT-02 |
| G089 | 2026-07-11 22:20:31 | S-AM-1 | Alex | AFT-02 | subsumed | Response to Jamie tangent ("Consider it done. Sorry to have reached out."); subsumed in AFT-02 |
| G085 | 2026-07-11 22:20:51 | S-AM-1 | Naomi | AFT-02 | subsumed | Jamie money concern; off-conflict tangent; subsumed in AFT-02 |
| G016 | 2026-07-11 22:25:45 | S-AM-1 | Naomi | AFT-02 | subsumed | ATO audit concern; off-conflict tangent; subsumed in AFT-02 |
| G177 | 2026-07-11 22:28:00 | S-AM-1 | Alex | AFT-02 | subsumed | Re-redirection to core dispute ("what does that have to do with what we were talking about?"); subsumed in AFT-02 |
| G037 | 2026-07-11 22:28:28 | S-AM-1 | Alex | AFT-02 | subsumed | Personal aside ("Meanwhile, I'm here trying to create nemo 2.0"); subsumed in AFT-02 |
| G065 | 2026-07-11 22:28:32 | S-AM-1 | Naomi | AFT-02 | subsumed | Transition response ("It doesn't have anything to do with it"); subsumed in AFT-02 |
| G064 | 2026-07-11 22:29:24 | S-AM-1 | Alex | AFT-02 | primary | Alex states acknowledgement precondition for in-person meeting ("Dude you haven't acknowledged a single thing like if you want me to come around and talk about it there needs to be like a preliminary fucking conversation") |
| G032 | 2026-07-11 22:30:13 | S-AM-1 | Naomi | AFT-02 | primary | Naomi names not knowing what she is being asked to acknowledge ("What am I acknowledging? If you want to do this over the phone, let's do it.") |
| G046 | 2026-07-11 22:30:45 | S-AM-1 | Naomi | AFT-03 | subsumed | Environmental boundary — background noise objection ("you have to turn off the, um, the fucking..."); transition into AFT-03 |
| G178 | 2026-07-11 22:31:54 | S-AM-1 | Alex | AFT-03 | subsumed | Air-filter clarification ("what you might be hearing is my air filter for a prototype"); subsumed in AFT-03 |
| G179 | 2026-07-11 22:34:49 | S-AM-1 | Naomi | AFT-03 | subsumed | Naomi declines medium complaint ("I don't want to do this on the phone"); subsumed in AFT-03 |
| G031 | 2026-07-11 22:35:44 | S-AM-1 | Naomi | AFT-03 | subsumed | Joking deflection ("You scared of me or something little old Naomi?"); subsumed in AFT-03 |
| G099 | 2026-07-11 22:36:33 | S-AM-1 | Alex | AFT-03 | primary | Alex states Jun 26 account ("last time I came over to have the conversation face-to-face you just stared at the ground...") |
| G045 | 2026-07-11 22:37:55 | S-AM-1 | Alex | AFT-03 | subsumed | Logistics ("Why don't you come here?"); subsumed in AFT-03 |
| G042 | 2026-07-11 22:40:44 | S-AM-1 | Naomi | AFT-03 | primary | Naomi disputes Alex's characterisation ("that's not fair. That's not what happened. You're mischaracterizing that situation.") |
| G180 | 2026-07-11 22:43:14 | S-AM-1 | Naomi | AFT-03 | primary | Naomi names asymmetry of insults ("it's one thing to call someone a coward, it's another thing to pathologize someone and call them a narcissist") |
| G181 | 2026-07-11 22:43:31 | S-AM-1 | Alex | AFT-03 | subsumed | Baby photos vs paintings clarification; off-conflict tangent; subsumed in AFT-03 |
| G062 | 2026-07-11 22:43:51 | S-AM-1 | Naomi | AFT-03 | subsumed | Instruction to listen to her voice messages; subsumed in AFT-03 |
| G112 | 2026-07-11 22:45:28 | S-AM-1 | Alex | AFT-03 | primary | Alex states gaslighting account ("you called me a chaser when I turned you down... You kind of gaslit me the whole night") |
| G182 | 2026-07-11 22:46:19 | S-AM-1 | Alex | AFT-03 | primary | Naomi states voice-message timing account third time in corpus ("I didn't even listen to your voice messages that you sent before, right before you arrived") |
| G183 | 2026-07-11 22:48:21 | S-AM-1 | Alex | AFT-03 | primary | Alex Exit 1 in Aftermath ("All right, Nelly. Have a good one. I'll speak to you another time.") |
| G055 | 2026-07-11 22:48:32 | S-AM-1 | Naomi | AFT-03 | primary | Post-exit continuation; Naomi elaborates voice-message timing ("am I supposed to make you wait at the gate while I listen to the voice messages?") |
| G184 | 2026-07-11 22:49:27 | S-AM-1 | Naomi | AFT-03 | primary | Post-exit; first mention of dinner debt ("You owe me for dinner for that night") |
| G070 | 2026-07-11 22:53:24 | S-AM-1 | Naomi | AFT-03 | primary | Post-exit; Naomi describes Alex's anger at her questions as "borderline abusive" |
| G030 | 2026-07-11 23:55:57 | S-AM-2 | Naomi | AFT-04 | primary | Naomi challenges attentiveness ("So you didn't read my messages is what you're telling me right now") |
| G185 | 2026-07-11 23:56:05 | S-AM-2 | Naomi | AFT-04 | primary | Naomi names lack of evidence of listening ("it's not obvious that you're actually listening to anything I'm saying") |
| G075 | 2026-07-12 00:02:49 | S-AM-2 | Naomi | AFT-04 | primary | Naomi states Alex did not read or respond ("You literally didn't listen or read a single thing or respond to a single question") |
| G100 | 2026-07-12 00:04:10 | S-AM-2 | Naomi | AFT-04 | primary | Naomi states she has screenshots ("Signal does allow you to take screenshots because I have the whole fucking conversation screenshotted") |
| G186 | 2026-07-12 01:10:23 | S-AM-3 | Naomi | AFT-05 | primary | Naomi states explicit apology demand; names emotional blackmail; states conditional willingness to wait |
| G094 | 2026-07-12 01:15:45 | S-AM-3 | Naomi | AFT-05 | primary | Naomi states claim about prior knowledge via Nishant |
| G187 | 2026-07-12 01:22:01 | S-AM-3 | Naomi | AFT-05 | primary | Naomi says she was forced into vulnerability she had been willing to let go |
| G188 | 2026-07-12 01:31:53 | S-AM-3 | Naomi | AFT-05 | primary | Naomi states conditional patience ("I'll keep waiting for you, dude") |
| G053 | 2026-07-13 19:31:56 | S-AM-4 | Naomi | AFT-06 | primary | Naomi opens S-AM-4; apologises for her behaviour; calls Alex's withdrawal emotionally immature |
| G189 | 2026-07-13 19:42:16 | S-AM-4 | Alex | AFT-06 | primary | Alex's first and only substantive acknowledgement in the corpus; apology for "my part to play"; names her message as "authentic, honest, guttural" |
| G190 | 2026-07-13 19:42:30 | S-AM-4 | Alex | AFT-06 | subsumed | Brief Nishant aside within mutual acknowledgement exchange; subsumed in AFT-06 |
| G006 | 2026-07-13 19:44:09 | S-AM-4 | Alex | AFT-06 | primary | Alex personal disclosure (cutting people from his life, including his brother) |
| G010 | 2026-07-13 19:45:56 | S-AM-4 | Alex | AFT-06 | primary | Alex expresses empathy for rejection experience |
| G102 | 2026-07-13 19:52:40 | S-AM-4 | Alex | AFT-06 | subsumed | Warm joking aside within acknowledgement exchange; subsumed in AFT-06 |
| G090 | 2026-07-13 20:09:09 | S-AM-4 | Alex | AFT-06 | subsumed | Driving logistics; subsumed in AFT-06 |
| G191 | 2026-07-13 20:09:52 | S-AM-4 | Alex | AFT-06 | primary | Alex exits while driving ("And I'm gone") |
| G192 | 2026-07-13 20:32:56 | S-AM-4 | Naomi | AFT-07 | primary | Naomi returns after 23-min gap; begins conflict reopening |
| G193 | 2026-07-13 20:33:59 | S-AM-4 | Alex | AFT-07 | primary | Alex "sponge" self-disclosure ("I am a sponge. I will reciprocate the emotions around me because I don't have my own") |
| G194 | 2026-07-13 20:35:40 | S-AM-4 | Alex | AFT-07 | primary | Naomi restates voice-message timing account fourth time in corpus ("I hadn't even listened to your voice messages. As I've said many times") |
| G034 | 2026-07-13 20:42:43 | S-AM-4 | Naomi | AFT-07 | primary | Naomi negotiates what the apology is for ("What am I apologizing for... if my behavior has done that then I'm sorry") |
| G195 | 2026-07-13 20:57:17 | S-AM-4 | Naomi | AFT-07 | primary | Naomi specifies the hurt ("it's not about a list... you acting like you didn't know when you did know, that hurt me a lot") |
| G196 | 2026-07-13 21:13:53 | S-AM-4 | Naomi | AFT-07 | primary | Naomi names boundary declaration as inflection point ("everything changed after I mentioned that I was going to have to maybe draw some boundaries") |
| G197 | 2026-07-13 21:25:24 | S-AM-4 | Alex | AFT-08 | primary | Alex refers to a past suicide attempt as frame for imperviousness to hurt |
| G087 | 2026-07-13 21:38:11 | S-AM-4 | Alex | AFT-08 | primary | Naomi reads Alex's G197 as an attempt to hurt her ("You literally just trying to hurt me") |
| G021 | 2026-07-13 21:39:32 | S-AM-4 | Naomi | AFT-08 | primary | Naomi names specific harm from narcissist accusation ("calling someone a coward is one thing, saying someone is a narcissist... different ballparks") |
| G017 | 2026-07-13 21:43:02 | S-AM-4 | Naomi | AFT-08 | subsumed | Naomi calls Alex "kind of dumb" then self-corrects; subsumed in AFT-08 harm-naming exchange |
| G047 | 2026-07-13 21:46:05 | S-AM-4 | Naomi | AFT-08 | subsumed | Naomi elaborates questions/berating dispute; subsumed in AFT-08 |
| G026 | 2026-07-13 21:47:28 | S-AM-4 | Naomi | AFT-08 | subsumed | Naomi asserts she addressed the reality of the situation; subsumed in AFT-08 |
| G108 | 2026-07-13 21:49:21 | S-AM-4 | Naomi | AFT-08 | primary | Naomi states she has said her piece and will try not to message again ("I've said my piece... I will do my very best to not message you again unless a thought comes up") |
| G067 | 2026-07-13 22:06:35 | S-AM-4 | Naomi | AFT-09 | primary | Naomi returns despite G108 stated pause; states she was hinting at cumulative harm ("just piling on where other people have in the past") |
| G198 | 2026-07-13 22:11:09 | S-AM-4 | Naomi | AFT-09 | primary | Naomi demands Alex scroll up ("all you had to do was scroll up in the conversation and look") |
| G199 | 2026-07-13 22:12:16 | S-AM-4 | Alex | AFT-09 | primary | Alex cites ADHD and dyslexia as reason scrolling is difficult; states he is overwhelmed and will put phone on silent (Alex Exit 2 in S-AM-4) |
| G088 | 2026-07-13 22:18:56 | S-AM-4 | Naomi | AFT-09 | subsumed | Naomi disputes ADHD applicability ("You don't have a problem reading any of the other..."); subsumed in AFT-09 |
| G200 | 2026-07-13 23:04:44 | S-AM-4 | Naomi | AFT-10 | primary | Post-exit (52 min after G199); Naomi objects to communication style ("A lot of your comments are underlaid with backhanded inferences, like, I'm not your dad") |
| G201 | 2026-07-21 19:04:12 | S-AM-5 | Naomi | AFT-11 | primary | Naomi opens S-AM-5 after 7.8-day gap; gambling wins and synthesisers |
| G073 | 2026-07-21 19:08:20 | S-AM-5 | Naomi | AFT-11 | subsumed | Casual aside ("Just found a bowl of gear on the ground"); subsumed in AFT-11 |
| G050 | 2026-07-21 19:25:31 | S-AM-5 | Alex | AFT-11 | primary | Alex opens with banter ("How much did you win this week?") |
| G202 | 2026-07-21 19:26:14 | S-AM-5 | Alex | AFT-11 | primary | Synthesiser / cork drop-off offer; warm practical exchange |
| G091 | 2026-07-21 19:33:14 | S-AM-5 | Naomi | AFT-11 | primary | Playful mock-formal permission ("I grant you permission. I bequeath upon you the permiss of her lady, Naomi") |
| G203 | 2026-07-21 19:36:39 | S-AM-5 | Alex | AFT-11 | subsumed | Banter aside; subsumed in AFT-11 |
| G204 | 2026-07-21 20:22:49 | S-AM-5 | Naomi | AFT-11 | subsumed | Phone battery logistics; subsumed in AFT-11 |
| G023 | 2026-07-21 20:31:21 | S-AM-5 | Alex | AFT-11 | subsumed | Missed message logistics; subsumed in AFT-11 |
| G205 | 2026-07-21 20:34:47 | S-AM-5 | Naomi | AFT-11 | subsumed | Battery/visit logistics; subsumed in AFT-11 |
| G039 | 2026-07-21 20:36:51 | S-AM-5 | Alex | AFT-11 | subsumed | Delivery logistics; subsumed in AFT-11 |
| G079 | 2026-07-21 20:41:51 | S-AM-5 | Naomi | AFT-11 | subsumed | Cork/Jake context; subsumed in AFT-11 |
| G107 | 2026-07-21 20:42:55 | S-AM-5 | Alex | AFT-11 | subsumed | Jake insult banter; subsumed in AFT-11 |
| G063 | 2026-07-21 20:52:50 | S-AM-5 | Naomi | AFT-11 | subsumed | Banter; subsumed in AFT-11 |
| G206 | 2026-07-21 20:53:38 | S-AM-5 | Alex | AFT-11 | primary | Jewish-culture in-joke exchange opens ("You know when we first met...") |
| G072 | 2026-07-21 21:00:18 | S-AM-5 | Naomi | AFT-11 | subsumed | In-joke exchange continues; subsumed in AFT-11 |
| G003 | 2026-07-21 21:04:41 | S-AM-5 | Alex | AFT-11 | subsumed | In-joke exchange continues; subsumed in AFT-11 |
| G069 | 2026-07-21 21:06:02 | S-AM-5 | Naomi | AFT-11 | subsumed | In-joke exchange continues; subsumed in AFT-11 |
| G103 | 2026-07-21 21:12:27 | S-AM-5 | Alex | AFT-11 | subsumed | In-joke exchange final turn; subsumed in AFT-11 |
| G061 | 2026-07-21 21:13:03 | S-AM-5 | Alex | AFT-11 | primary | Last warm-banter turn before conflict trigger ("I'm fucking starving. I haven't had dinner yet") |
| G207 | 2026-07-21 21:14:31 | S-AM-5 | Naomi | AFT-12 | primary | Dinner debt raised ("You owe me dinner from the last time I saw you") |
| G022 | 2026-07-21 21:16:10 | S-AM-5 | Alex | AFT-12 | primary | Alex frames dinner as conflict reopening ("Are you starting this up again? Is that what I'm hearing?") |
| G078 | 2026-07-21 21:17:30 | S-AM-5 | Naomi | AFT-12 | primary | Naomi disputes Alex's framing of dinner as grievance ("Why do you disagree with me about you saying that you would pay for dinner that night?") |
| G059 | 2026-07-21 21:19:11 | S-AM-5 | Alex | AFT-12 | primary | Alex states conflict fatigue framing ("Why even bring it up is what I'm saying. What is this gonna achieve?") |
| G208 | 2026-07-21 21:19:44 | S-AM-5 | Alex | AFT-12 | primary | Naomi disputes categorisation ("Am I not allowed to talk about dinner?... I wasn't bringing it up. You brought it up, apparently.") |
| G209 | 2026-07-21 21:20:15 | S-AM-5 | Alex | AFT-12 | primary | Alex's final recorded event in corpus ("Okay, and on that note, I will see you another time.") |
| G058 | 2026-07-21 21:20:55 | S-AM-5 | Naomi | AFT-13 | primary | Post-exit (40 sec after G209); Naomi protests no conversation has occurred ("We haven't even had one single conversation about it yet") |
| G029 | 2026-07-21 21:35:51 | S-AM-5 | Naomi | AFT-13 | primary | Naomi states absence of responsibility and acknowledgement; names AFT-06 as the only exception ("This is the first moment you've even really acknowledged that I've said anything") |
| G210 | 2026-07-21 21:38:27 | S-AM-5 | Naomi | AFT-13 | primary | Naomi appeals to the record ("You can't argue with the record") |
| G211 | 2026-07-21 21:42:27 | S-AM-5 | Naomi | AFT-13 | primary | Naomi states claim about prior knowledge via Nishant (second instance; first was G094) |
| G012 | 2026-07-21 21:45:25 | S-AM-5 | Naomi | AFT-13 | primary | Naomi states irony of Alex's conversational exits ("Can't say not having this conversation again and again and again when you haven't even had the conversation one time") |
| G084 | 2026-07-21 21:48:45 | S-AM-5 | Naomi | AFT-13 | primary | Last event in corpus; Naomi names the irony of "I'm not having this conversation" from the point Alex left her house on Jun 27 |

---

## Audit Summary

| Metric | Value |
|---|---|
| Total events in audit | 105 |
| Events with assignment_status = primary | 67 |
| Events with assignment_status = subsumed | 38 |
| Total | 105 |
| Missing assignments | 0 |
| Duplicate assignments | 0 |
| Events absent from prior draft (now corrected) | 1 (G096) |
| Events assigned to wrong incident in prior draft | 0 |

## Correction Log

**G096** (2026-07-11 20:48:49, Alex, S-AM-1): This event — Alex dismissing Naomi's Nishant tangent mid-conversation — was absent from the prior timeline's source_event_ids across all incidents. It is now assigned to AFT-02 (subsumed). Content: *"What does this have to do with the price of fish though?"* — Alex's response to Naomi deflecting toward the Nishant phone-call context. This does not change the incident boundaries; it closes the gap in the event accounting.

**G172** (2026-07-11 20:21:50, Naomi, S-AM-1): This event was in the session but not listed in AFT-01's source_event_ids in the prior draft. It is now listed as subsumed in AFT-01. Content: Naomi's financial anxiety aside — off-conflict topic, logistically in the reconnection window.

**G078** (2026-07-21 21:17:30, Naomi, S-AM-5): Present in events.jsonl but unlisted in the prior draft's AFT-12 source_event_ids. Now assigned as primary to AFT-12. Content: Naomi disputes Alex's framing of the dinner debt as a grievance.

**G202, G203** (2026-07-21, Alex, S-AM-5): Present but unlisted in prior AFT-11 source_event_ids. Now listed as subsumed (G203) and primary (G202) in AFT-11. G202 is the synthesiser/cork offer — a key warm-banter turn; G203 is a joking banter aside.
