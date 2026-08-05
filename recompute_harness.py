import json, re, datetime as dt, statistics as st
from collections import Counter, defaultdict

rows=[json.loads(l) for l in open('events.jsonl')]
def parse(r):
    t=r['t'].strip(); approx=t.startswith('~')
    t=t.lstrip('~').strip()
    d,tm=t.split(' ',1)
    if ':' in tm:
        p=tm.split(':')
        while len(p)<3: p.append('00')
        tm=':'.join(x.zfill(2) for x in p); prec = 'min' if len(r['t'].strip().lstrip('~').split(' ',1)[1].split(':'))==2 else 'sec'
    else:
        tm=tm.ljust(6,'0'); tm=f'{tm[0:2]}:{tm[2:4]}:{tm[4:6]}'; prec='sec'
    return dt.datetime.strptime(d+' '+tm,'%Y-%m-%d %H:%M:%S'), approx, prec
for r in rows:
    r['_dt'],r['_approx'],r['_prec']=parse(r)
rows.sort(key=lambda r:(r['_dt'], r['eid']))

PH=[('Baseline','2026-04-01','2026-06-22'),('Conflict','2026-06-23','2026-07-05'),
    ('Silence','2026-07-06','2026-07-10'),('Aftermath','2026-07-11','2026-07-21')]
def phase(r):
    d=r['_dt'].date().isoformat()
    for n,a,b in PH:
        if a<=d<=b: return n
    return 'OUT'
for r in rows: r['_ph']=phase(r)

def text(r):
    return r.get('txt') or ''
def words(r):
    return len(re.findall(r"[A-Za-z0-9']+", text(r)))
for r in rows: r['_w']=words(r); r['_q']= '?' in text(r)

# sessions: 60-min gap
def sessionize(sub, gap_min=60):
    ss=[]; cur=[]
    for r in sub:
        if cur and (r['_dt']-cur[-1]['_dt']).total_seconds()>gap_min*60:
            ss.append(cur); cur=[]
        cur.append(r)
    if cur: ss.append(cur)
    return ss
