/* insight.js — 닥터인사이트 시안 v3 공용 스크립트 (의존성 없음) */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* 헤더: 스크롤하면 바탕이 생김 */
  const header = $('.ins-header');
  const onScroll = () => header && header.classList.toggle('is-scrolled', scrollY > 24);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* 모바일 메뉴: 링크를 누르면 닫힘 */
  $$('.ins-menu .panel a').forEach(a => a.addEventListener('click', () => a.closest('details').removeAttribute('open')));

  /* 등장 모션: 한 번만, 내용이 숨은 채로 남지 않게 */
  const targets = $$('[data-reveal]');
  if ('IntersectionObserver' in window && !reduce) {
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    targets.forEach(t => io.observe(t));
    addEventListener('load', () => setTimeout(() => targets.forEach(t => { const r = t.getBoundingClientRect(); if (r.top < innerHeight && r.bottom > 0) t.classList.add('is-in'); }), 2000));
  } else targets.forEach(t => t.classList.add('is-in'));

  /* 동작 줄이기: 배경 영상 정지 */
  if (reduce) $$('video[autoplay]').forEach(v => { v.pause(); v.removeAttribute('autoplay'); });

  /* 치아백과 빠른 검색 */
  const TERMS = [
    ['시린이', '증상·통증', 'tooth-sensitivity', '찬물, 바람, 양치 자극에 짧고 날카롭게 시린 상태', '시림 이시림 찬물'],
    ['치아우식증', '보존·신경치료', 'tooth-decay', '세균이 만든 산으로 치아가 손상되는 질환, 흔히 말하는 충치', '충치 썩은'],
    ['근관치료', '보존·신경치료', 'root-canal-treatment', '손상된 치수 조직을 제거하고 안쪽을 채우는 치료', '신경치료 신경'],
    ['복합레진', '보존·신경치료', 'composite-resin', '치아색 재료로 작은 결손이나 충치 부위를 메우는 방법', '레진 때우기'],
    ['치과 크라운', '보철·수복', 'dental-crown', '남은 치아를 덮어 모양과 씹는 기능을 되살리는 보철물', '크라운 씌우기 보철'],
    ['인레이·온레이', '보철·수복', 'inlay-onlay', '본떠 만든 수복물을 붙여 빈 부위를 채우는 치료', '인레이 온레이'],
    ['치과 브리지', '보철·수복', 'dental-bridge', '양옆 치아를 지지대로 빈 자리를 연결하는 고정성 보철', '브릿지 빠진'],
    ['틀니', '보철·수복', 'dentures', '여러 치아가 없을 때 끼웠다 뺄 수 있게 만드는 보철물', '의치 부분틀니'],
    ['치과임플란트', '임플란트·발치', 'dental-implant', '턱뼈에 인공치근을 심고 보철물을 연결하는 치료', '임플란트 빠진'],
    ['골이식', '임플란트·발치', 'bone-grafting', '임플란트를 위해 부족한 잇몸뼈를 보완하는 시술', '뼈이식'],
    ['사랑니', '임플란트·발치', 'wisdom-tooth', '가장 안쪽에 나는 세 번째 큰어금니', '발치 매복'],
    ['치주염', '잇몸·예방', 'periodontitis', '치아를 받치는 잇몸과 주변 조직에 생긴 염증', '잇몸 출혈 피 풍치'],
    ['스케일링', '잇몸·예방', 'scaling', '칫솔로 없애기 어려운 치석을 기구로 제거하는 처치', '치석 잇몸'],
    ['투명교정장치', '교정·성장', 'clear-aligners', '단계별로 바꿔 끼우며 치아를 옮기는 투명 장치', '투명교정 교정'],
    ['성장기교정', '교정·성장', 'growth-orthodontics', '자라는 아이의 치열과 턱 성장을 살피는 교정 진료', '아이 어린이 교정'],
    ['교정 유지장치', '교정·성장', 'orthodontic-retainers', '교정 후 치아가 자리 잡도록 돕는 장치', '유지장치 교정'],
    ['턱관절장애', '턱관절·구강외과', 'temporomandibular-disorder', '턱관절·씹는 근육의 통증, 소리, 입 벌리기 불편', '턱 소리 턱관절'],
    ['이갈이·이악물기', '턱관절·구강외과', 'bruxism', '이를 갈거나 강하게 무는 행동이 반복되는 것', '이갈이 턱'],
    ['교합', '검사·진단', 'occlusion', '씹을 때 위아래 치아가 만나는 관계', '맞물림'],
    ['임플란트 건강보험', '보험·비용', 'dental-implant-insurance', '연령, 인정 개수, 본인부담 등 급여 기준', '보험 비용 임플란트']
  ];
  const box = $('#ins-results'), input = $('#ins-q');
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  function search() {
    if (!box || !input) return;
    const q = input.value.trim();
    if (!q) { box.innerHTML = ''; return; }
    const words = q.split(/\s+/);
    const hits = TERMS.map(t => ({ t, s: words.reduce((n, w) => n + (t[0].includes(w) ? 4 : 0) + (t[4].includes(w) ? 3 : 0) + (t[1].includes(w) ? 2 : 0) + (t[3].includes(w) ? 1 : 0), 0) }))
      .filter(x => x.s > 0).sort((a, b) => b.s - a.s).slice(0, 4);
    box.innerHTML = hits.length ? hits.map(({ t }) => `<a href="${t[2] === 'dental-implant' ? 'knowledge-implant.html' : `https://yidoinsight.com/knowledge/${t[2]}/`}"><strong>${esc(t[0])}</strong><span>${esc(t[3])}</span><em>${esc(t[1])}</em></a>`).join('')
      : `<p class="empty">‘${esc(q)}’에 맞는 용어가 아직 없습니다. 아래 분류에서 찾아보거나 증상으로 찾기를 이용해 주세요.</p>`;
  }
  if (input) {
    input.addEventListener('input', search);
    $('#ins-search-form')?.addEventListener('submit', e => { e.preventDefault(); search(); });
    $$('.ins-chips button').forEach(b => b.addEventListener('click', () => { input.value = b.textContent.trim(); search(); }));
  }


  /* 사진 초점 (data-pos → object-position) */
  $$('img[data-pos]').forEach(img => { img.style.objectPosition = img.dataset.pos; });

  /* 치아백과 목록: 분야 필터 + 검색 */
  const grid = $('#kb-grid');
  if (grid) {
    const cards = $$('.term-card', grid), chips = $$('.kb-filter button'), q = $('#kb-q'), count = $('#kb-count'), empty = $('#kb-empty');
    const ALIAS = { '씌우기': '크라운', '신경치료': '근관치료', '충치': '우식', '레진': '복합레진', '잇몸': '치주염 스케일링 잇몸', '교정': '교정', '빠진': '임플란트 브리지 틀니', '시림': '시린이' };
    let cat = '전체';
    const apply = () => {
      const raw = (q.value || '').trim(); const words = raw ? raw.split(/\s+/).flatMap(w => [w, ...(ALIAS[w] || '').split(' ').filter(Boolean)]) : [];
      let n = 0;
      cards.forEach(c => { const okCat = cat === '전체' || c.dataset.cat === cat; const okQ = !words.length || words.some(w => c.dataset.name.includes(w)); const on = okCat && okQ; c.hidden = !on; if (on) n++; });
      count.textContent = `용어 ${n}개` + (cat !== '전체' ? ` · ${cat}` : '') + (raw ? ` · ‘${raw}’` : '');
      empty.hidden = n > 0;
    };
    chips.forEach(b => b.addEventListener('click', () => { cat = b.dataset.filter; chips.forEach(x => { x.classList.toggle('is-on', x === b); x.setAttribute('aria-pressed', x === b); }); apply(); }));
    q.addEventListener('input', apply);
    $('#kb-form').addEventListener('submit', e => { e.preventDefault(); apply(); });
  }

  /* 아티클 목차: 읽는 위치 표시 */
  const tocLinks = $$('.article-toc a');
  if (tocLinks.length && 'IntersectionObserver' in window) {
    const map = new Map(tocLinks.map(a => [a.getAttribute('href').slice(1), a]));
    const io2 = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { tocLinks.forEach(a => a.classList.remove('is-on')); map.get(e.target.id)?.classList.add('is-on'); } }), { rootMargin: '-30% 0px -60% 0px' });
    map.forEach((_, id) => { const el = document.getElementById(id); if (el) io2.observe(el); });
  }

  /* 오늘 진료 상태 (한국 시간) */
  const H = { 0: null, 1: [930, 2030], 2: [930, 1830], 3: [930, 1830], 4: [930, 2030], 5: [930, 1830], 6: [930, 1430] };
  const D = ['일', '월', '화', '수', '목', '금', '토'];
  const hhmm = n => `${String(Math.floor(n / 100)).padStart(2, '0')}:${String(n % 100).padStart(2, '0')}`;
  function status() {
    let now; try { now = new Date(new Date().toLocaleString('en-US', { timeZone: 'Asia/Seoul' })); } catch (e) { now = new Date(); }
    const d = now.getDay(), t = now.getHours() * 100 + now.getMinutes(), h = H[d];
    const next = () => { for (let i = 1; i < 8; i++) { const n = (d + i) % 7; if (H[n]) return `${D[n]}요일 ${hhmm(H[n][0])}`; } };
    let text, state = 'open';
    if (!h) { text = `오늘 휴진 · ${next()} 진료`; state = 'closed'; }
    else if (t < h[0]) { text = `오늘 ${hhmm(h[0])} – ${hhmm(h[1])} 진료`; state = 'closed'; }
    else if (t >= h[1]) { text = `진료 마감 · ${next()} 진료`; state = 'closed'; }
    else if (d !== 6 && t >= 1230 && t < 1400) { text = '점심시간 · 14:00 진료 재개'; state = 'break'; }
    else text = `지금 진료 중 · ${hhmm(h[1])}까지`;
    $$('[data-status]').forEach(el => el.textContent = text);
    $$('.ins-dot').forEach(el => el.dataset.state = state);
    $$('.ins-hours tr[data-days]').forEach(tr => tr.classList.toggle('today', tr.dataset.days.split(',').map(Number).includes(d)));
  }
  status(); setInterval(status, 60000);
})();
