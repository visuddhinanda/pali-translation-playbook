# 翻译策略倾向

本文件由开放式固定搭配、开放式特殊句式和风格观察综合生成。它不以少数预设公式作为策略范围，而是把全量发现的候选归纳为可人工复核的策略假设。

## 摘要索引

| ID | Name | Related Entries | Evidence |
| --- | --- | ---: | ---: |
| strategy-open-frequency-first | 高频证据优先 | 8 | 8 |
| strategy-open-explanatory-citation | 解释与引文显化 | 3 | 8 |
| strategy-open-decomposition | 长句拆解与补足 | 3 | 8 |
| strategy-open-relation-explicitation | 关系词显化 | 7 | 8 |
| strategy-open-verbal-relation | 动作关系处理 | 2 | 8 |

## 条目

## strategy-open-frequency-first

```yaml
id: strategy-open-frequency-first
version_id: 74ebf4c5-c243-4948-955d-6c277e29276a
type: strategy
name: 高频证据优先
description: 先从全量语料中发现高频、跨 chunk 重复的搭配和句法信号，再由人工筛选为稳定规则。
definition: 先从全量语料中发现高频、跨 chunk 重复的搭配和句法信号，再由人工筛选为稳定规则。
when_used:
- 固定搭配抽取
- 版本内风格画像
- RAG 候选知识生成
risks:
- 高频不等于高价值，可能混入泛化词、引用缩写或格式噪声。
related_entry_ids:
- open-collocation-bhikkhave-83862b30
- open-collocation-bhante-dd737d96
- open-collocation-vuccati-67761320
- open-collocation-uppajjati-711283a4
- open-collocation-honti-8a2d0644
- open-collocation-bhagava-8b0af50d
- open-collocation-katham-63d98d73
- open-collocation-nanam-59d24ca5
evidence:
- unit_id: 64-111-87-116
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-111-87-116
  line: 55
  source_quote: ‘‘ so vata, bhikkhave, bhikkhu ābhisamācārikaṃ dhammaṃ aparipūretvā
    ādibrahmacariyakaṃ dhammaṃ paripūressatīti netaṃ ṭhānaṃ vijjatī’’ ti( a. ni.5.21).
  target_quote: “诸比库，若比库未圆满增上行仪法，而能圆满初梵行法者，无有此理！”（增支部·5·21）
- unit_id: 65-59-20-37
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:65-59-20-37
  line: 548
  source_quote: ‘‘ chandañce, bhikkhave, bhikkhu nissāya labhati samādhiṃ, labhati
    cittassekaggataṃ, ayaṃ vuccati chandasamādhi.
  target_quote: “诸比库，若比库依靠欲而得定，得心一境性，这称为欲定。
- unit_id: 65-59-50-78
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:65-59-50-78
  line: 550
  source_quote: Iti ayañca chando ayañca chandasamādhi ime ca padhānasaṅkhārā, ayaṃ
    vuccati, bhikkhave, chandasamādhipadhānasaṅkhārasamannāgato iddhipādo’’ ti( saṃ.
    ni.5.825).
  target_quote: 如此，有这欲、这欲定及这些勤行。诸比库，这些称作具足欲定勤行的神足。”（相应部·5·825）
- unit_id: 65-93-2-44
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:65-93-2-44
  line: 684
  source_quote: Apica tambapaṇṇidīpe talaṅgaravāsī dhammadinnattheropi tissamahāvihāre
    cetiyaṅgaṇasmiṃ nisīditvā‘‘ tīhi, bhikkhave, dhammehi samannāgato bhikkhu apaṇṇakapaṭipadaṃ
    paṭipanno hotī’’ ti apaṇṇakasuttaṃ( a. ni.3.16) kathento…
  target_quote: 此外，住在铜掌岛塔兰嘎拉的法授长老也坐于帝思大寺的塔院中开示着《无过经》（增支部·3·16）：“诸比库，具足三法的比库践行无过行道”，他向下挥扇，直至无间地狱而成一平面。
- unit_id: 65-100-2-34
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:65-100-2-34
  line: 715
  source_quote: ‘ ‘ Atha khvāhaṃ, bhikkhave, tathārūpaṃ iddhābhisaṅkhāraṃ abhisaṅkhāsiṃ‘
    ettāvatā brahmā ca brahmaparisā ca brahmapārisajjā ca saddañca me sossanti, na
    ca maṃ dakkhissantī’ ti antarahito imaṃ gāthaṃ abhāsiṃ–
  target_quote: “诸比库，当[到达梵天界]时，我完成像这样的神变加行后，[令心转向：]‘这么多的梵天及梵天的随众能听见我的声音，却看不见我。’我隐身而说出这首偈颂：
- unit_id: 65-788-39-72
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:65-788-39-72
  line: 1033
  source_quote: ‘‘ yo, bhikkhave, dukkhaṃ passati, dukkhasamudayampi so passati, dukkhanirodhampi
    passati, dukkhanirodhagāminiṃ paṭipadampi passatī’’ ti( saṃ. ni.5.1100) sabbaṃ
    vattabbaṃ.
  target_quote: '“诸比丘！见苦

    者，亦见苦之集，亦见苦之灭，亦见导至苦灭之道”等一切当知。'
- unit_id: 67-1300-17-28
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:67-1300-17-28
  line: 2069
  source_quote: Yathāha‘‘ yaṃ, bhikkhave, pañcupādānakkhandhā aniccā dukkhā vipariṇāmadhammā.
  target_quote: '如此说，

    “何以故，比库，五取蕴(pañcupādānakkhandha)是无常、苦和会变质的法。”'
- unit_id: 67-1300-29-39
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:67-1300-29-39
  line: 2070
  source_quote: Ayaṃ, bhikkhave, pañcasu upādānakkhandhesu ādīnavo’’ ti.
  target_quote: 比库们，这就是在五取蕴的过患。
confidence: 0.72
review_status: machine_generated
discovery_method: open_synthesis
```

## strategy-open-explanatory-citation

```yaml
id: strategy-open-explanatory-citation
version_id: 74ebf4c5-c243-4948-955d-6c277e29276a
type: strategy
name: 解释与引文显化
description: 对引文、设问、词义解释和定义公式，倾向用引号、冒号、所谓、意思是、说等方式显化原文的解释结构。
definition: 对引文、设问、词义解释和定义公式，倾向用引号、冒号、所谓、意思是、说等方式显化原文的解释结构。
when_used:
- 注释书解释
- 词义训释
- 经论引文
- 设问回答
risks:
- 引号内内容、译者补足和原文引文需要分层保存。
related_entry_ids:
- open-syntax-iti-gloss-b181fd91
- open-syntax-quoted-text-ti-fa894249
- open-syntax-question-explanation-52d70666
evidence:
- unit_id: 9-35-22-34
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:9-35-22-34
  line: 1
  source_quote: Sogate sugatassa vacanabhūte āgame piṭakattaye, tañhi āgacchanti tividhasampattiyo
    etenāti āgamoti vuccati.
  target_quote: 佛语，作为善至之语的阿含，三藏(tipiṭaka)， 所传承的、完成三部分所凭借的，称为阿含。
- unit_id: 9-54-92-124
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:9-54-92-124
  line: 2
  source_quote: Pisitaṃ maṃsaṃ asati bhakkhatīti pisāco, sakuni sakuntiādiko kuverānucaro,
    yadādinā pisitassa pibhāvo, asa ssa ca sācā desabhāvo[ pāṇini6.3.109; moggallānapañcikā1.47].
  target_quote: '吃肉pisita，故为啖肉灵，

    俱吠罗，统治北方的神的追随者，

    pi取pisita(肉)的含义，

    sāca取asa（吃）的含义'
- unit_id: 9-66-81-91
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:9-66-81-91
  line: 3
  source_quote: Pajānaṃ sattānaṃ pati sāmibhūto pajāpati, pajaṃ pāletīti vā pajāpati.
  target_quote: '作为有情（pajā）的主人（pati），即 生主(Pajāpati)；

    对子嗣pajā的保护，即 佑嗣(pajāpati)。'
- unit_id: 9-480-9-24
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:9-480-9-24
  line: 4
  source_quote: Kaṃ pānīyaṃ sevateti kasāvo, avo, atha vā kaṃ savāpetīti kasāvo su
    savane.
  target_quote: '服用的是什么水，故为kasāva——苦涩味；

    流出的是什么，故为kasāva——流出物。'
- unit_id: 9-507-12-24
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:9-507-12-24
  line: 5
  source_quote: Ārammaṇe paṭihaññatīti paṭighaṃ, hana hiṃsāyaṃ, paṭigha saddoyaṃ pulliṅge
    vā bhavati.
  target_quote: '由于在所缘上被折磨，故为厌恶，

    词根hana取伤害的意思，

    paṭigha这个词是阳性(pulliṅga)。'
- unit_id: 9-593-10-47
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:9-593-10-47
  line: 6
  source_quote: Vānarasīsaṃ, taṃsaṇṭhāno vā pāsāṇo ettha atthīti‘‘ vānarasīsan’’ ti
    vattabbe va ssa ba ttaṃ, vaṇṇavipariyayaṃ, dīghaṃ, ṇa ttaṃ, sa ssa lopañca katvā‘‘
    bārāṇasī’’ ti vuttaṃ.
  target_quote: '这里有猴头形状的岩石，

    在说“vānarasīsa”的时候，音节va变化成ba，并加长音（成为bā），

    （音节na）变成ṇa，

    字母sa略去，

    而说成bārāṇasī。'
- unit_id: 9-593-48-78
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:9-593-48-78
  line: 7
  source_quote: Savatthassa isino nivāsanaṭṭhānattā sāvatthi, sabbaṃ dhanamettha atthīti
    vā sāvatthi[ ma. ni. aṭṭha.1.14], sabbassa sāvo, dhanavācako attha saddo, i.
  target_quote: '名叫savattha的仙人居住的地方，故称 尽有城，

    有着一切财富的地方，即 尽有城，

    sabba即sāva，attha这个词表示财富，再加上后缀i。'
- unit_id: 9-673-86-101
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:9-673-86-101
  line: 8
  source_quote: Pajaṃ puttaṃ pāletīti pajāpati, pā pālane, ti, ā ttaṃ, rassattañca
    .
  target_quote: 对子嗣pajā的保护，故为佑嗣，词根pā取保护的意思，ti作为tta的缩写。
confidence: 0.72
review_status: machine_generated
discovery_method: open_synthesis
```

## strategy-open-decomposition

```yaml
id: strategy-open-decomposition
version_id: 74ebf4c5-c243-4948-955d-6c277e29276a
type: strategy
name: 长句拆解与补足
description: 遇到长句、多层注释或隐含关系时，用换行、方括号、分句和补足语把结构展开。
definition: 遇到长句、多层注释或隐含关系时，用换行、方括号、分句和补足语把结构展开。
when_used:
- 长复句
- 多重并列
- 隐含主宾语
- 术语说明
risks:
- 补足内容不能直接当作原文逐词对应。
related_entry_ids:
- open-syntax-bracketed-supplement-syntax-550f5a6c
- open-syntax-long-sentence-decomposition-da6644d0
- open-syntax-newline-decomposition-syntax-585a7090
evidence:
- unit_id: 37-75-278-303
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:37-75-278-303
  line: 21
  source_quote: Dīghanikāyaṭṭhakathāyaṃ pana evaṃ vuttaṃ‘‘ paṭisambhidāppattehi vassasahassaṃ
    aṭṭhāsi, chaḷabhiññehi vassasahassaṃ, tevijjehi vassasahassaṃ, sukkhavipassakehi
    vassasahassaṃ, pātimokkhena vassasahassaṃ aṭṭhāsī’’ ti.
  target_quote: '而在中部义註中则说：

    “依达成辨析者而持续千年，

    依得具六通者者而持续千年，

    依有具足[三]明者(tevijja)者而持续千年，

    依干观者而持续千年，

    依巴帝摩卡而持续千年。”

    Pātimokkhehi vassasahassaṃ aṭṭhāsi .'
- unit_id: 64-106-5-18
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-106-5-18
  line: 26
  source_quote: Tathā ābhisamācārikaādibrahmacariyakavasena, viratiavirativasena,
    nissitānissitavasena, kālapariyantaāpāṇakoṭikavasena, sapariyantāpariyantavasena,
    lokiyalokuttaravasena ca.
  target_quote: 同样地，以增上行仪、初梵行，离、不离，依著、不依著，时限、终生，有限、无限，世间、出世间[而有两种]。
- unit_id: 64-107-5-14
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-107-5-14
  line: 28
  source_quote: Tathā attādhipateyyalokādhipateyyadhammādhipateyyavasena, parāmaṭṭhāparāmaṭṭhapaṭippassaddhivasena,
    visuddhāvisuddhavematikavasena, sekkhāsekkhanevasekkhanāsekkhavasena ca.
  target_quote: 同样地，以我增上、世间增上、法增上，执取、不执取、止息，清净、不清净、疑惑，有学、无学、非有学非无学[而有三种]。
- unit_id: 64-108-5-12
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-108-5-12
  line: 30
  source_quote: Tathā bhikkhubhikkhunīanupasampannagahaṭṭhasīlavasena, pakatiācāradhammatāpubbahetukasīlavasena,
    pātimokkhasaṃvaraindriyasaṃvaraājīvapārisuddhipaccayasannissitasīlavasena ca.
  target_quote: 同样地，以比库戒、比库尼戒、未达上戒、在家戒，自然戒、惯性戒、法性戒、宿因戒，巴帝摩卡防护戒、根防护戒、活命清净戒、资具依止戒[而有四种]。
- unit_id: 64-109-36-38
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-109-36-38
  line: 33
  source_quote: Tathā pahānaveramaṇīcetanāsaṃvarāvītikkamavasena.
  target_quote: 同样地，以舍断、远离、思、克制、不违犯[而有五种]。
- unit_id: 64-110-2-10
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-110-2-10
  line: 34
  source_quote: 11. Tattha ekavidhakoṭṭhāse attho vuttanayeneva veditabbo.
  target_quote: 11.在其中的一种[戒的]部分中，当依前述方法了知[其]义。
- unit_id: 64-110-11-25
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-110-11-25
  line: 35
  source_quote: Duvidhakoṭṭhāse yaṃ bhagavatā‘‘ idaṃ kattabban’’ ti paññattasikkhāpadapūraṇaṃ,
    taṃ cārittaṃ.
  target_quote: 在二种[戒的]部分中，凡世尊[以]“这应当作”，而有所制学处的履行，那即是**“作持[戒]”**。
- unit_id: 64-110-26-40
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-110-26-40
  line: 36
  source_quote: Yaṃ‘‘ idaṃ na kattabban’’ ti paṭikkhittassa akaraṇaṃ, taṃ vārittaṃ.
  target_quote: 凡世尊[以]“这不应作”，而有禁止[之事]的不作，那即是**“止持戒”**。
confidence: 0.72
review_status: machine_generated
discovery_method: open_synthesis
```

## strategy-open-relation-explicitation

```yaml
id: strategy-open-relation-explicitation
version_id: 74ebf4c5-c243-4948-955d-6c277e29276a
type: strategy
name: 关系词显化
description: 把条件、原因、方式、处所、并列、选择和对应关系转成中文关系词或语序结构。
definition: 把条件、原因、方式、处所、并列、选择和对应关系转成中文关系词或语序结构。
when_used:
- 条件句
- 原因句
- X-vasena
- yathā/tathā
- ya-/ta- 对应
- 多项并列
risks:
- 同一巴利形式在不同上下文中可能需要不同中文关系词。
related_entry_ids:
- open-syntax-alternative-series-18071276
- open-syntax-coordinated-series-9a122f4e
- open-syntax-conditional-clause-848b81ac
- open-syntax-relative-correlative-56a796f6
- open-syntax-cause-reason-relation-43b7ef06
- open-syntax-vasena-relation-202efe52
- open-syntax-yatha-tatha-correlative-73c1c803
evidence:
- unit_id: 9-593-10-47
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:9-593-10-47
  line: 6
  source_quote: Vānarasīsaṃ, taṃsaṇṭhāno vā pāsāṇo ettha atthīti‘‘ vānarasīsan’’ ti
    vattabbe va ssa ba ttaṃ, vaṇṇavipariyayaṃ, dīghaṃ, ṇa ttaṃ, sa ssa lopañca katvā‘‘
    bārāṇasī’’ ti vuttaṃ.
  target_quote: '这里有猴头形状的岩石，

    在说“vānarasīsa”的时候，音节va变化成ba，并加长音（成为bā），

    （音节na）变成ṇa，

    字母sa略去，

    而说成bārāṇasī。'
- unit_id: 64-113-11-62
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-113-11-62
  line: 60
  source_quote: Tattha yaṃ‘‘ imināhaṃ sīlena devo vā bhavissāmi devaññataro vā’’ ti(
    dī. ni.3.320; ma. ni.1.186; a. ni.5.206;7.50) evaṃ bhavasampattiṃ ākaṅkhamānena
    pavattitaṃ, idaṃ taṇhānissitaṃ.
  target_quote: “我以此戒，将成为[知名]天人或某位[无名]天人”（长部·3·320；中部·1·186；增支部·5·206,7·50），如此透过希求有成就而产生任何[戒]，这即是爱依著。
- unit_id: 64-120-21-31
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-120-21-31
  line: 102
  source_quote: Vatthumhi vā āpattiyā vā ajjhācāre vā vematikassa sīlaṃ vematikasīlaṃ
    nāma.
  target_quote: 对[罪]事[是否构成罪]、[犯何种]罪或[是否]犯[罪]有疑惑者的戒是有疑戒。
- unit_id: 64-156-85-99
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-156-85-99
  line: 142
  source_quote: Na {nimittaggāhī}ti itthipurisanimittaṃ vā subhanimittādikaṃ vā kilesavatthubhūtaṃ
    nimittaṃ na gaṇhāti, diṭṭhamatteyeva saṇṭhāti.
  target_quote: “不取于相”：对男女相、净相等[增长]烦恼之事而产生的相不执取，[不颠倒而]就只住于所见。
- unit_id: 64-161-2-12
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-161-2-12
  line: 151
  source_quote: ‘ ‘ Nābhijānāmi itthī vā, puriso vā ito gato;
  target_quote: “我不知男女，从此而走过；
- unit_id: 64-163-43-51
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-163-43-51
  line: 156
  source_quote: Tattha kiñcāpi cakkhundriye saṃvaro vā asaṃvaro vā natthi.
  target_quote: 此[“在眼根达成防护”的文句]处，眼根并不存在任何防护或不防护。
- unit_id: 64-163-52-61
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-163-52-61
  line: 157
  source_quote: Na hi cakkhupasādaṃ nissāya sati vā muṭṭhasaccaṃ vā uppajjati.
  target_quote: 因为，[正]念或失念并非依于眼净色而生起。
- unit_id: 64-164-2-14
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-164-2-14
  line: 163
  source_quote: Tatrāpi neva bhavaṅgasamaye, na āvajjanādīnaṃ aññatarasamaye saṃvaro
    vā asaṃvaro vā atthi.
  target_quote: 在那[紧接着生起的路心]中，不论是有分生起时，还是转向等之一生起时，都没有防护或不防护。
confidence: 0.72
review_status: machine_generated
discovery_method: open_synthesis
```

## strategy-open-verbal-relation

```yaml
id: strategy-open-verbal-relation
version_id: 74ebf4c5-c243-4948-955d-6c277e29276a
type: strategy
name: 动作关系处理
description: 对绝对分词、义务式或可行性形式，按上下文处理为先后、方式、原因、应当、可知等关系。
definition: 对绝对分词、义务式或可行性形式，按上下文处理为先后、方式、原因、应当、可知等关系。
when_used:
- -tvā/-tvāna
- -tabba
- -anīya
- 动作串联
- 说明性指令
risks:
- 形式信号只能生成候选，不能机械套用固定译法。
related_entry_ids:
- open-syntax-absolutive-sequence-4e2ef2a0
- open-syntax-gerundive-obligation-fcba4188
evidence:
- unit_id: 9-593-10-47
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:9-593-10-47
  line: 6
  source_quote: Vānarasīsaṃ, taṃsaṇṭhāno vā pāsāṇo ettha atthīti‘‘ vānarasīsan’’ ti
    vattabbe va ssa ba ttaṃ, vaṇṇavipariyayaṃ, dīghaṃ, ṇa ttaṃ, sa ssa lopañca katvā‘‘
    bārāṇasī’’ ti vuttaṃ.
  target_quote: '这里有猴头形状的岩石，

    在说“vānarasīsa”的时候，音节va变化成ba，并加长音（成为bā），

    （音节na）变成ṇa，

    字母sa略去，

    而说成bārāṇasī。'
- unit_id: 64-111-87-116
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-111-87-116
  line: 55
  source_quote: ‘‘ so vata, bhikkhave, bhikkhu ābhisamācārikaṃ dhammaṃ aparipūretvā
    ādibrahmacariyakaṃ dhammaṃ paripūressatīti netaṃ ṭhānaṃ vijjatī’’ ti( a. ni.5.21).
  target_quote: “诸比库，若比库未圆满增上行仪法，而能圆满初梵行法者，无有此理！”（增支部·5·21）
- unit_id: 64-114-2-8
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-114-2-8
  line: 63
  source_quote: Pañcamaduke kālaparicchedaṃ katvā samādinnaṃ sīlaṃ kālapariyantaṃ.
  target_quote: 在第五组二法中，作了时间限制而受持之戒为**“时限[戒]”**。
- unit_id: 64-114-9-18
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-114-9-18
  line: 64
  source_quote: Yāvajīvaṃ samādiyitvā tatheva pavattitaṃ āpāṇakoṭikan ti evaṃ kālapariyantaāpāṇakoṭikavasena
    duvidhaṃ.
  target_quote: 受持直至命终，并就在那[受持]之时所产生的[戒]为**“终生[戒]”**。如此，以时限、终生而有两种[戒]。
- unit_id: 64-120-2-15
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-120-2-15
  line: 100
  source_quote: Catutthattike yaṃ āpattiṃ anāpajjantena pūritaṃ, āpajjitvā vā puna
    katapaṭikammaṃ, taṃ visuddhaṃ.
  target_quote: 在第四组三法中，凡以不犯罪而圆满[之戒]，或者违犯后再作忏悔[之戒]，那即是**“清净[戒]”**。
- unit_id: 64-120-32-53
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-120-32-53
  line: 103
  source_quote: Tattha yoginā avisuddhasīlaṃ visodhetabbaṃ, vematike vatthujjhācāraṃ
    akatvā vimati paṭivinetabbā‘‘ iccassa phāsu bhavissatī’’ ti evaṃ visuddhādivasena
    tividhaṃ.
  target_quote: 其中，禅修者应净化不清净戒，有疑时不违越[该]事，并应消除疑惑，“这样他将安乐”。如此，以清净等而有三种[戒]。
- unit_id: 64-139-77-146
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-139-77-146
  line: 134
  source_quote: Sotena saddaṃ sutvā… pe… ghānena gandhaṃ ghāyitvā… pe… jivhāya rasaṃ
    sāyitvā… pe… kāyena phoṭṭhabbaṃ phusitvā… pe… manasā dhammaṃ viññāya na nimittaggāhī…
    pe… manindriye saṃvaraṃ āpajjatī’’ ti( ma. ni.1.22,411; dī. ni.1.213; a. ni.4.198)
    vuttaṃ, idaṃ indriyas…
  target_quote: '以耳闻声……以鼻嗅香……以舌尝味……以身碰触……以意知法，不取于相……实行意根防护“

    （中部·1·22Yañhissa , bhikkhaveT1.17 , manindriyasaṃvaraṃ asaṃvutassa viharato uppajjeyyuṃ
    āsavā vighātapariḷāhā , manindriyasaṃvaraṃ saṃvutassa viharato evaṃsa te āsavā
    vighātapariḷāhā na honti .

    ；411So iminā ariyena i…'
- unit_id: 64-157-2-27
  unit_key: 74ebf4c5-c243-4948-955d-6c277e29276a:64-157-2-27
  line: 144
  source_quote: Theraṃ kira cetiyapabbatā anurādhapuraṃ piṇḍacāratthāya āgacchantaṃ
    aññatarā kulasuṇhā sāmikena saddhiṃ bhaṇḍitvā sumaṇḍitapasādhitā devakaññā viya
    kālasseva anurādhapurato nikkhamitvā ñātigharaṃ gacchantī antarāmagge disvā vipallatthacittā
    mahāhasitaṃ hasi.
  target_quote: 据说，长老为了集食而从塔山去往阿努拉德普勒期间，某位良家妇女同丈夫争吵后，盛装打扮得犹如天女一般。她清早从阿努拉德普勒出发，前往娘家时，途中见到[长老]后，起了颠倒心而放声大笑。
confidence: 0.72
review_status: machine_generated
discovery_method: open_synthesis
```
