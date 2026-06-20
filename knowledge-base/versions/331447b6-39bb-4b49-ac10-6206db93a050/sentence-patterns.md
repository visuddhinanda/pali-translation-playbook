# 开放式特殊句式翻译技巧候选

本文件按开放式句法信号生成：不限定某几个既有规则，而是从全量语料中寻找可复用的句法处理方式。结果是机器候选，供人工筛选、合并和改写。

- source file: `translations/331447b6-39bb-4b49-ac10-6206db93a050.jsonl`
- chunk count: `117`
- candidate count: `18`
- review status: `machine_generated`

## 摘要索引

| ID | Category | Source Pattern | Translation Pattern | Count | Chunks |
| --- | --- | --- | --- | ---: | ---: |
| open-syntax-iti-gloss-b181fd91 | gloss_or_definition | X-ti / X ti + explanation | 说 / 不 / 以 / 时 / 无 / 如 | 3488 | 107 |
| open-syntax-quoted-text-ti-fa894249 | quotation_or_citation | quoted text + ti / iti | 说 / 以 / 不 / 如 / 由于 / 因此 | 1380 | 74 |
| open-syntax-bracketed-supplement-syntax-550f5a6c | supplemented_syntax | implicit source relation + bracketed target supplement | 以 / 不 / 说 / 时 / 由于 / 无 | 1284 | 71 |
| open-syntax-long-sentence-decomposition-da6644d0 | long_sentence | long multi-clause sentence | 说 / 不 / 以 / 时 / 如 / 无 | 726 | 78 |
| open-syntax-negative-clause-81fab4d0 | negation | na / no / natthi / mā + predicate | 不 / 说 / 无 / 由于 / 没有 / 以 | 704 | 64 |
| open-syntax-absolutive-sequence-4e2ef2a0 | absolutive_or_converb | verb-tvā / verb-tvāna | 说 / 以 / 不 / 如 / 时 / 无 | 698 | 67 |
| open-syntax-locative-topic-01bea915 | locative_topic | ettha / tattha / idha | 说 / 不 / 以 / 由于 / 无 / 时 | 561 | 72 |
| open-syntax-gerundive-obligation-fcba4188 | gerundive_or_obligation | -tabba / -anīya forms | 应 / 当 / 当知 / 以 / 说 / 不 | 397 | 58 |
| open-syntax-coordinated-series-9a122f4e | coordination | X ca Y ca | 以 / 不 / 和 / 说 / 如 / 无 | 230 | 52 |
| open-syntax-simile-comparison-800fcd10 | simile | viya / iva / seyyathāpi | 如 / 不 / 由于 / 以 / 说 / 时 | 221 | 47 |
| open-syntax-question-explanation-52d70666 | question_or_problem | interrogative + explanatory answer | ？ / 说 / 如 / 不 / 时 / 以 | 150 | 47 |
| open-syntax-relative-correlative-56a796f6 | relative_correlative | ya-/yo- relative + ta-/so- correlative | 说 / 不 / 以 / 或 / 时 / 如 | 117 | 37 |
| open-syntax-alternative-series-18071276 | alternative_or_variant | X vā Y vā | 或 / 不 / 时 / 说 / 以 / 如 | 100 | 40 |
| open-syntax-newline-decomposition-syntax-585a7090 | decomposition | complex source + target line breaks | 说 / 以 / 不 / 无 / 如 / 时 | 94 | 34 |
| open-syntax-conditional-clause-848b81ac | conditional | sace / ce / yadi + clause | 如 / 若 / 说 / 不 / 如果 / ？ | 76 | 29 |
| open-syntax-vasena-relation-202efe52 | relation_by_mode | X-vasena | 以 / 说 / 依 / 由于 / 无 / 通过 | 65 | 26 |
| open-syntax-cause-reason-relation-43b7ef06 | cause_or_reason | kāraṇā / hetu / hetunā / paccayā | 不 / 和 / 时 / 以 / 依 / 无 | 44 | 21 |
| open-syntax-yatha-tatha-correlative-73c1c803 | correlative_comparison | yathā ... tathā ... | 同样 / 如 / 不 / 以 / 无 / 依 | 20 | 17 |

## 条目

## open-syntax-iti-gloss-b181fd91

```yaml
id: open-syntax-iti-gloss-b181fd91
version_id: 331447b6-39bb-4b49-ac10-6206db93a050
type: sentence_pattern
name: gloss_or_definition
description: 把被解释词、引文或定义对象显化为冒号、引号、所谓、意思是。
grammar_category: gloss_or_definition
source_pattern: X-ti / X ti + explanation
translation_pattern: 说 / 不 / 以 / 时 / 无 / 如
technique: 把被解释词、引文或定义对象显化为冒号、引号、所谓、意思是。
occurrence_count: 3488
chunk_count: 107
top_chunks:
- chunk_id: chunk-0037
  count: 98
- chunk_id: chunk-0063
  count: 98
- chunk_id: chunk-0104
  count: 95
- chunk_id: chunk-0108
  count: 92
- chunk_id: chunk-0096
  count: 92
- chunk_id: chunk-0009
  count: 88
- chunk_id: chunk-0007
  count: 88
- chunk_id: chunk-0010
  count: 86
evidence:
- unit_id: 1-348-17-29
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:1-348-17-29
  line: 1
  source_quote: '{Bodhimūle}ti ettha bodhīti vuccati rukkhopi, maggopi, sabbaññutañāṇampi,
    nibbānampi.'
  target_quote: 菩提树下：在这里将“菩提”称为树、道、一切知智(sabbaññutañāṇa)、涅槃。
- unit_id: 1-348-30-46
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:1-348-30-46
  line: 2
  source_quote: Tattha hi bodhirukkhamūle paṭhamābhi sambuddhoti ca, antarā ca bodhiṃ
    antarā ca gayanti ca āgataṭṭhāne rukkho.
  target_quote: 因为在这里，他初成正觉于菩提树下，（此）树在菩提与伽耶之间往来之处。
- unit_id: 1-414-48-54
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:1-414-48-54
  line: 3
  source_quote: Samantacakkhu vuccati sabbaññutañāṇanti idaṃ samantacakkhu nāma.
  target_quote: 将普眼称为一切知智。这就叫普眼。
- unit_id: 1-491-38-44
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:1-491-38-44
  line: 4
  source_quote: Gaganūpamadhin ti ettha dhī vuccati sabbaññutañāṇaṃ.
  target_quote: “如空之智”：此处"智"（dhī）特指一切知智。
- unit_id: 1-491-45-49
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:1-491-45-49
  line: 5
  source_quote: Tasmā ākāsūpamasabbaññuta ñāṇavantanti attho.
  target_quote: 因为意指将天空比喻为具有一切知智。
- unit_id: 9-940-18-32
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:9-940-18-32
  line: 6
  source_quote: Pakaṭṭhe tiṭṭhatīti paṭṭhānaṃ, yu[ abhidhānappadīpikā ṭīkā983,1123
    gāthāsupi passitabbaṃ].
  target_quote: 因‘站立于显著位置’，故称‘paṭṭhāna。
- unit_id: 14-2126-2-8
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2126-2-8
  line: 8
  source_quote: Upasagganipāta pubbako samāso abyayībhāva sañño hoti.
  target_quote: 前面有前缀、不变词的复合词称为不变释（复合词）。
- unit_id: 14-2526-2-6
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2526-2-6
  line: 12
  source_quote: Dhīrā taranti kavino puthubuddhināvā.
  target_quote: 智者以广阔智慧之舟横渡$诗人的(海洋)$。
variant_translations:
- 菩提树下：在这里将“菩提”称为树、道、一切知智(sabbaññutañāṇa)、涅槃。
- 因为在这里，他初成正觉于菩提树下，（此）树在菩提与伽耶之间往来之处。
- 将普眼称为一切知智。这就叫普眼。
- “如空之智”：此处"智"（dhī）特指一切知智。
- 因为意指将天空比喻为具有一切知智。
- 因‘站立于显著位置’，故称‘paṭṭhāna。
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.88
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-quoted-text-ti-fa894249

```yaml
id: open-syntax-quoted-text-ti-fa894249
version_id: 331447b6-39bb-4b49-ac10-6206db93a050
type: sentence_pattern
name: quotation_or_citation
description: 将引文或被解释词显化为中文引号、冒号或引用句。
grammar_category: quotation_or_citation
source_pattern: quoted text + ti / iti
translation_pattern: 说 / 以 / 不 / 如 / 由于 / 因此
technique: 将引文或被解释词显化为中文引号、冒号或引用句。
occurrence_count: 1380
chunk_count: 74
top_chunks:
- chunk_id: chunk-0023
  count: 67
- chunk_id: chunk-0009
  count: 55
- chunk_id: chunk-0007
  count: 51
- chunk_id: chunk-0107
  count: 50
- chunk_id: chunk-0010
  count: 46
- chunk_id: chunk-0116
  count: 45
- chunk_id: chunk-0096
  count: 43
- chunk_id: chunk-0102
  count: 41
evidence:
- unit_id: 14-2566-2-10
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2566-2-10
  line: 65
  source_quote: ‘ ‘ Kāle’’ iccetaṃ adhikāratthaṃ veditabbaṃ.
  target_quote: 在时态方面的含义应被了知如下：
- unit_id: 14-2627-6-27
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2627-6-27
  line: 138
  source_quote: Yo koci karoti, taṃ añño‘‘ karohi karohi’’ iccevaṃ bravīti, atha vā
    karontaṃ payojayati= kāreti.
  target_quote: 若有人 (yo koci) 做 (karoti), 其他人 (añño)对他(taṃ)说 (bhavīti), "你来做 (karohi),
    你来做 (karohi)", 又或(atha vā) 他从事 (payojayati) 177Payojayatī ti (Sī).正做 (karontaṃ)
    = (他) 使人做 (kāreti).
- unit_id: 14-2651-2-31
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2651-2-31
  line: 175
  source_quote: Yo koci karoti, taṃ añño‘‘ karohi karohi’’ iccevaṃ bravīti, atha vā
    karontaṃ payojayati = kāreti, kārayati, kārāpeti, kārā payati.
  target_quote: 若有人 (yo koci) 做 (karoti), 其他人 (añño)这样 (evaṃ) 对他 (taṃ)说 (bhavīti)
    , "你来做 (karohi), 你来做(karohi)", 或(atha vā) 他 (him) 从事于 (payojayati) 正做的事 (karontaṃ)
    = (他) 令自己做 (kāreti, kārayati, kārāpeti, kārāpayati).
- unit_id: 14-2651-32-54
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2651-32-54
  line: 176
  source_quote: Ye keci karonti, te aññe‘‘ karotha karotha’’ iccevaṃ bruvanti= kārenti,
    kārayanti, kārāpenti, kārāpayanti.
  target_quote: 若有些人 (ye keci) 做 (karonti),其他一些人 (aññe) 如此 (evaṃ)对他们 (te)说 (bruvanti),
    "你们来做 (karotha), 你们来做 (karotha)" = (他们) 令其他一些人做 (kārenti, kārayanti, kārāpenti,
    kārāpayanti).
- unit_id: 14-2651-55-82
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2651-55-82
  line: 177
  source_quote: Yo koci pacati, taṃ añño‘‘ pacāhi pacāhi’’ iccevaṃ bravīti, atha vā
    pacantaṃ payojayati= pāceti, pācayati, pācāpeti, pācāpayati.
  target_quote: 若有人 (yo koci) 烹饪 (pacati), 其他人 (añño) 这样(evaṃ) 对他 (taṃ)说 (bhavīti),
    "你来烹饪 (pacāhi), 你来烹饪  (pacāhi)", 或者 (atha vā) (他) (him) 从事于 (payojati) 烹饪 (pacantaṃ)
    = (他) 令他烹饪 (pāceti, pācayati, pācāpeti, pācāpayati).
- unit_id: 14-2651-83-103
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2651-83-103
  line: 178
  source_quote: Ye keci pacanti, te aññe‘‘ pacatha pacatha’’ iccevaṃ bruvanti= pācenti,
    pācayanti, pācāpenti.
  target_quote: 若有些人 (ye keci) 烹饪(pacanti), 其他一些人 (aññe) 这样 (evaṃ)对他们 (te)说 (bruvanti)
    , "你们来烹饪 (pacatha), 你们来烹饪 (pacatha)" = (他们) 令他们烹饪 (pāceti, pācayati, pācāpeti,
- unit_id: 16-481-8-24
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:16-481-8-24
  line: 544
  source_quote: ‘‘ Kiṃ panāyasmā devānamindo kammaṃ katvā imaṃ ṭhānaṃ patto’’ tiādīsu
    hi issariye dissati.
  target_quote: 譬如：“具寿，天帝做了什么事而达到该地位……”表达权力之意。
- unit_id: 16-481-25-34
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:16-481-25-34
  line: 545
  source_quote: ‘‘ Ṭhānakusalo hoti akkhaṇavedhī’’ tiādīsu ṭhitiyaṃ.
  target_quote: '**止住熟练者是闪电般的射击者……”表达稳定性之意。'
variant_translations:
- 在时态方面的含义应被了知如下：
- 若有人 (yo koci) 做 (karoti), 其他人 (añño)对他(taṃ)说 (bhavīti), "你来做 (karohi), 你来做 (karohi)",
  又或(atha vā) 他…
- 若有人 (yo koci) 做 (karoti), 其他人 (añño)这样 (evaṃ) 对他 (taṃ)说 (bhavīti) , "你来做 (karohi),
  你来做(karohi)", 或(…
- 若有些人 (ye keci) 做 (karonti),其他一些人 (aññe) 如此 (evaṃ)对他们 (te)说 (bruvanti), "你们来做 (karotha),
  你们来做 (karot…
- 若有人 (yo koci) 烹饪 (pacati), 其他人 (añño) 这样(evaṃ) 对他 (taṃ)说 (bhavīti), "你来烹饪 (pacāhi),
  你来烹饪 (pacāhi)",…
- 若有些人 (ye keci) 烹饪(pacanti), 其他一些人 (aññe) 这样 (evaṃ)对他们 (te)说 (bruvanti) , "你们来烹饪
  (pacatha), 你们来烹饪 (p…
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.88
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-bracketed-supplement-syntax-550f5a6c

```yaml
id: open-syntax-bracketed-supplement-syntax-550f5a6c
version_id: 331447b6-39bb-4b49-ac10-6206db93a050
type: sentence_pattern
name: supplemented_syntax
description: 用方括号补出主语、宾语、语境、逻辑关系或术语说明。
grammar_category: supplemented_syntax
source_pattern: implicit source relation + bracketed target supplement
translation_pattern: 以 / 不 / 说 / 时 / 由于 / 无
technique: 用方括号补出主语、宾语、语境、逻辑关系或术语说明。
occurrence_count: 1284
chunk_count: 71
top_chunks:
- chunk_id: chunk-0116
  count: 58
- chunk_id: chunk-0111
  count: 53
- chunk_id: chunk-0114
  count: 52
- chunk_id: chunk-0101
  count: 52
- chunk_id: chunk-0115
  count: 49
- chunk_id: chunk-0086
  count: 48
- chunk_id: chunk-0087
  count: 47
- chunk_id: chunk-0112
  count: 45
evidence:
- unit_id: 14-2685-2-11
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2685-2-11
  line: 225
  source_quote: Dibbati , thibbati, yujjhati, vijjhati, bujjhati.
  target_quote: '(他) 游戏或发光 (dibbati), (他) 缝 (sibbati), (他) 对抗 (yujjhati), (他) 射击 (vijjhati),
    (他) 知道 (bujjhati).


    "dibbati"结构演变.

    1.divu

    (§457)

    2.div~~u~~ (§521)

    3.div + ti

    (§414)

    4.div + ya


    ti (§447)


    5.div + ya


    ti (§444)Comment [UN120]: please check this.


    6.divv


    a + ti (§…'
- unit_id: 14-2694-2-5
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2694-2-5
  line: 234
  source_quote: Gheppati , gaṇhāti.
  target_quote: '(他) 带 (gheppati, gaṇhāti).


    "gaṇhāti"结构演变.

    1.gaha

    (§457)

    2.gaha + ti

    (§414)

    3.gaha + ṇhā


    ti (§450)


    4.Comment [UN121]: please explain this step and number of sutta.

    5.gaṇhāti

    (§11)'
- unit_id: 23-1037-86-93
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:23-1037-86-93
  line: 573
  source_quote: Natthi attanā gahitaṃ kiñci ārammaṇaṃnāma assāti anārammaṇaṃ.
  target_quote: 对于那[色]来说，的确没有哪个所缘被自身所包含，故为无所缘。
- unit_id: 23-1327-103-112
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:23-1327-103-112
  line: 576
  source_quote: Paṭhapeti saṅkhatadhamme nānāpakārehi paccayabhedehi pavatteti deseti
    etthāti paṭṭhānaṃ.
  target_quote: 在此[经]中，对有为法以各种各样的缘的类别来使其安置、展示、阐述，即为”paṭṭhāna“。
- unit_id: 64-2219-16-30
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:64-2219-16-30
  line: 594
  source_quote: So sattasaññāya samūhatattā vāḷamigayakkharakkhasādivikappaṃ anāvajjamāno
    bhayabheravasaho hoti, aratiratisaho, na iṭṭhāniṭṭhesu ugghātanigghātaṃ pāpuṇāti.
  target_quote: 那位[修行者]由于根除了有情想的缘故，[如同在自身相续中一样，在他人的相续中也（有）界的性质的善见，故象漏尽者一样]，不去分别猛兽、夜叉、罗剎等，因而成为能克服恐惧、害怕的人，[成为]能在不乐与乐中忍耐的人，能在愉快和不愉快中不变得激动、堕落。
- unit_id: 64-2219-31-39
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:64-2219-31-39
  line: 595
  source_quote: Mahāpañño ca pana hoti amatapariyosāno vā sugatiparāyano vāti.
  target_quote: 大慧者或究竟不死，或所往之处[为]善趣；
- unit_id: 64-2223-2-41
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:64-2223-2-41
  line: 599
  source_quote: 361. Ettāvatā ca yaṃ samādhissa vitthāraṃ bhāvanānayañca dassetuṃ‘‘
    ko samādhi, kenaṭṭhena samādhī’’ tiādinā nayena pañhākammaṃ kataṃ, tattha‘‘ kathaṃ
    bhāvetabbo’’ ti imassa padassa sabbappakārato atthavaṇṇanā samattā hoti.
  target_quote: （论修定的结语）到此，为了详示三摩地的修习方法，依“什么是定？什么是定的含义？……”这样的方式已作了提问，在这些[问题]中，“应如何
    修习”那句即依各个方面的含义注释已经完成。
- unit_id: 64-2224-2-10
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:64-2224-2-10
  line: 600
  source_quote: Duvidhoyeva hayaṃ idha adhippeto upacārasamādhi ceva appanāsamādhi
    ca.
  target_quote: 确实，在该[修习]中,意味的就是近行定和安止定这两种三摩地。
variant_translations:
- (他) 游戏或发光 (dibbati), (他) 缝 (sibbati), (他) 对抗 (yujjhati), (他) 射击 (vijjhati), (他)
  知道 (bujjhati). "dib…
- (他) 带 (gheppati, gaṇhāti). "gaṇhāti"结构演变. 1.gaha (§457) 2.gaha + ti (§414) 3.gaha
  + ṇhā ti (§450) 4…
- 对于那[色]来说，的确没有哪个所缘被自身所包含，故为无所缘。
- 在此[经]中，对有为法以各种各样的缘的类别来使其安置、展示、阐述，即为”paṭṭhāna“。
- 那位[修行者]由于根除了有情想的缘故，[如同在自身相续中一样，在他人的相续中也（有）界的性质的善见，故象漏尽者一样]，不去分别猛兽、夜叉、罗剎等，因而成为能克服恐惧、害怕的人，[成为]能在不乐与乐中…
- 大慧者或究竟不死，或所往之处[为]善趣；
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.88
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-long-sentence-decomposition-da6644d0

```yaml
id: open-syntax-long-sentence-decomposition-da6644d0
version_id: 331447b6-39bb-4b49-ac10-6206db93a050
type: sentence_pattern
name: long_sentence
description: 把长句拆为分号、句号、方括号补足或换行结构。
grammar_category: long_sentence
source_pattern: long multi-clause sentence
translation_pattern: 说 / 不 / 以 / 时 / 如 / 无
technique: 把长句拆为分号、句号、方括号补足或换行结构。
occurrence_count: 726
chunk_count: 78
top_chunks:
- chunk_id: chunk-0023
  count: 38
- chunk_id: chunk-0037
  count: 36
- chunk_id: chunk-0096
  count: 30
- chunk_id: chunk-0036
  count: 28
- chunk_id: chunk-0046
  count: 26
- chunk_id: chunk-0098
  count: 25
- chunk_id: chunk-0112
  count: 22
- chunk_id: chunk-0101
  count: 21
evidence:
- unit_id: 1-348-17-29
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:1-348-17-29
  line: 1
  source_quote: '{Bodhimūle}ti ettha bodhīti vuccati rukkhopi, maggopi, sabbaññutañāṇampi,
    nibbānampi.'
  target_quote: 菩提树下：在这里将“菩提”称为树、道、一切知智(sabbaññutañāṇa)、涅槃。
- unit_id: 14-2587-2-13
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2587-2-13
  line: 86
  source_quote: Mā gamā, mā vacā, mā gamī, mā vacī.
  target_quote: 禁止 (mā) 去 (gamā), 禁止 (mā) 说(vacā); 禁止(mā) 去 (gamī), 禁止 (mā) 说 (vacī).
- unit_id: 14-2595-2-25
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2595-2-25
  line: 97
  source_quote: 423,426. {Vattamānā}ti anti, si tha, mi ma, te ante, se vhe, e mhe.
  target_quote: Ti anti, si tha, mi ma; te ante, se vhe, e mhe 为现在时（语尾）。
- unit_id: 14-2596-2-26
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2596-2-26
  line: 98
  source_quote: Vattamānā iccesā saññā {hoti}ti anti, si tha, mi ma, te ante, se vhe,
    e mhe iccetesaṃ dvādasannaṃ padānaṃ.
  target_quote: '(表示）现在时的词尾有: ti anti, si tha, mi ma; te ante, se vhe, e mhe.'
- unit_id: 14-2598-2-23
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2598-2-23
  line: 101
  source_quote: 424,450. Pañcamī tu antu, hitha, mima, taṃ antaṃ, ssu vho, e āmase.
  target_quote: Tu antu, hi tha, mi ma; taṃ antaṃ, ssu vho, e āmase 是命令式（语尾）。
- unit_id: 14-2599-2-26
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2599-2-26
  line: 102
  source_quote: Pañcamī iccesā saññā hoti tu antu, hi tha, mima, taṃ antaṃ, ssu vho,
    e āmase iccetesaṃ dvādasannaṃ padānaṃ.
  target_quote: '命令式有这十二种词尾: Tu antu, hi tha, mi ma; taṃ antaṃ, ssu vho, e āmase.'
- unit_id: 14-2601-2-27
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2601-2-27
  line: 105
  source_quote: 425,453. Sattamī eyya eyyuṃ, eyyā si eyyā tha, eyyāmi eyyāma, etha
    eraṃ, etho eyyāvho, eyyaṃ eyyāmhe.
  target_quote: （表达）潜能式的语尾有：eyya eyyuṃ, eyyāsi eyyātha, eyyāmi eyyāma; etha eraṃ,
    etho eyyāvho, eyyaṃ eyyāmhe。
- unit_id: 14-2602-2-27
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2602-2-27
  line: 106
  source_quote: Sattamī iccesā saññā hoti eyya eyyuṃ, eyyāsi eyyātha, eyyāmi eyyāma,
    etha eraṃ, etho, eyyāvho, eyyaṃ eyyāmhe iccetesaṃ dvādasannaṃ padānaṃ.
  target_quote: '潜能式有这十二个语尾: eyya eyyuṃ, eyyāsi eyyātha, eyyāmi eyyāma; etha eraṃ,
    etho eyyāvho, eyyaṃ eyyāmhe.'
variant_translations:
- 菩提树下：在这里将“菩提”称为树、道、一切知智(sabbaññutañāṇa)、涅槃。
- 禁止 (mā) 去 (gamā), 禁止 (mā) 说(vacā); 禁止(mā) 去 (gamī), 禁止 (mā) 说 (vacī).
- Ti anti, si tha, mi ma; te ante, se vhe, e mhe 为现在时（语尾）。
- '(表示）现在时的词尾有: ti anti, si tha, mi ma; te ante, se vhe, e mhe.'
- Tu antu, hi tha, mi ma; taṃ antaṃ, ssu vho, e āmase 是命令式（语尾）。
- '命令式有这十二种词尾: Tu antu, hi tha, mi ma; taṃ antaṃ, ssu vho, e āmase.'
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.88
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-negative-clause-81fab4d0

```yaml
id: open-syntax-negative-clause-81fab4d0
version_id: 331447b6-39bb-4b49-ac10-6206db93a050
type: sentence_pattern
name: negation
description: 把否定结构译为不、没有、不能、无等。
grammar_category: negation
source_pattern: na / no / natthi / mā + predicate
translation_pattern: 不 / 说 / 无 / 由于 / 没有 / 以
technique: 把否定结构译为不、没有、不能、无等。
occurrence_count: 704
chunk_count: 64
top_chunks:
- chunk_id: chunk-0098
  count: 43
- chunk_id: chunk-0046
  count: 38
- chunk_id: chunk-0007
  count: 37
- chunk_id: chunk-0101
  count: 32
- chunk_id: chunk-0102
  count: 32
- chunk_id: chunk-0023
  count: 31
- chunk_id: chunk-0096
  count: 30
- chunk_id: chunk-0103
  count: 30
evidence:
- unit_id: 14-2586-2-13
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2586-2-13
  line: 85
  source_quote: Hiyyattanīajjatanī iccetā vibhattiyo yadā mā yogā, tadā sabbakāle
    ca honti.
  target_quote: 无论是未完成时还是不定过去时，都可以与 "mā"连用。
- unit_id: 14-2587-2-13
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2587-2-13
  line: 86
  source_quote: Mā gamā, mā vacā, mā gamī, mā vacī.
  target_quote: 禁止 (mā) 去 (gamā), 禁止 (mā) 说(vacā); 禁止(mā) 去 (gamī), 禁止 (mā) 说 (vacī).
- unit_id: 14-2588-7-9
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2588-7-9
  line: 88
  source_quote: Mā gacchāhi.
  target_quote: 禁止(mā) 去 (gacchāhi).
- unit_id: 14-2790-2-9
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2790-2-9
  line: 350
  source_quote: Mikāraggahaṇena hivibhattimhi a kāro kvaci na dīghamāpajjate.
  target_quote: $带有“mi"的$，连接语尾”hi"时，有时字母a不需加强为长音。
- unit_id: 14-2872-2-15
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2872-2-15
  line: 445
  source_quote: 502,493. Yamhi dā dhā mā ṭhā hā pā mahamathādīnamī.
  target_quote: '"dā", "dhā", "mā", "ṭhā", "hā", "pā", "maha", "matha"开头的词根，当遇到 "ya"时,
    有（插入） "ī"  .'
- unit_id: 14-2873-2-19
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2873-2-19
  line: 446
  source_quote: Ya mhi paccaye pare dā dhā mā ṭhā hā pā maha matha iccevamādīnaṃ dhātūnaṃ
    anto ī kāramāpajjate.
  target_quote: 当有词缀"ya" 跟随时, 词根 "dā", "dhā", "mā", "ṭhā", "hā", "pā", "maha", "matha"末端,
    变成 "ī".
- unit_id: 23-244-57-65
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:23-244-57-65
  line: 567
  source_quote: Soyeva yadā attano balena kusalacittaṃ samuṭṭhāpetuṃ na sakkoti.
  target_quote: 正是当以自我之力那善心无法生起时，
- unit_id: 23-523-23-26
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:23-523-23-26
  line: 571
  source_quote: Na paññattidhammeti natthi.
  target_quote: （但）并非不（能作为）概念法所缘。
variant_translations:
- 无论是未完成时还是不定过去时，都可以与 "mā"连用。
- 禁止 (mā) 去 (gamā), 禁止 (mā) 说(vacā); 禁止(mā) 去 (gamī), 禁止 (mā) 说 (vacī).
- 禁止(mā) 去 (gacchāhi).
- $带有“mi"的$，连接语尾”hi"时，有时字母a不需加强为长音。
- '"dā", "dhā", "mā", "ṭhā", "hā", "pā", "maha", "matha"开头的词根，当遇到 "ya"时, 有（插入） "ī"
  .'
- 当有词缀"ya" 跟随时, 词根 "dā", "dhā", "mā", "ṭhā", "hā", "pā", "maha", "matha"末端, 变成 "ī".
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.88
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-absolutive-sequence-4e2ef2a0

```yaml
id: open-syntax-absolutive-sequence-4e2ef2a0
version_id: 331447b6-39bb-4b49-ac10-6206db93a050
type: sentence_pattern
name: absolutive_or_converb
description: 把先行动作、方式、原因或条件关系译成后、而、以、通过等。
grammar_category: absolutive_or_converb
source_pattern: verb-tvā / verb-tvāna
translation_pattern: 说 / 以 / 不 / 如 / 时 / 无
technique: 把先行动作、方式、原因或条件关系译成后、而、以、通过等。
occurrence_count: 698
chunk_count: 67
top_chunks:
- chunk_id: chunk-0023
  count: 61
- chunk_id: chunk-0088
  count: 37
- chunk_id: chunk-0016
  count: 30
- chunk_id: chunk-0114
  count: 26
- chunk_id: chunk-0024
  count: 23
- chunk_id: chunk-0086
  count: 22
- chunk_id: chunk-0108
  count: 21
- chunk_id: chunk-0113
  count: 21
evidence:
- unit_id: 16-481-8-24
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:16-481-8-24
  line: 544
  source_quote: ‘‘ Kiṃ panāyasmā devānamindo kammaṃ katvā imaṃ ṭhānaṃ patto’’ tiādīsu
    hi issariye dissati.
  target_quote: 譬如：“具寿，天帝做了什么事而达到该地位……”表达权力之意。
- unit_id: 16-481-45-56
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:16-481-45-56
  line: 547
  source_quote: ‘‘ Ṭhānañca ṭhānaso ñatvā aṭṭhānañca aṭṭhānaso’’ tiādīsu kāraṇe.
  target_quote: “知道了正确的因，也就（知道了）错误的因”此处表达原因之意。
- unit_id: 22-2376-2-29
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:22-2376-2-29
  line: 561
  source_quote: Api ca kattabbanti kammaṃ, dhāretabbanti dhāriyaṃ, kammañca taṃ dhāriyañcāti
    kammadhāriyaṃ, yaṃkiñci hitakammaṃ, kammadhāriyasaddasadisattā sabbo cāyaṃ samāso
    {kammadhārayo}ti vuccati issa attaṃ katvā.
  target_quote: '此外，”kamma（行为）“指“应做之事”，而“赋予”指”应被赋予之物“，因此“行为”和“赋予”指“行为所赋予的”，即指任何有益于行为的。

    由于类似于‘kammadhāriya’，故这样的词通常也被称为"持业释"，因此指代自己的同时，'
- unit_id: 22-2420-2-21
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:22-2420-2-21
  line: 566
  source_quote: Pādipubbapado ca niccasamāsova, pakaṭṭhaṃ vacanaṃ pāvacanaṃ, dīghattaṃ,
    pakaṭṭhaṃ hutvā nītaṃ paṇītaṃ, pamukhaṃ hutvā dhānaṃ padhānaṃ.
  target_quote: 'pa等前缀也是不变释复合词，（例如：）1.pakaṭṭhaṃ vacanaṃ → pāvacanaṃ圣经，（变成）长（音），2.pakaṭṭhaṃ
    hutvā nītaṃ→ paṇītaṃ适用的

    3. pamukha hutvā dhānaṃ→padhāna首要的。'
- unit_id: 23-1327-86-102
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:23-1327-86-102
  line: 575
  source_quote: Iti sabbesaṃ paccayapaccayuppanna bhūtānaṃ saṅkhatadhammānaṃ paccayā
    satta vuttitāsaṅkhāto paṭiccasamuppādoca so nīyati ñāyati paṭivijjhīyatīti katvā
    nayocāti paṭiccasamuppādanayo.
  target_quote: 综上所述，作为一切缘、缘生的有为法，其缘依存的条件被称为缘起。该法应被引导、应被知、应被通达，故称为“缘起法"。
- unit_id: 44-211-2-42
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:44-211-2-42
  line: 585
  source_quote: Vissajjanā – tena bhante bhagavatā jānatā passatā arahatā sammāsambuddhena
    abhisambuddhakālato sattame vasse manussaloke sāvatthiyaṃ kaṇḍambamūle yamakapāṭihīraṃ
    dassetvā tadanantaraṃ tāvatiṃsadevalokaṃ gantvā tattha paṇḍukambalasilāyaṃ sannipatitvā
    dasahi ca…
  target_quote: 答：尊者，世尊——那位知者、见证者、阿拉汉、正自觉者——在证悟后的第七年，于人间沙瓦提的迦兰陀竹园示现双神变（Yamakapāṭihāriya）后，随即前往三十三天界。在那里，坐在红毯石座上，为从十万轮围世界聚集而来的诸天众宣讲阿毗达摩教法。以此方式讲授了前六部阿毗达摩论，之后继续讲授了未尽的、完整的《发趣论》的第七部大论。
- unit_id: 65-908-59-74
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-908-59-74
  line: 608
  source_quote: Tattha kiñcāpi ṭhapetvā lokuttaraṃ saccadvayaṃ sesaṭṭhānesu ārammaṇavasena
    avijjā uppajjati, evaṃ santepi paṭicchādanavaseneva idha adhippetā.
  target_quote: 这里，除了出世间的（灭、道）二谛，于其他诸处依所缘而生起无明，即使如此，但这里依“遮蔽”之意（解）。
- unit_id: 65-908-75-111
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-908-75-111
  line: 609
  source_quote: Sā hi uppannā dukkhasaccaṃ paṭicchādetvā tiṭṭhati, yāthāvasarasalakkhaṇaṃ
    paṭivijjhituṃ na deti, tathā samudayaṃ, nirodhaṃ, maggaṃ, pubbantasaṅkhātaṃ atītaṃ
    khandhapañcakaṃ, aparantasaṅkhātaṃ anāgataṃ khandhapañcakaṃ, pubbantāparantasaṅkhātaṃ
    tadubhayaṃ, idap…
  target_quote: 由于（无明）生起，苦谛（便）被持续遮蔽，(便）不得如实通达这（苦谛）的作用和特相。同理，集、灭、道，称前际为过去的五蕴,称后际为未来的五蕴,称前后际为两者的（五蕴）。称此缘性(idapaccayatā)、缘生法为此缘性、和缘生法被持续遮蔽。
variant_translations:
- 譬如：“具寿，天帝做了什么事而达到该地位……”表达权力之意。
- “知道了正确的因，也就（知道了）错误的因”此处表达原因之意。
- 此外，”kamma（行为）“指“应做之事”，而“赋予”指”应被赋予之物“，因此“行为”和“赋予”指“行为所赋予的”，即指任何有益于行为的。 由于类似于‘kammadhāriya’，故这样的词通常也被…
- pa等前缀也是不变释复合词，（例如：）1.pakaṭṭhaṃ vacanaṃ → pāvacanaṃ圣经，（变成）长（音），2.pakaṭṭhaṃ hutvā
  nītaṃ→ paṇītaṃ适用的 3…
- 综上所述，作为一切缘、缘生的有为法，其缘依存的条件被称为缘起。该法应被引导、应被知、应被通达，故称为“缘起法"。
- 答：尊者，世尊——那位知者、见证者、阿拉汉、正自觉者——在证悟后的第七年，于人间沙瓦提的迦兰陀竹园示现双神变（Yamakapāṭihāriya）后，随即前往三十三天界。在那里，坐在红毯石座上，为从十…
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.88
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-locative-topic-01bea915

```yaml
id: open-syntax-locative-topic-01bea915
version_id: 331447b6-39bb-4b49-ac10-6206db93a050
type: sentence_pattern
name: locative_topic
description: 把处所或论题入口译为在此、此中、其中、这里。
grammar_category: locative_topic
source_pattern: ettha / tattha / idha
translation_pattern: 说 / 不 / 以 / 由于 / 无 / 时
technique: 把处所或论题入口译为在此、此中、其中、这里。
occurrence_count: 561
chunk_count: 72
top_chunks:
- chunk_id: chunk-0108
  count: 23
- chunk_id: chunk-0101
  count: 22
- chunk_id: chunk-0111
  count: 20
- chunk_id: chunk-0112
  count: 19
- chunk_id: chunk-0114
  count: 18
- chunk_id: chunk-0100
  count: 18
- chunk_id: chunk-0019
  count: 18
- chunk_id: chunk-0107
  count: 17
evidence:
- unit_id: 1-348-17-29
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:1-348-17-29
  line: 1
  source_quote: '{Bodhimūle}ti ettha bodhīti vuccati rukkhopi, maggopi, sabbaññutañāṇampi,
    nibbānampi.'
  target_quote: 菩提树下：在这里将“菩提”称为树、道、一切知智(sabbaññutañāṇa)、涅槃。
- unit_id: 1-348-30-46
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:1-348-30-46
  line: 2
  source_quote: Tattha hi bodhirukkhamūle paṭhamābhi sambuddhoti ca, antarā ca bodhiṃ
    antarā ca gayanti ca āgataṭṭhāne rukkho.
  target_quote: 因为在这里，他初成正觉于菩提树下，（此）树在菩提与伽耶之间往来之处。
- unit_id: 1-491-38-44
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:1-491-38-44
  line: 4
  source_quote: Gaganūpamadhin ti ettha dhī vuccati sabbaññutañāṇaṃ.
  target_quote: “如空之智”：此处"智"（dhī）特指一切知智。
- unit_id: 14-2604-2-20
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2604-2-20
  line: 109
  source_quote: 426,459. Parokkhā au ettha, aṃmha, tthare, ttho vho, iṃ mhe.
  target_quote: 完成时的词尾有a  u, e  ttha, aṃ mha164Amha (Sī).; ttha  re, ttho vho, iṃ
    mhe165Imhe (Sī).
- unit_id: 14-2605-2-24
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2605-2-24
  line: 110
  source_quote: Parokkhā iccesā saññā hoti a u, ettha, aṃ mha, ttha re ttho vho, iṃ
    mhe iccetesaṃ dvādasannaṃ padānaṃ.
  target_quote: '完成时有这十二种词尾: a u, e ttha, aṃ mha; ttha re, ttho vho, iṃ mhe.'
- unit_id: 14-2927-2-12
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2927-2-12
  line: 510
  source_quote: Idha ākhyāte aniddiṭṭhesu sādhanesu kvaci dhātuvibhattipaccayānaṃ
    dīghaviparītādesalopāgamaiccetāni kāriyāni jinavacanānurūpāni kātabbāni.
  target_quote: 这里，$动词未示例的，有时词缀各种变化：长音、颠倒（换位）、替换、省略、插入、等等诸如此类的，应与耆那语保持一致。$
- unit_id: 16-481-2-7
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:16-481-2-7
  line: 543
  source_quote: Tattha ṭhāna saddo issariyaṭhitikhaṇakāraṇesu dissati.
  target_quote: 这里ṭhāna一词表达主权、稳定性、片刻、原因（的含义）。
- unit_id: 16-481-57-68
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:16-481-57-68
  line: 548
  source_quote: Kāraṇañhi yasmā tattha phalaṃ tiṭṭhati tadāyattavuttibhāvena, tasmā
    ṭhānan ti vuccati.
  target_quote: 由于作为原因时，其中果的成立依存于该条件，因此称为：“因”。
variant_translations:
- 菩提树下：在这里将“菩提”称为树、道、一切知智(sabbaññutañāṇa)、涅槃。
- 因为在这里，他初成正觉于菩提树下，（此）树在菩提与伽耶之间往来之处。
- “如空之智”：此处"智"（dhī）特指一切知智。
- 完成时的词尾有a u, e ttha, aṃ mha164Amha (Sī).; ttha re, ttho vho, iṃ mhe165Imhe (Sī).
- '完成时有这十二种词尾: a u, e ttha, aṃ mha; ttha re, ttho vho, iṃ mhe.'
- 这里，$动词未示例的，有时词缀各种变化：长音、颠倒（换位）、替换、省略、插入、等等诸如此类的，应与耆那语保持一致。$
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.88
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-gerundive-obligation-fcba4188

```yaml
id: open-syntax-gerundive-obligation-fcba4188
version_id: 331447b6-39bb-4b49-ac10-6206db93a050
type: sentence_pattern
name: gerundive_or_obligation
description: 把应做、可做、当知、应被理解等义务或可能性显化。
grammar_category: gerundive_or_obligation
source_pattern: -tabba / -anīya forms
translation_pattern: 应 / 当 / 当知 / 以 / 说 / 不
technique: 把应做、可做、当知、应被理解等义务或可能性显化。
occurrence_count: 397
chunk_count: 58
top_chunks:
- chunk_id: chunk-0098
  count: 29
- chunk_id: chunk-0114
  count: 18
- chunk_id: chunk-0102
  count: 18
- chunk_id: chunk-0113
  count: 16
- chunk_id: chunk-0063
  count: 16
- chunk_id: chunk-0115
  count: 15
- chunk_id: chunk-0103
  count: 15
- chunk_id: chunk-0007
  count: 15
evidence:
- unit_id: 9-940-18-32
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:9-940-18-32
  line: 6
  source_quote: Pakaṭṭhe tiṭṭhatīti paṭṭhānaṃ, yu[ abhidhānappadīpikā ṭīkā983,1123
    gāthāsupi passitabbaṃ].
  target_quote: 因‘站立于显著位置’，故称‘paṭṭhāna。
- unit_id: 14-2548-2-10
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2548-2-10
  line: 41
  source_quote: Sabbesaṃ tiṇṇaṃ paṭhamamajjhimuttama purisānaṃ ekābhidhāne paro puriso
    gahetabbo.
  target_quote: 当所有三种人称都（具有）时，$那么按最后一人的人称来取用。$
- unit_id: 14-2549-23-29
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2549-23-29
  line: 45
  source_quote: Evaṃ sesāsu vibhattīsu paro puriso yojetabbo.
  target_quote: 这样在其余变化之后，人称应被结合（进动词的变形）
- unit_id: 14-2566-2-10
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2566-2-10
  line: 65
  source_quote: ‘ ‘ Kāle’’ iccetaṃ adhikāratthaṃ veditabbaṃ.
  target_quote: 在时态方面的含义应被了知如下：
- unit_id: 14-2627-50-52
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2627-50-52
  line: 141
  source_quote: Evamaññepi yojetabbā.
  target_quote: 其他也如此连接。
- unit_id: 14-2639-20-22
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2639-20-22
  line: 157
  source_quote: Evamaññepi yojetabbā.
  target_quote: 其他也应像这样连接。
- unit_id: 14-2644-10-12
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2644-10-12
  line: 165
  source_quote: Evamaññepi yojetabbā.
  target_quote: 其他也应如此连接。
- unit_id: 14-2648-9-11
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2648-9-11
  line: 172
  source_quote: Evamaññepi yojetabbā.
  target_quote: 其他也应如此连接。
variant_translations:
- 因‘站立于显著位置’，故称‘paṭṭhāna。
- 当所有三种人称都（具有）时，$那么按最后一人的人称来取用。$
- 这样在其余变化之后，人称应被结合（进动词的变形）
- 在时态方面的含义应被了知如下：
- 其他也如此连接。
- 其他也应像这样连接。
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.88
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-coordinated-series-9a122f4e

```yaml
id: open-syntax-coordinated-series-9a122f4e
version_id: 331447b6-39bb-4b49-ac10-6206db93a050
type: sentence_pattern
name: coordination
description: 把多项并列译为和、与、以及，或用顿号/换行列举。
grammar_category: coordination
source_pattern: X ca Y ca
translation_pattern: 以 / 不 / 和 / 说 / 如 / 无
technique: 把多项并列译为和、与、以及，或用顿号/换行列举。
occurrence_count: 230
chunk_count: 52
top_chunks:
- chunk_id: chunk-0101
  count: 12
- chunk_id: chunk-0094
  count: 11
- chunk_id: chunk-0110
  count: 10
- chunk_id: chunk-0097
  count: 10
- chunk_id: chunk-0103
  count: 10
- chunk_id: chunk-0019
  count: 10
- chunk_id: chunk-0089
  count: 10
- chunk_id: chunk-0046
  count: 9
evidence:
- unit_id: 1-348-30-46
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:1-348-30-46
  line: 2
  source_quote: Tattha hi bodhirukkhamūle paṭhamābhi sambuddhoti ca, antarā ca bodhiṃ
    antarā ca gayanti ca āgataṭṭhāne rukkho.
  target_quote: 因为在这里，他初成正觉于菩提树下，（此）树在菩提与伽耶之间往来之处。
- unit_id: 14-2571-2-10
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2571-2-10
  line: 70
  source_quote: Āṇatyatthe ca āsīsatthe ca anuttakāle pañcamī vibhatti hoti.
  target_quote: 在（表示）命令、祝愿、以及不定时态中，有命令式的语尾变化。
- unit_id: 14-2574-2-10
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2574-2-10
  line: 73
  source_quote: Anumatyatthe ca parikappatthe ca anuttakāle sattamī vibhatti hoti.
  target_quote: 在（表达）允许、假定、和不定时态中，用潜能式的语尾变化。
- unit_id: 14-2702-2-8
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2702-2-8
  line: 242
  source_quote: Bhāve ca kammani ca attanopadāni honti.
  target_quote: 中间语态也有（表示）状态和被动的含义
- unit_id: 22-2376-75-86
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:22-2376-75-86
  line: 565
  source_quote: So eva ca visesanapadavasena guṇavisesadīpanattā‘ visesanasamāso’
    ti ca vuccati.
  target_quote: 又因为这种复合词通过修饰词揭示属性，故也称为“限定性复合词”。
- unit_id: 48-915-2-36
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:48-915-2-36
  line: 589
  source_quote: Gamanatthato akammakato ca kriyatthā ādhāre kto hoti kattari bhāvakammesu
    ca-yātavanto’ sminti yātaṃ-( ṭhānaṃ) -yā tavanto yānā-yānaṃ yātaṃ-yāyitthāti yāto-(
    patho) -āsitavanto’ sminti āsitaṃ-( ṭhānaṃ) -āsitavanto āsitā-āsana māsitaṃ-ñi.
  target_quote: '"对于具有移动意义且无动作对象（不及物）的动词，在表达动作所属范围（ādhāra）时，用的是‘kto’后缀（形成分词），同时适用于主动、抽象、被动。

    譬如：移动动词 √yā “走” ，yātaṃ（过去分词）："已行走的" → "yātavanto"（完成者，“已行走的人”）。

    yānaṃ（名词）："行走；车辆"。

    yāto（路径）：指“行走的结果”（如“走过的路”）。

    再如：（动词 √ās “坐”）：

    āsitaṃ（过去分词）："已坐的" → "āsitavanto"（完成者，“已坐的人”）。

    āsanaṃ（名词…'
- unit_id: 64-1660-27-36
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:64-1660-27-36
  line: 592
  source_quote: Phuṭṭhaphuṭṭhaṭṭhāneyeva pana gaṇento gaṇanāya ca phusanāya ca manasi
    karoti.
  target_quote: 即仅在每每所触之处而数（息）者，以数与触（同时）作意。
- unit_id: 65-959-106-175
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-959-106-175
  line: 656
  source_quote: Tasmā ayamidha avijjā vijjamānesupi aññesu vatthārammaṇasahajātadhammādīsu
    saṅkhārakāraṇesu‘‘ assādānupassino taṇhā pavaḍḍhatī’’ ti( saṃ. ni.2.52) ca‘‘ avijjāsamudayā
    āsavasamudayo’’ ti( ma. ni.1.104) ca vacanato aññesampi taṇhādīnaṃ saṅkhārahetūnaṃ
    hetūti pa…
  target_quote: 因此，在行的其他因中诸如依处、所缘、俱生法此类即使存在，[但依]这“随观乐味者而爱增”( 相应部. ni.2.52）[经句]及“以无明集而有漏集”(
    ma. ni.1.104)（中部）[之经]句所述，虽有爱等的其他的行之因，但[无明成为]行之因即由于（其）重要性；（又依）“诸比库，无知而有无明者，行作福行”[这经句]，当知阐述了（以无明）作为行之因是由于其明了性及不共的性。
variant_translations:
- 因为在这里，他初成正觉于菩提树下，（此）树在菩提与伽耶之间往来之处。
- 在（表示）命令、祝愿、以及不定时态中，有命令式的语尾变化。
- 在（表达）允许、假定、和不定时态中，用潜能式的语尾变化。
- 中间语态也有（表示）状态和被动的含义
- 又因为这种复合词通过修饰词揭示属性，故也称为“限定性复合词”。
- '"对于具有移动意义且无动作对象（不及物）的动词，在表达动作所属范围（ādhāra）时，用的是‘kto’后缀（形成分词），同时适用于主动、抽象、被动。 譬如：移动动词
  √yā “走” ，yātaṃ（过…'
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.88
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-simile-comparison-800fcd10

```yaml
id: open-syntax-simile-comparison-800fcd10
version_id: 331447b6-39bb-4b49-ac10-6206db93a050
type: sentence_pattern
name: simile
description: 把譬喻关系译为如、譬如、犹如、像。
grammar_category: simile
source_pattern: viya / iva / seyyathāpi
translation_pattern: 如 / 不 / 由于 / 以 / 说 / 时
technique: 把譬喻关系译为如、譬如、犹如、像。
occurrence_count: 221
chunk_count: 47
top_chunks:
- chunk_id: chunk-0105
  count: 23
- chunk_id: chunk-0115
  count: 10
- chunk_id: chunk-0116
  count: 10
- chunk_id: chunk-0056
  count: 10
- chunk_id: chunk-0010
  count: 10
- chunk_id: chunk-0100
  count: 9
- chunk_id: chunk-0114
  count: 8
- chunk_id: chunk-0101
  count: 8
evidence:
- unit_id: 65-1284-77-88
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-1284-77-88
  line: 723
  source_quote: Yasmā vā panettha avijjā appaṭipattimicchāpaṭipattibhāvena satte abhibhavati
    paṭalaṃ viya akkhīni .
  target_quote: 或者，由此，在这[有轮]中，无明 如同覆盖了双眼的翳，以不行道、邪行道的状态，支配诸有情。
- unit_id: 65-1284-89-99
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-1284-89-99
  line: 724
  source_quote: Tadabhibhūto ca bālo punabbhavikehi saṅkhārehi attānaṃ veṭheti kosakārakimi
    viya kosappadesehi.
  target_quote: 为无明所支配的愚人，以 再有之类的 诸行包裹自己，如蚕 以茧房 作茧自缚。
- unit_id: 65-1284-110-119
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-1284-110-119
  line: 725
  source_quote: Upapattinimittaparikappanato viññāṇaṃ paṭisandhiyaṃ anekappakāraṃ
    nāmarūpaṃ abhinibbatteti māyākāro viya māyaṃ.
  target_quote: 因为遍计生起之相，而识于结生中生起 多种的名色，如幻师之现幻相。
- unit_id: 66-82-12-23
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:66-82-12-23
  line: 732
  source_quote: Na aniccatādi viya, ruppanaṃ viya vā sāmaññalakkhaṇaṃ, evamidhāpi
    daṭṭhabbaṃ.
  target_quote: 譬如无常性，或譬如变坏，没有共相,即使如此，也应意识到这（点）。
- unit_id: 66-1138-109-133
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:66-1138-109-133
  line: 819
  source_quote: ‘‘ seyyathāpi, bhikkhave, mahāakālamegho uṭṭhito’’ tiādi( saṃ. ni.5.985;
    pārā.165).
  target_quote: “诸比库，就好象大片不合时宜的积雨云的出现”（相应部.ni.5.985; pārā.165）。
- unit_id: 66-1138-162-180
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:66-1138-162-180
  line: 823
  source_quote: Ariyamaggassa pādakabhūto ayaṃ samādhi anukkamena vaḍḍhitvā ariyamaggabhāvaṃ
    upagato viya hotīti āha‘‘ anupubbena ariyamaggavuddhippatto’’ ti.
  target_quote: 作为圣道基础的这三摩地,逐渐增长，从而象是走近圣道，故说“以次第圣道 的增进”。
- unit_id: 66-1144-2-7
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:66-1144-2-7
  line: 847
  source_quote: Vatthuvijjācariyo viya bhagavā yogīnaṃ anurūpanivāsaṭṭhānupadisanato.
  target_quote: 由于指出禅修者适合居住的处所，故世尊如宅地学的（工程）师。
- unit_id: 66-1147-173-189
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:66-1147-173-189
  line: 866
  source_quote: Parīti pariggahaṭṭho‘‘ pariṇāyikā’’ tiādīsu( dha. sa.16) viya.
  target_quote: “遍”──为 遍持之义类似于智“pariṇāyikā”等（dha. sa.16）。
variant_translations:
- 或者，由此，在这[有轮]中，无明 如同覆盖了双眼的翳，以不行道、邪行道的状态，支配诸有情。
- 为无明所支配的愚人，以 再有之类的 诸行包裹自己，如蚕 以茧房 作茧自缚。
- 因为遍计生起之相，而识于结生中生起 多种的名色，如幻师之现幻相。
- 譬如无常性，或譬如变坏，没有共相,即使如此，也应意识到这（点）。
- “诸比库，就好象大片不合时宜的积雨云的出现”（相应部.ni.5.985; pārā.165）。
- 作为圣道基础的这三摩地,逐渐增长，从而象是走近圣道，故说“以次第圣道 的增进”。
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.88
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-question-explanation-52d70666

```yaml
id: open-syntax-question-explanation-52d70666
version_id: 331447b6-39bb-4b49-ac10-6206db93a050
type: sentence_pattern
name: question_or_problem
description: 把问句或设问译为何、为什么、若问等解释性结构。
grammar_category: question_or_problem
source_pattern: interrogative + explanatory answer
translation_pattern: ？ / 说 / 如 / 不 / 时 / 以
technique: 把问句或设问译为何、为什么、若问等解释性结构。
occurrence_count: 150
chunk_count: 47
top_chunks:
- chunk_id: chunk-0023
  count: 11
- chunk_id: chunk-0110
  count: 9
- chunk_id: chunk-0098
  count: 8
- chunk_id: chunk-0024
  count: 8
- chunk_id: chunk-0094
  count: 7
- chunk_id: chunk-0112
  count: 7
- chunk_id: chunk-0007
  count: 7
- chunk_id: chunk-0107
  count: 6
evidence:
- unit_id: 16-481-8-24
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:16-481-8-24
  line: 544
  source_quote: ‘‘ Kiṃ panāyasmā devānamindo kammaṃ katvā imaṃ ṭhānaṃ patto’’ tiādīsu
    hi issariye dissati.
  target_quote: 譬如：“具寿，天帝做了什么事而达到该地位……”表达权力之意。
- unit_id: 39-239-2-10
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:39-239-2-10
  line: 580
  source_quote: Pucchā – catumahāpadesadhammadesanā panāvuso bhagavatā kattha bhāsitā.
  target_quote: 问：四大教示是法的宣说，那么朋友，世尊是在哪里说的？
- unit_id: 64-2223-2-41
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:64-2223-2-41
  line: 599
  source_quote: 361. Ettāvatā ca yaṃ samādhissa vitthāraṃ bhāvanānayañca dassetuṃ‘‘
    ko samādhi, kenaṭṭhena samādhī’’ tiādinā nayena pañhākammaṃ kataṃ, tattha‘‘ kathaṃ
    bhāvetabbo’’ ti imassa padassa sabbappakārato atthavaṇṇanā samattā hoti.
  target_quote: （论修定的结语）到此，为了详示三摩地的修习方法，依“什么是定？什么是定的含义？……”这样的方式已作了提问，在这些[问题]中，“应如何
    修习”那句即依各个方面的含义注释已经完成。
- unit_id: 64-2224-32-46
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:64-2224-32-46
  line: 604
  source_quote: Tena vuttaṃ‘‘ kathaṃ bhāvetabboti imassa padassa sabbappakārato atthavaṇṇanā
    samattā’’ ti.
  target_quote: 因此说：“ '应如何修习'那句即依各个方面的含义注释已经完成”。
- unit_id: 65-953-11-12
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-953-11-12
  line: 631
  source_quote: Kathaṃ?
  target_quote: 何故？
- unit_id: 65-955-2-18
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-955-2-18
  line: 635
  source_quote: 617. Etthāha– kiṃ panāyamekāva avijjā saṅkhārānaṃ paccayo, udāhu aññepi
    paccayā santīti?
  target_quote: 此处有（人）[质疑]：然而为何仅这一种无明成为诸行的缘，是否还有其它成为（诸行）的缘？
- unit_id: 65-955-19-28
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-955-19-28
  line: 636
  source_quote: Kiṃ panettha, yadi tāva ekāva, ekakāraṇavādo āpajjati.
  target_quote: 那么究竟怎样呢？如果就只有一种（缘），则陷于一因说；
- unit_id: 65-955-45-46
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-955-45-46
  line: 639
  source_quote: Kasmā?
  target_quote: 何故？
variant_translations:
- 譬如：“具寿，天帝做了什么事而达到该地位……”表达权力之意。
- 问：四大教示是法的宣说，那么朋友，世尊是在哪里说的？
- （论修定的结语）到此，为了详示三摩地的修习方法，依“什么是定？什么是定的含义？……”这样的方式已作了提问，在这些[问题]中，“应如何 修习”那句即依各个方面的含义注释已经完成。
- 因此说：“ '应如何修习'那句即依各个方面的含义注释已经完成”。
- 何故？
- 此处有（人）[质疑]：然而为何仅这一种无明成为诸行的缘，是否还有其它成为（诸行）的缘？
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.88
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-relative-correlative-56a796f6

```yaml
id: open-syntax-relative-correlative-56a796f6
version_id: 331447b6-39bb-4b49-ac10-6206db93a050
type: sentence_pattern
name: relative_correlative
description: 把关系从句转成汉语的所、凡、若、此/彼对应关系。
grammar_category: relative_correlative
source_pattern: ya-/yo- relative + ta-/so- correlative
translation_pattern: 说 / 不 / 以 / 或 / 时 / 如
technique: 把关系从句转成汉语的所、凡、若、此/彼对应关系。
occurrence_count: 117
chunk_count: 37
top_chunks:
- chunk_id: chunk-0046
  count: 9
- chunk_id: chunk-0102
  count: 7
- chunk_id: chunk-0056
  count: 7
- chunk_id: chunk-0111
  count: 6
- chunk_id: chunk-0063
  count: 6
- chunk_id: chunk-0036
  count: 5
- chunk_id: chunk-0109
  count: 5
- chunk_id: chunk-0098
  count: 5
evidence:
- unit_id: 14-2627-6-27
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2627-6-27
  line: 138
  source_quote: Yo koci karoti, taṃ añño‘‘ karohi karohi’’ iccevaṃ bravīti, atha vā
    karontaṃ payojayati= kāreti.
  target_quote: 若有人 (yo koci) 做 (karoti), 其他人 (añño)对他(taṃ)说 (bhavīti), "你来做 (karohi),
    你来做 (karohi)", 又或(atha vā) 他从事 (payojayati) 177Payojayatī ti (Sī).正做 (karontaṃ)
    = (他) 使人做 (kāreti).
- unit_id: 14-2651-2-31
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2651-2-31
  line: 175
  source_quote: Yo koci karoti, taṃ añño‘‘ karohi karohi’’ iccevaṃ bravīti, atha vā
    karontaṃ payojayati = kāreti, kārayati, kārāpeti, kārā payati.
  target_quote: 若有人 (yo koci) 做 (karoti), 其他人 (añño)这样 (evaṃ) 对他 (taṃ)说 (bhavīti)
    , "你来做 (karohi), 你来做(karohi)", 或(atha vā) 他 (him) 从事于 (payojayati) 正做的事 (karontaṃ)
    = (他) 令自己做 (kāreti, kārayati, kārāpeti, kārāpayati).
- unit_id: 14-2651-32-54
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2651-32-54
  line: 176
  source_quote: Ye keci karonti, te aññe‘‘ karotha karotha’’ iccevaṃ bruvanti= kārenti,
    kārayanti, kārāpenti, kārāpayanti.
  target_quote: 若有些人 (ye keci) 做 (karonti),其他一些人 (aññe) 如此 (evaṃ)对他们 (te)说 (bruvanti),
    "你们来做 (karotha), 你们来做 (karotha)" = (他们) 令其他一些人做 (kārenti, kārayanti, kārāpenti,
    kārāpayanti).
- unit_id: 14-2651-55-82
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2651-55-82
  line: 177
  source_quote: Yo koci pacati, taṃ añño‘‘ pacāhi pacāhi’’ iccevaṃ bravīti, atha vā
    pacantaṃ payojayati= pāceti, pācayati, pācāpeti, pācāpayati.
  target_quote: 若有人 (yo koci) 烹饪 (pacati), 其他人 (añño) 这样(evaṃ) 对他 (taṃ)说 (bhavīti),
    "你来烹饪 (pacāhi), 你来烹饪  (pacāhi)", 或者 (atha vā) (他) (him) 从事于 (payojati) 烹饪 (pacantaṃ)
    = (他) 令他烹饪 (pāceti, pācayati, pācāpeti, pācāpayati).
- unit_id: 14-2651-83-103
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2651-83-103
  line: 178
  source_quote: Ye keci pacanti, te aññe‘‘ pacatha pacatha’’ iccevaṃ bruvanti= pācenti,
    pācayanti, pācāpenti.
  target_quote: 若有些人 (ye keci) 烹饪(pacanti), 其他一些人 (aññe) 这样 (evaṃ)对他们 (te)说 (bruvanti)
    , "你们来烹饪 (pacatha), 你们来烹饪 (pacatha)" = (他们) 令他们烹饪 (pāceti, pācayati, pācāpeti,
- unit_id: 14-2714-2-10
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2714-2-10
  line: 254
  source_quote: Bhū iccevamādayo ye saddagaṇā, te dhātusaññā honti.
  target_quote: 诸如"bhū"这样开头的音节，它们是词根。
- unit_id: 14-2723-2-11
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2723-2-11
  line: 264
  source_quote: Dvebhūtassa dhātussa yo pubbo, so abbhāsa sañño hoti.
  target_quote: 凡是重叠词根的前面一个音节，叫重复音节。
- unit_id: 41-200-2-11
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:41-200-2-11
  line: 584
  source_quote: ‘ ‘ Yaṃ taṃ isīhi pattabbaṃ, ṭhānaṃ durabhisambhavaṃ;
  target_quote: 凡被诸仙抵达之处，皆是难到达之处。
variant_translations:
- 若有人 (yo koci) 做 (karoti), 其他人 (añño)对他(taṃ)说 (bhavīti), "你来做 (karohi), 你来做 (karohi)",
  又或(atha vā) 他…
- 若有人 (yo koci) 做 (karoti), 其他人 (añño)这样 (evaṃ) 对他 (taṃ)说 (bhavīti) , "你来做 (karohi),
  你来做(karohi)", 或(…
- 若有些人 (ye keci) 做 (karonti),其他一些人 (aññe) 如此 (evaṃ)对他们 (te)说 (bruvanti), "你们来做 (karotha),
  你们来做 (karot…
- 若有人 (yo koci) 烹饪 (pacati), 其他人 (añño) 这样(evaṃ) 对他 (taṃ)说 (bhavīti), "你来烹饪 (pacāhi),
  你来烹饪 (pacāhi)",…
- 若有些人 (ye keci) 烹饪(pacanti), 其他一些人 (aññe) 这样 (evaṃ)对他们 (te)说 (bruvanti) , "你们来烹饪
  (pacatha), 你们来烹饪 (p…
- 诸如"bhū"这样开头的音节，它们是词根。
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.82
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-alternative-series-18071276

```yaml
id: open-syntax-alternative-series-18071276
version_id: 331447b6-39bb-4b49-ac10-6206db93a050
type: sentence_pattern
name: alternative_or_variant
description: 把多项替代或并列解释译为或、或者、换行列举。
grammar_category: alternative_or_variant
source_pattern: X vā Y vā
translation_pattern: 或 / 不 / 时 / 说 / 以 / 如
technique: 把多项替代或并列解释译为或、或者、换行列举。
occurrence_count: 100
chunk_count: 40
top_chunks:
- chunk_id: chunk-0101
  count: 7
- chunk_id: chunk-0113
  count: 6
- chunk_id: chunk-0016
  count: 6
- chunk_id: chunk-0094
  count: 5
- chunk_id: chunk-0108
  count: 5
- chunk_id: chunk-0041
  count: 5
- chunk_id: chunk-0112
  count: 4
- chunk_id: chunk-0116
  count: 4
evidence:
- unit_id: 14-2580-2-12
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2580-2-12
  line: 79
  source_quote: Hiyyopabhuti atīte kāle paccakkhe vā apaccakkhe vā hiyyattanī vibhatti
    hoti.
  target_quote: 过去时中，始于昨天的，现见的或未现见的，是未完成时的语尾变化。
- unit_id: 14-2583-2-13
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2583-2-13
  line: 82
  source_quote: Ajjappabhuti atīte kāle paccakkhe vā apaccakkhe vā samīpe ajjatanī
    vibhatti hoti.
  target_quote: 在过去时中，始于今天，现见的或未现见的，词尾为不定过去时变形。
- unit_id: 14-2756-2-9
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2756-2-9
  line: 302
  source_quote: Pā iccetassa dhātussa pi vādeso hoti vā.
  target_quote: 有时用piva替换词根里的pā.
- unit_id: 64-2219-31-39
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:64-2219-31-39
  line: 595
  source_quote: Mahāpañño ca pana hoti amatapariyosāno vā sugatiparāyano vāti.
  target_quote: 大慧者或究竟不死，或所往之处[为]善趣；
- unit_id: 65-959-2-22
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-959-2-22
  line: 648
  source_quote: Bhagavā hi katthaci padhānattā, katthaci pākaṭattā, katthaci asādhāraṇattā
    desanāvilāsassa ca veneyyānañca anurūpato ekameva hetuṃ vā phalaṃ vā dīpeti.
  target_quote: 由于世尊（教法）有些地方是依主要性，有些地方是依明了性，有些地方是依不共通性，（所以是）微妙的、易于指导的教法，由于（它）顺应（各人）意向，故阐述一因一果。
- unit_id: 65-978-2-23
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-978-2-23
  line: 689
  source_quote: Paṭiccasamuppannadhammesu vimūḷho avijjādīhi saṅkhārādīnaṃ pavattiṃ
    agaṇhanto‘‘ attā jānāti vā na jānāti vā, so eva karoti ca kāreti ca.
  target_quote: 迷妄于诸缘生法之处者，不接受由于无明生起诸行，却妄计“我知或不知，我作或令作”。
- unit_id: 65-978-48-77
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-978-48-77
  line: 692
  source_quote: So puna bhavantare bhavatī’’ ti vā,‘‘ sabbe sattā niyatisaṅgatibhāvapariṇatā’’
    ti( dī. ni.1.168) vā vikappeti.
  target_quote: 他更于后有而存在，或妄计“一切有情被命运、偶然、自性改变”( 长部. ni.1.168)等。
- unit_id: 65-1026-2-11
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-1026-2-11
  line: 704
  source_quote: Dve vā tayo vā dasakā, omato ādinā saha.
  target_quote: 与 最初[所提及的“混合、不混合”二法中的混合的识]一起, 至少有二三十法。
variant_translations:
- 过去时中，始于昨天的，现见的或未现见的，是未完成时的语尾变化。
- 在过去时中，始于今天，现见的或未现见的，词尾为不定过去时变形。
- 有时用piva替换词根里的pā.
- 大慧者或究竟不死，或所往之处[为]善趣；
- 由于世尊（教法）有些地方是依主要性，有些地方是依明了性，有些地方是依不共通性，（所以是）微妙的、易于指导的教法，由于（它）顺应（各人）意向，故阐述一因一果。
- 迷妄于诸缘生法之处者，不接受由于无明生起诸行，却妄计“我知或不知，我作或令作”。
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.8
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-newline-decomposition-syntax-585a7090

```yaml
id: open-syntax-newline-decomposition-syntax-585a7090
version_id: 331447b6-39bb-4b49-ac10-6206db93a050
type: sentence_pattern
name: decomposition
description: 用换行拆解并列、长句、偈颂或注释层次。
grammar_category: decomposition
source_pattern: complex source + target line breaks
translation_pattern: 说 / 以 / 不 / 无 / 如 / 时
technique: 用换行拆解并列、长句、偈颂或注释层次。
occurrence_count: 94
chunk_count: 34
top_chunks:
- chunk_id: chunk-0037
  count: 8
- chunk_id: chunk-0094
  count: 8
- chunk_id: chunk-0114
  count: 8
- chunk_id: chunk-0098
  count: 7
- chunk_id: chunk-0100
  count: 6
- chunk_id: chunk-0097
  count: 5
- chunk_id: chunk-0099
  count: 4
- chunk_id: chunk-0102
  count: 4
evidence:
- unit_id: 14-2677-2-10
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2677-2-10
  line: 217
  source_quote: Bhavati , paṭhati, pacati, jayati.
  target_quote: '(他) 是 (bhavati), (他) 读 (paṭhati), (他) 煮 (pacati), (他) 征服 (jayati).


    "bhavati"结构演变:

    1.bhū

    (§457)

    2.bhū + ti

    (§414)

    3.bhū + a+ ti (§445)

    4.bho + a + ti (§485)

    5.bhava + a + ti (§513)

    6.bhava + a + ti (83)

    7.bhavati

    (§11)


    "pacati"结构演变

    1.paca (§457)

    2.pac~~a~~ (…'
- unit_id: 14-2682-2-13
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2682-2-13
  line: 222
  source_quote: Rundhiti , rundhīti, rundheti, rundhoti, sumbhoti, parisumbhoti.
  target_quote: '(他) 阻止 (rundhiti, rundhīti, rundheti, rundhoti), (他) 攻击 (sumbhoti,
    parisumbhoti).


    "rundhati"结构演变.

    1.rudha

    (§457)

    2.rudh~~a~~ (§521)

    3.rudh + ti

    (§414)

    4.rudh + a


    ti (§445)


    5.ruṃdh + a + ti (§446)

    6.rundh + a + ti (§31)

    7.rundhati

    (§11)'
- unit_id: 14-2685-2-11
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2685-2-11
  line: 225
  source_quote: Dibbati , thibbati, yujjhati, vijjhati, bujjhati.
  target_quote: '(他) 游戏或发光 (dibbati), (他) 缝 (sibbati), (他) 对抗 (yujjhati), (他) 射击 (vijjhati),
    (他) 知道 (bujjhati).


    "dibbati"结构演变.

    1.divu

    (§457)

    2.div~~u~~ (§521)

    3.div + ti

    (§414)

    4.div + ya


    ti (§447)


    5.div + ya


    ti (§444)Comment [UN120]: please check this.


    6.divv


    a + ti (§…'
- unit_id: 14-2688-2-18
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2688-2-18
  line: 228
  source_quote: Abhisuṇoti , abhisuṇāti, saṃvuṇoti, saṃvuṇāti, āvuṇoti, āvuṇāti, pāpuṇoti,
    pāpuṇāti.
  target_quote: '(他）听 (abhisuṇoti, abhisuṇāti); (他) 抑制 (saṃvuṇoti, saṃvuṇāti); (他)
    绑住 (āvuṇoti, āvuṇāti); (他) 得到 (pāpuṇoti, pāpuṇāti).


    "suṇoti"结构演变.

    1.su

    (§457)

    2.su + ti

    (§414)

    3.su + ṇu


    ti (§448)


    4.su + ṇo


    ti (§485)


    5.suṇoti

    (§11)


    "suṇāti" 结构演变.

    1.su

    (§457)

    2.su + ti

    …'
- unit_id: 14-2691-2-13
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2691-2-13
  line: 231
  source_quote: Kiṇāti , jināti, dhunāti, munāti, lunāti, punāti.
  target_quote: '(他) 买 (kiṇāti), (他) 征服 (jināti), (他) 抖落 (dhunāti), (他) 知道 (munāti),
    (他) 切 (lunāti), (他) 清理 (punāti205Muṇāti, luṇāti, puṇati (Sī).).


    "kiṇāti"结构演变.

    1.kī

    (§457)

    2.kī + ti

    (§414)

    3.kī + nā


    ti (§449)


    4.ki


    nā + ti (§517)


    5.ki + ṇā + ti (§449)

    6.kiṇāti

    (§11)'
- unit_id: 14-2694-2-5
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2694-2-5
  line: 234
  source_quote: Gheppati , gaṇhāti.
  target_quote: '(他) 带 (gheppati, gaṇhāti).


    "gaṇhāti"结构演变.

    1.gaha

    (§457)

    2.gaha + ti

    (§414)

    3.gaha + ṇhā


    ti (§450)


    4.Comment [UN121]: please explain this step and number of sutta.

    5.gaṇhāti

    (§11)'
- unit_id: 14-2697-2-15
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2697-2-15
  line: 237
  source_quote: Tanoti , tanohi, karoti, karohi, kayi rati, kayirāhi.
  target_quote: '(他) 伸展 (tanoti), (你来)伸展 (tanohi); (他) 做 (karoti), (你来) 做 (karohi);
    $(他) 被做 (kayirati), (你) 应该做 (kayirāhi).$


    "tanoti"的结构演变.

    1.tanu

    (§457)

    2.tan~~u~~ (§521)

    3.tan + ti

    (§414)

    4.tan + o+ ti (§451)

    5.tanoti

    (§11)'
- unit_id: 14-2700-2-13
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2700-2-13
  line: 240
  source_quote: Coreti , corayati, cinteti, cintayati, manteti, mantayati.
  target_quote: '(他) 偷 (coreti, corayati); (他) 想 (cinteti, cintayati); (他) 商量 (manteti,
    mantayati).


    "coreti"结构演变.

    1.cura

    (§457)

    2.cur~~a~~ (§521)

    3.cur +ti

    (§414)

    4.cur + ṇe


    ti (§452)


    5.cur + ṇe


    ti (§523)


    6.cor + e + ti (§483)

    7.coreti

    (§11)


    "corayati"结构演变.

    1.cura

    (§457…'
variant_translations:
- '(他) 是 (bhavati), (他) 读 (paṭhati), (他) 煮 (pacati), (他) 征服 (jayati). "bhavati"结构演变:
  1.bhū (§457) 2.bh…'
- (他) 阻止 (rundhiti, rundhīti, rundheti, rundhoti), (他) 攻击 (sumbhoti, parisumbhoti).
  "rundhati"结构演变. 1…
- (他) 游戏或发光 (dibbati), (他) 缝 (sibbati), (他) 对抗 (yujjhati), (他) 射击 (vijjhati), (他)
  知道 (bujjhati). "dib…
- (他）听 (abhisuṇoti, abhisuṇāti); (他) 抑制 (saṃvuṇoti, saṃvuṇāti); (他) 绑住 (āvuṇoti, āvuṇāti);
  (他) 得到 (pā…
- (他) 买 (kiṇāti), (他) 征服 (jināti), (他) 抖落 (dhunāti), (他) 知道 (munāti), (他) 切 (lunāti),
  (他) 清理 (punāti2…
- (他) 带 (gheppati, gaṇhāti). "gaṇhāti"结构演变. 1.gaha (§457) 2.gaha + ti (§414) 3.gaha
  + ṇhā ti (§450) 4…
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.79
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-conditional-clause-848b81ac

```yaml
id: open-syntax-conditional-clause-848b81ac
version_id: 331447b6-39bb-4b49-ac10-6206db93a050
type: sentence_pattern
name: conditional
description: 把条件从句译为若、如果、当……时等条件关系。
grammar_category: conditional
source_pattern: sace / ce / yadi + clause
translation_pattern: 如 / 若 / 说 / 不 / 如果 / ？
technique: 把条件从句译为若、如果、当……时等条件关系。
occurrence_count: 76
chunk_count: 29
top_chunks:
- chunk_id: chunk-0098
  count: 10
- chunk_id: chunk-0023
  count: 8
- chunk_id: chunk-0100
  count: 5
- chunk_id: chunk-0094
  count: 4
- chunk_id: chunk-0096
  count: 4
- chunk_id: chunk-0101
  count: 4
- chunk_id: chunk-0102
  count: 4
- chunk_id: chunk-0016
  count: 4
evidence:
- unit_id: 14-2594-2-9
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2594-2-9
  line: 95
  source_quote: So ce taṃ yānaṃ alabhissā, agacchissā.
  target_quote: 如果(ce) 他 (so) 已经得到了 (alabhissā) 那 (taṃ) 马车 (yānaṃ), 他 (so) 就已经来了 (agacchissā).
- unit_id: 14-2594-10-17
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2594-10-17
  line: 96
  source_quote: Te ce taṃ yānaṃ alabhissaṃsu, agacchissaṃsu.
  target_quote: 如果(ce) 他们 (te)已经得到了 (alabhissaṃsu) 那 (taṃ) 马车 (yānaṃ),他们 (te) 就已经来了
    (agacchissaṃsu).
- unit_id: 65-955-19-28
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-955-19-28
  line: 636
  source_quote: Kiṃ panettha, yadi tāva ekāva, ekakāraṇavādo āpajjati.
  target_quote: 那么究竟怎样呢？如果就只有一种（缘），则陷于一因说；
- unit_id: 65-971-2-14
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-971-2-14
  line: 681
  source_quote: Kathaṃ pana yo etesu vimuyhati, so tividhepete saṅkhāre karotīti ce.
  target_quote: （问:)再[说说]任何那迷妄于(缘生法)的人，他们则怎样造作这三种行？
- unit_id: 65-1061-2-47
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-1061-2-47
  line: 713
  source_quote: 635. Yopi vadeyya‘‘ evaṃ santepi ete saṅkhārā vijjamānā vā phalassa
    paccayā siyuṃ, avijjamānā vā, yadi ca vijjamānā pavattikkhaṇeyeva nesaṃ vipākena
    bhavitabbaṃ, atha avijjamānā pavattito pubbe pacchā ca niccaṃ phalāvahā siyun’’
    ti, so evaṃ vattabbo–
  target_quote: 还有人会问：“即使这样，彼等诸行的存在是果之缘？亦或不存在[是果之缘]？假若存在[而为果之缘]，[象这样时]仅应在[诸行 ]发生的刹那，而有那些诸行的果；若不存在[彼等诸行而为果之缘]，[象这样时]则在发生前、和后
    常能感果？”对此答复如下：
- unit_id: 65-1256-2-10
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-1256-2-10
  line: 718
  source_quote: Evaṃ sati avijjāpaccayā saṅkhārāti idaṃ ādimattakathanaṃ virujjhatīti
    ce.
  target_quote: （问）如果这样，岂非与“无明缘行”这　有始性之说相矛盾吗？
- unit_id: 66-875-127-144
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:66-875-127-144
  line: 743
  source_quote: Yadi vimokkhantikaṃ, atha kasmā aññehi khīṇāsavehi asādhāraṇanti āha‘‘
    saha sabbaññutaññāṇassa paṭilābhā’’ ti.
  target_quote: 若说‘终极解脱者’，为何不与其他的漏尽者共？答：‘因与一切知智[同时]获得’。"
- unit_id: 66-1148-45-97
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:66-1148-45-97
  line: 872
  source_quote: Yadi‘‘ satova assasati sato passasatī’’ ti etassa vibhaṅge( ma. ni.3.148;
    saṃ. ni.5.986; pārā.165) vuttaṃ, atha kasmā‘‘ assasati passasati’’ cceva avatvā‘‘
    satokārī’’ ti vuttaṃ?
  target_quote: 若“只念出息念入息”即指这分别(ma. ni.3.148; saṃ. ni.5.986; pārā.165)中所说，又为何不说“出息入息”而说“念行者”呢？
variant_translations:
- 如果(ce) 他 (so) 已经得到了 (alabhissā) 那 (taṃ) 马车 (yānaṃ), 他 (so) 就已经来了 (agacchissā).
- 如果(ce) 他们 (te)已经得到了 (alabhissaṃsu) 那 (taṃ) 马车 (yānaṃ),他们 (te) 就已经来了 (agacchissaṃsu).
- 那么究竟怎样呢？如果就只有一种（缘），则陷于一因说；
- （问:)再[说说]任何那迷妄于(缘生法)的人，他们则怎样造作这三种行？
- 还有人会问：“即使这样，彼等诸行的存在是果之缘？亦或不存在[是果之缘]？假若存在[而为果之缘]，[象这样时]仅应在[诸行 ]发生的刹那，而有那些诸行的果；若不存在[彼等诸行而为果之缘]，[象这样时]…
- （问）如果这样，岂非与“无明缘行”这 有始性之说相矛盾吗？
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.76
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-vasena-relation-202efe52

```yaml
id: open-syntax-vasena-relation-202efe52
version_id: 331447b6-39bb-4b49-ac10-6206db93a050
type: sentence_pattern
name: relation_by_mode
description: 把方式、依据、范围译为以、依、由于、按照……方式。
grammar_category: relation_by_mode
source_pattern: X-vasena
translation_pattern: 以 / 说 / 依 / 由于 / 无 / 通过
technique: 把方式、依据、范围译为以、依、由于、按照……方式。
occurrence_count: 65
chunk_count: 26
top_chunks:
- chunk_id: chunk-0111
  count: 6
- chunk_id: chunk-0108
  count: 5
- chunk_id: chunk-0102
  count: 5
- chunk_id: chunk-0109
  count: 4
- chunk_id: chunk-0103
  count: 4
- chunk_id: chunk-0104
  count: 4
- chunk_id: chunk-0107
  count: 3
- chunk_id: chunk-0110
  count: 3
evidence:
- unit_id: 65-1141-13-34
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:65-1141-13-34
  line: 715
  source_quote: Cattāri pana bhūtāni avisesato paṭisandhiyaṃ pavatte ca yaṃ yaṃ āyatanaṃ
    uppajjati, tassa tassa vasena pañcannampi cakkhāyatanādīnaṃ sahajātanissayaatthiavigatapaccayehi
    catudhā paccayā honti.
  target_quote: 但是，四大种通常在五蕴有的结生和转起过程中，无论生起的某个处，其以什么样的方式（生起），对眼处等五处，则以俱生、依止、有、不离去缘四种为缘。
- unit_id: 66-1133-2-10
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:66-1133-2-10
  line: 753
  source_quote: Soḷasavatthukan ti catūsu anupassanāsu catunnaṃ catukkānaṃ vasena
    soḷasaṭṭhānaṃ.
  target_quote: 十六事：四随观中 以四个一组、四组的方式 计十六处。
- unit_id: 66-1137-108-122
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:66-1137-108-122
  line: 800
  source_quote: '{Madhūro}ti iṭṭho, cetasikasukhapaṭilābhasaṃvattanaṃ tikacatukkajjhānavasena,
    upekkhāya vā santabhāvena sukhagatikattā sabbesampi vasena veditabbaṃ.'
  target_quote: 美妙：令人愉快的， 当知籍由三、四禅那导致心乐(cetasikasukha)的获得, 或者，通过捨的寂静 导向乐，故当知（是）通过一切的[
    禅那 ]的方式。
- unit_id: 66-1139-2-9
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:66-1139-2-9
  line: 824
  source_quote: Ayaṃ panattho virāganirodhapaṭinissaggānupassanānaṃ vasena sammadeva
    yujjati.
  target_quote: 而且，该意通过离染的灭尽(virāganirodha)、定弃观的方式就完全（有）可能。
- unit_id: 66-1149-87-94
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:66-1149-87-94
  line: 882
  source_quote: Paṭinissaggānupassī {assāsavasenā}ti paṭinissaggānupassī hutvā assasanassa
    vasena.
  target_quote: 依paṭinissaggānupassī出息：paṭinissaggānupassī是出息的方式。
- unit_id: 66-1154-2-32
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:66-1154-2-32
  line: 913
  source_quote: '{Navahākārehī}ti bhāvanamanuyuñjantassa pubbenāparaṃ aladdhavisesassa
    kevalaṃ addhānavasena ādito vuttā tayo ākārā, te ca kho ekacco assāsaṃ suṭṭhu
    sallakkheti, ekacco passāsaṃ, ekacco tadubhayanti imesaṃ tiṇṇaṃ puggalānaṃ vasena.'
  target_quote: 以九种方法：对于专心修习的前后 没有区别 而仅以时间的方式，于开头所说的三种方法，该三种（方法）中的一部分人易观察出息, 一部分人[易观察]入息,
    一部分人[易观察]这两者（出息入息），因此是以这三种人的方式。
- unit_id: 66-1155-2-30
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:66-1155-2-30
  line: 916
  source_quote: Kāmaṃ cettha ekassa puggalassa tayo eva ākārā labbhanti, tantivasena
    pana sabbesaṃ pāḷiāruḷhattā, tesaṃ vasena parikammassa kātabbattā ca‘‘ tatrāyaṃ
    bhikkhu navahākārehī’’ ti vuttaṃ.
  target_quote: 这[九种方法]中，对于一个人的确仅存在三种方法，然而由于所有（方法）以圣典的方式出现于（巴利）三藏圣典, 以及由于根据这些（方法）应能进行遍作(三摩地)，因此说：“此中，这比丘以九种方法”。
- unit_id: 66-1159-87-97
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:66-1159-87-97
  line: 929
  source_quote: '{Chandavasenā}ti tathāpavattachandassa vasena savisesaṃ bhāvanamanuyuñjantassa
    kammaṭṭhānaṃ vuddhiṃ phātiṃ gamentassa.'
  target_quote: '与（之前的）欲相比: 对于专心修习使业处趋向于增长、增加时，与象这样发生的欲相比有区别，'
variant_translations:
- 但是，四大种通常在五蕴有的结生和转起过程中，无论生起的某个处，其以什么样的方式（生起），对眼处等五处，则以俱生、依止、有、不离去缘四种为缘。
- 十六事：四随观中 以四个一组、四组的方式 计十六处。
- 美妙：令人愉快的， 当知籍由三、四禅那导致心乐(cetasikasukha)的获得, 或者，通过捨的寂静 导向乐，故当知（是）通过一切的[ 禅那 ]的方式。
- 而且，该意通过离染的灭尽(virāganirodha)、定弃观的方式就完全（有）可能。
- 依paṭinissaggānupassī出息：paṭinissaggānupassī是出息的方式。
- 以九种方法：对于专心修习的前后 没有区别 而仅以时间的方式，于开头所说的三种方法，该三种（方法）中的一部分人易观察出息, 一部分人[易观察]入息, 一部分人[易观察]这两者（出息入息），因此是以这三…
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.74
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-cause-reason-relation-43b7ef06

```yaml
id: open-syntax-cause-reason-relation-43b7ef06
version_id: 331447b6-39bb-4b49-ac10-6206db93a050
type: sentence_pattern
name: cause_or_reason
description: 把原因、条件或依据译为因为、由于、以……为缘。
grammar_category: cause_or_reason
source_pattern: kāraṇā / hetu / hetunā / paccayā
translation_pattern: 不 / 和 / 时 / 以 / 依 / 无
technique: 把原因、条件或依据译为因为、由于、以……为缘。
occurrence_count: 44
chunk_count: 21
top_chunks:
- chunk_id: chunk-0094
  count: 7
- chunk_id: chunk-0036
  count: 6
- chunk_id: chunk-0037
  count: 5
- chunk_id: chunk-0103
  count: 3
- chunk_id: chunk-0046
  count: 3
- chunk_id: chunk-0096
  count: 2
- chunk_id: chunk-0099
  count: 2
- chunk_id: chunk-0104
  count: 2
evidence:
- unit_id: 14-2625-2-11
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2625-2-11
  line: 135
  source_quote: 432,362. Dhātuliṅgehi parā paccayā.
  target_quote: 跟在词根词干后面的是后缀。
- unit_id: 14-2626-2-6
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2626-2-6
  line: 136
  source_quote: Dhātuliṅgaiccetehi parā paccayā honti.
  target_quote: 跟着词根词干后面的就是后缀。
- unit_id: 14-2629-2-15
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2629-2-15
  line: 143
  source_quote: Tija gupa kita mānu iccetehi dhātūhi kha cha sa iccete paccayā honti
    vā.
  target_quote: 在词根 "tija"（忍耐）, "gupa"（厌恶）, "kita"（治愈）, 和 "māna"(研究，评估）后面, 有时有后缀 "kha",
    "cha", 和 "sa".
- unit_id: 14-2633-2-18
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2633-2-18
  line: 148
  source_quote: Bhuja ghasa hara su pā iccevamādīhi dhātūhi tumicchatthesu kha cha
    sa iccete paccayā honti vā.
  target_quote: 用"bhuja"吞, "ghasa"吃, "hara"拿, 带上, "su"听, 和"pā"喝, 这些词根开头，在表达自我意图时，有时有后缀"kha",
    "cha"和 "sa".
- unit_id: 14-2650-2-14
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2650-2-14
  line: 174
  source_quote: Sabbehi dhātūhi ṇeṇaya ṇāpe ṇāpaya iccete paccayā honti kārita saññā
    ca hetvatthe.
  target_quote: 所有词根后的"ṇe", "ṇaya", "ṇāpe", "ṇāpaya"这些词缀，是使役（动词）的标记和目的。
- unit_id: 14-2657-2-8
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2657-2-8
  line: 189
  source_quote: Caggahaṇena āra āla iccete paccayā honti.
  target_quote: 连接 "ca"的 还有词缀 "āra" 和 "āla".
- unit_id: 14-2681-2-11
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2681-2-11
  line: 221
  source_quote: Caggahaṇena i ī e o iccete paccayā honti niggahitapubbañca.
  target_quote: 以"ca" 连接后缀 "i", "ī", "e", "o" 时，前面会有鼻音 .
- unit_id: 14-2687-2-13
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2687-2-13
  line: 227
  source_quote: Su iccevamādito dhātugaṇato ṇu ṇā u ṇā iccete paccayā honti kattari.
  target_quote: 以 "su"开头的这类词根后,有后缀 "ṇu", "ṇā", "uṇā" 时是主动语态.
variant_translations:
- 跟在词根词干后面的是后缀。
- 跟着词根词干后面的就是后缀。
- 在词根 "tija"（忍耐）, "gupa"（厌恶）, "kita"（治愈）, 和 "māna"(研究，评估）后面, 有时有后缀 "kha", "cha", 和
  "sa".
- 用"bhuja"吞, "ghasa"吃, "hara"拿, 带上, "su"听, 和"pā"喝, 这些词根开头，在表达自我意图时，有时有后缀"kha", "cha"和
  "sa".
- 所有词根后的"ṇe", "ṇaya", "ṇāpe", "ṇāpaya"这些词缀，是使役（动词）的标记和目的。
- 连接 "ca"的 还有词缀 "āra" 和 "āla".
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.7
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-yatha-tatha-correlative-73c1c803

```yaml
id: open-syntax-yatha-tatha-correlative-73c1c803
version_id: 331447b6-39bb-4b49-ac10-6206db93a050
type: sentence_pattern
name: correlative_comparison
description: 把如是对应结构译为如……同样/也……。
grammar_category: correlative_comparison
source_pattern: yathā ... tathā ...
translation_pattern: 同样 / 如 / 不 / 以 / 无 / 依
technique: 把如是对应结构译为如……同样/也……。
occurrence_count: 20
chunk_count: 17
top_chunks:
- chunk_id: chunk-0102
  count: 3
- chunk_id: chunk-0052
  count: 2
- chunk_id: chunk-0037
  count: 1
- chunk_id: chunk-0053
  count: 1
- chunk_id: chunk-0107
  count: 1
- chunk_id: chunk-0109
  count: 1
- chunk_id: chunk-0110
  count: 1
- chunk_id: chunk-0111
  count: 1
evidence:
- unit_id: 14-2673-2-15
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:14-2673-2-15
  line: 213
  source_quote: Yathā heṭṭhā bhāvakammesu ya paccayassa ādeso hoti tathā kattaripi
    ya paccayassa ādeso kātabbo.
  target_quote: 正如上文在（表示）状态和被动的词缀中ya被替换，同理，主动语态里的词缀ya也应被替换。
- unit_id: 17-2051-14-23
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:17-2051-14-23
  line: 552
  source_quote: Yathā hi tappurisa saddo guṇamativatto, tathā ayaṃ samāsopi.
  target_quote: 尽管超出了偏正短语该词的原本属性，但同样是这种复合词。
- unit_id: 22-2375-7-46
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:22-2375-7-46
  line: 560
  source_quote: Yathā kammaṃ kriyañca payojanañca dvayaṃ dhāreti kamme sati tassa
    dvayassa sambhavato, tathā ayaṃ samāso ekassa atthassa dve nāmāni dhāreti imasmiṃ
    samāse sati ekatthajotakassa nāmadvayassa sambhavatoti[ ka.324; rū.339; nī.702].
  target_quote: '这就好比‘行为’（kamma）具有‘动作’和‘目的’双重属性，

    只要有行为存在，这两者就必然存在，

    该复合词也是如此，具有相同含义的两个名称，

    只要该复合词存在，表达同一个含义两个名称就必然存在。'
- unit_id: 22-2376-30-42
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:22-2376-30-42
  line: 562
  source_quote: Yathā hi kammadhāriyasaddo ekassa atthassa dve nāmāni dhāreti, tathā
    ayaṃ samāsopīti.
  target_quote: 这种复合词还可以这样：即如‘行为所赋予的’一词用一个含义被赋予了两个名称。
- unit_id: 66-1142-16-30
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:66-1142-16-30
  line: 845
  source_quote: Daḷhan ti thiraṃ, yathā satokārissa upacārappanābhedo samādhi ijjhati,
    tathā thāmagataṃ katvāti attho.
  target_quote: 坚固的：牢固的，如同有念者达成的近行定、安止定那样达到稳定之意。
- unit_id: 66-1185-13-33
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:66-1185-13-33
  line: 1110
  source_quote: '{Phusanā}ti assāsapassāse gaṇentassa gaṇanaṃ paṭisaṃharitvā te satiyā
    anubandhantassa yathā appanā hoti, tathā cittaṃ ṭhapentassa ca nāsikaggādiṭṭhānassa
    nesaṃ phusanā.'
  target_quote: 触：当数入出息时（是安止的）；当舍弃数（息）后，那些[ 入出息 ]以念的方式保持，也是安止的；当令心安置时，也以同样的方式，将鼻腔末端处作为那些[  入出息
    ]的触。
- unit_id: 66-1206-44-58
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:66-1206-44-58
  line: 1260
  source_quote: Yathā matānaṃ samuṭṭhāpakacittābhāvato, evaṃ asaññībhūtānaṃ mucchāparetānaṃ,
    asaññīsu vā jātānaṃ, tathā nirodhasamāpannānaṃ.
  target_quote: 对于死者，由于等起的心不存在的状态，故[不会发生入出息 ]，同样地，对于无想天人受无知觉的折磨，在无想（天）出生，故[不会发生]，同理，对于灭尽定(nirodhasamāpanna)者
    [也不会发生]。
- unit_id: 66-1231-116-133
  unit_key: 331447b6-39bb-4b49-ac10-6206db93a050:66-1231-116-133
  line: 1439
  source_quote: Atha vā so evaṃ viratto yathā diṭṭhaṃ saṅkhāragataṃ, tathā adiṭṭhaṃ
    attano ñāṇena nirodheti, no samudeti.
  target_quote: 又或，厌离的那[禅修者]息灭所见的行依照什么样的方式 ，依同样的方式 以自我的智息灭、而非生起未见的[过去和未来的行法]。
variant_translations:
- 正如上文在（表示）状态和被动的词缀中ya被替换，同理，主动语态里的词缀ya也应被替换。
- 尽管超出了偏正短语该词的原本属性，但同样是这种复合词。
- 这就好比‘行为’（kamma）具有‘动作’和‘目的’双重属性， 只要有行为存在，这两者就必然存在， 该复合词也是如此，具有相同含义的两个名称， 只要该复合词存在，表达同一个含义两个名称就必然存在。
- 这种复合词还可以这样：即如‘行为所赋予的’一词用一个含义被赋予了两个名称。
- 坚固的：牢固的，如同有念者达成的近行定、安止定那样达到稳定之意。
- 触：当数入出息时（是安止的）；当舍弃数（息）后，那些[ 入出息 ]以念的方式保持，也是安止的；当令心安置时，也以同样的方式，将鼻腔末端处作为那些[ 入出息 ]的触。
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.66
review_status: machine_generated
discovery_method: open_syntactic_signal
```
