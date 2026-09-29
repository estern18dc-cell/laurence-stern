"""Builds the Laurence Stern site: index.html (stories), files.html, bio.html."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
REC = "https://www.cia.gov/readingroom/document/"
PDF = "https://www.cia.gov/readingroom/docs/"

# (date, sort key, title, summary, record id, has pdf)
STORIES = [
    ("Feb 19, 1965", "1965-02-19", "Don't Talk to a Martini, Olive May Be Listening",
     "A light piece on the new electronic bugs turning up in Washington, including a transmitter hidden in a cocktail olive with the toothpick as its antenna.",
     "cia-rdp67b00446r000300110014-2"),
    ("c. June 1963", "1963-06", "Fulbright Lays French Hostility to Alliance to Poor War Record",
     "Senator J. William Fulbright says France is hostile to the Atlantic Alliance because it is still overcompensating for its record in World War II.",
     "cia-rdp75-00149r000200930060-5"),
    ("Sep 11, 1963", "1963-09-11", "Bills Offered to Curb Foreign Lobbying",
     "Senators Fulbright and Bourke Hickenlooper introduce bills to tighten controls on foreign lobbying after a year-long Foreign Relations Committee investigation.",
     "cia-rdp75-00149r000200930042-5"),
    ("Nov 30, 1967", "1967-11-30", "A Spasm of Gullibility",
     "A book review revealing who wrote Report from Iron Mountain, the anonymous study on the “possibility and desirability” of peace that had Washington guessing all autumn.",
     "cia-rdp88-01350r000200370003-1"),
    ("Aug 3, 1971", "1971-08-03", "Deeper CIA Role in Laos Revealed",
     "A Senate report shows the CIA spent about $70 million in a year to run an irregular army of more than 30,000 men in Laos.",
     "cia-rdp80-01601r000900180001-6"),
    ("Jan 9, 1972", "1972-01-09", "White House Took Steps to Stop Leaks Months Before Anderson",
     "Written with Sanford J. Ungar. During secret deliberations on the India-Pakistan crisis, a Pentagon official accused the press of slanting its war coverage against Pakistan.",
     "cia-rdp74b00415r000300020017-5"),
    ("Feb 6, 1973", "1973-02-06", "Senate Foreign Relations Interrogators Turn Amiable",
     "A news analysis on how the Senate Foreign Relations Committee, once the toughest questioner of American foreign policy, went easy on a witness.",
     "cia-rdp84-00161r000400210024-1"),
    ("Mar 17, 1973", "1973-03-17", "Senate Panel Opens Investigation of ITT Operations in Chile",
     "A special Senate subcommittee opens its inquiry into charges that ITT tried to interfere in Chile's politics.",
     "cia-rdp91-00901r000600100017-6"),
    ("Mar 29, 1973", "1973-03-29", "I.T.T. and Chile",
     "Senate investigators look into a report that the CIA was authorized to spend $400,000 on covert propaganda against Salvador Allende.",
     "cia-rdp91-00901r000600100006-8"),
    ("May 18, 1973", "1973-05-18", "Symington Doubts Nixon Was Unaware of CIA Role",
     "Senator Stuart Symington reveals that the CIA resisted eight months of pressure from top White House aides to help cover up Watergate.",
     "cia-rdp77-00432r000100160001-9"),
    ("Jul 3, 1973", "1973-07-03", "Colby Says He Would Curb C.I.A. in U.S. and Abroad",
     "William Colby, Nixon's choice to head the CIA, gives Congress a carefully hedged promise to keep the agency out of domestic affairs.",
     "cia-rdp77-00432r000100190001-6"),
    ("Aug 22, 1973", "1973-08-22", "Colby Plans Changes in CIA Evaluation Unit",
     "Acting CIA Director William Colby says “some changes will occur” in the Office of National Estimates, the agency's top analytical body.",
     "cia-rdp84-00499r000200050001-9"),
    ("Sep 7, 1973", "1973-09-07", "Colby Revamps CIA Unit in White House Shakeup",
     "The Nixon administration abolishes the Office of National Estimates, a unit known for delivering unwelcome news.",
     "cia-rdp77-00432r000100230001-1"),
    ("Sep 21, 1973", "1973-09-21", "CIA Seeking to Eliminate 100 Pages of Upcoming Book",
     "The CIA tries to cut about 100 pages from a 530-page book on its operations by former officer Victor Marchetti.",
     "cia-rdp75-00001r000200480003-1"),
    ("Nov 8, 1973", "1973-11-08", "FBI Leaks Feared by Helms",
     "Richard Helms proposed tight limits on the Watergate investigation in Mexico because he feared FBI leaks would expose CIA operations.",
     "cia-rdp84-00161r000400210002-5"),
    ("Nov 17, 1973", "1973-11-17", "Colby, Helms Deny CIA Foreknowledge of Watergate Entry",
     "The current and former CIA directors tell a closed Senate Armed Services hearing they had no advance knowledge of the Watergate burglary.",
     "cia-rdp84-00161r000400210004-3"),
    ("Nov 17, 1973", "1973-11-17b", "Ex-CIA Director Tried to Limit FBI on Watergate",
     "Eleven days after the break-in, Richard Helms had his deputy ask the FBI to confine its investigation to people already arrested or under suspicion.",
     "cia-rdp84-00161r000400210003-4"),
    ("Nov 28, 1973", "1973-11-28", "Prosecutors Take a New Look at CIA's Watergate Role",
     "Richard Helms is returning from his ambassadorship in Iran for another round of testimony on the CIA's part in Watergate.",
     "cia-rdp91-00901r000700090055-5"),
    ("Feb 22, 1974", "1974-02-22", "Not Watergate Material, Nedzi Says; CIA Is Backed on Tapes",
     "Rep. Lucien Nedzi concludes that no Watergate-related or presidential conversations were among the tapes the CIA destroyed in January 1973.",
     "cia-rdp91-00901r000700090052-8"),
    ("Sep 8, 1974", "1974-09-08", "CIA Role in Chile Revealed",
     "Rep. Michael Harrington makes public William Colby's secret testimony on U.S. covert activities in Chile.",
     "cia-rdp09t00207r001000020129-1"),
    ("c. Sept 1974", "1974-09-09", "Panel to Probe CIA Role in Chile",
     "After revelations of covert U.S. intervention in Chile, including $1 million authorized to destabilize the Allende government, a congressional panel prepares an inquiry.",
     "cia-rdp09t00207r001000020078-8"),
    ("Sep 12, 1974", "1974-09-12", "CIA Chief Colby Facing Confrontation on Chile Operations",
     "William Colby agrees to appear at a two-day conference where he will face questions about covert U.S. operations in Chile.",
     "cia-rdp88-01315r000200010022-1"),
    ("Sep 14, 1974", "1974-09-14", "Colby Coolly Confronts Chile Critics",
     "William Colby faces his critics in public, with Rep. Michael Harrington leading the questioning on Chile.",
     "cia-rdp88-01315r000200010012-2"),
    ("c. Sept 1974", "1974-09-17", "President Defends Operations in Chile",
     "President Ford defends U.S. covert political operations in Chile after the 1970 election of Salvador Allende.",
     "cia-rdp09t00207r001000020084-1"),
    ("Sep 29, 1974", "1974-09-29", "CIA: Silent Partner of Foreign Policy",
     "An essay on the long-running argument over whether the United States should wage secret political warfare abroad.",
     "cia-rdp09t00207r001000020025-6"),
    ("Oct 2, 1974", "1974-10-02", "CIA to Share Operations Data with Foreign Affairs Panel",
     "Henry Kissinger and William Colby agree to share details of covert political operations with members of the House Foreign Affairs Committee.",
     "cia-rdp79-00957a000100070040-9"),
    ("c. 1974", "1974-12", "Perjury Inquiry Urged on Chile Data",
     "A Senate staff report recommends a perjury investigation of Richard Helms and says Henry Kissinger misled the Foreign Relations Committee.",
     "cia-rdp09t00207r001000020083-2"),
    ("Oct 22, 1975", "1975-10-22", "Watergate Reaction Ended Snooping",
     "The CIA's retired security director tells Senate investigators the agency's illegal mail-opening program was shut down because of Watergate.",
     "cia-rdp88-01315r000400020017-1"),
    ("Nov 5, 1975", "1975-11-05", "'Politics' at CIA Feared",
     "Written with Walter Pincus. Senator Frank Church and others warn that naming George Bush to head the CIA could bring election-year politics into the agency.",
     "cia-rdp91-00901r000700080014-1"),
    ("Dec 25, 1975", "1975-12-25", "CIA Agent's Murder Spurs Accusations",
     "The killing of CIA Athens station chief Richard Welch by three masked gunmen sets off an exchange of accusations.",
     "cia-rdp88-01314r000100370009-6"),
    ("Jan 14, 1976", "1976-01-14", "Educator, CIA Ties Probed",
     "Senate investigators look into the CIA's relationships with educators, journalists, missionaries and publishing houses.",
     "cia-rdp90-01208r000100150187-1"),
    ("Jan 24, 1976", "1976-01-24", "Colby Scolds Hill for Data Leaks",
     "In his last testimony as CIA director, William Colby says every new covert program reported to Congress in 1975 leaked to the press.",
     "cia-rdp91-00561r000100090063-3"),
    ("Jan 27, 1976", "1976-01-27", "Ford, Hill Clash on Secrets",
     "The Ford administration and Congress come close to open political warfare over control of intelligence secrets after the House committee report leaks.",
     "cia-rdp91-00561r000100090053-4"),
    ("Feb 14, 1976", "1976-02-14", "Schorr Says He Leaked Material",
     "CBS correspondent Daniel Schorr acknowledges he was the source of the House intelligence report excerpts printed in the Village Voice.",
     "cia-rdp88-01314r000300300007-3"),
    ("Feb 24, 1976", "1976-02-24", "Schorr Relieved of Reporting Duties",
     "CBS News takes Daniel Schorr off the air after his role in getting the House intelligence report to the Village Voice.",
     "cia-rdp88-01315r000400290005-5"),
    ("May 27, 1976", "1976-05-27", "CIA Policy on Journalists Draws Assent, Bush Says",
     "CIA Director George Bush says his policy on using journalists in intelligence work has met with “considerable quiet understanding” in the press.",
     "cia-rdp99-00498r000100030106-4"),
    ("c. 1977", "1977-06", "CIA Expected to Alter Iran Radar Stand",
     "Iran wants to buy seven radar-equipped Boeing 707s, and CIA Director Stansfield Turner is expected to give Congress new testimony on the sale.",
     "cia-rdp99-00498r000100100028-3"),
    ("Sep 13, 1978", "1978-09-13", "Ex-Envoy's Possession of Secret Data Probed",
     "Written with John M. Goshko. The Justice Department investigates why former ambassador Graham Martin had top-secret files at his home and in his car.",
     "cia-rdp81m00980r000600050022-7"),
]

FILES = [
    ("Aug 21, 1968", "New York Times", "Editors Reassigned by Washington Post",
     "Stern, national editor for the previous three years, moves to the Post's investigative reporting team.",
     [("Record", REC + "cia-rdp88-01314r000300380135-3"), ("PDF", PDF + "CIA-RDP88-01314R000300380135-3.pdf")]),
    ("Oct 17, 1970", "Newspaper clipping", "Promotions Announced for Eight Post Editors",
     "Stern is named assistant managing editor for Style.",
     [("Record", REC + "cia-rdp88-01314r000300380107-4"), ("PDF", PDF + "CIA-RDP88-01314R000300380107-4.pdf")]),
    ("Jul 10, 1973", "CIA legislative journal", "Journal, Office of Legislative Counsel",
     "A CIA officer asks Rep. Lucien Nedzi to help counter Stern's story that Richard Helms misled the Senate about the agency's domestic role. Nedzi says Stern used little of a long interview because it did not fit his thesis.",
     [("Record", REC + "cia-rdp75b00380r000100080090-8"), ("PDF", PDF + "CIA-RDP75B00380R000100080090-8.pdf")]),
    ("Jul 10, 1973", "CIA memo", "Briefing of the CIA Subcommittee of Senate Armed Services",
     "A follow-up item: a paper for Senator Symington on the Helms statement “as reported in the Laurence Stern article.”",
     [("Record", REC + "cia-rdp75b00380r000200010126-4"), ("PDF", PDF + "CIA-RDP75B00380R000200010126-4.pdf")]),
    ("Jul 12, 1973", "CIA legislative journal", "Journal, Office of Legislative Counsel",
     "House Armed Services staff ask the CIA for a memo on the context of statements in Stern's article, after questions from Rep. William Bray.",
     [("Copy 1", REC + "cia-rdp75b00380r000200050091-9"), ("Copy 2", REC + "cia-rdp75b00380r000100080079-1")]),
    ("Jun 26, 1974", "CIA legislative journal", "Journal, Office of Legislative Counsel",
     "A Senate staffer asks for a copy of the CIA Director's secrecy proposal after reading Stern's article about it that day.",
     [("Record", REC + "cia-rdp75b00380r000600200032-3"), ("PDF", PDF + "CIA-RDP75B00380R000600200032-3.pdf")]),
    ("Jan 13, 1975", "CIA memo", "Allegations re Intercept of George Meany's Mail",
     "After Stern reported that the CIA read AFL-CIO president George Meany's mail, the agency searched its files and found no evidence of an intercept.",
     [("Record", REC + "01435020")]),
]

CSS = """
:root{--bg:#000;--fg:#fff;--dim:rgba(255,255,255,.62);--line:rgba(255,255,255,.16);--hover:rgba(255,255,255,.06);
--sans:"Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;--mono:"Geist Mono",ui-monospace,Menlo,monospace;color-scheme:dark}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--sans);font-size:16px;line-height:1.55;-webkit-font-smoothing:antialiased}
a{color:inherit}
a:focus-visible,input:focus-visible{outline:2px solid var(--fg);outline-offset:2px}
.bar{position:sticky;top:0;z-index:10;background:rgba(0,0,0,.78);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid var(--line);padding-top:env(safe-area-inset-top,0px)}
.bar-in,.wrap{max-width:960px;margin:0 auto;padding-inline:20px}
.bar-in{display:flex;align-items:center;justify-content:space-between;gap:16px;height:56px}
.logo{font-weight:600;letter-spacing:-.01em;text-decoration:none}
nav{display:flex;gap:4px}
nav a{font-size:14px;text-decoration:none;color:var(--dim);padding:6px 12px;border-radius:999px}
nav a:hover{color:var(--fg)}
nav a[aria-current="page"]{color:var(--bg);background:var(--fg)}
.hero{padding-block:72px 40px}
.hero h1{font-size:clamp(44px,9vw,96px);line-height:.95;letter-spacing:-.045em;font-weight:700;margin:0 0 20px;text-wrap:balance}
.hero p{color:var(--dim);font-size:18px;max-width:56ch;margin:0}
.tools{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px;margin-bottom:8px}
.tools h2{font-size:22px;letter-spacing:-.02em;margin:0}
.tools.top{padding-block:48px 16px;border-bottom:1px solid var(--line);margin:0}
.tools h1{font-size:clamp(36px,6vw,56px);letter-spacing:-.04em;line-height:1;margin:0}
.search{flex:1 1 240px;max-width:320px;background:transparent;color:var(--fg);border:1px solid var(--line);border-radius:999px;padding:10px 16px;font:inherit;font-size:14px}
.search::placeholder{color:var(--dim)}
.year{display:grid;grid-template-columns:96px 1fr;gap:0 24px;border-top:1px solid var(--line)}
.year > h3{margin:0;padding-top:22px;font-family:var(--mono);font-size:14px;font-weight:500;color:var(--dim)}
.rows{min-width:0}
.row{padding:20px 0;border-bottom:1px solid var(--line);min-width:0}
.row:last-child{border-bottom:0}
.row .date{font-family:var(--mono);font-size:12px;color:var(--dim);font-variant-numeric:tabular-nums}
.row h4{font-size:19px;font-weight:600;letter-spacing:-.015em;line-height:1.3;margin:4px 0 6px;text-wrap:balance}
.row p{color:var(--dim);margin:0 0 12px;max-width:66ch}
.btns{display:flex;flex-wrap:wrap;gap:8px}
.btn{font-family:var(--mono);font-size:12px;text-decoration:none;border:1px solid var(--line);border-radius:999px;padding:5px 12px;transition:background .15s,color .15s,border-color .15s}
.btn:hover{background:var(--fg);color:var(--bg);border-color:var(--fg)}
.empty{color:var(--dim);padding:24px 0}
.prose{font-size:18px;max-width:64ch}
.prose p{margin:0 0 1.1em}
.timeline{list-style:none;margin:40px 0 0;padding:0;border-top:1px solid var(--line)}
.timeline li{display:grid;grid-template-columns:96px 1fr;gap:24px;padding:14px 0;border-bottom:1px solid var(--line)}
.timeline span{font-family:var(--mono);font-size:14px;color:var(--dim)}
footer{margin-top:72px;border-top:1px solid var(--line);padding-block:24px 48px;font-size:14px;color:var(--dim)}
@media (max-width:600px){.year,.timeline li{grid-template-columns:1fr;gap:4px}.year > h3{padding-top:16px}.hero{padding-block:48px 32px}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.btn{transition:none}}
"""

NAV = [("./", "Stories", "stories"), ("files.html", "Files", "files"), ("bio.html", "Bio", "bio")]


def page(key, title, body, script=""):
    nav = "".join(f'<a href="{h}"' + (' aria-current="page"' if k == key else "") + f">{t}</a>" for h, t, k in NAV)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="Laurence Stern's reporting and the CIA's files on him, from the CIA FOIA Reading Room.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap">
<style>{CSS}</style>
</head>
<body>
<header class="bar"><div class="bar-in"><a class="logo" href="./">Laurence Stern</a><nav aria-label="Site">{nav}</nav></div></header>
<main class="wrap">
{body}
</main>
<footer class="wrap">All documents come from the <a href="https://www.cia.gov/readingroom/search/site/laurence%20stern">CIA FOIA Electronic Reading Room</a>. Summaries are based on the archive's OCR text, which is often garbled, so check the PDFs for exact wording.</footer>
{script}
</body>
</html>
"""


def buttons(links):
    return '<div class="btns">' + "".join(
        f'<a class="btn" href="{u}" target="_blank" rel="noopener">{t} ↗</a>' for t, u in links) + "</div>"


def story_links(doc):
    return [("Read PDF", PDF + doc.upper() + ".pdf"), ("CIA record", REC + doc)]


def build_stories():
    ordered = [STORIES[0]] + sorted(STORIES[1:], key=lambda s: s[1])
    rows = "".join(
        f'<article class="row" data-q="{(t + " " + x).lower().replace(chr(34), "")}">'
        f'<div class="date">{d}</div><h4>{t}</h4><p>{x}</p>{buttons(story_links(doc))}</article>'
        for d, _, t, x, doc in ordered)
    body = f"""<div class="tools top"><h1>Stories</h1><input class="search" id="q" type="search" placeholder="Search stories" aria-label="Search stories"></div>
<div class="rows list">{rows}</div>
<p class="empty" id="none" hidden>No stories match that search.</p>"""
    script = """<script>
const q=document.getElementById('q'),none=document.getElementById('none');
q.addEventListener('input',()=>{const v=q.value.trim().toLowerCase();let any=false;
document.querySelectorAll('.row').forEach(r=>{const m=!v||r.dataset.q.includes(v);r.hidden=!m;if(m)any=true});
none.hidden=any;});
</script>"""
    return page("stories", "Laurence Stern", body, script)


def build_files():
    rows = "".join(
        f'<article class="row"><div class="date">{d} · {src}</div><h4>{t}</h4><p>{x}</p>{buttons(links)}</article>'
        for d, src, t, x, links in FILES)
    body = f"""<section class="hero">
<h1>Files</h1>
<p>Internal CIA records that mention Stern or respond to his reporting, plus press items about his career.</p>
</section>
<section class="year"><h3>{len(FILES)} items</h3><div class="rows">{rows}</div></section>"""
    return page("files", "Files · Laurence Stern", body)


def build_bio():
    body = """<section class="hero">
<h1>Bio</h1>
<p>1929–1979</p>
</section>
<div class="prose">
<p>Laurence Stern was a Washington Post reporter and editor who covered Congress, national security, intelligence and foreign policy. In the early 1960s he covered the Senate Foreign Relations Committee under J. William Fulbright. By 1968 he had been national editor for three years, and that summer he moved to the paper's investigative reporting team. In 1970 he was named assistant managing editor for Style.</p>
<p>In the 1970s he became one of the leading reporters on the CIA, covering the agency's links to Watergate, covert operations in Chile and Laos, ITT's role in Chile, and the Senate and House intelligence investigations. CIA records show officials working to counter his stories in Congress. He also wrote <em>The Wrong Horse</em> (1977), a book on U.S. policy toward Cyprus.</p>
<p>Stern died in 1979 at age 50. A journalism fellowship was later created in his name.</p>
</div>
<ul class="timeline">
<li><span>1963</span>Covers Fulbright and the Senate Foreign Relations Committee</li>
<li><span>1968</span>Moves from national editor to the investigative team</li>
<li><span>1970</span>Named assistant managing editor, Style</li>
<li><span>1973</span>Covers the CIA, ITT in Chile and Watergate</li>
<li><span>1974</span>Covers the revelations of covert action in Chile</li>
<li><span>1975–76</span>Covers the congressional intelligence investigations</li>
<li><span>1977</span>Publishes <em>The Wrong Horse</em></li>
<li><span>1979</span>Dies at 50</li>
</ul>"""
    return page("bio", "Bio · Laurence Stern", body)


for name, html in [("index.html", build_stories()), ("files.html", build_files()), ("bio.html", build_bio())]:
    with open(os.path.join(OUT, name), "w") as f:
        f.write(html)
print(len(STORIES), "stories,", len(FILES), "files")
