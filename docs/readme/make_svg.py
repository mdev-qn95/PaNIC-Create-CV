# Sinh các SVG minh họa cho README: python docs/readme/make_svg.py
# textLength cố định độ rộng mỗi chữ nên dải chạy lặp liền mạch bất kể font của máy người xem.
import pathlib

OUT = pathlib.Path(__file__).parent
ACC, ACC_D, TEAL, INK, BG, MUTED = '#8B8BFF', '#4338CA', '#5EEAD4', '#0B0D12', '#0D0E1A', '#9BA3B7'
FONT = "'Be Vietnam Pro','Segoe UI',system-ui,-apple-system,Roboto,Arial,sans-serif"
STAR = 'M0-11C2-2 2-2 11 0C2 2 2 2 0 11C-2 2-2 2-11 0C-2-2-2-2 0-11Z'
DEFS = f'''<defs>
<radialGradient id="glow" cx="15%" cy="0%" r="90%"><stop offset="0" stop-color="#24206b"/><stop offset=".6" stop-color="{BG}"/></radialGradient>
<linearGradient id="brand" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8B8BFF"/><stop offset="1" stop-color="{ACC_D}"/></linearGradient>
<pattern id="grid" width="44" height="44" patternUnits="userSpaceOnUse"><path d="M44 0H0V44" fill="none" stroke="#8B8BFF" stroke-opacity=".07"/></pattern>
</defs>'''
STYLE = f'''<style>text{{font-family:{FONT}}}
@keyframes left{{to{{transform:translateX(var(--w))}}}}.left{{animation:left linear infinite}}
@keyframes right{{from{{transform:translateX(var(--w))}}to{{transform:translateX(0)}}}}.right{{animation:right linear infinite}}
@keyframes float{{50%{{transform:translateY(-10px)}}}}.float{{animation:float 6s ease-in-out infinite}}
@keyframes pop{{0%,60%{{transform:scale(0)}}75%{{transform:scale(1.12)}}85%,100%{{transform:scale(1)}}}}.pop{{animation:pop 4s ease-out infinite;transform-box:fill-box;transform-origin:center}}
@keyframes blink{{50%{{opacity:0}}}}.blink{{animation:blink 1s steps(1) infinite}}
@keyframes grow{{from{{transform:scaleX(0)}}}}.grow{{animation:grow 1.6s cubic-bezier(.22,1,.36,1) both;transform-box:fill-box;transform-origin:left}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}</style>'''


def tape(items, y, size, per_char, color, fill, sep_color, cls, dur):
    """Một dải chữ chạy liền mạch: lặp nhóm chữ đủ phủ khung rồi dịch đúng 1 nhóm."""
    parts, x = [], 0.0
    for t in items:
        w = len(t) * per_char
        parts.append((t, x, w))
        x += w + 64
    set_w = x
    out = []
    for rep in range(-1, int(1400 / set_w) + 2):
        for t, px, w in parts:
            bx = px + rep * set_w
            out.append(f'<text x="{bx:.1f}" y="{y}" font-size="{size}" font-weight="800" textLength="{w:.1f}" lengthAdjust="spacingAndGlyphs" fill="{color}">{t}</text>'
                       f'<path d="{STAR}" transform="translate({bx + w + 32:.1f} {y - size * .36:.1f})" fill="{sep_color}"/>')
    return f'<g class="{cls}" style="--w:{-set_w:.1f}px;animation-duration:{dur}s">{"".join(out)}</g>'


def marquee():
    a = ['15 MẪU CV', 'XUẤT PDF CHUẨN A4', 'ẢNH PNG', 'TRANG HTML', 'XEM TRƯỚC TỨC THÌ', 'MIỄN PHÍ']
    b = ['sinh viên.', 'mới tốt nghiệp.', 'nhiều kinh nghiệm.', 'đẹp.', 'chỉn chu.', 'dễ đọc.']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="190" viewBox="0 0 1280 190" role="img" aria-labelledby="t">
<title id="t">15 mẫu CV · Xuất PDF chuẩn A4 · Ảnh PNG · Trang HTML · Xem trước tức thì · Miễn phí</title>{STYLE}{DEFS}
<clipPath id="c"><rect width="1280" height="190" rx="32"/></clipPath>
<g clip-path="url(#c)"><rect width="1280" height="190" fill="url(#glow)"/><rect width="1280" height="190" fill="url(#grid)"/>
<g transform="rotate(-1.4 640 60)"><rect x="-80" y="26" width="1440" height="66" fill="url(#brand)"/>{tape(a, 71, 30, 20.5, '#fff', '', TEAL, 'left', 40)}</g>
<g transform="rotate(1 640 145)"><rect x="-80" y="118" width="1440" height="56" fill="#171B26"/>{tape(b, 156, 27, 14.6, TEAL, '', '#8B8BFF', 'right', 34)}</g></g>
<rect x=".5" y=".5" width="1279" height="189" rx="31.5" fill="none" stroke="#232838"/></svg>'''


def cv_card(x, y, kind, delay):
    """CV thu nhỏ dạng khối hình (3 kiểu bố cục) để minh họa."""
    w, h, body = 210, 297, []
    line = lambda lx, ly, lw, c='#D9DEE7', hh=6: f'<rect x="{lx}" y="{ly}" width="{lw}" height="{hh}" rx="3" fill="{c}"/>'
    if kind == 'sidebar':
        body += [f'<rect width="72" height="{h}" fill="#2B3036"/>', '<rect x="12" y="14" width="48" height="48" rx="6" fill="#59606B"/>',
                 line(12, 74, 44, ACC, 7), line(12, 88, 36, '#59606B'), line(12, 112, 40, ACC, 5)]
        body += [line(12, 124 + i * 12, 46 - (i % 3) * 8, '#59606B', 4) for i in range(10)]
        for s in range(3):
            sy = 18 + s * 92
            body += [line(86, sy, 60, ACC, 7), f'<rect x="152" y="{sy + 3}" width="46" height="2" fill="{ACC}"/>']
            body += [line(86, sy + 18 + i * 12, 110 - (i % 4) * 14, '#C9CFD9', 4) for i in range(5)]
    elif kind == 'header':
        body += [f'<rect width="{w}" height="70" fill="#2B3036"/>', f'<circle cx="40" cy="35" r="20" fill="#59606B" stroke="{ACC}" stroke-width="3"/>',
                 line(70, 24, 90, '#fff', 9), line(70, 41, 60, '#8B93A1', 5)]
        for s in range(3):
            sy = 88 + s * 68
            body += [line(14, sy, 70, '#2B3036', 6), f'<circle cx="18" cy="{sy + 19}" r="4" fill="#fff" stroke="{ACC}" stroke-width="2"/>']
            body += [line(28, sy + 16 + i * 11, 100 - (i % 3) * 18, '#C9CFD9', 4) for i in range(4)]
        body += [f'<rect x="146" y="84" width="1" height="200" fill="#E5E7EB"/>'] + [line(154, 92 + i * 12, 44 - (i % 3) * 10, '#C9CFD9', 4) for i in range(14)]
    else:
        body += [f'<rect x="14" y="16" width="4" height="40" fill="{ACC}"/>', line(26, 20, 110, '#2B3036', 11), line(26, 40, 70, ACC, 5),
                 '<rect x="158" y="14" width="38" height="38" rx="8" fill="#D9DEE7"/>']
        for s in range(4):
            sy = 72 + s * 54
            body += [f'<rect x="14" y="{sy - 6}" width="182" height="1" fill="#E5E7EB"/>', line(14, sy, 34, ACC, 5)]
            body += [line(62, sy + i * 11, 134 - (i % 3) * 22, '#C9CFD9', 4) for i in range(4)]
    return (f'<g class="float" style="animation-delay:{delay}s"><g transform="translate({x} {y})">'
            f'<rect x="-2" y="6" width="{w + 4}" height="{h}" rx="10" fill="#000" opacity=".35"/>'
            f'<rect width="{w}" height="{h}" rx="8" fill="#fff"/><g clip-path="inset(0 round 8px)">{"".join(body)}</g></g></g>')


def hero():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="520" viewBox="0 0 1280 520" role="img" aria-labelledby="t">
<title id="t">PaNIC CV Studio — tạo CV đẹp, chuẩn nhà tuyển dụng</title>{STYLE}{DEFS}
<clipPath id="c"><rect width="1280" height="520" rx="32"/></clipPath>
<g clip-path="url(#c)"><rect width="1280" height="520" fill="url(#glow)"/><rect width="1280" height="520" fill="url(#grid)"/>
<g transform="translate(76 92)">
  <rect width="58" height="58" rx="15" fill="url(#brand)"/>
  <g transform="scale(.906)"><path d="M18 13.5h20.5l8 8V48.5a3.5 3.5 0 0 1-3.5 3.5H18a3.5 3.5 0 0 1-3.5-3.5v-31.5a3.5 3.5 0 0 1 3.5-3.5z" fill="#fff"/><path d="M38.5 13.5v5.5a2.5 2.5 0 0 0 2.5 2.5h5.5z" fill="#C7C9FF"/><circle cx="23.5" cy="24" r="4.6" fill="#4F46E5"/><rect x="31" y="20.6" width="9" height="3" rx="1.5" fill="#1E1B4B"/><rect x="31" y="25.6" width="6" height="2.6" rx="1.3" fill="#A5A8F5"/><rect x="19" y="33" width="21" height="2.8" rx="1.4" fill="#C7C9FF"/><rect x="19" y="38.6" width="16" height="2.8" rx="1.4" fill="#C7C9FF"/><rect x="19" y="44.2" width="12" height="2.8" rx="1.4" fill="#C7C9FF"/><circle cx="45" cy="45" r="10.5" fill="#5EEAD4" stroke="#3B33C4" stroke-width="2.5"/><path d="M45 38.6c.7 3.6 2.8 5.7 6.4 6.4-3.6.7-5.7 2.8-6.4 6.4-.7-3.6-2.8-5.7-6.4-6.4 3.6-.7 5.7-2.8 6.4-6.4z" fill="#1E1B4B"/></g>
  <text x="76" y="26" font-size="24" font-weight="700" fill="#EEF1F7">PaNIC CV Studio</text>
  <text x="76" y="50" font-size="13" font-weight="600" letter-spacing="3" fill="#7C8498">TRÌNH TẠO CV</text>
  <text y="146" font-size="54" font-weight="800" letter-spacing="-1.5" fill="#EEF1F7">Tạo CV đẹp,</text>
  <text y="210" font-size="54" font-weight="800" letter-spacing="-1.5" fill="{ACC}">chuẩn nhà tuyển dụng<tspan class="blink" fill="{ACC}">_</tspan></text>
  <text y="262" font-size="19" fill="{MUTED}">Chọn mẫu theo đối tượng, điền nội dung và xem trước ngay.</text>
  <text y="290" font-size="19" fill="{MUTED}">Xuất PDF chuẩn A4, ảnh PNG hoặc trang web độc lập.</text>
  <g transform="translate(0 322)">
    <rect width="132" height="40" rx="20" fill="none" stroke="#2C3244"/><text x="66" y="26" font-size="15" font-weight="600" text-anchor="middle" fill="#EEF1F7">15 mẫu CV</text>
    <rect x="144" width="160" height="40" rx="20" fill="none" stroke="#2C3244"/><text x="224" y="26" font-size="15" font-weight="600" text-anchor="middle" fill="#EEF1F7">PDF · PNG · HTML</text>
    <rect x="316" width="104" height="40" rx="20" fill="none" stroke="#2C3244"/><text x="368" y="26" font-size="15" font-weight="600" text-anchor="middle" fill="#EEF1F7">Miễn phí</text>
  </g>
</g>
<g transform="rotate(-6 820 260)">{cv_card(700, 120, 'sidebar', 0)}</g>
<g transform="rotate(4 1060 260)">{cv_card(1000, 80, 'label', -2)}</g>
<g transform="rotate(-1 940 300)">{cv_card(850, 170, 'header', -4)}</g>
<g class="pop" transform="translate(1032 382)"><rect width="128" height="46" rx="23" fill="url(#brand)"/>
  <path d="M28 14v12m-6-5 6 6 6-6M20 32h16" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="48" y="30" font-size="17" font-weight="800" fill="#fff">Xuất PDF</text></g>
</g><rect x=".5" y=".5" width="1279" height="519" rx="31.5" fill="none" stroke="#232838"/></svg>'''


def steps():
    data = [('1', 'Chọn đối tượng &amp; mẫu', ['Sinh viên, mới tốt nghiệp', 'hay nhiều kinh nghiệm —', 'mỗi nhóm 5 mẫu riêng.']),
            ('2', 'Điền nội dung', ['Gõ bên trái, CV bên phải', 'cập nhật ngay. Mục trống', 'tự ẩn, ngắt trang gọn gàng.']),
            ('3', 'Tải về &amp; ứng tuyển', ['PDF chữ sắc nét, chuẩn A4,', 'ảnh PNG độ phân giải cao', 'hoặc một trang web độc lập.'])]
    cards = []
    for i, (n, title, lines) in enumerate(data):
        x = 40 + i * 410
        cards.append(f'''<g transform="translate({x} 40)"><rect width="370" height="200" rx="22" fill="#151925" stroke="#262C3C"/>
<circle cx="52" cy="56" r="26" fill="url(#brand)"/><text x="52" y="65" font-size="24" font-weight="800" text-anchor="middle" fill="#fff">{n}</text>
<text x="94" y="64" font-size="22" font-weight="700" fill="#EEF1F7">{title}</text>
<rect x="28" y="98" width="314" height="3" rx="1.5" fill="{ACC}" class="grow" style="animation-delay:{i * .5}s" opacity=".85"/>
{"".join(f'<text x="28" y="{136 + j * 26}" font-size="16" fill="{MUTED}">{t}</text>' for j, t in enumerate(lines))}</g>''')
        if i < 2:
            cards.append(f'<path d="M{x + 378} 140h24m-8-8 8 8-8 8" stroke="{ACC}" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="280" viewBox="0 0 1280 280" role="img" aria-labelledby="t">
<title id="t">Ba bước: chọn mẫu, điền nội dung, tải về</title>{STYLE}{DEFS}
<rect width="1280" height="280" rx="32" fill="{BG}"/><rect width="1280" height="280" rx="32" fill="url(#grid)"/>{"".join(cards)}
<rect x=".5" y=".5" width="1279" height="279" rx="31.5" fill="none" stroke="#232838"/></svg>'''


for name, svg in [('marquee.svg', marquee()), ('hero.svg', hero()), ('steps.svg', steps())]:
    (OUT / name).write_text(svg, encoding='utf-8')
    print(name, len(svg))
