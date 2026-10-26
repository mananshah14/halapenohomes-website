from playwright.sync_api import sync_playwright
import pathlib; url='file://'+str(pathlib.Path(__file__).resolve().parent.parent/'index.html')
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={'width':1440,'height':900}); errs=[]
    pg.on('pageerror',lambda e: errs.append(str(e)))
    pg.on('console',lambda m: errs.append(m.text) if m.type=='error' and 'fonts' not in m.text else None)
    pg.goto(url); pg.wait_for_timeout(800)
    pg.screenshot(path='src/dist/v3_hero0.png')
    # measure hero travel over first 700px
    def panelX(): return pg.evaluate("document.getElementById('pl').getBoundingClientRect().right")
    x0=panelX(); pg.evaluate("window.scrollTo(0,700)"); pg.wait_for_timeout(300); x1=panelX()
    print('panel travel over 700px scroll:', round(x0-x1,1),'px')
    m0=pg.evaluate("getComputedStyle(document.getElementById('mark')).letterSpacing")
    pg.screenshot(path='src/dist/v3_hero700.png')
    pg.evaluate("window.scrollTo(0,1400)"); pg.wait_for_timeout(300); pg.screenshot(path='src/dist/v3_hero1400.png')
    pg.evaluate("window.scrollTo(0,2200)"); pg.wait_for_timeout(300); pg.screenshot(path='src/dist/v3_hero2200.png')
    print('letter-spacing at 700:',m0,'-> at 2200:',pg.evaluate("getComputedStyle(document.getElementById('mark')).letterSpacing"))
    # reversibility
    pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(300); print('reversed panel right edge:', panelX(), 'vs start', x0)
    # sections
    for sel,name in [('#fold','v3_fold'),('#homes','v3_homes'),('#roster','v3_roster'),('#dates','v3_dates'),('#close','v3_close')]:
        pg.evaluate(f"document.querySelector('{sel}').scrollIntoView()"); pg.wait_for_timeout(1200); pg.screenshot(path='src/dist/'+name+'.png')
    # deck keyboard
    pg.focus('#deck'); before=pg.evaluate("document.querySelector('#dots i.on') && [...document.querySelectorAll('#dots i')].indexOf(document.querySelector('#dots i.on'))")
    pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(600); after=pg.evaluate("[...document.querySelectorAll('#dots i')].indexOf(document.querySelector('#dots i.on'))")
    print('deck dot before/after arrow:',before,after)
    pg.screenshot(path='src/dist/v3_deck_after.png')
    print('errors:',errs)
    # reduced motion: content visible without js-motion class
    pg2=b.new_page(viewport={'width':1440,'height':900},reduced_motion='reduce'); pg2.goto(url); pg2.wait_for_timeout(500)
    print('reduced-motion js-motion class present?', pg2.evaluate("document.documentElement.classList.contains('js-motion')"), '| fold h2 opacity:', pg2.evaluate("getComputedStyle(document.querySelector('#fold h2')).opacity"))
    # mobile
    pm=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True); pm.goto(url); pm.wait_for_timeout(600)
    pm.screenshot(path='src/dist/v3_m_hero.png')
    for sel,name in [('#homes','v3_m_homes'),('#roster','v3_m_roster'),('#dates','v3_m_dates'),('#close','v3_m_close')]:
        pm.evaluate(f"document.querySelector('{sel}').scrollIntoView()"); pm.wait_for_timeout(900); pm.screenshot(path='src/dist/'+name+'.png')
    print('mobile horizontal overflow:', pm.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth"))
    b.close()
