# 翻译策略倾向

本文件由开放式固定搭配、开放式特殊句式和风格观察综合生成。它不以少数预设公式作为策略范围，而是把全量发现的候选归纳为可人工复核的策略假设。

## 摘要索引

| ID | Name | Related Entries | Evidence |
| --- | --- | ---: | ---: |
| strategy-open-frequency-first | 高频证据优先 | 8 | 8 |
| strategy-open-explanatory-citation | 解释与引文显化 | 3 | 8 |
| strategy-open-decomposition | 长句拆解与补足 | 3 | 8 |
| strategy-open-relation-explicitation | 关系词显化 | 5 | 8 |
| strategy-open-verbal-relation | 动作关系处理 | 2 | 8 |

## 条目

## strategy-open-frequency-first

```yaml
id: strategy-open-frequency-first
version_id: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc
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
- open-collocation-bhagava-8b0af50d
- open-collocation-sesesupi-eseva-nayo-3a05cf8f
- open-collocation-sammasambuddho-vijjacaranasampanno-sugato-lokavidu-anuttaro-purisadammasarathi-3bbba4f7
- open-collocation-araham-sammasambuddho-vijjacaranasampanno-sugato-lokavidu-anuttaro-4c77653c
- open-collocation-vijjacaranasampanno-sugato-lokavidu-anuttaro-purisadammasarathi-sattha-84d7cb31
- open-collocation-sugato-lokavidu-anuttaro-purisadammasarathi-sattha-devamanussanam-a89740f1
- open-collocation-lokavidu-anuttaro-purisadammasarathi-sattha-devamanussanam-buddho-4c3d80a1
- open-collocation-anuttaro-purisadammasarathi-sattha-devamanussanam-buddho-bhagava-be0ec826
evidence:
- unit_id: 76-449-2-18
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:76-449-2-18
  line: 477
  source_quote: Idha tathāgato loke uppajjati arahaṃ sammāsambuddho vijjācaraṇasampanno
    sugato lokavidū anuttaro purisadammasārathi satthā devamanussānaṃ buddho bhagavā.
  target_quote: 现在有如来在世界上出现，即阿拉汉，完全自我觉悟者，具足明智与践行(vijjācaraṇasampanna)，善至，知解世界者(lokavidū)，无与伦比的，可调伏之人的驯驭师(purisadammasārathi)，天神和人类的导师，佛，世尊。
- unit_id: 83-98-127-145
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:83-98-127-145
  line: 544
  source_quote: ‘ itipi so bhagavā arahaṃ sammāsambuddho vijjācaraṇasampanno sugato
    lokavidū anuttaro purisadammasārathi satthā devamanussānaṃ buddho bhagavā’ ti.
  target_quote: 那位世尊即阿拉汉，完全自我觉悟者，具足明智与践行，善至，知解世界者，无与伦比的，可调伏之人的驯驭师，天神和人类的导师，佛，世尊。
- unit_id: 83-116-12-33
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:83-116-12-33
  line: 546
  source_quote: ‘ itipi so bhagavā arahaṃ sammāsambuddho vijjācaraṇasampanno sugato
    lokavidū anuttaro purisadammasārathi , satthā devamanussānaṃ buddho bhagavā’ ti.
  target_quote: 那位世尊即阿拉汉，完全自我觉悟者，具足明智与践行，善至，知解世界者，无与伦比的，可调伏之人的驯驭师，天神和人类的导师，佛，世尊。
- unit_id: 84-5-47-49
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:84-5-47-49
  line: 549
  source_quote: Bhagavā etadavoca–
  target_quote: 气运加身者这样说：
- unit_id: 86-563-52-97
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:86-563-52-97
  line: 551
  source_quote: ‘ itipi so bhagavā arahaṃ sammāsambuddho vijjācaraṇasampanno sugato
    lokavidū anuttaro purisadammasārathi satthā devamanussānaṃ buddho bhagavā’ ti[
    bhagavā( sī. syā kaṃ. pī.) idaṃ suttavaṇṇanāya aṭṭhakathāya saṃsandetabb…
  target_quote: 那位世尊即阿拉汉，完全自我觉悟者，具足明智与践行，善至，知解世界者，无与伦比的，可调伏之人的驯驭师，天神和人类的导师，佛，世尊。
- unit_id: 86-741-45-62
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:86-741-45-62
  line: 552
  source_quote: ‘ itipi so bhagavā arahaṃ sammāsambuddho vijjācaraṇasampanno sugato
    lokavidū anuttaro purisadammasārathi satthā devamanussānaṃ buddho bhagavā’ ti.
  target_quote: 那位世尊即阿拉汉，完全自我觉悟者，具足明智与践行，善至，知解世界者，无与伦比的，可调伏之人的驯驭师，天神和人类的导师，佛，世尊。
- unit_id: 86-743-23-41
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:86-743-23-41
  line: 553
  source_quote: ‘ itipi so bhagavā arahaṃ sammāsambuddho vijjācaraṇasampanno sugato
    lokavidū anuttaro purisadammasārathi satthā devamanussānaṃ buddho bhagavā’ ti.
  target_quote: 那位世尊即阿拉汉，完全自我觉悟者，具足明智与践行，善至，知解世界者，无与伦比的，可调伏之人的驯驭师，天神和人类的导师，佛，世尊。
- unit_id: 86-828-48-59
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:86-828-48-59
  line: 557
  source_quote: ‘ itipi so bhagavā arahaṃ sammāsambuddho vijjācaraṇasampanno sugato
    lokavidū anuttaro purisadammasārathi;
  target_quote: ‘那位世尊即阿拉汉，完全自我觉悟者，具足明智与践行，善至，知解世界者，无与伦比的，可调伏之人的驯驭师；
confidence: 0.72
review_status: machine_generated
discovery_method: open_synthesis
```

## strategy-open-explanatory-citation

```yaml
id: strategy-open-explanatory-citation
version_id: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc
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
- unit_id: 9-49-68-76
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-49-68-76
  line: 1
  source_quote: Nibbhayaṭṭhena khemaṃ, khayanti vā etena rāgaggiādayoti khemaṃ.
  target_quote: 以无畏之义为安心，或以其耗尽爱欲之火等，为安心。
- unit_id: 9-95-6-16
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-95-6-16
  line: 2
  source_quote: Sinā soceyye, sināti soceti deveti sineru, eru paccayo.
  target_quote: sinā，泪洗，洗涤、忧伤、悲泣为须弥山，eru为后缀。
- unit_id: 9-95-17-30
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-95-17-30
  line: 3
  source_quote: Mī hiṃsāyaṃ, mināti hiṃsati sabbe pabbate attano uccataraṭṭhenāti
    meru, ru paccayo.
  target_quote: '“mī”，有伤害，丈量，压倒性，在众山中其自身更高，而成为压迫“meru”，ru

    是后缀。'
- unit_id: 9-555-2-11
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-555-2-11
  line: 6
  source_quote: 183. Vedena paññāya īhanti etthāti vedeho.
  target_quote: 那里他们敏而勤学吠陀，而成为勤学者(vedeha)。
- unit_id: 9-555-12-26
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-555-12-26
  line: 7
  source_quote: So eva videho, imaṃ dīpamupādāya sineruno pubbadisābhāgattā pubbo
    ca so videho ceti pubbavideho.
  target_quote: 就这样（上述）的videha，相关的这座大陆由于地处须弥山的东部，结合东和videha而称为东勤学大陆。
- unit_id: 9-556-45-76
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-556-45-76
  line: 8
  source_quote: Kuṃ pāpaṃ rundhatīti kuru, khattiyakumārā, tesaṃ nivāso kurū, paccayalopato
    na vuddhi, sabbatrevaṃ[ pāṇini1.2.524.2.81 suttesu passitabbaṃ].
  target_quote: 阻隔恶劣为止恶，王公贵族王子们居住处为止恶，因为省略后缀而不扩词，一切处都这样。
- unit_id: 9-556-90-101
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-556-90-101
  line: 9
  source_quote: Magena saddhiṃ dhāvantīti magadhā, kvi, maṃsesu gijjhantīti vā magadhā.
  target_quote: '与鹿一起奔跑，为magadhā，

    在肉方面有渴望的，为magadhā。'
- unit_id: 9-556-122-177
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-556-122-177
  line: 10
  source_quote: Kala sadde, iṅga paccayo, kaliṅgā , tesaṃ nivāso kaliṅgā, uttarāpatho[‘‘
    jagannāthā pubbabhāge kaṇhātīrantaraṃ sive kaliṅgadeso saṃvutto’’ ityuttadese(
    thomanidhi)], kaliṃ gaṇhantīti vā kaliṅgā, kvi, kalaṃ madhurasaddaṃ gāyantītivā
    kaliṅgā, assittaṃ, kena suk…
  target_quote: 'kala意为声音，iṅga意为缘，[ 音缘国(kaliṅga)王子]他们的住所，即[kaliṅga]]，位于[ 莲雾洲 ]北部地区[的国家]；

    困苦（kali）的获取（gaha）故为 音缘国，达成；

    将甜美的声音（kala）唱（ge）出来故为 音缘国，其[额外]有[字母]“i”；

    能通过任何（ka）快乐来促成（liṅga）故为 音缘国，liṅga意为是促成，daṇḍaka为词根(dhātu2)。'
confidence: 0.72
review_status: machine_generated
discovery_method: open_synthesis
```

## strategy-open-decomposition

```yaml
id: strategy-open-decomposition
version_id: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc
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
- open-syntax-newline-decomposition-syntax-585a7090
- open-syntax-long-sentence-decomposition-da6644d0
- open-syntax-bracketed-supplement-syntax-550f5a6c
evidence:
- unit_id: 9-95-17-30
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-95-17-30
  line: 3
  source_quote: Mī hiṃsāyaṃ, mināti hiṃsati sabbe pabbate attano uccataraṭṭhenāti
    meru, ru paccayo.
  target_quote: '“mī”，有伤害，丈量，压倒性，在众山中其自身更高，而成为压迫“meru”，ru

    是后缀。'
- unit_id: 9-112-49-59
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-112-49-59
  line: 5
  source_quote: Virūpāni akkhīni yassa virūpakkho, vividhasaṇṭhānāni akkhīni yassa
    vā virūpakkho.
  target_quote: '他的眼睛丑陋为异眸，

    或他的眼睛形态各异为异眸。'
- unit_id: 9-556-90-101
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-556-90-101
  line: 9
  source_quote: Magena saddhiṃ dhāvantīti magadhā, kvi, maṃsesu gijjhantīti vā magadhā.
  target_quote: '与鹿一起奔跑，为magadhā，

    在肉方面有渴望的，为magadhā。'
- unit_id: 9-556-122-177
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-556-122-177
  line: 10
  source_quote: Kala sadde, iṅga paccayo, kaliṅgā , tesaṃ nivāso kaliṅgā, uttarāpatho[‘‘
    jagannāthā pubbabhāge kaṇhātīrantaraṃ sive kaliṅgadeso saṃvutto’’ ityuttadese(
    thomanidhi)], kaliṃ gaṇhantīti vā kaliṅgā, kvi, kalaṃ madhurasaddaṃ gāyantītivā
    kaliṅgā, assittaṃ, kena suk…
  target_quote: 'kala意为声音，iṅga意为缘，[ 音缘国(kaliṅga)王子]他们的住所，即[kaliṅga]]，位于[ 莲雾洲 ]北部地区[的国家]；

    困苦（kali）的获取（gaha）故为 音缘国，达成；

    将甜美的声音（kala）唱（ge）出来故为 音缘国，其[额外]有[字母]“i”；

    能通过任何（ka）快乐来促成（liṅga）故为 音缘国，liṅga意为是促成，daṇḍaka为词根(dhātu2)。'
- unit_id: 9-556-219-228
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-556-219-228
  line: 11
  source_quote: Gaṃ pathaviṃ dhārentīti gandhārā, kittigandhena arantīti vā gandhārā.
  target_quote: '持有行走的大地，为gandhāra，

    或因声名流芳而到达，为gandhāra。'
- unit_id: 9-593-168-194
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-593-168-194
  line: 13
  source_quote: Takka ūhe, ūho ūnapūraṇaṃ, takkanaṃ takko, so sīlaṃ sabhāvo yattha
    sā takkasīlā, yo hi purisakārena ūno, so tattha gantvā tamūnaṃ pūretīti.
  target_quote: 'takka思考的意思，思考即补充不足，

    思考补充不足的动作即takka，

    在思惯这个城市有思考的习惯，'
- unit_id: 9-594-38-54
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-594-38-54
  line: 14
  source_quote: Indaṃ paramissariyabhāvaṃ pāpuṇanti etthāti indapattaṃ, indo vā sakko
    devarājā, so patto etthāti indapattaṃ.
  target_quote: '获得支配他人的权利之地，为帝·印达，

    天帝即萨卡天帝天帝到来的地方，为帝·印达。'
- unit_id: 14-1934-2-14
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:14-1934-2-14
  line: 19
  source_quote: Samaṇassa cīvaraṃ dadāti, samaṇassa rocate saccaṃ, devadattassa suvaṇṇacchattaṃ
    dhārayate yaññadatto.
  target_quote: '把衣给到沙门；

    对沙门来说，现实是值得高兴的；

    yaññadatta为天赐撑起黄金的伞盖。'
confidence: 0.72
review_status: machine_generated
discovery_method: open_synthesis
```

## strategy-open-relation-explicitation

```yaml
id: strategy-open-relation-explicitation
version_id: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc
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
- open-syntax-relative-correlative-56a796f6
- open-syntax-conditional-clause-848b81ac
- open-syntax-vasena-relation-202efe52
evidence:
- unit_id: 9-556-122-177
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-556-122-177
  line: 10
  source_quote: Kala sadde, iṅga paccayo, kaliṅgā , tesaṃ nivāso kaliṅgā, uttarāpatho[‘‘
    jagannāthā pubbabhāge kaṇhātīrantaraṃ sive kaliṅgadeso saṃvutto’’ ityuttadese(
    thomanidhi)], kaliṃ gaṇhantīti vā kaliṅgā, kvi, kalaṃ madhurasaddaṃ gāyantītivā
    kaliṅgā, assittaṃ, kena suk…
  target_quote: 'kala意为声音，iṅga意为缘，[ 音缘国(kaliṅga)王子]他们的住所，即[kaliṅga]]，位于[ 莲雾洲 ]北部地区[的国家]；

    困苦（kali）的获取（gaha）故为 音缘国，达成；

    将甜美的声音（kala）唱（ge）出来故为 音缘国，其[额外]有[字母]“i”；

    能通过任何（ka）快乐来促成（liṅga）故为 音缘国，liṅga意为是促成，daṇḍaka为词根(dhātu2)。'
- unit_id: 64-184-59-72
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:64-184-59-72
  line: 100
  source_quote: Yo hi kuladārake dhāti viya aṅkena vā khandhena vā paribhaṭati, dhāretīti
    attho.
  target_quote: 他好像家庭的乳母/育儿嫂，用腰或背而抱负。
- unit_id: 64-1974-2-26
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:64-1974-2-26
  line: 168
  source_quote: Upekkhāvihārissa pana‘‘ sattā sukhitā vā hontu dukkhato vā vimuccantu,
    sampattasukhato vā mā vimuccantū’’ ti ābhogābhāvato sukhadukkhādiparamatthagāhavimukhabhāvato
    avijjamānaggahaṇadukkhaṃ cittaṃ hoti.
  target_quote: '有趣的是，因为对于舍住(upekkhāvihārī)者来说没有去想“愿众生快乐；愿众生从苦中摆脱，愿众生不失去所得的快乐”，因为摆脱了苦乐等究竟义的想法，

    该心是难以理解那从究竟义上不存在的概念。'
- unit_id: 65-225-75-86
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:65-225-75-86
  line: 178
  source_quote: So ca jānaṃ vā upavadeyya ajānaṃ vā, ubhayathāpi ariyūpavādova hoti.
  target_quote: 如果他批评，无论是否知道（圣者的圣境），两种情况都构成错评圣者。
- unit_id: 65-227-59-70
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:65-227-59-70
  line: 179
  source_quote: Sace disāpakkanto hoti, sayaṃ vā gantvā saddhivihārikādike vā pesetvā
    khamāpetabbo.
  target_quote: 如果被谤者已离开到别地方去，则他应自己去或拜托同门等前去（向圣者）求忏悔。
- unit_id: 65-1499-169-192
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:65-1499-169-192
  line: 204
  source_quote: Pavattidukkhatāya, dukkhassa ca ādīnavatāya ādīnavato, atha vā ādīnaṃ
    vāti gacchati pavattatīti ādīnavo, kapaṇamanussassetaṃ adhivacanaṃ, khandhāpi
    ca kapaṇāyevāti ādīnavasadisatāya ādīnavato.
  target_quote: '由于运转发生之苦状态，由于苦的ādīnavatā，即由于过患

    。

    另一方面：（拆分：）ādīna+va，过得很凄惨，运转得很凄惨，

    就像是孤苦伶仃的人的譬喻，五蕴也是孤苦伶仃，就像其过患，故由于过患。'
- unit_id: 66-159-128-173
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:66-159-128-173
  line: 228
  source_quote: ‘‘ Cīvaran’’ ti ekavacanaṃ ekattamattaṃ vācakanti adhippāyena‘‘ antaravāsakādīsu
    yaṃ kiñcī’’ ti vuttaṃ, jātisaddatāya pana tassa pāḷiyaṃ ekavacananti yattakāni
    cīvarāni yoginā pariharitabbāni, tesaṃ sabbesaṃ ekajjhaṃ gahaṇanti sakkā viññātuṃ,
    yaṃ {kiñcī}ti vā…
  target_quote: '（针对）“‘衣’中用单数来表达只有一个”这样的观点

    而说**“下衣等中的任何一种”，

    因为（衣）这个（词）的种类的含义，在圣典原文中用单数，

    所以，不管禅修者保留多少衣，

    他们全部视为一个整体，

    或者说，“任何一种”**也可以是完整包含一切，而不是不确定词。'
- unit_id: 66-339-79-93
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:66-339-79-93
  line: 248
  source_quote: Evañca katvā‘‘ satiyā vā nikantiyā vā’’ ti vikappavacanañca yuttaṃ
    hoti.
  target_quote: 这样做了之后，“念或欲求”这样是与不同想法/安排的言辞相关。
confidence: 0.72
review_status: machine_generated
discovery_method: open_synthesis
```

## strategy-open-verbal-relation

```yaml
id: strategy-open-verbal-relation
version_id: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc
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
- unit_id: 9-593-168-194
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-593-168-194
  line: 13
  source_quote: Takka ūhe, ūho ūnapūraṇaṃ, takkanaṃ takko, so sīlaṃ sabhāvo yattha
    sā takkasīlā, yo hi purisakārena ūno, so tattha gantvā tamūnaṃ pūretīti.
  target_quote: 'takka思考的意思，思考即补充不足，

    思考补充不足的动作即takka，

    在思惯这个城市有思考的习惯，'
- unit_id: 23-449-67-88
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:23-449-67-88
  line: 53
  source_quote: Micchāpaṭipattīti pāpapakkhe micchāñāṇameva vuccatīti, tathā hi pāpapakkhaṃ
    patvā pañcadhammā ñāṇagatikā honti moho, lobho, diṭṭhi, vitakko, vicāroti.
  target_quote: '所说的邪行道：即为了恶（而生起的）邪智，

    这样确实达到恶的一面之后有五种与智慧类似的法——痴，贪，成见，贯注，徘徊。'
- unit_id: 23-977-128-153
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:23-977-128-153
  line: 66
  source_quote: Pamādapakkhe patitvā vissaṭṭhajjhānānaṃ tatoyevaca appahīnehi orambhāviya
    saṃyojanehi heṭṭhabhāgaṃ ākaḍḍhita mānasānaṃ kāmabhave uppajjamānānaṃ tesaṃ thapetvā
    tihetu kukkaṭṭhabhūtaṃ upacārajjhānacetanaṃ aññaṃ dubbalakammaṃ okāsaṃ nalabhatīti
    vuttaṃ tathā {kām…
  target_quote: 当堕入放逸的一面时，当放弃禅那被下分结(orambhāgiyasaṃyojana)向下拉的心并出现在欲有时，作为殊胜三因的接近禅定的思，不会给其他弱业机会，而说是欲界三因。
- unit_id: 23-980-32-42
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:23-980-32-42
  line: 73
  source_quote: Sayaṃ balavatarassapi sato paṭisandhiṃ adatvā dubbalassa kammantarassa
    upatthambhane kāraṇaṃ natthīti.
  target_quote: '由于无法给出比自己更强的结生，

    因此在弱的业力的支持下不会有（强力结生的）因存在。'
- unit_id: 24-266-443-463
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:24-266-443-463
  line: 90
  source_quote: ‘‘ Aniccampi vaṭṭatī’’ ti samādāna divasaṃ atikkamitvā vikāla bhojanādiṃ
    karontassa vītikkama dosovā duccarita doso vā natthīti adhippāyo.
  target_quote: '非日常(持守)也是合适的，

    过午之后进行非时食的违犯的过患并不是不善行的过失。'
- unit_id: 64-705-85-111
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:64-705-85-111
  line: 111
  source_quote: Thero sabbaṃ hunti paṭibāhitvā‘‘ āvuso, tayā paṭhamaṃ kathito eva
    ācariyamaggo, ācariyamukhato pana anuggahitattā‘ evaṃ ācariyā vadantī’ ti saṇṭhātuṃ
    nāsakkhi.
  target_quote: '长老都用“哼”来质疑，然后对他说：

    “朋友，第一次你所说的是老师们的论调，然而因为你不是从阿阇梨之口学得的，所以你无法确定‘老师们是这么说的’。'
- unit_id: 64-1653-69-74
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:64-1653-69-74
  line: 135
  source_quote: Tasmā ete dose vajjetvā gaṇetabbaṃ.
  target_quote: 因此应该避免这些过失来数（出入息）。
- unit_id: 64-1654-9-21
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:64-1654-9-21
  line: 137
  source_quote: Dhaññamāpako hi nāḷiṃ pūretvā‘‘ ekan’’ ti vatvā okirati.
  target_quote: 量谷者会在装满量米用的筒子后，唸“一”然后倒出（谷粒）。
confidence: 0.72
review_status: machine_generated
discovery_method: open_synthesis
```
