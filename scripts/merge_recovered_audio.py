import json
import hashlib

# Text payloads
b122_text = "You weren't interested in me. You just didn't have any way to smoke gear. You needed someone to smoke gear. Even though you didn't really enjoy my company that much, you just needed someone to smoke gear that was comfortable and welcomed you. Silly me. Silly me. Oh, God."

b127_text = "Look at the harm. Done. And people can't be honest with the people around them. It's all kinds of people. I can't believe, honestly, like I was not expecting you to be proud of hurting me. As you have been tonight. Like, you know, just like, I'm just trying to hurt me more. Just like, like, suffer. Suffer. Suffer the worst fucking misery of your life. Like, you didn't even try to protect me at all. You like, you like, so didn't try to protect me to the point of like, gaslighting me. Um, trying to, you know, act like things that happened didn't happen. Um, weird. Honestly. Um, that's why this is me protecting your ego, not the other way around. Um, who cares about Naomi's ego? She can take it."

b128_text = "Um, I really done a number on this one, Alex. Truly scorched. I don't know to do. Hold up. Now you kind of created this whole thing. We're like, oh, you're avoiding me and Ned or some shit. I just asked for clarification that you wouldn't give me. You've had all night to like bring this stuff up. You've been gaslighting me. And then you turn around, call me the gaslighter. Like, I don't know what the fuck you want, dude. I said that last week. And we spoke about it. And that conversation ended and then you brought it back up. Um, but I'm saying you created this whole scenario months ago. Like, answer my question. Answer any one of my questions. All of them, please. I would prefer that. Why did you bring the Ned thing back up? Like, why did you seek me out to speak to me about this? Like, why did you want to speak about it?"

payloads = {
    "B122": b122_text,
    "B127": b127_text,
    "B128": b128_text
}

with open('events.jsonl', 'r', encoding='utf-8') as f:
    events = [json.loads(line) for line in f]

for e in events:
    if e.get('eid') in payloads:
        print(f"Updating {e['eid']}...")
        e['txt'] = payloads[e['eid']]
        
        # Remove flags
        if 'no_audio_available' in e:
            del e['no_audio_available']
            
        if 'flags' in e and "timestamp_inferred" in e['flags']:
            e['flags'].remove("timestamp_inferred")
            if "recovered_from_summaryai" not in e['flags']:
                e['flags'].append("recovered_from_summaryai")
                
        # Recompute hash. The join key is (t, s, txt).
        key = f"{e['t']}|{e['s']}|{e['txt']}"
        e['sha256'] = hashlib.sha256(key.encode('utf-8')).hexdigest()

with open('events.jsonl', 'w', encoding='utf-8') as f:
    for e in events:
        f.write(json.dumps(e) + '\n')

print("Update complete!")
