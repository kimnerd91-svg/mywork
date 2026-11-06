"""시안 v3 서브페이지 + 테마 폴더 출력.  python3 sub.py
메인(build.py)과 서브 5종을 a/ b/ c/ 폴더로 내보낸다. 공용 css·js·assets는 루트에 둔다.
"""
import re
from pathlib import Path
import build as m

ROOT = Path(__file__).parent
B, BOOK, MAP = m.B, m.BOOK, m.MAP
THEMES = {"a": "Clinic White", "b": "Night Studio", "c": "Lounge"}
NAV = [("치아백과", "knowledge.html"), ("원장 칼럼", "column.html"), ("의료진", "doctors.html"), ("진료시간·오시는 길", "visit.html")]


# ---------------------------------------------------------------- 헤더: 서브페이지로 연결
def header(theme):
    h = m.header(theme)
    for (t, old) in [("치아백과", "#encyclopedia"), ("원장 칼럼", "#columns"), ("의료진", "#doctors"), ("진료시간·오시는 길", "#visit")]:
        new = dict(NAV)[t]
        h = h.replace(f'<a href="{old}">{t}</a>', f'<a href="{new}">{t}</a>')
    h = h.replace('<a href="#faq">자주 묻는 질문</a>', '<a href="index.html">메인</a>')
    return h.replace('class="ins-logo" href="#top"', 'class="ins-logo" href="index.html"')


def relink(html):
    """원본 사이트 링크 중 시안에 있는 페이지는 시안 페이지로."""
    for a, b in [(f'{B}/knowledge/dental-implant/', 'knowledge.html#dental-implant'), (f'{B}/knowledge/"', 'knowledge.html"'),
                 (f'{B}/columns/attention-to-one-patient/', 'column.html'), (f'{B}/doctors/"', 'doctors.html"'),
                 (f'{B}/visit/"', 'visit.html"')]:
        html = html.replace(a, b)
    html = html.replace('knowledge.html#dental-implant', 'knowledge-implant.html')
    return html


def to_folder(html):
    return re.sub(r'(href|src|poster)="(css|assets|js)/', r'\1="../\2/', html)


def page(theme, title, body, current=""):
    h = m.head(theme, f"{title} | 서울이도치과 닥터인사이트 · 시안 {theme.upper()}")
    hd = header(theme)
    if current:
        hd = hd.replace(f'<a href="{current}">', f'<a href="{current}" aria-current="page">')
    return to_folder(relink(h + hd + body + m.footer() + m.dock()))


# ---------------------------------------------------------------- 서브 비주얼 (테마별 구성)
def sub_hero(theme, crumbs, title, lead, img, alt, meta="", pos="50% 50%"):
    cr = "".join(f'<li><a href="{h}">{t}</a></li>' if h else f'<li aria-current="page">{t}</li>' for t, h in crumbs)
    crumb = f'<nav aria-label="현재 위치"><ol class="ins-crumb">{cr}</ol></nav>'
    meta_html = f'<p class="sub-meta c-fs-14 m-0">{meta}</p>' if meta else ''
    if theme == "b":
        return f"""
<main id="top">
  <section class="sub-hero sub-hero-b" aria-labelledby="page-title">
    <img src="assets/img/{img}" alt="{alt}" width="1600" height="1067" data-pos="{pos}">
    <div class="scrim" aria-hidden="true"></div>
    <div class="inner u-1440 ins-wrap">
      <div data-rise style="--d:0">{crumb}</div>
      <h1 id="page-title" class="m-0" data-rise style="--d:1">{title}</h1>
      <p class="sub-lead c-fs-20 c-fs-16-sm u-lh-17 m-0" data-rise style="--d:2">{lead}</p>
      <div data-rise style="--d:3">{meta_html}</div>
    </div>
  </section>"""
    shape = "arch" if theme == "c" else "frame"
    return f"""
<main id="top">
  <section class="sub-hero sub-hero-{theme}" aria-labelledby="page-title">
    <div class="u-1440 ins-wrap">
      <div class="grid">
        <div>
          <div data-rise style="--d:0">{crumb}</div>
          <h1 id="page-title" class="m-0" data-rise style="--d:1">{title}</h1>
          <p class="sub-lead c-fs-20 c-fs-16-sm u-lh-17 m-0" data-rise style="--d:2">{lead}</p>
          <div data-rise style="--d:3">{meta_html}</div>
        </div>
        <figure class="{shape} m-0" data-rise style="--d:2"><img src="assets/img/{img}" alt="{alt}" width="1600" height="1067" data-pos="{pos}"></figure>
      </div>
    </div>
  </section>"""


def cta_band(title="읽은 뒤에는, 상담에서 확인하세요", text="같은 증상도 원인이 다를 수 있습니다. 궁금한 점을 정리해 오시면 진료실에서 함께 확인합니다."):
    return f"""
  <section class="u-pb-140 u-pb-80-sm">
    <div class="u-1440 ins-wrap">
      <div class="cta-band" data-reveal>
        <div>
          <h2 class="t-fs-40 t-fs-28-sm u-lh-13 m-0">{title}</h2>
          <p class="c-fs-18 c-fs-16-sm u-mt-16 m-0">{text}</p>
        </div>
        <div class="d-flex flex-wrap u-gap-12">
          <a class="u-btn u-btn-main u-btn-lg" href="{BOOK}" target="_blank" rel="noopener">네이버 예약하기</a>
          <a class="u-btn u-btn-outline u-btn-lg" href="tel:027062080">전화 02-706-2080</a>
        </div>
      </div>
    </div>
  </section>"""


# ---------------------------------------------------------------- 1. 치아백과 목록
TERMS = [
    ("임플란트·발치", "치과임플란트", "dental-implant", "치아가 없는 부위의 턱뼈에 인공치근을 심고 상부 보철물을 연결하는 치료입니다."),
    ("임플란트·발치", "골이식", "bone-grafting", "임플란트 등을 계획할 때 부족한 치조골을 보완하기 위해 고려하는 술식입니다."),
    ("임플란트·발치", "사랑니", "wisdom-tooth", "가장 뒤쪽에서 나오는 세 번째 큰어금니로 위치와 주변 상태에 따라 관리가 달라집니다."),
    ("보철·수복", "치과 크라운", "dental-crown", "남아 있는 치아를 덮어 형태와 기능을 보완하는 고정성 보철물입니다."),
    ("보철·수복", "인레이·온레이", "inlay-onlay", "치아 일부를 본떠 제작한 수복물을 붙여 결손 부위를 보완하는 치료입니다."),
    ("보철·수복", "치과 브리지", "dental-bridge", "빠진 치아 양옆의 치아 등을 지지대로 사용해 결손 부위를 연결하는 고정성 보철입니다."),
    ("보철·수복", "틀니", "dentures", "여러 개의 치아가 없을 때 끼웠다 뺄 수 있도록 제작하는 보철물입니다."),
    ("보존·신경치료", "치아우식증", "tooth-decay", "구강 내 세균이 만든 산으로 치아 조직이 손상되는 질환입니다."),
    ("보존·신경치료", "초기 충치", "", "치아 표면의 무기질이 빠지기 시작했지만 아직 뚜렷한 구멍이 생기지 않은 초기 우식과 관리 방법입니다."),
    ("보존·신경치료", "인접면 충치", "", "칫솔이 닿기 어려운 치아 사이의 우식이 어떻게 발견되고 어떤 검사가 필요한지 정리합니다."),
    ("보존·신경치료", "2차 충치", "", "기존 수복물 가장자리에 생기는 우식의 의미와 검사·치료 판단 기준입니다."),
    ("보존·신경치료", "근관치료", "root-canal-treatment", "치아 안쪽의 감염되거나 손상된 치수 조직을 제거하고 내부를 세척·충전하는 치료입니다."),
    ("보존·신경치료", "복합레진", "composite-resin", "치아색 재료를 치아에 접착해 작은 결손이나 충치 부위를 수복하는 방법입니다."),
    ("잇몸·예방", "치주염", "periodontitis", "치아를 지지하는 잇몸과 주변 조직에 염증이 진행된 상태를 말합니다."),
    ("잇몸·예방", "스케일링", "scaling", "칫솔질로 제거하기 어려운 치석과 침착물을 기구로 제거하는 처치입니다."),
    ("교정·성장", "투명교정장치", "clear-aligners", "치아 이동을 위해 단계별로 교체해 착용하는 투명한 가철성 교정장치입니다."),
    ("교정·성장", "성장기교정", "growth-orthodontics", "성장 중인 어린이의 치열과 턱 성장 상태를 살펴 필요한 시기와 방법을 정하는 교정 진료입니다."),
    ("교정·성장", "교정 유지장치", "orthodontic-retainers", "교정치료 후 치아가 이동한 위치에 적응하도록 돕는 고정식 또는 가철식 장치입니다."),
    ("턱관절·구강외과", "턱관절장애", "temporomandibular-disorder", "턱관절이나 씹는 근육에서 통증, 소리, 입 벌리기 제한이 나타나는 상태를 포괄합니다."),
    ("턱관절·구강외과", "이갈이·이악물기", "bruxism", "잠을 자거나 깨어 있을 때 이를 갈거나 강하게 무는 반복 행동입니다."),
    ("증상·통증", "시린이", "tooth-sensitivity", "찬물, 바람, 양치 자극에 짧고 날카로운 통증이 느껴지는 상태를 설명합니다."),
    ("검사·진단", "교합", "occlusion", "입을 다물거나 씹을 때 위아래 치아가 만나는 관계입니다."),
    ("보험·비용", "치과임플란트 건강보험", "dental-implant-insurance", "연령, 치아 상태, 인정 개수와 본인부담 등 일반 급여 기준을 확인합니다."),
]
PATHS = [
    ("빠진 치아, 어떤 방법으로 채울까요?", "각 방법이 무엇을 지지대로 쓰는지 비교하고, 보험 조건은 따로 확인하세요.", ["치과임플란트", "치과 브리지", "틀니", "치과임플란트 건강보험"]),
    ("충치 치료, 얼마나 덮어야 할까요?", "손상 범위에 따라 달라지는 수복 방법을 순서대로 살펴보세요.", ["치아우식증", "복합레진", "인레이·온레이", "치과 크라운"]),
    ("잇몸이 불편하거나 이가 시리다면", "느껴지는 증상에서 시작해 검사와 관리의 차이를 알아보세요.", ["시린이", "치주염", "스케일링"]),
    ("아이의 교정부터 치료 후 관리까지", "상담 시기, 장치 선택과 유지관리를 한 흐름으로 읽어보세요.", ["성장기교정", "투명교정장치", "교정 유지장치"]),
]


def term_href(name):
    for _, n, slug, _ in TERMS:
        if n == name:
            return "knowledge-implant.html" if slug == "dental-implant" else (f"{B}/knowledge/{slug}/" if slug else f"{B}/knowledge/")
    return f"{B}/knowledge/"


def knowledge(theme):
    cats = ["전체"] + list(dict.fromkeys(c for c, *_ in TERMS))
    chips = "".join(f'<button type="button" class="{"is-on" if i == 0 else ""}" data-filter="{c}" aria-pressed="{"true" if i == 0 else "false"}">{c}</button>' for i, c in enumerate(cats))
    cards = "".join(f"""<a class="term-card" href="{term_href(n)}" data-cat="{c}" data-name="{n} {d}">
          <span class="cat">{c}</span><h3 class="t-fs-22 t-fs-20-sm fw-700 m-0">{n}</h3><p class="c-fs-16 m-0">{d}</p><span class="go">설명 읽기 <span class="ins-arrow" aria-hidden="true">→</span></span></a>""" for c, n, slug, d in TERMS)
    paths = "".join(f"""<article class="path" data-reveal style="--d:{i}">
          <h3 class="t-fs-24 t-fs-20-sm fw-700 u-lh-135 m-0">{t}</h3><p class="c-fs-16 u-mt-12 m-0">{d}</p>
          <ol class="path-steps">{"".join(f'<li><a href="{term_href(x)}">{x}</a></li>' for x in steps)}</ol></article>""" for i, (t, d, steps) in enumerate(PATHS))
    body = sub_hero(theme, [("메인", "index.html"), ("치아백과", "")], "서울이도 치아백과",
                    "치과에서 들었지만 정확히 묻지 못했던 말. 치료를 결정하기 전에 뜻과 확인할 질문부터 차분히 알아보세요.",
                    "model-park.jpg", "치아 모형을 들고 보철 상담을 하는 박지현 대표원장", meta=f"용어 {len(TERMS)}개 · 진료 분야 {len(cats) - 1}개", pos="40% 45%") + f"""
  <section class="u-py-120 u-py-80-sm" aria-labelledby="kb-title">
    <div class="u-1440 ins-wrap">
      <div class="row g-5 align-items-end u-mb-48 u-mb-32-sm">
        <div class="col-lg-5" data-reveal><h2 id="kb-title" class="t-fs-40 t-fs-28-sm fw-700 u-lh-13 m-0">어떤 말이 궁금한가요?</h2>
          <p class="c-fs-18 c-fs-16-sm ins-body u-mt-16 m-0">치료명, 증상, 익숙한 표현을 입력해 보세요. ‘치아 씌우기’로 찾아도 크라운이 나옵니다.</p></div>
        <div class="col-lg-7" data-reveal style="--d:1">
          <form class="ins-search" role="search" id="kb-form"><label class="visually-hidden" for="kb-q">용어 검색</label>
            <div class="field"><input id="kb-q" type="search" autocomplete="off" placeholder="예: 신경치료, 씌우기, 잇몸"><button class="u-btn u-btn-main" type="submit">찾기</button></div></form>
        </div>
      </div>
      <div class="kb-filter ins-chips" role="group" aria-label="진료 분야">{chips}</div>
      <p class="kb-count c-fs-14 ins-muted u-mt-24 m-0" aria-live="polite" id="kb-count">용어 {len(TERMS)}개</p>
      <div class="kb-grid u-mt-16" id="kb-grid">{cards}</div>
      <p class="kb-empty c-fs-16 ins-muted" id="kb-empty" hidden>일치하는 항목이 없습니다. 다른 말로 찾아보거나 <a href="{B}/symptoms/">증상으로 찾기</a>를 이용해 주세요.</p>
    </div>
  </section>

  <section class="ins-section-alt u-py-140 u-py-80-sm" aria-labelledby="path-title">
    <div class="u-1440 ins-wrap">
      {m.sec_head("", '<span id="path-title">혼자 고르기 어렵다면, 이 순서로 읽어보세요</span>', "같은 고민에 연결되는 글을 모았습니다. 치료를 정하기 전에 방법의 차이와 확인할 질문을 알아보세요.")}
      <div class="g-cols-1 g-cols-2-md u-gap-24">{paths}</div>
    </div>
  </section>

  <section class="u-py-140 u-py-80-sm" aria-labelledby="use-title">
    <div class="u-1440 ins-wrap">
      <div class="row g-5">
        <div class="col-lg-4" data-reveal><h2 id="use-title" class="t-fs-40 t-fs-28-sm fw-700 u-lh-13 m-0">백과사전은<br>질문을 준비하는 곳입니다</h2></div>
        <div class="col-lg-8">
          <p class="c-fs-18 c-fs-16-sm ins-body m-0" data-reveal>같은 증상도 원인이 다를 수 있습니다. 온라인 설명만으로 스스로 진단하기보다, 상담에서 무엇을 확인할지 정리하는 데 활용하세요.</p>
          <dl class="use-list u-mt-48 m-0">
            <div data-reveal style="--d:0"><dt>한 문장으로 뜻부터</dt><dd>낯선 용어의 핵심 의미를 먼저 설명합니다.</dd></div>
            <div data-reveal style="--d:1"><dt>증상과 치료를 연결해</dt><dd>가능한 원인을 단정하지 않고 확인 과정을 함께 보여드립니다.</dd></div>
            <div data-reveal style="--d:2"><dt>읽은 뒤 질문할 수 있게</dt><dd>진료실에서 확인하면 좋은 질문과 주의 신호를 정리합니다.</dd></div>
          </dl>
        </div>
      </div>
    </div>
  </section>
{cta_band()}
</main>
"""
    return page(theme, "치아백과", body, "knowledge.html")


# ---------------------------------------------------------------- 2. 치아백과 상세 (임플란트)
def knowledge_implant(theme):
    toc = [("role", "인공치근과 보철물은 역할이 다릅니다"), ("exam", "검사에서 치료 순서와 대안을 정합니다"), ("care", "치료가 끝난 뒤에도 관리가 이어집니다"),
           ("compare", "빠진 치아를 채우는 방법 비교"), ("ask", "상담에서 물어보세요"), ("sources", "참고한 자료")]
    toc_html = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    related = [("골이식", "bone-grafting", "임플란트 등을 계획할 때 부족한 치조골을 보완하기 위해 고려하는 술식입니다."),
               ("치과임플란트 건강보험", "dental-implant-insurance", "연령, 치아 상태, 인정 개수와 본인부담 등 일반 급여 기준을 확인합니다."),
               ("치과 브리지", "dental-bridge", "빠진 치아 양옆의 치아 등을 지지대로 사용해 결손 부위를 연결하는 고정성 보철입니다.")]
    rel = "".join(f'<a class="term-card" href="{B}/knowledge/{s}/"><span class="cat">이어서 읽기</span><h3 class="t-fs-20 fw-700 m-0">{n}</h3><p class="c-fs-16 m-0">{d}</p><span class="go">설명 읽기 <span class="ins-arrow" aria-hidden="true">→</span></span></a>' for n, s, d in related)
    body = sub_hero(theme, [("메인", "index.html"), ("치아백과", "knowledge.html"), ("치과임플란트", "")],
                    "빠진 치아를 대신하는 임플란트,<br>무엇부터 확인할까요?",
                    "인공치근을 심는 과정부터 그 위에 치아를 연결하는 과정까지. 치료 범위와 관리 계획을 함께 이해합니다.",
                    "consult-ko.jpg", "상담실에서 진료 자료를 보며 설명하는 고성민 대표원장", meta="임플란트·발치 · 자료 확인 2026.10.06", pos="60% 40%") + f"""
  <div class="u-1440 ins-wrap u-py-120 u-py-80-sm">
    <div class="article-grid">
      <aside class="article-toc" aria-label="이 글의 목차">
        <details open><summary>이 글의 목차</summary><ol>{toc_html}</ol></details>
      </aside>
      <article class="ins-prose">
        <section id="role" aria-labelledby="h-role">
          <h2 id="h-role">인공치근과 보철물은 역할이 다릅니다</h2>
          <p>뼈 속의 임플란트가 지지 기반이 되고, 그 위의 연결부와 보철물이 씹는 부분을 구성합니다. 상담에서는 식립 수술만인지, 연결부와 최종 보철까지 포함한 계획인지 구분해 확인하세요.</p>
          <ol class="layers" aria-label="임플란트의 세 부분 (위에서 아래로)">
            <li><b>보철물</b><span>입안에서 보이고 씹는 기능을 맡는 부분</span></li>
            <li><b>연결부</b><span>인공치근과 보철물을 연결</span></li>
            <li><b>인공치근</b><span>턱뼈에 놓이는 지지 구조</span></li>
          </ol>
        </section>
        <section id="exam" aria-labelledby="h-exam">
          <h2 id="h-exam">검사에서 치료 순서와 대안을 정합니다</h2>
          <p>뼈의 양과 형태, 남은 치아·잇몸의 상태를 확인하고 복용약과 전신질환을 검토합니다. 골이식이나 기존 염증의 치료가 먼저 필요할 수 있으며, 식립과 보철 연결의 간격도 개인마다 다릅니다. 브리지·틀니 등 다른 방법도 함께 비교할 수 있습니다.</p>
          <figure class="prose-figure"><img src="assets/img/xray-ko.jpg" alt="진료 의자 옆 모니터의 X-ray를 가리키며 설명하는 고성민 대표원장" width="960" height="540" loading="lazy"><figcaption>상담실에서 X-ray 화면을 함께 보며 설명합니다. 실제 진단 사례 사진이 아닙니다.</figcaption></figure>
        </section>
        <section id="care" aria-labelledby="h-care">
          <h2 id="h-care">치료가 끝난 뒤에도 관리가 이어집니다</h2>
          <p>임플란트 주변에도 염증이 생길 수 있어 청결 관리와 정기 점검이 필요합니다. 수술에는 출혈·감염·신경 손상 등의 위험이 있고, 뼈와 잘 결합하지 않거나 보철물에 문제가 생길 수도 있습니다. 본인에게 해당하는 위험과 문제 발생 시 대응을 치료 전에 설명받으세요.</p>
        </section>
        <section id="compare" aria-labelledby="h-compare">
          <h2 id="h-compare">빠진 치아를 채우는 방법, 지지 방식이 다릅니다</h2>
          <div class="table-scroll"><table class="compare">
            <caption class="visually-hidden">빠진 치아를 채우는 방법별 지지 구조와 확인할 점</caption>
            <thead><tr><th scope="col">방법</th><th scope="col">무엇이 지지하나요?</th><th scope="col">함께 확인할 점</th></tr></thead>
            <tbody>
              <tr><th scope="row">임플란트</th><td>턱뼈에 놓인 인공치근</td><td>수술 적합성, 뼈와 잇몸 상태, 유지관리</td></tr>
              <tr><th scope="row">치과 브리지</th><td>주변 치아 등의 지지 구조</td><td>지지 치아의 처치 범위와 청소 방법</td></tr>
              <tr><th scope="row">가철성 틀니</th><td>잇몸과 남아 있는 치아 등</td><td>남은 치아 상태, 맞음새와 탈착 관리</td></tr>
            </tbody></table></div>
          <p class="note">구조를 비교한 표입니다. 어느 방법이 적합한지는 남은 치아와 구강 상태를 확인해 결정합니다.</p>
        </section>
        <section id="ask" aria-labelledby="h-ask" class="ask-box">
          <h2 id="h-ask">상담에서 물어보세요</h2>
          <ul>
            <li>브리지나 틀니와 비교했을 때 제 상태에서의 차이는 무엇인가요?</li>
            <li>골이식과 임시치아, 최종 보철까지 치료 범위에 포함되나요?</li>
            <li>집에서 어떤 도구로 관리하고 점검은 어떻게 받나요?</li>
          </ul>
        </section>
        <section id="sources" aria-labelledby="h-sources" class="sources">
          <h2 id="h-sources">참고한 자료</h2>
          <ul>
            <li><a href="https://www.cuh.nhs.uk/" target="_blank" rel="noopener">Cambridge University Hospitals · Dental implants in restorative dentistry</a> — 임플란트 구성, 적용 판단과 유지관리</li>
            <li><a href="https://www.leedsth.nhs.uk/" target="_blank" rel="noopener">Leeds Teaching Hospitals · Dental implants</a> — 임플란트 치료 계획과 대안</li>
          </ul>
          <p class="note">자료 확인일 2026.10.06 · 해외 자료의 비용·보험 제도는 국내에 그대로 적용되지 않습니다. 개인별 진단과 치료 계획은 진료에서 확인하세요.</p>
        </section>
      </article>
      <aside class="article-aside" aria-label="상담 준비">
        <div class="aside-card">
          <h2 class="t-fs-22 fw-700 u-lh-135 m-0">이 글을 읽고<br>상담을 준비한다면</h2>
          <p class="c-fs-16 u-mt-12 m-0">궁금한 점을 메모해 오시면 진료실에서 함께 확인합니다.</p>
          <div class="d-grid u-gap-12 u-mt-24">
            <a class="u-btn u-btn-main" href="{BOOK}" target="_blank" rel="noopener">네이버 예약</a>
            <a class="u-btn u-btn-outline" href="tel:027062080">전화 02-706-2080</a>
          </div>
          <a class="aside-link" href="column.html"><span>원장 칼럼</span>치료를 결정하기 전, 제가 먼저 생각하는 것 <span class="ins-arrow" aria-hidden="true">→</span></a>
        </div>
      </aside>
    </div>
  </div>

  <section class="ins-section-alt u-py-120 u-py-80-sm" aria-labelledby="rel-title">
    <div class="u-1440 ins-wrap">
      {m.sec_head("", '<span id="rel-title">이어서 읽어보세요</span>', "", ("치아백과 전체", "knowledge.html"))}
      <div class="kb-grid">{rel}</div>
    </div>
  </section>
</main>
"""
    return page(theme, "치과임플란트", body, "knowledge.html")


# ---------------------------------------------------------------- 3. 원장 칼럼 상세
COLUMN = [
    ("남길 수 있는 치아를 먼저 생각합니다", [
        "임플란트는 잃은 치아를 대신하는 치료 방법입니다. 턱뼈에 심은 구조물이 인공 치아를 지지하며, 식립 이후의 회복과 보철 단계까지 이어집니다. 저는 이러한 치료를 이야기하는 출발점에서도 현재 남아 있는 치아의 가치를 먼저 생각하고 싶습니다. 임플란트를 할 수 있다는 사실이 곧 지금의 치아를 빼야 하는 이유가 되지는 않습니다.",
        "그렇다고 자연치아라는 이유만으로 무조건 남기는 것이 정답이라고 생각하지는 않습니다. 남길 수 있는지와 남긴 뒤 사용할 수 있는 상태인지는 함께 판단해야 합니다. 치아를 보존하려는 방향과 필요한 치료를 놓치지 않으려는 판단이 균형을 이루어야 합니다.",
        "작은 문제를 발견했다고 곧바로 치료의 크기를 키우기보다 지금 필요한 처치와 관찰할 부분을 구분합니다. 추적관찰을 선택한다면 무엇을 지켜보고, 어떤 변화가 생기면 다시 판단할지도 계획에 있어야 합니다. ‘아직 치료하지 않는다’는 말에도 그에 맞는 진단과 관리의 책임이 따른다고 생각합니다."]),
    ("치과 치료를 받는 것은 치아가 아니라 한 사람입니다", [
        "수술을 계획할 때 입안의 상태만으로 모든 설명이 끝나지는 않습니다. 같은 치과 치료를 앞두고 있어도 전신 건강과 복용 약, 이전 치료 경험에 따라 살펴야 할 조건이 달라집니다. 나이 하나로 가능 여부를 단정하기 어려운 이유입니다.",
        "저는 병력을 확인하는 시간을 진료 앞에 붙는 형식적인 절차로 여기고 싶지 않습니다. 처방약과 일반의약품, 최근의 건강 변화까지 정확히 알아야 필요한 판단을 할 수 있습니다. 환자에게 약을 스스로 끊거나 바꾸게 할 일이 아니라, 의료진이 그 정보를 바탕으로 치료를 계획할 일입니다."]),
    ("두려움도 치료 계획에서 다루어야 합니다", [
        "제가 생각하는 편안한 진료는 환자에게 긴장을 참으라고 요구하는 진료가 아닙니다. 주사에 대한 두려움, 입을 오래 벌리는 부담, 무엇을 하고 있는지 알 수 없을 때의 불안은 서로 다른 경험입니다.",
        "통증이나 불편을 느낄 때 표현할 수 있고, 잠시 쉬어야 할 때 알릴 수 있다는 감각도 중요합니다. 환자가 자신이 겪는 과정을 전할 수 있어야 진료하는 사람도 그 반응을 살필 수 있습니다."]),
    ("좋은 계획은 환자의 생활 안에서 이어져야 합니다", [
        "진료실의 일정표와 환자의 일정표는 다릅니다. 의료진에게 한 번의 내원은 진료 단계이지만, 환자에게는 근무를 조정하고 가족의 도움을 구하며 이동 시간을 확보하는 일입니다.",
        "확정된 일정과 상태를 보며 정할 일정을 구분하는 편이 환자에게 더 정직한 설명이라고 생각합니다. 계획이 달라졌을 때에는 변화 자체보다 왜 달라졌는지를 이해할 수 있는 것이 중요합니다."]),
    ("제가 지키고 싶은 것은 선택의 이유입니다", [
        "좋은 치료를 하나의 시술 이름이나 장비로 설명하기는 어렵습니다. 제게 중요한 것은 진단에서 결정까지의 이유가 이어지는가입니다.",
        "진료실을 나서는 환자에게 ‘왜 이 치료를 선택했는지 이해했다’는 생각이 남는 것. 제가 먼저 지키고 싶은 기준은 거기에 있습니다."]),
]


def column(theme):
    secs = []
    for i, (h, ps) in enumerate(COLUMN):
        p = "".join(f"<p>{x}</p>" for x in ps)
        fig = ""
        if i == 1:
            fig = '<figure class="prose-figure wide"><img src="assets/img/consult-ko.jpg" alt="상담실에서 환자의 이야기를 듣는 고성민 대표원장" width="1600" height="1067" loading="lazy"><figcaption>상담실에서 이야기를 듣는 고성민 대표원장</figcaption></figure>'
        if i == 2:
            fig = '<blockquote class="pull"><p>지금 이 사람에게 필요한 치료와 그 이유를 분명하게 설명하는 치과의사이고 싶습니다.</p></blockquote>'
        if i == 3:
            fig = '<figure class="prose-figure wide"><img src="assets/img/window-ko.jpg" alt="진료실 창가에 선 고성민 대표원장" width="1600" height="1068" loading="lazy"><figcaption>창가에 선 고성민 대표원장</figcaption></figure>'
        secs.append(f'<section aria-labelledby="c{i}"><h2 id="c{i}">{h}</h2>{p}{fig}</section>')
    others = "".join(f'<a class="ins-card" href="{B}{href}"><div class="ph u-ratio-4-3"><img src="assets/img/{img}" alt="{who} 인터뷰 장면" width="1200" height="801" loading="lazy"></div><span class="who">{who}</span><h3 class="t-fs-22 fw-700 u-lh-135 m-0">{t}</h3></a>' for img, who, t, d, href in m.COLUMNS[1:])
    body = sub_hero(theme, [("메인", "index.html"), ("원장 칼럼", ""), ("치료를 선택하는 기준", "")],
                    "치료를 결정하기 전,<br>제가 먼저 생각하는 것",
                    "저는 치료 이름보다 그 치료가 필요한 이유를 먼저 생각합니다. 치아의 상태, 몸의 건강, 치료를 이어갈 생활까지 한 사람의 계획 안에 담고 싶습니다.",
                    "col-ko.jpg", "인터뷰 중인 고성민 대표원장", meta="고성민 대표원장 · 편집 칼럼 · 읽는 시간 약 7분", pos="58% 40%") + f"""
  <div class="u-1440 ins-wrap u-py-120 u-py-80-sm">
    <div class="ins-prose column-prose">
      <div class="summary" data-reveal>
        <h2 class="t-fs-20 fw-700 m-0">이 글에서 읽는 것</h2>
        <ul><li>자연치아를 남길 가능성과 치료 시기를 함께 판단하기</li><li>수술·진정치료 전에 몸의 상태와 두려움 살피기</li><li>치료 이후의 생활까지 이어지는 계획 세우기</li></ul>
      </div>
      <p class="dek">저는 치료 계획을 생각할 때 ‘무엇을 할 수 있는가’보다 ‘왜 지금 이 치료가 필요한가’를 먼저 묻고 싶습니다. 치료의 이름은 같아도 그 선택을 받아들이는 사정은 한 사람씩 다르기 때문입니다.</p>
      {"".join(secs)}
      <div class="author" data-reveal>
        <img src="assets/img/dr-ko.jpg" alt="고성민 대표원장" width="900" height="1125" loading="lazy">
        <div><p class="c-fs-14 ins-muted m-0">글쓴이</p><h2 class="t-fs-24 fw-700 u-mt-8 m-0">고성민 <small>대표원장</small></h2>
          <p class="c-fs-16 u-mt-8 m-0">임플란트 수술 · 진정치료 · 턱관절·구강외과</p><a class="aside-inline" href="doctors.html">의료진 소개 보기 <span class="ins-arrow" aria-hidden="true">→</span></a></div>
      </div>
      <section class="sources" aria-labelledby="col-src">
        <h2 id="col-src">칼럼 구성과 참고 자료</h2>
        <p class="note">의료진의 진료 분야와 병원의 진료 철학을 바탕으로 편집부가 구성한 1인칭 칼럼입니다.</p>
        <ul>
          <li>서울이도치과의원 · 브랜드 가이드 — 병원 제공 이름·가치·진료 철학</li>
          <li><a href="https://www.ada.org/" target="_blank" rel="noopener">미국치과의사협회 ADA · Implants</a> — 임플란트의 구조와 치료 단계</li>
          <li><a href="https://www.ada.org/" target="_blank" rel="noopener">ADA · Medications and Oral Health</a> — 복용 약과 건강 변화를 의료진에게 알리기</li>
          <li><a href="https://www.ada.org/" target="_blank" rel="noopener">ADA · Anxiety</a> — 치과 방문의 불안을 알리고 쉬는 신호 정하기</li>
        </ul>
      </section>
    </div>
  </div>

  <section class="ins-section-alt u-py-120 u-py-80-sm" aria-labelledby="more-title">
    <div class="u-1440 ins-wrap">
      {m.sec_head("", '<span id="more-title">다른 원장의 칼럼</span>', "", ("치아백과로 가기", "knowledge.html"))}
      <div class="g-cols-1 g-cols-2-md u-gap-32">{others}</div>
    </div>
  </section>
</main>
"""
    return page(theme, "원장 칼럼", body, "column.html")


# ---------------------------------------------------------------- 4. 의료진
DOC_DETAIL = {
    "고성민": ("임플란트 수술, 진정치료, 턱관절·구강외과 진료", [("임플란트 상담 준비", f"{B}/guides/gongdeok-implant-consultation/"), ("원장 칼럼 · 치료를 결정하기 전, 제가 먼저 생각하는 것", "column.html")], "영어 · 일본어"),
    "박지현": ("심미보철, 임플란트 보철, 전악수복", [("보철 상담: 모양과 씹는 느낌", f"{B}/journal/restoration-consultation/"), ("크라운 알아보기", f"{B}/knowledge/dental-crown/")], "중국어"),
    "원소윤": ("심미보철, 라미네이트 비니어, 레진 수복", [("보철 상담: 모양과 씹는 느낌", f"{B}/journal/restoration-consultation/"), ("원장 칼럼 · 자연스러운 미소를 위해", f"{B}/columns/care-in-the-details/")], "영어"),
    "한이연": ("브라켓 교정, 투명교정, 성장기교정", [("교정 상담 전 확인할 내용", f"{B}/journal/orthodontic-consultation/"), ("성장기교정 설명", f"{B}/knowledge/growth-orthodontics/")], ""),
}


def doctors(theme):
    rows = []
    for i, (img, name, role, spec, fields, href) in enumerate(m.DOCTORS):
        f, reads, lang = DOC_DETAIL[name]
        ph = (f'<img src="assets/img/{img}" alt="{name} {role}" width="900" height="1125" loading="lazy">' if img
              else f'<div class="mono"><b>{name}</b><span>{role} · 사진 준비 중</span></div>')
        sp = f'<span class="spec">{spec}</span>' if spec else ''
        rd = "".join(f'<li><a href="{h}">{t} <span class="ins-arrow" aria-hidden="true">→</span></a></li>' for t, h in reads)
        ln = f'<div><dt>공개 영상 안내 언어</dt><dd>{lang}</dd></div>' if lang else ''
        rows.append(f"""<article class="doc-row{' flip' if i % 2 else ''}" id="dentist-{i + 1}" data-reveal>
          <div class="ins-doc"><div class="ph">{ph}</div></div>
          <div class="info">
            <h2 class="t-fs-48 t-fs-28-sm u-lh-12 m-0">{name} <small>{role}</small></h2>
            {sp}
            <dl class="doc-facts">
              <div><dt>{'진료분야' if spec else '관심 진료분야'}</dt><dd>{f}</dd></div>
              {ln}
            </dl>
            <h3 class="c-fs-14 fw-600 ins-muted u-mt-32 m-0">함께 읽을 글</h3>
            <ul class="doc-reads">{rd}</ul>
          </div>
        </article>""")
    principles = [("발언과 편집의 구분", "의료진의 직접 설명이 담긴 글은 발언한 의료진을 표시하고, 편집부가 자료를 바탕으로 정리한 글은 편집 글로 구분합니다."),
                  ("내용 확인", "치료 정보의 적용 범위와 주의할 점이 빠지지 않았는지 살펴봅니다."),
                  ("쉬운 설명", "어려운 용어는 환자가 읽기 쉬운 일상의 언어로 풀어 씁니다."),
                  ("정보 업데이트", "제도나 진료정보가 달라지면 관련 내용을 다시 확인하고 고칩니다.")]
    pr = "".join(f'<div data-reveal style="--d:{i}"><dt>{t}</dt><dd>{d}</dd></div>' for i, (t, d) in enumerate(principles))
    body = sub_hero(theme, [("메인", "index.html"), ("의료진", "")], "서울이도치과<br>의료진을 소개합니다",
                    "의료진의 전문의 자격과 진료분야를 살펴보세요. 내 상태에 맞는 진료와 치료 계획은 상담을 통해 확인할 수 있습니다.",
                    "team.jpg", "서울이도치과 로고 앞에 선 의료진", meta="전문의 자격과 진료분야는 서로 구분해서 안내합니다", pos="50% 30%") + f"""
  <section class="u-py-120 u-py-80-sm" aria-label="의료진 목록">
    <div class="u-1440 ins-wrap">
      <div class="doc-list">{"".join(rows)}</div>
      <p class="c-fs-14 ins-muted u-mt-48 m-0">공식 홈페이지 게시 정보 확인 2026.11.04 · 개별 의료진의 진료일과 예약 가능 여부는 병원에 확인해 주세요.</p>
    </div>
  </section>

  <section class="ins-section-alt u-py-140 u-py-80-sm" aria-labelledby="pr-title">
    <div class="u-1440 ins-wrap">
      <div class="row g-5">
        <div class="col-lg-4" data-reveal><h2 id="pr-title" class="t-fs-40 t-fs-28-sm fw-700 u-lh-13 m-0">한 편의 글이<br>만들어질 때</h2>
          <p class="c-fs-16 ins-body u-mt-16 m-0">누가 설명했고 누가 내용을 확인했는지, 필요한 정보는 글 안에서 안내합니다.</p></div>
        <dl class="col-lg-8 principles m-0">{pr}</dl>
      </div>
    </div>
  </section>
{cta_band("원하는 원장에게 상담받고 싶다면", "예약할 때 원하는 의료진과 진료일을 함께 확인해 주세요.")}
</main>
"""
    return page(theme, "의료진", body, "doctors.html")


# ---------------------------------------------------------------- 5. 방문 안내
VISIT_FAQ = [
    ("서울이도치과의원은 어디에 있나요?", "서울특별시 마포구 만리재로 24, 2층에 있습니다. 방문 전 전화 또는 네이버 예약을 통해 진료 일정을 확인해 주세요."),
    ("첫 방문에는 무엇을 준비하면 좋을까요?", "불편한 부위와 증상, 복용 중인 약, 알레르기, 기존 치료 경험을 정리해 주세요. 치료에 대한 걱정이나 질문도 의료진에게 알려주세요."),
    ("예약은 어떻게 하나요?", "네이버 예약 버튼으로 병원의 예약 페이지를 열거나 02-706-2080으로 전화하실 수 있습니다. 실제 예약 확정 여부는 예약 서비스 또는 병원의 안내를 확인해 주세요."),
    ("어떤 언어로 상담할 수 있나요?", "공개 영상에서 영어는 고성민·원소윤, 일본어는 고성민, 중국어는 박지현 원장이 안내합니다. 예약할 때 원하는 언어, 담당 의료진의 진료일과 상담 범위를 확인해 주세요."),
    ("해외에서 예약 문의를 하려면요?", "전화는 +82-2-706-2080입니다. 진료시간은 한국 표준시(KST, UTC+9) 기준입니다. 네이버 예약도 이용할 수 있으며 로그인이나 해외 이용 가능 여부는 해당 서비스에서 확인해 주세요."),
    ("치료 기간과 비용을 먼저 알고 싶어요.", "현재 상태를 확인해야 계획과 비용을 설명할 수 있습니다. 상담에서는 필요한 검사, 가능한 선택지, 예상 방문 횟수와 관리 방법을 함께 물어보세요."),
    ("의료진 약력과 정보의 출처는 어디인가요?", "의료진 정보는 서울이도치과의원 공식 홈페이지를 바탕으로 정리했습니다. 구강 건강 안내에는 해당 내용을 확인할 수 있는 공공기관 원문을 함께 표시합니다."),
]
ROUTES = [
    ("신공덕동", "서울이도치과의 실제 소재지는 신공덕동입니다. 도로명 주소는 만리재로 24, 2층이며 지번 주소는 신공덕동 178입니다."),
    ("공덕동에서", "목적지는 신공덕동의 서울이도치과로 설정해 주세요. ‘공덕’ 지역명만 검색하기보다 만리재로 24를 입력하면 목적지 확인에 도움이 됩니다."),
    ("도화동에서", "출발 건물이나 주소를 기준으로 경로를 확인해 주세요. 마포역과 공덕역은 서로 다른 역이며, 병원은 공덕역 인근 신공덕동에 있습니다."),
    ("아현동에서", "지도에 현재 위치와 목적지 ‘서울이도치과의원’을 입력해 도보·버스·지하철 경로를 비교해 주세요. 아현역과 공덕역은 서로 다른 역입니다."),
]


def visit(theme):
    faq = "".join(f'<details{" open" if i == 0 else ""}><summary>{q}<span class="pm" aria-hidden="true"></span></summary><div class="answer c-fs-16"><p class="m-0">{a}</p></div></details>' for i, (q, a) in enumerate(VISIT_FAQ))
    routes = "".join(f'<article class="route" data-reveal style="--d:{i}"><h3 class="t-fs-22 fw-700 m-0">{t}</h3><p class="c-fs-16 u-mt-12 m-0">{d}</p></article>' for i, (t, d) in enumerate(ROUTES))
    body = sub_hero(theme, [("메인", "index.html"), ("진료시간·오시는 길", "")], "공덕에서 만나는<br>서울이도치과",
                    "위치와 진료시간을 확인하고 방문을 준비하세요. 월요일과 목요일은 저녁 8시 30분까지 진료합니다.",
                    "lounge.jpg", "서울이도치과 라운지", meta='<span class="ins-dot" aria-hidden="true"></span> <span data-status>진료시간 확인 중</span>', pos="60% 50%") + f"""
  <section class="u-py-120 u-py-80-sm" aria-labelledby="hours-title">
    <div class="u-1440 ins-wrap">
      <div class="row g-5">
        <div class="col-lg-6" data-reveal>
          <h2 id="hours-title" class="t-fs-40 t-fs-28-sm fw-700 u-lh-13 m-0">진료시간</h2>
          <p class="ins-status u-mt-16 u-mb-24 m-0"><span class="ins-dot" aria-hidden="true"></span><span data-status>진료시간 확인 중</span></p>
          {m.hours_table()}
          <p class="c-fs-14 ins-muted u-mt-16 m-0">한국 표준시(KST) 기준 · 원장별 진료일은 예약할 때 확인해 주세요.</p>
        </div>
        <div class="col-lg-6" data-reveal style="--d:1">
          <div class="ins-panel ins-section-alt">
            <h2 class="t-fs-28 t-fs-24-sm fw-700 u-mb-16 m-0">서울이도치과의원</h2>
            {m.visit_info()}
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="ins-section-alt u-py-140 u-py-80-sm" aria-labelledby="way-title">
    <div class="u-1440 ins-wrap">
      {m.sec_head("", '<span id="way-title">지하철이나 차로 오신다면</span>', "출발 위치와 보행 경로에 따라 시간은 달라질 수 있습니다.")}
      <div class="g-cols-1 g-cols-3-lg u-gap-24">
        <article class="route" data-reveal><h3 class="t-fs-22 fw-700 m-0">지하철</h3><p class="c-fs-16 u-mt-12 m-0">공덕역 5·6번 출구에서 도보 약 3분입니다.</p></article>
        <article class="route" data-reveal style="--d:1"><h3 class="t-fs-22 fw-700 m-0">차량</h3><p class="c-fs-16 u-mt-12 m-0">신공덕 아이파크 지하주차장 2시간 무료. 주차 등록 방법과 초과 요금은 방문 전 병원에 확인해 주세요.</p></article>
        <article class="route" data-reveal style="--d:2"><h3 class="t-fs-22 fw-700 m-0">해외에서 문의</h3><p class="c-fs-16 u-mt-12 m-0">전화 +82-2-706-2080. 진료시간은 한국 표준시(UTC+9) 기준입니다.</p></article>
      </div>
      <h3 class="t-fs-28 t-fs-20-sm fw-700 u-mt-80 u-mt-48-sm u-mb-24 m-0" data-reveal>주변 동네에서 오실 때</h3>
      <div class="g-cols-1 g-cols-2-md g-cols-4-lg u-gap-24">{routes}</div>
      <p class="c-fs-14 ins-muted u-mt-24 m-0">위 동네는 출발 지역이며, 해당 동에 별도 지점이 있다는 뜻은 아닙니다.</p>
    </div>
  </section>

  <section class="u-py-140 u-py-80-sm" aria-labelledby="first-title">
    <div class="u-1440 ins-wrap">
      <div class="row g-5">
        <div class="col-lg-4" data-reveal><h2 id="first-title" class="t-fs-40 t-fs-28-sm fw-700 u-lh-13 m-0">첫 방문 전에<br>메모해 오세요</h2>
          <p class="c-fs-16 ins-body u-mt-16 m-0">정리해 오시면 상담 시간을 알차게 쓸 수 있습니다.</p></div>
        <div class="col-lg-8" data-reveal style="--d:1">
          <ul class="checklist">
            <li>불편한 부위와 증상, 시작된 때</li><li>복용 중인 약과 알레르기</li><li>이전에 받은 치과 치료</li><li>치료에 대한 걱정과 궁금한 점</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="ins-section-alt u-py-140 u-py-80-sm" aria-labelledby="vfaq-title">
    <div class="u-1440 ins-wrap">
      <div class="row g-5">
        <div class="col-lg-4" data-reveal><h2 id="vfaq-title" class="t-fs-40 t-fs-28-sm fw-700 u-lh-13 m-0">방문 전,<br>궁금한 이야기</h2></div>
        <div class="col-lg-8 ins-faq" data-reveal style="--d:1">{faq}</div>
      </div>
    </div>
  </section>
</main>
"""
    return page(theme, "진료시간·오시는 길", body, "visit.html")


# ---------------------------------------------------------------- 출력
def main_page(theme):
    html = {"a": m.page_a, "b": m.page_b, "c": m.page_c}[theme]()
    i = html.index('<header class="ins-header">'); j = html.index('</header>') + len('</header>')
    html = html[:i] + header(theme).rstrip() + html[j:]
    return to_folder(relink(html))


def chooser():
    rows = []
    pages = [("index.html", "메인"), ("knowledge.html", "치아백과 목록"), ("knowledge-implant.html", "치아백과 상세"), ("column.html", "원장 칼럼"), ("doctors.html", "의료진"), ("visit.html", "진료시간·오시는 길")]
    for t, name in THEMES.items():
        links = "".join(f'<a href="{t}/{h}">{n}</a>' for h, n in pages)
        rows.append(f'<article class="ins-card"><a href="{t}/index.html" class="ph u-ratio-16-9"><img src="previews/{t}-main-fold.jpg" alt="시안 {t.upper()} {name} 첫 화면" loading="lazy"></a><h2 class="t-fs-24 fw-700 m-0">{t.upper()} · {name}</h2><nav class="chooser-links" aria-label="시안 {t.upper()} 페이지">{links}</nav></article>')
    return m.head("a", "닥터인사이트 리뉴얼 시안 v3") + f"""
<main class="u-1440 ins-wrap u-py-120 u-py-80-sm">
  <h1 class="t-fs-48 t-fs-28-sm fw-700 m-0">서울이도치과 닥터인사이트 · 리뉴얼 시안 v3</h1>
  <p class="c-fs-18 ins-body u-mt-16 u-mb-48 m-0">세 가지 톤마다 메인과 서브 5종(치아백과 목록·상세, 원장 칼럼, 의료진, 진료시간·오시는 길)을 만들었습니다.</p>
  <div class="g-cols-1 g-cols-3-lg u-gap-32">{"".join(rows)}</div>
</main>
<script src="js/insight.js"></script>
</body>
</html>
"""


if __name__ == "__main__":
    for t in THEMES:
        d = ROOT / t; d.mkdir(exist_ok=True)
        files = {"index.html": main_page(t), "knowledge.html": knowledge(t), "knowledge-implant.html": knowledge_implant(t),
                 "column.html": column(t), "doctors.html": doctors(t), "visit.html": visit(t)}
        for n, h in files.items():
            (d / n).write_text(h, encoding="utf-8")
    (ROOT / "index.html").write_text(chooser(), encoding="utf-8")
    for old in ["a-clinic-white.html", "b-night-studio.html", "c-lounge.html"]:
        p = ROOT / old
        if p.exists():
            p.unlink()
    print("built a/ b/ c/ (6 pages each) + index.html")
