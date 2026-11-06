"""시안 v3 HTML 생성기 — 같은 콘텐츠로 테마별 구성을 만든다.  python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
B = "https://yidoinsight.com"
BOOK = "https://booking.naver.com/booking/13/bizes/1712749"
MAP = "https://map.naver.com/p/search/%EC%84%9C%EC%9A%B8%EC%9D%B4%EB%8F%84%EC%B9%98%EA%B3%BC%EC%9D%98%EC%9B%90"
KAKAO = "https://pf.kakao.com/_JKXBX"

# ---------------------------------------------------------------- 콘텐츠 (원본 사이트 기준)
CATS = [
    ("임플란트·발치", "Implant", "빠진 치아를 되살리는 치료와 사랑니까지", [("치과임플란트", "dental-implant"), ("골이식", "bone-grafting"), ("사랑니", "wisdom-tooth")]),
    ("보철·수복", "Restoration", "씌우고, 채우고, 연결하는 치료", [("치과 크라운", "dental-crown"), ("인레이·온레이", "inlay-onlay"), ("치과 브리지", "dental-bridge"), ("틀니", "dentures")]),
    ("보존·신경치료", "Endodontics", "충치부터 신경치료, 레진까지", [("치아우식증", "tooth-decay"), ("근관치료", "root-canal-treatment"), ("복합레진", "composite-resin")]),
    ("잇몸·예방", "Gum care", "양치할 때 피가 나거나 잇몸이 붓는다면", [("치주염", "periodontitis"), ("스케일링", "scaling")]),
    ("교정·성장", "Orthodontics", "성인 교정부터 아이의 성장기 교정까지", [("투명교정장치", "clear-aligners"), ("성장기교정", "growth-orthodontics"), ("교정 유지장치", "orthodontic-retainers")]),
    ("턱관절·구강외과", "TMJ", "턱에서 소리가 나거나 아침에 뻐근하다면", [("턱관절장애", "temporomandibular-disorder"), ("이갈이·이악물기", "bruxism")]),
    ("증상·통증", "Symptoms", "찬물에 시리거나 씹을 때 불편할 때", [("시린이", "tooth-sensitivity")]),
    ("검사·진단", "Diagnosis", "상담에서 자주 듣는 진단 용어", [("교합", "occlusion")]),
    ("보험·비용", "Insurance", "건강보험 적용 기준을 미리 확인", [("임플란트 건강보험", "dental-implant-insurance")]),
]
COLUMNS = [
    ("col-ko.jpg", "고성민 대표원장", "치료를 결정하기 전, 제가 먼저 생각하는 것", "치료의 필요성과 환자의 건강·생활을 함께 살피는 관점을 정리했습니다.", "/columns/attention-to-one-patient/"),
    ("col-park.jpg", "박지현 대표원장 · 치과보철과 전문의", "보철의 완성은, 다시 편하게 씹는 데 있습니다", "치아 모양뿐 아니라 잇몸과 맞물림, 일상의 씹는 느낌까지 살펴봅니다.", "/columns/form-and-function/"),
    ("col-won.jpg", "원소윤 수석원장", "자연스러운 미소를 위해, 덜 바꾸는 방법부터 생각합니다", "어울리는 부분은 남기고 필요한 변화만 구분하는 심미치료의 기준입니다.", "/columns/care-in-the-details/"),
]
GUIDES = [
    ("공덕 임플란트 상담 준비", "치료를 권하는 이유와 견적의 범위를 같은 기준으로 확인하기", "/guides/gongdeok-implant-consultation/"),
    ("보철 상담, 모양과 씹는 느낌", "원하는 모습과 씹을 때의 불편을 나누어 이야기하기", "/journal/restoration-consultation/"),
    ("교정 상담 전 물어볼 것", "시기, 방법, 기간을 묻는 순서", "/journal/orthodontic-consultation/"),
    ("양치할 때 잇몸에서 피가 난다면", "일상에서 느낀 불편을 정리하는 방법", "/journal/gum-health/"),
    ("첫 방문, 무엇을 이야기할까요?", "불편한 점과 궁금한 내용을 메모해 가기", "/journal/first-visit/"),
]
DOCTORS = [
    ("dr-ko.jpg", "고성민", "대표원장", "", "임플란트 수술 · 진정치료 · 턱관절·구강외과", "/doctors/ko-sungmin/"),
    ("dr-park.jpg", "박지현", "대표원장", "치과보철과 전문의", "심미보철 · 임플란트 보철 · 전악수복", "/doctors/park-jihyun/"),
    ("dr-won.jpg", "원소윤", "수석원장", "", "심미보철 · 라미네이트 비니어 · 레진 수복", "/doctors/won-soyun/"),
    (None, "한이연", "교정원장", "치과교정과 전문의", "브라켓 교정 · 투명교정 · 성장기교정", "/doctors/#han-iyeon"),
]
SPACES = [
    ("consult-ko.jpg", "상담실", "모니터로 사진과 X-ray를 함께 보며, 치료를 정하기 전에 충분히 설명합니다.", "상담실에서 환자에게 설명하는 고성민 대표원장"),
    ("lab.jpg", "원내 기공실", "보철물을 병원 안에서 만들고 다듬어, 진료실과 바로 의견을 주고받습니다.", "원내 기공실에서 보철물을 다듬는 치과기공사"),
    ("lounge.jpg", "라운지", "진료 전 기다리는 시간도 편안하도록 넓고 조용한 대기 공간을 두었습니다.", "서울이도치과 라운지"),
]
FAQ = [
    ("임플란트 상담에서 비용 말고 무엇을 물어봐야 할까요?", "왜 임플란트를 권하는지, 견적에 어떤 항목이 들어 있는지, 치료 일정과 이후 관리는 어떻게 되는지 물어보세요. 실제 비용과 치료 계획은 진찰 후에 정해집니다.", "임플란트 상담 준비 읽기", "/guides/gongdeok-implant-consultation/"),
    ("찬물을 마시면 이가 시려요. 무엇부터 읽으면 좋을까요?", "치아백과의 시린이 설명에서 용어의 뜻과 상담 전에 확인할 질문을 볼 수 있습니다. 언제, 어느 쪽이 시린지 기억해 진료 때 알려주세요.", "시린이 설명 읽기", "/knowledge/tooth-sensitivity/"),
    ("양치할 때 잇몸에서 피가 나요.", "언제부터, 얼마나 자주 나는지 적어 오시면 상담이 빨라집니다. 잇몸 건강 글에서 일상의 불편을 정리하는 방법을 읽어보세요.", "잇몸 건강 이야기", "/journal/gum-health/"),
    ("크라운 재료는 어떻게 고르나요?", "원하는 색과 모양, 씹을 때의 느낌을 나누어 이야기해 보세요. 재료를 권하는 이유와 제작 과정, 관리 방법을 함께 확인하면 좋습니다.", "보철 상담 이야기", "/journal/restoration-consultation/"),
    ("아이 교정은 언제 상담하면 될까요?", "필요한 시기와 방법은 아이의 현재 치열과 턱 성장 상태를 본 뒤 정합니다. 성장기교정에 쓰이는 말과 상담에서 확인할 질문을 먼저 읽어보세요.", "성장기교정 설명", "/knowledge/growth-orthodontics/"),
    ("주차와 야간 진료가 되나요?", "월요일과 목요일은 저녁 8시 30분까지 진료합니다. 차량은 신공덕 아이파크 지하주차장을 2시간 무료로 이용할 수 있으며, 등록 방법은 방문 시 안내해 드립니다.", "방문 안내 보기", "/visit/"),
]
HOURS = [("1,4", "월 · 목", "09:30 – 20:30", "야간진료"), ("2,3,5", "화 · 수 · 금", "09:30 – 18:30", ""), ("6", "토요일", "09:30 – 14:30", "점심시간 없음"), ("", "평일 점심", "12:30 – 14:00", ""), ("0", "일요일 · 공휴일", "휴진", "")]
CHIPS = ["임플란트", "시린이", "크라운", "잇몸 출혈", "사랑니", "교정"]


def lead_text():
    return "서울이도치과 의료진이 진료실에서 다 하지 못한 설명을 치아백과와 원장 칼럼으로 정리했습니다. 치료를 정하기 전에 먼저 읽어보세요."


# ---------------------------------------------------------------- 공용 조각
def head(theme, title):
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="마포구 신공덕동, 공덕역 인근 서울이도치과의 치아백과와 원장 칼럼. 진료 전에 읽는 치과 용어와 상담 준비 글, 진료시간과 위치를 확인하세요.">
<script>document.documentElement.classList.add('js')</script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
<link rel="stylesheet" href="css/setting.css">
<link rel="stylesheet" href="css/insight.css">
</head>
<body class="u-pretendard" data-theme="{theme}">
"""


def header(theme):
    logo = {"a": '<img class="on-light" src="assets/logo-dark.svg" alt="서울이도치과" width="926" height="250">',
            "b": '<img class="on-light" src="assets/logo-dark.svg" alt="" width="926" height="250"><img class="on-dark" src="assets/logo-light.svg" alt="서울이도치과" width="926" height="250">',
            "c": '<img class="on-light" src="assets/logo-walnut.svg" alt="서울이도치과" width="926" height="250">'}[theme]
    nav = [("치아백과", "#encyclopedia"), ("원장 칼럼", "#columns"), ("의료진", "#doctors"), ("진료시간·오시는 길", "#visit")]
    links = "".join(f'<a href="{h}">{t}</a>' for t, h in nav)
    return f"""<header class="ins-header">
  <div class="bar u-1440 ins-wrap">
    <a class="ins-logo" href="#top" aria-label="서울이도치과 닥터인사이트 처음으로">{logo}</a>
    <nav class="ins-nav" aria-label="주요 메뉴">{links}</nav>
    <div class="actions">
      <a class="tel" href="tel:027062080">02-706-2080</a>
      <a class="u-btn u-btn-main" href="{BOOK}" target="_blank" rel="noopener">네이버 예약</a>
    </div>
    <details class="ins-menu">
      <summary aria-label="메뉴 열기"><span></span></summary>
      <div class="panel">{links}<a href="#faq">자주 묻는 질문</a></div>
    </details>
  </div>
</header>
"""


def cta_buttons(extra=""):
    return f"""<div class="d-flex flex-wrap u-gap-12 {extra}">
          <a class="u-btn u-btn-main u-btn-lg" href="{BOOK}" target="_blank" rel="noopener">네이버 예약하기 <span class="ins-arrow" aria-hidden="true">→</span></a>
          <a class="u-btn u-btn-outline u-btn-lg" href="tel:027062080">전화 02-706-2080</a>
        </div>"""


def facts():
    return """<ul class="ins-facts list-unstyled m-0">
          <li>월·목 저녁 8시 30분까지 진료</li>
          <li>공덕역 5·6번 출구 도보 3분</li>
          <li>주차 2시간 무료</li>
        </ul>"""


def search_block(dark=False):
    chips = "".join(f'<button type="button">{c}</button>' for c in CHIPS)
    return f"""<form class="ins-search" id="ins-search-form" role="search">
          <label class="visually-hidden" for="ins-q">치료 이름이나 증상 검색</label>
          <div class="field">
            <input id="ins-q" type="search" autocomplete="off" placeholder="예: 시린이, 크라운, 잇몸 출혈">
            <button class="u-btn u-btn-main" type="submit">찾기</button>
          </div>
          <div class="ins-chips u-mt-16" aria-label="많이 찾는 말">{chips}</div>
          <div class="ins-results" id="ins-results" aria-live="polite"></div>
        </form>"""


def cat_cards(soft=False):
    out = []
    for i, (name, en, desc, terms) in enumerate(CATS):
        t = "".join(f'<a href="{B}/knowledge/{s}/">{n}</a>' for n, s in terms)
        out.append(f"""<article class="ins-cat{' is-soft' if soft else ''}" data-reveal style="--d:{i % 3}">
            <h3 class="t-fs-24 t-fs-20-sm fw-700 m-0">{name}<small>{len(terms)}개 용어</small></h3>
            <p class="c-fs-16 ins-muted m-0">{desc}</p>
            <div class="terms">{t}</div>
          </article>""")
    return "\n          ".join(out)


def col_cards(ratio="u-ratio-4-3"):
    out = []
    for i, (img, who, title, desc, href) in enumerate(COLUMNS):
        out.append(f"""<a class="ins-card" href="{B}{href}" data-reveal style="--d:{i}">
            <div class="ph {ratio}"><img src="assets/img/{img}" alt="{who} 인터뷰 장면" width="1200" height="801" loading="lazy"></div>
            <span class="who">{who}</span>
            <h3 class="t-fs-24 t-fs-20-sm fw-700 u-lh-135 m-0">{title}</h3>
            <p class="c-fs-16 ins-muted m-0">{desc}</p>
          </a>""")
    return "\n          ".join(out)


def guides():
    rows = "".join(f'<a href="{B}{h}"><span><strong>{t}</strong><span>{d}</span></span><span class="ins-arrow" aria-hidden="true">→</span></a>' for t, d, h in GUIDES)
    return f'<nav class="ins-guides" aria-label="상담 준비 글">{rows}</nav>'


def doctor_cards():
    out = []
    for i, (img, name, role, spec, fields, href) in enumerate(DOCTORS):
        ph = (f'<img src="assets/img/{img}" alt="{name} {role}" width="900" height="1125" loading="lazy">' if img
              else f'<div class="mono"><b>{name}</b><span>{role} · 사진 준비 중</span></div>')
        sp = f'<span class="spec">{spec}</span>' if spec else ''
        out.append(f"""<a class="ins-doc" id="dentist-{i + 1}" href="{B}{href}" data-reveal style="--d:{i}">
            <div class="ph">{ph}</div>
            <div class="name"><h3 class="t-fs-24 t-fs-20-sm fw-700 m-0">{name}</h3><span class="ins-muted c-fs-16">{role}</span></div>
            {sp}
            <p class="c-fs-16 ins-body m-0">{fields}</p>
          </a>""")
    return "\n          ".join(out)


def hours_table():
    rows = []
    for days, label, time, tag in HOURS:
        cls = ' class="off"' if days == "0" else ''
        t = f'<span class="tag">{tag}</span>' if tag else ''
        rows.append(f'<tr data-days="{days}"{cls}><th scope="row">{label}{t}</th><td>{time}</td></tr>')
    return f'<table class="ins-hours"><caption class="visually-hidden">서울이도치과 진료시간</caption><tbody>{"".join(rows)}</tbody></table>'


def visit_info():
    return f"""<dl class="ins-info m-0">
              <div><dt>주소</dt><dd>서울 마포구 만리재로 24, 2층<br><span class="ins-muted c-fs-14">신공덕동 178 · 서울이도치과의원</span></dd></div>
              <div><dt>지하철</dt><dd>공덕역 5·6번 출구에서 도보 약 3분</dd></div>
              <div><dt>주차</dt><dd>신공덕 아이파크 지하주차장 2시간 무료</dd></div>
              <div><dt>전화</dt><dd><a href="tel:027062080">02-706-2080</a></dd></div>
            </dl>
            <div class="d-flex flex-wrap u-gap-12 u-mt-32">
              <a class="u-btn u-btn-main" href="{BOOK}" target="_blank" rel="noopener">네이버 예약</a>
              <a class="u-btn u-btn-outline" href="{MAP}" target="_blank" rel="noopener">네이버 지도 길찾기</a>
            </div>"""


def faq_list():
    out = []
    for i, (q, a, lt, lh) in enumerate(FAQ):
        out.append(f"""<details{' open' if i == 0 else ''}>
              <summary>{q}<span class="pm" aria-hidden="true"></span></summary>
              <div class="answer c-fs-16"><p class="m-0">{a}</p><a href="{B}{lh}">{lt} <span class="ins-arrow" aria-hidden="true">→</span></a></div>
            </details>""")
    return "\n            ".join(out)


def footer():
    return f"""<footer class="ins-footer u-py-120 u-py-80-sm">
  <div class="u-1440 ins-wrap">
    <div class="row g-5 align-items-end">
      <div class="col-lg-7">
        <h2 class="cta-line m-0">궁금한 점은<br>전화로 먼저 물어보셔도 됩니다.</h2>
      </div>
      <div class="col-lg-5 d-flex flex-column align-items-lg-end u-gap-16">
        <a class="tel-big" href="tel:027062080">02-706-2080</a>
        <div class="d-flex flex-wrap u-gap-12">
          <a class="u-btn u-btn-main" href="{BOOK}" target="_blank" rel="noopener">네이버 예약</a>
          <a class="u-btn u-btn-outline" href="{KAKAO}" target="_blank" rel="noopener">카카오톡 문의</a>
        </div>
      </div>
    </div>
    <div class="divider u-my-48"></div>
    <div class="row g-4 c-fs-14">
      <div class="col-lg-4"><strong class="d-block c-fs-16 u-mb-12">서울이도치과의원</strong>서울 마포구 만리재로 24, 2층 (신공덕동 178)<br>공덕역 5·6번 출구 도보 약 3분 · 02-706-2080</div>
      <div class="col-lg-4"><strong class="d-block c-fs-16 u-mb-12">진료시간</strong>월·목 09:30 – 20:30 · 화·수·금 09:30 – 18:30<br>토 09:30 – 14:30 · 일·공휴일 휴진 · 평일 점심 12:30 – 14:00</div>
      <div class="col-lg-4"><strong class="d-block c-fs-16 u-mb-12">닥터인사이트</strong>
        <nav class="d-flex flex-wrap u-gap-16" aria-label="안내">
          <a href="{B}/knowledge/">치아백과</a><a href="{B}/symptoms/">증상으로 찾기</a><a href="{B}/columns/">칼럼</a><a href="{B}/sources/">참고자료</a><a href="{B}/privacy/">개인정보처리방침</a><a href="https://seoulyido.com/">병원 공식 홈페이지</a>
        </nav>
      </div>
    </div>
    <div class="d-flex flex-wrap justify-content-between u-gap-16 u-mt-48 c-fs-14">
      <span>이 사이트의 의료정보는 일반적인 안내이며, 개인의 진단과 치료를 대신하지 않습니다.</span>
      <span class="d-flex u-gap-16"><a href="{B}/en/">English</a><a href="{B}/ja/">日本語</a><a href="{B}/zh-cn/">中文</a><span>© 2026 Seoul Yido Dental</span></span>
    </div>
  </div>
</footer>
"""


def dock():
    return f"""<nav class="ins-dock" aria-label="빠른 연락">
  <a class="call" href="tel:027062080">전화 상담</a>
  <a class="book" href="{BOOK}" target="_blank" rel="noopener">네이버 예약</a>
</nav>
<script src="js/insight.js"></script>
</body>
</html>
"""


def sec_head(label, title, desc="", link=None, center=False):
    l = f'<a class="c-fs-16 fw-600 d-inline-flex u-gap-8 align-items-center" href="{link[1]}">{link[0]} <span class="ins-arrow" aria-hidden="true">→</span></a>' if link else ''
    d = f'<p class="c-fs-18 c-fs-16-sm ins-body u-mt-16 m-0 ins-measure">{desc}</p>' if desc else ''
    return f"""<div class="d-flex flex-wrap justify-content-between align-items-end u-gap-24 u-mb-48 u-mb-32-sm" data-reveal>
        <div>
          <h2 class="t-fs-48 t-fs-28-sm fw-700 u-lh-125 m-0">{title}</h2>
          {d}
        </div>
        {l}
      </div>"""


H1 = '<span class="kicker">마포·공덕역 서울이도치과 닥터인사이트</span>치료보다 먼저,<br>이해할 수 있도록'


# ---------------------------------------------------------------- A · Clinic White
def page_a():
    return head("a", "서울이도치과 닥터인사이트 | 시안 A · Clinic White") + header("a") + f"""
<main id="top">
  <section class="ins-hero hero-a" aria-labelledby="hero-title">
    <div class="u-1440 ins-wrap">
      <div class="grid">
        <div>
          <h1 id="hero-title" class="t-fs-72 t-fs-36-sm fw-700 u-lh-12 m-0" data-rise style="--d:0">{H1}</h1>
          <p class="c-fs-20 c-fs-16-sm ins-body u-lh-17 u-mt-32 u-mt-24-sm m-0 ins-measure" data-rise style="--d:1">{lead_text()}</p>
          <div data-rise style="--d:2">{cta_buttons('u-mt-40')}</div>
          <div class="u-mt-48" data-rise style="--d:3">{facts()}</div>
        </div>
        <figure class="media m-0">
          <video autoplay muted loop playsinline preload="auto" poster="assets/video/consult-poster.jpg" aria-label="고성민 대표원장이 X-ray 화면을 보며 환자에게 설명하는 모습"><source src="assets/video/consult-loop.webm" type="video/webm"><source src="assets/video/consult-loop.mp4" type="video/mp4"></video>
          <div class="today"><small>오늘 진료</small><strong><span class="ins-dot" aria-hidden="true"></span><span data-status>09:30 – 18:30 진료</span></strong></div>
        </figure>
      </div>
    </div>
  </section>

  <section class="ins-section-alt u-py-120 u-py-80-sm" aria-labelledby="search-title">
    <div class="u-1440 ins-wrap">
      <div class="row g-5 align-items-center">
        <div class="col-lg-5" data-reveal>
          
          <h2 id="search-title" class="t-fs-48 t-fs-28-sm fw-700 u-lh-125 m-0">진료실에서 들은 말,<br>여기서 쉽게 풀어드려요</h2>
          <p class="c-fs-18 c-fs-16-sm ins-body u-mt-16 m-0">치료 이름을 알면 이름으로, 모르면 불편한 증상으로 찾아보세요.</p>
        </div>
        <div class="col-lg-7" data-reveal style="--d:1">{search_block()}</div>
      </div>
    </div>
  </section>

  <section class="u-py-140 u-py-80-sm" id="encyclopedia" aria-labelledby="enc-title">
    <div class="u-1440 ins-wrap">
      {sec_head("Dental Encyclopedia", '<span id="enc-title">진료 분야별 치아백과</span>', "상담에서 자주 듣는 말 20개를 진료 분야별로 정리했습니다. 용어를 누르면 쉬운 설명으로 이어집니다.", ("치아백과 전체 보기", B + "/knowledge/"))}
      <div class="g-cols-1 g-cols-2-md g-cols-3-lg u-gap-24">
          {cat_cards(soft=True)}
      </div>
    </div>
  </section>

  <section class="ins-section-alt u-py-140 u-py-80-sm" id="columns" aria-labelledby="col-title">
    <div class="u-1440 ins-wrap">
      {sec_head("Doctor's Column", '<span id="col-title">원장이 직접 설명하는 진료 이야기</span>', "", ("칼럼 전체 보기", B + "/columns/"))}
      <div class="g-cols-1 g-cols-3-lg u-gap-32">
          {col_cards()}
      </div>
      <div class="row g-5 u-mt-120 u-mt-48-sm">
        <div class="col-lg-4" data-reveal>
          <h3 class="t-fs-32 t-fs-24-sm fw-700 u-lh-13 m-0">상담 전에<br>읽어보세요</h3>
          <p class="c-fs-16 ins-muted u-mt-16 m-0">진료실에서 무엇을 물어볼지 미리 정리하면 상담 시간을 알차게 쓸 수 있습니다.</p>
        </div>
        <div class="col-lg-8" data-reveal style="--d:1">{guides()}</div>
      </div>
    </div>
  </section>

  <section class="u-py-140 u-py-80-sm" aria-labelledby="space-title">
    <div class="u-1440 ins-wrap">
      {sec_head("Our Space", '<span id="space-title">편하게 묻고, 충분히 듣는 공간</span>')}
      <div class="row g-4">
        <div class="col-lg-7" data-reveal>
          <figure class="ins-card m-0"><div class="ph u-ratio-4-3"><img src="assets/img/{SPACES[0][0]}" alt="{SPACES[0][3]}" width="1600" height="1067" loading="lazy"></div>
            <figcaption><h3 class="t-fs-24 fw-700 m-0">{SPACES[0][1]}</h3><p class="c-fs-16 ins-muted u-mt-8 m-0">{SPACES[0][2]}</p></figcaption></figure>
        </div>
        <div class="col-lg-5 d-flex flex-column u-gap-32">
          <figure class="ins-card m-0" data-reveal style="--d:1"><div class="ph u-ratio-16-9"><img src="assets/img/{SPACES[1][0]}" alt="{SPACES[1][3]}" width="1600" height="900" loading="lazy"></div>
            <figcaption><h3 class="t-fs-24 fw-700 m-0">{SPACES[1][1]}</h3><p class="c-fs-16 ins-muted u-mt-8 m-0">{SPACES[1][2]}</p></figcaption></figure>
          <figure class="ins-card m-0" data-reveal style="--d:2"><div class="ph u-ratio-16-9"><img src="assets/img/{SPACES[2][0]}" alt="{SPACES[2][3]}" width="1600" height="900" loading="lazy"></div>
            <figcaption><h3 class="t-fs-24 fw-700 m-0">{SPACES[2][1]}</h3><p class="c-fs-16 ins-muted u-mt-8 m-0">{SPACES[2][2]}</p></figcaption></figure>
        </div>
      </div>
    </div>
  </section>

  <section class="ins-section-alt u-py-140 u-py-80-sm" id="doctors" aria-labelledby="doc-title">
    <div class="u-1440 ins-wrap">
      {sec_head("Doctors", '<span id="doc-title">서울이도치과 의료진</span>', "전문의 자격과 진료분야를 나누어 안내합니다. 원장별 진료일은 병원에 확인해 주세요.", ("의료진 약력 보기", B + "/doctors/"))}
      <div class="g-cols-2 g-cols-4-lg u-gap-24 u-gap-12-sm">
          {doctor_cards()}
      </div>
    </div>
  </section>

  <section class="u-py-140 u-py-80-sm" id="visit" aria-labelledby="visit-title">
    <div class="u-1440 ins-wrap">
      <div class="row g-5">
        <div class="col-lg-6" data-reveal>
          
          <h2 id="visit-title" class="t-fs-48 t-fs-28-sm fw-700 u-lh-125 m-0">월·목은 저녁 8시 30분까지<br>진료합니다</h2>
          <p class="ins-status u-mt-24 u-mb-24 m-0"><span class="ins-dot" aria-hidden="true"></span><span data-status>진료시간 확인 중</span></p>
          {hours_table()}
        </div>
        <div class="col-lg-6" data-reveal style="--d:1">
          <div class="ins-panel ins-section-alt">
            {visit_info()}
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="ins-section-alt u-py-140 u-py-80-sm" id="faq" aria-labelledby="faq-title">
    <div class="u-1440 ins-wrap">
      <div class="row g-5">
        <div class="col-lg-4" data-reveal>
          
          <h2 id="faq-title" class="t-fs-48 t-fs-28-sm fw-700 u-lh-125 m-0">상담 전에<br>많이 묻는 것</h2>
          <p class="c-fs-14 ins-muted u-mt-24 m-0">글은 일반 정보이며, 개인의 진단과 치료를 대신하지 않습니다.</p>
        </div>
        <div class="col-lg-8 ins-faq" data-reveal style="--d:1">
            {faq_list()}
        </div>
      </div>
    </div>
  </section>
</main>
""" + footer() + dock()


# ---------------------------------------------------------------- B · Night Studio
def page_b():
    rows = []
    for i, (name, en, desc, terms) in enumerate(CATS):
        t = "".join(f'<a href="{B}/knowledge/{s}/">{n}</a>' for n, s in terms)
        rows.append(f"""<div class="cat-row" data-reveal>
            <span class="no">{en}</span>
            <div><h3 class="t-fs-28 t-fs-20-sm m-0">{name}</h3><p class="c-fs-14 ins-muted u-mt-8 m-0">{desc}</p></div>
            <div class="terms c-fs-18 c-fs-16-sm">{t}</div>
          </div>""")
    feats = []
    for i, (img, who, title, desc, href) in enumerate(COLUMNS):
        feats.append(f"""<a class="feature-b{' flip' if i % 2 else ''} d-grid" href="{B}{href}" data-reveal>
          <div class="ph"><img src="assets/img/{img}" alt="{who} 인터뷰 장면" width="1200" height="801" loading="lazy"></div>
          <div>
            <h3 class="t-fs-40 t-fs-24-sm fw-300 u-lh-13 m-0">{title}</h3>
            <p class="c-fs-18 c-fs-16-sm ins-body u-mt-24 m-0">{desc}</p>
            <p class="c-fs-14 ins-muted u-mt-24 m-0">{who}</p>
            <span class="ins-more d-inline-flex u-gap-8 u-mt-32 c-fs-16 fw-500">칼럼 읽기 <span class="ins-arrow" aria-hidden="true">→</span></span>
          </div>
        </a>""")
    return head("b", "서울이도치과 닥터인사이트 | 시안 B · Night Studio") + header("b") + f"""
<main id="top">
  <section class="ins-hero hero-b" aria-labelledby="hero-title">
    <video autoplay muted loop playsinline preload="auto" poster="assets/video/film-poster.jpg" aria-hidden="true"><source src="assets/video/film-loop.webm" type="video/webm"><source src="assets/video/film-loop.mp4" type="video/mp4"></video>
    <div class="scrim" aria-hidden="true"></div>
    <div class="inner u-1440 ins-wrap">
      <h1 id="hero-title" class="m-0" data-rise style="--d:0"><span class="kicker">마포·공덕역 서울이도치과 닥터인사이트</span>치료보다 먼저,<br>이해할 수 있도록</h1>
      <div class="row g-4 align-items-end u-mt-40">
        <div class="col-lg-6" data-rise style="--d:1"><p class="hero-lead c-fs-20 c-fs-16-sm u-lh-17 m-0">마포·공덕역 서울이도치과 의료진이 진료실에서 다 하지 못한 설명을 치아백과와 원장 칼럼으로 정리했습니다.</p></div>
        <div class="col-lg-6 d-flex justify-content-lg-end" data-rise style="--d:2">
          <div class="d-flex flex-wrap u-gap-12">
            <a class="u-btn u-btn-main u-btn-lg" href="{BOOK}" target="_blank" rel="noopener">네이버 예약하기</a>
            <a class="u-btn u-btn-outline u-btn-lg" href="tel:027062080">02-706-2080</a>
          </div>
        </div>
      </div>
    </div>
    <div class="band u-1440 ins-wrap" data-rise style="--d:3">
      <ul>
        <li><small>오늘 진료</small><strong class="d-flex align-items-center u-gap-8"><span class="ins-dot" aria-hidden="true"></span><span data-status>09:30 – 18:30</span></strong></li>
        <li><small>야간 진료</small><strong>월·목 저녁 8시 30분까지</strong></li>
        <li><small>오시는 길</small><strong>공덕역 5·6번 출구 도보 3분</strong></li>
      </ul>
    </div>
  </section>

  <section class="u-py-140 u-py-80-sm" aria-labelledby="way-title">
    <div class="u-1440 ins-wrap">
      <h2 id="way-title" class="visually-hidden">진료를 대하는 방식</h2>
      <p class="statement-b t-fs-48 t-fs-24-sm fw-300 u-lh-14 m-0" data-reveal>치아 상태만 보지 않습니다. 불편했던 시간과 치료에 대한 걱정까지 먼저 듣고, 사진과 모형으로 설명한 뒤 함께 결정합니다.</p>
      <div class="g-cols-1 g-cols-3-lg u-gap-48 u-gap-24-sm u-mt-80 u-mt-48-sm">
        <div data-reveal style="--d:0"><h3 class="t-fs-24 fw-300 m-0">충분히 듣기</h3><p class="c-fs-16 ins-muted u-mt-12 m-0">언제부터, 어디가, 어떻게 불편한지부터 묻습니다.</p></div>
        <div data-reveal style="--d:1"><h3 class="t-fs-24 fw-300 m-0">쉽게 설명하기</h3><p class="c-fs-16 ins-muted u-mt-12 m-0">X-ray와 모형을 함께 보며 지금 상태를 보여드립니다.</p></div>
        <div data-reveal style="--d:2"><h3 class="t-fs-24 fw-300 m-0">함께 결정하기</h3><p class="c-fs-16 ins-muted u-mt-12 m-0">치료 방법과 순서는 환자와 상의해서 정합니다.</p></div>
      </div>
    </div>
  </section>

  <section class="ins-section-alt u-py-120 u-py-80-sm" aria-labelledby="search-title">
    <div class="u-1440 ins-wrap">
      <div class="row g-5">
        <div class="col-lg-5" data-reveal><h2 id="search-title" class="t-fs-48 t-fs-28-sm u-lh-125 m-0">진료실에서 들은 말을<br>찾아보세요</h2></div>
        <div class="col-lg-7" data-reveal style="--d:1">{search_block()}</div>
      </div>
    </div>
  </section>

  <section class="u-py-140 u-py-80-sm" id="encyclopedia" aria-labelledby="enc-title">
    <div class="u-1440 ins-wrap">
      {sec_head("Dental Encyclopedia", '<span id="enc-title">진료 분야별 치아백과</span>', "", ("치아백과 전체 보기", B + "/knowledge/"))}
      <div class="cat-list">
          {chr(10).join(rows)}
      </div>
    </div>
  </section>

  <section class="u-py-140 u-py-80-sm" id="columns" aria-labelledby="col-title">
    <div class="u-1440 ins-wrap">
      {sec_head("Doctor's Column", '<span id="col-title">원장이 말하는 진료의 기준</span>', "", ("칼럼 전체 보기", B + "/columns/"))}
      {chr(10).join(feats)}
    </div>
  </section>

  <section class="craft-b" aria-labelledby="craft-title">
    <img src="assets/img/lab.jpg" alt="원내 기공실에서 보철물을 다듬는 치과기공사" width="1600" height="900" loading="lazy">
    <div class="scrim" aria-hidden="true"></div>
    <div class="inner u-1440 ins-wrap w-100">
      <div class="row g-4 align-items-end">
        <div class="col-lg-7" data-reveal><h2 id="craft-title" class="t-fs-56 t-fs-32-sm u-lh-12 m-0">보철물 뒤의 사람과 과정,<br>원내 기공실</h2></div>
        <p class="craft-text col-lg-5 c-fs-18 c-fs-16-sm m-0" data-reveal style="--d:1">보철물을 병원 안에서 만들고 다듬어, 진료실과 기공실이 바로 의견을 주고받습니다. 모양과 씹는 느낌을 함께 맞춰 갑니다.</p>
      </div>
    </div>
  </section>

  <section class="u-py-140 u-py-80-sm" id="doctors" aria-labelledby="doc-title">
    <div class="u-1440 ins-wrap">
      {sec_head("Doctors", '<span id="doc-title">서울이도치과 의료진</span>', "전문의 자격과 진료분야를 나누어 안내합니다.", ("의료진 약력 보기", B + "/doctors/"))}
      <div class="g-cols-2 g-cols-4-lg u-gap-24 u-gap-12-sm">
          {doctor_cards()}
      </div>
    </div>
  </section>

  <section class="ins-section-alt u-py-140 u-py-80-sm" id="visit" aria-labelledby="visit-title">
    <div class="u-1440 ins-wrap">
      <div class="row g-5">
        <div class="col-lg-6" data-reveal>
          
          <h2 id="visit-title" class="t-fs-48 t-fs-28-sm u-lh-125 m-0">월·목은 저녁 8시 30분까지</h2>
          <p class="ins-status u-mt-24 u-mb-24 m-0"><span class="ins-dot" aria-hidden="true"></span><span data-status>진료시간 확인 중</span></p>
          {hours_table()}
        </div>
        <div class="col-lg-6" data-reveal style="--d:1"><div class="ins-panel panel-base">{visit_info()}</div></div>
      </div>
    </div>
  </section>

  <section class="u-py-140 u-py-80-sm" id="faq" aria-labelledby="faq-title">
    <div class="u-1440 ins-wrap">
      <div class="row g-5">
        <div class="col-lg-4" data-reveal><h2 id="faq-title" class="t-fs-48 t-fs-28-sm u-lh-125 m-0">상담 전에<br>많이 묻는 것</h2></div>
        <div class="col-lg-8 ins-faq" data-reveal style="--d:1">
            {faq_list()}
        </div>
      </div>
    </div>
  </section>
</main>
""" + footer() + dock()


# ---------------------------------------------------------------- C · Lounge
def page_c():
    return head("c", "서울이도치과 닥터인사이트 | 시안 C · Lounge") + header("c") + f"""
<main id="top">
  <section class="ins-hero hero-c" aria-labelledby="hero-title">
    <div class="u-1440 ins-wrap">
      <div class="grid">
        <div>
          <h1 id="hero-title" class="t-fs-72 t-fs-36-sm u-lh-125 m-0" data-rise style="--d:0">{H1}</h1>
          <p class="c-fs-20 c-fs-16-sm ins-body u-lh-17 u-mt-32 u-mt-24-sm m-0 ins-measure" data-rise style="--d:1">{lead_text()}</p>
          <div data-rise style="--d:2">{cta_buttons('u-mt-40')}</div>
          <div class="u-mt-48" data-rise style="--d:3">{facts()}</div>
        </div>
        <div class="stack">
          <figure class="arch m-0"><img src="assets/img/lounge.jpg" alt="서울이도치과 라운지" width="1600" height="900" class="pos-lounge"></figure>
          <figure class="round m-0" data-rise style="--d:4"><img src="assets/img/consult-won.jpg" alt="환자와 상담하는 원소윤 수석원장" width="1600" height="1067" class="pos-won"></figure>
        </div>
      </div>
    </div>
  </section>

  <section class="u-pb-140 u-pb-80-sm" aria-labelledby="search-title">
    <div class="u-1440 ins-wrap">
      <div class="ins-section-alt u-round-50 u-p-80 u-p-24-sm">
        <div class="row g-5 align-items-center">
          <div class="col-lg-5" data-reveal><h2 id="search-title" class="t-fs-44 t-fs-28-sm u-lh-13 m-0">진료실에서 들은 말,<br>천천히 찾아보세요</h2>
            <p class="c-fs-18 c-fs-16-sm ins-body u-mt-16 m-0">치료 이름을 몰라도 괜찮아요. 불편한 증상으로 시작해도 됩니다.</p></div>
          <div class="col-lg-7" data-reveal style="--d:1">{search_block()}</div>
        </div>
      </div>
    </div>
  </section>

  <section class="u-pb-140 u-pb-80-sm" id="encyclopedia" aria-labelledby="enc-title">
    <div class="u-1440 ins-wrap">
      {sec_head("치아백과", '<span id="enc-title">진료 분야별로 읽어보기</span>', "상담에서 자주 듣는 말 20개를 진료 분야별로 정리했습니다.", ("치아백과 전체 보기", B + "/knowledge/"))}
      <div class="g-cols-1 g-cols-2-md g-cols-3-lg u-gap-24">
          {cat_cards()}
      </div>
    </div>
  </section>

  <section class="ins-section-alt u-py-140 u-py-80-sm" aria-labelledby="space-title">
    <div class="u-1440 ins-wrap">
      <div class="row g-5 align-items-center">
        <div class="col-lg-5" data-reveal>
          
          <h2 id="space-title" class="t-fs-48 t-fs-28-sm u-lh-125 m-0">긴장을 내려놓는 데서<br>진료가 시작됩니다</h2>
          <div class="d-flex flex-column u-gap-24 u-mt-48">
            <div><h3 class="t-fs-22 m-0">{SPACES[0][1]}</h3><p class="c-fs-16 ins-body u-mt-8 m-0">{SPACES[0][2]}</p></div>
            <div><h3 class="t-fs-22 m-0">{SPACES[1][1]}</h3><p class="c-fs-16 ins-body u-mt-8 m-0">{SPACES[1][2]}</p></div>
            <div><h3 class="t-fs-22 m-0">{SPACES[2][1]}</h3><p class="c-fs-16 ins-body u-mt-8 m-0">{SPACES[2][2]}</p></div>
          </div>
        </div>
        <div class="col-lg-7">
          <div class="row g-3">
            <div class="col-12" data-reveal><div class="ins-card"><div class="ph u-ratio-16-9"><img src="assets/img/{SPACES[0][0]}" alt="{SPACES[0][3]}" width="1600" height="1067" loading="lazy"></div></div></div>
            <div class="col-6" data-reveal style="--d:1"><div class="ins-card"><div class="ph u-ratio-1-1"><img src="assets/img/{SPACES[1][0]}" alt="{SPACES[1][3]}" width="1600" height="900" loading="lazy"></div></div></div>
            <div class="col-6" data-reveal style="--d:2"><div class="ins-card"><div class="ph u-ratio-1-1"><img src="assets/img/model-hands.jpg" alt="치아 모형으로 설명하는 손" width="1000" height="1500" loading="lazy"></div></div></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="u-py-140 u-py-80-sm" id="columns" aria-labelledby="col-title">
    <div class="u-1440 ins-wrap">
      {sec_head("원장 칼럼", '<span id="col-title">원장이 들려주는 진료 이야기</span>', "", ("칼럼 전체 보기", B + "/columns/"))}
      <div class="g-cols-1 g-cols-3-lg u-gap-32">
          {col_cards()}
      </div>
      <div class="ins-section-alt u-round-40 u-p-64 u-p-24-sm u-mt-80 u-mt-48-sm">
        <div class="row g-5">
          <div class="col-lg-4" data-reveal><h3 class="t-fs-32 t-fs-24-sm u-lh-13 m-0">상담 전에<br>읽어보세요</h3><p class="c-fs-16 ins-body u-mt-16 m-0">물어볼 것을 미리 적어 오시면 상담 시간을 알차게 쓸 수 있어요.</p></div>
          <div class="col-lg-8" data-reveal style="--d:1">{guides()}</div>
        </div>
      </div>
    </div>
  </section>

  <section class="u-pb-140 u-pb-80-sm" id="doctors" aria-labelledby="doc-title">
    <div class="u-1440 ins-wrap">
      {sec_head("의료진", '<span id="doc-title">서울이도치과 의료진</span>', "전문의 자격과 진료분야를 나누어 안내합니다.", ("의료진 약력 보기", B + "/doctors/"))}
      <div class="g-cols-2 g-cols-4-lg u-gap-24 u-gap-12-sm">
          {doctor_cards()}
      </div>
    </div>
  </section>

  <section class="u-pb-140 u-pb-80-sm" id="visit" aria-labelledby="visit-title">
    <div class="u-1440 ins-wrap">
      <div class="ins-section-alt u-round-50 u-p-80 u-p-24-sm">
        <div class="row g-5">
          <div class="col-lg-6" data-reveal>
            
            <h2 id="visit-title" class="t-fs-44 t-fs-28-sm u-lh-13 m-0">퇴근 후에도 들르실 수 있게,<br>월·목은 저녁 8시 30분까지</h2>
            <p class="ins-status u-mt-24 u-mb-24 m-0"><span class="ins-dot" aria-hidden="true"></span><span data-status>진료시간 확인 중</span></p>
            {hours_table()}
          </div>
          <div class="col-lg-6" data-reveal style="--d:1"><div class="ins-panel panel-light">{visit_info()}</div></div>
        </div>
      </div>
    </div>
  </section>

  <section class="u-pb-140 u-pb-80-sm" id="faq" aria-labelledby="faq-title">
    <div class="u-1440 ins-wrap">
      <div class="row g-5">
        <div class="col-lg-4" data-reveal><h2 id="faq-title" class="t-fs-44 t-fs-28-sm u-lh-13 m-0">상담 전에<br>많이 묻는 것</h2></div>
        <div class="col-lg-8 ins-faq" data-reveal style="--d:1">
            {faq_list()}
        </div>
      </div>
    </div>
  </section>
</main>
""" + footer() + dock()


def index_page():
    cards = [("a-clinic-white.html", "A · Clinic White", "밝고 깨끗한 프리미엄 클리닉. 실제 상담 영상과 정돈된 정보 타일"),
             ("b-night-studio.html", "B · Night Studio", "브랜드 필름을 깐 다크 하이엔드. 원내 기공실과 장인정신"),
             ("c-lounge.html", "C · Lounge", "아이보리와 월넛, 아치형 사진의 호텔 라운지 톤")]
    items = "".join(f'<a class="ins-card" href="{h}"><div class="ph u-ratio-16-9"><img src="previews/{h.split(".")[0]}-fold.jpg" alt="{t} 첫 화면" loading="lazy"></div><h2 class="t-fs-24 fw-700 m-0">{t}</h2><p class="c-fs-16 ins-muted m-0">{d}</p></a>' for h, t, d in cards)
    return head("a", "닥터인사이트 리뉴얼 시안 v3") + f"""
<main class="u-1440 ins-wrap u-py-120 u-py-80-sm">
  <h1 class="t-fs-48 t-fs-28-sm fw-700 m-0">서울이도치과 닥터인사이트 · 리뉴얼 시안 v3</h1>
  <p class="c-fs-18 ins-body u-mt-16 u-mb-48 m-0">같은 콘텐츠와 setting.css 체계로 만든 세 가지 톤입니다. 각 시안을 눌러 보세요.</p>
  <div class="g-cols-1 g-cols-3-lg u-gap-32">{items}</div>
</main>
<script src="js/insight.js"></script>
</body>
</html>
"""


if __name__ == "__main__":
    (ROOT / "a-clinic-white.html").write_text(page_a(), encoding="utf-8")
    (ROOT / "b-night-studio.html").write_text(page_b(), encoding="utf-8")
    (ROOT / "c-lounge.html").write_text(page_c(), encoding="utf-8")
    (ROOT / "index.html").write_text(index_page(), encoding="utf-8")
    print("built")
