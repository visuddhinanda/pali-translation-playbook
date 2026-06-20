# 开放式特殊句式翻译技巧候选

本文件按开放式句法信号生成：不限定某几个既有规则，而是从全量语料中寻找可复用的句法处理方式。结果是机器候选，供人工筛选、合并和改写。

- source file: `translations/5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0.jsonl`
- chunk count: `55`
- candidate count: `18`
- review status: `machine_generated`

## 摘要索引

| ID | Category | Source Pattern | Translation Pattern | Count | Chunks |
| --- | --- | --- | --- | ---: | ---: |
| open-syntax-quoted-text-ti-fa894249 | quotation_or_citation | quoted text + ti / iti | 说 / ？ / 时 / 不 / 如 / 以 | 3799 | 54 |
| open-syntax-iti-gloss-b181fd91 | gloss_or_definition | X-ti / X ti + explanation | 说 / 时 / 不 / 如 / ？ / 以 | 3773 | 54 |
| open-syntax-absolutive-sequence-4e2ef2a0 | absolutive_or_converb | verb-tvā / verb-tvāna | 说 / 时 / 如 / 不 / 以 / ？ | 3006 | 53 |
| open-syntax-bracketed-supplement-syntax-550f5a6c | supplemented_syntax | implicit source relation + bracketed target supplement | 时 / 说 / 如 / 不 / 以 / ？ | 1602 | 53 |
| open-syntax-long-sentence-decomposition-da6644d0 | long_sentence | long multi-clause sentence | 说 / 时 / 不 / 如 / ？ / 以 | 1396 | 53 |
| open-syntax-negative-clause-81fab4d0 | negation | na / no / natthi / mā + predicate | 不 / 说 / 时 / 如 / 无 / ？ | 1302 | 54 |
| open-syntax-question-explanation-52d70666 | question_or_problem | interrogative + explanatory answer | ？ / 说 / 时 / 如 / 不 / 当 | 696 | 52 |
| open-syntax-newline-decomposition-syntax-585a7090 | decomposition | complex source + target line breaks | 说 / 时 / 以 / 不 / 在此 / 无 | 595 | 43 |
| open-syntax-locative-topic-01bea915 | locative_topic | ettha / tattha / idha | 在此 / 说 / 不 / 时 / 以 / 如 | 411 | 53 |
| open-syntax-simile-comparison-800fcd10 | simile | viya / iva / seyyathāpi | 如 / 说 / 时 / 不 / 以 / 无 | 241 | 48 |
| open-syntax-alternative-series-18071276 | alternative_or_variant | X vā Y vā | 或 / 不 / 说 / 时 / 如 / 以 | 233 | 51 |
| open-syntax-conditional-clause-848b81ac | conditional | sace / ce / yadi + clause | 说 / 不 / 如 / 若 / 时 / 以 | 147 | 46 |
| open-syntax-coordinated-series-9a122f4e | coordination | X ca Y ca | 和 / 时 / 不 / 以 / 说 / 如 | 132 | 50 |
| open-syntax-relative-correlative-56a796f6 | relative_correlative | ya-/yo- relative + ta-/so- correlative | 说 / 若 / 不 / 以 / 如 / 时 | 127 | 44 |
| open-syntax-gerundive-obligation-fcba4188 | gerundive_or_obligation | -tabba / -anīya forms | 应 / 不 / 时 / 说 / 如 / ？ | 83 | 36 |
| open-syntax-cause-reason-relation-43b7ef06 | cause_or_reason | kāraṇā / hetu / hetunā / paccayā | ？ / 说 / 时 / 因为 / 以 / 当 | 52 | 28 |
| open-syntax-yatha-tatha-correlative-73c1c803 | correlative_comparison | yathā ... tathā ... | 如 / 同样 / 不 / 时 / 说 / 无 | 18 | 13 |
| open-syntax-vasena-relation-202efe52 | relation_by_mode | X-vasena | 以 / 不 / 通过 / 说 / 如 / 无 | 16 | 9 |

## 条目

## open-syntax-quoted-text-ti-fa894249

```yaml
id: open-syntax-quoted-text-ti-fa894249
version_id: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0
type: sentence_pattern
name: quotation_or_citation
description: 将引文或被解释词显化为中文引号、冒号或引用句。
grammar_category: quotation_or_citation
source_pattern: quoted text + ti / iti
translation_pattern: 说 / ？ / 时 / 不 / 如 / 以
technique: 将引文或被解释词显化为中文引号、冒号或引用句。
occurrence_count: 3799
chunk_count: 54
top_chunks:
- chunk_id: chunk-0015
  count: 112
- chunk_id: chunk-0014
  count: 104
- chunk_id: chunk-0032
  count: 103
- chunk_id: chunk-0027
  count: 101
- chunk_id: chunk-0002
  count: 97
- chunk_id: chunk-0026
  count: 92
- chunk_id: chunk-0016
  count: 91
- chunk_id: chunk-0017
  count: 90
evidence:
- unit_id: 122-42-2-12
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-42-2-12
  line: 26
  source_quote: Tato naṃ dukkhamanveti, cakkaṃva vahato padan’’ ti.
  target_quote: 由此苦随彼，如轮随牛足。”
- unit_id: 122-44-13-65
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-44-13-65
  line: 32
  source_quote: So ekadivasaṃ nhānatitthaṃ nhatvā natvā āgacchanto antarāmagge sampannapattasākhaṃ
    ekaṃ vanappatiṃ disvā‘‘ ayaṃ mahesakkhāya devatāya pariggahito bhavissatī’’ ti
    tassa heṭṭhābhāgaṃ sodhāpetvā pākāraparikkhepaṃ kārāpetvā vālukaṃ okirāpetvā dhajapaṭākaṃ
    ussāpet…
  target_quote: 一天，他在浴场洗完澡回来的路上看到一棵枝繁叶茂的树王，（心想）这树上一定住有大威力的天神。于是他将树下打扫干净，建了围墙并铺上沙子，还竖了一面旗幡。装饰了树王后合掌说：“如果能获得一个儿子或者女儿，我将向您做大敬奉。”许完愿他就离开了。
- unit_id: 122-46-56-81
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-56-81
  line: 45
  source_quote: Anāthapiṇḍikopi visākhāpi mahāupāsikā nibaddhaṃ divasassa dve vāre
    tathāgatassa upaṭṭhānaṃ gacchanti, gacchantā ca‘‘ daharasāmaṇerā no hatthe olokessantī’’
    ti tucchahatthā na gatapubbā.
  target_quote: 给孤独[大富翁]和维沙卡大近事女总是每天两次为前去侍奉如来，当去的时候想“年轻的比库、沙马内勒们将会看着我们的手”，就从未空手而去。
- unit_id: 122-46-125-152
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-125-152
  line: 50
  source_quote: So kira‘‘ tathāgato buddhasukhumālo khattiyasukhumālo,‘ bahūpakāro
    me, gahapatī’ ti mayhaṃ dhammaṃ desento kilameyyā’’ ti satthari adhimattasinehena
    pañhaṃ na pucchati.
  target_quote: 据说他[出于]：“如来身为佛陀而娇嫩，身为刹帝利而娇嫩，若[想着]‘[这位]家主对我助益良多’而对我说法会疲倦”，由于对导师强烈的敬爱而没有问过问题。
- unit_id: 122-46-153-164
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-153-164
  line: 51
  source_quote: Satthā pana tasmiṃ nisinnamatteyeva‘‘ ayaṃ seṭṭhi maṃ arakkhitabbaṭṭhāne
    rakkhati.
  target_quote: 正当他坐着时，导师则[想]：“这位富翁在不需要保护之处保护我。
- unit_id: 122-46-186-196
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-186-196
  line: 53
  source_quote: Esa maṃ arakkhitabbaṭṭhāne rakkhatī’’ ti ekaṃ dhammadesanaṃ kathetiyeva.
  target_quote: 他在不需要保护之处保护我。”于是（佛陀）就作了一场佛法开示。
- unit_id: 122-47-39-76
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-47-39-76
  line: 57
  source_quote: Athekadivasaṃ mahāpālo ariyasāvake gandhamālādihatthe vihāraṃ gacchante
    disvā‘‘ ayaṃ mahājano kuhiṃ gacchatī’’ ti pucchitvā‘‘ dhammassavanāyā’’ ti sutvā‘‘
    ahampi gamissāmī’’ ti gantvā satthāraṃ vanditvā parisapariyante nisīdi.
  target_quote: 当时有一天，大护（mahāpāla）看到那些圣弟子们手里拿着香和花前去寺院，问道：“这一大群人是去哪里呢？”听到“去听闻佛法”后，就说“我也要去。”去到后礼敬了导师，接着在听众的外围坐下。
- unit_id: 122-48-50-76
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-48-50-76
  line: 61
  source_quote: ‘‘ paralokaṃ gacchantaṃ puttadhītaro vā bhātaro vā bhogā vā nānugacchanti,
    sarīrampi attanā saddhiṃ na gacchati, kiṃ me gharāvāsena pabbajissāmī’’ ti.
  target_quote: “儿女、兄弟、财产都不会跟着去往来世者而去，连身体也不会同自己一起去，住在家里对我又有何益？我要出家！”
variant_translations:
- 由此苦随彼，如轮随牛足。”
- 一天，他在浴场洗完澡回来的路上看到一棵枝繁叶茂的树王，（心想）这树上一定住有大威力的天神。于是他将树下打扫干净，建了围墙并铺上沙子，还竖了一面旗幡。装饰了树王后合掌说：“如果能获得一个儿子或者女儿，…
- 给孤独[大富翁]和维沙卡大近事女总是每天两次为前去侍奉如来，当去的时候想“年轻的比库、沙马内勒们将会看着我们的手”，就从未空手而去。
- 据说他[出于]：“如来身为佛陀而娇嫩，身为刹帝利而娇嫩，若[想着]‘[这位]家主对我助益良多’而对我说法会疲倦”，由于对导师强烈的敬爱而没有问过问题。
- 正当他坐着时，导师则[想]：“这位富翁在不需要保护之处保护我。
- 他在不需要保护之处保护我。”于是（佛陀）就作了一场佛法开示。
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.88
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-iti-gloss-b181fd91

```yaml
id: open-syntax-iti-gloss-b181fd91
version_id: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0
type: sentence_pattern
name: gloss_or_definition
description: 把被解释词、引文或定义对象显化为冒号、引号、所谓、意思是。
grammar_category: gloss_or_definition
source_pattern: X-ti / X ti + explanation
translation_pattern: 说 / 时 / 不 / 如 / ？ / 以
technique: 把被解释词、引文或定义对象显化为冒号、引号、所谓、意思是。
occurrence_count: 3773
chunk_count: 54
top_chunks:
- chunk_id: chunk-0051
  count: 102
- chunk_id: chunk-0047
  count: 92
- chunk_id: chunk-0010
  count: 91
- chunk_id: chunk-0038
  count: 90
- chunk_id: chunk-0046
  count: 90
- chunk_id: chunk-0013
  count: 89
- chunk_id: chunk-0006
  count: 87
- chunk_id: chunk-0035
  count: 86
evidence:
- unit_id: 122-22-2-8
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-22-2-8
  line: 11
  source_quote: Na sādhayati sesānaṃ, sattānaṃ hitasampadaṃ;
  target_quote: 未令余有情，获利益成就；
- unit_id: 122-25-2-7
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-25-2-7
  line: 13
  source_quote: Iti āsīsamānena, dantena samacārinā;
  target_quote: 如是有期待，已调.寂行者，
- unit_id: 122-36-2-6
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-36-2-6
  line: 21
  source_quote: Manaso pītipāmojjaṃ, atthadhammūpanissitanti.
  target_quote: 带给诸智者，内心喜与乐。
- unit_id: 122-41-2-10
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-41-2-10
  line: 25
  source_quote: Manasā ce paduṭṭhena, bhāsati vā karoti vā;
  target_quote: 若以染污意，或语或行动；
- unit_id: 122-42-2-12
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-42-2-12
  line: 26
  source_quote: Tato naṃ dukkhamanveti, cakkaṃva vahato padan’’ ti.
  target_quote: 由此苦随彼，如轮随牛足。”
- unit_id: 122-43-2-6
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-43-2-6
  line: 27
  source_quote: Ayaṃ dhammadesanā kattha bhāsitāti?
  target_quote: 这佛法开示是在何处说的呢？
- unit_id: 122-43-9-11
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-43-9-11
  line: 29
  source_quote: Kaṃ ārabbhāti?
  target_quote: 就谁（而说的）呢？
- unit_id: 122-44-13-65
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-44-13-65
  line: 32
  source_quote: So ekadivasaṃ nhānatitthaṃ nhatvā natvā āgacchanto antarāmagge sampannapattasākhaṃ
    ekaṃ vanappatiṃ disvā‘‘ ayaṃ mahesakkhāya devatāya pariggahito bhavissatī’’ ti
    tassa heṭṭhābhāgaṃ sodhāpetvā pākāraparikkhepaṃ kārāpetvā vālukaṃ okirāpetvā dhajapaṭākaṃ
    ussāpet…
  target_quote: 一天，他在浴场洗完澡回来的路上看到一棵枝繁叶茂的树王，（心想）这树上一定住有大威力的天神。于是他将树下打扫干净，建了围墙并铺上沙子，还竖了一面旗幡。装饰了树王后合掌说：“如果能获得一个儿子或者女儿，我将向您做大敬奉。”许完愿他就离开了。
variant_translations:
- 未令余有情，获利益成就；
- 如是有期待，已调.寂行者，
- 带给诸智者，内心喜与乐。
- 若以染污意，或语或行动；
- 由此苦随彼，如轮随牛足。”
- 这佛法开示是在何处说的呢？
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
version_id: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0
type: sentence_pattern
name: absolutive_or_converb
description: 把先行动作、方式、原因或条件关系译成后、而、以、通过等。
grammar_category: absolutive_or_converb
source_pattern: verb-tvā / verb-tvāna
translation_pattern: 说 / 时 / 如 / 不 / 以 / ？
technique: 把先行动作、方式、原因或条件关系译成后、而、以、通过等。
occurrence_count: 3006
chunk_count: 53
top_chunks:
- chunk_id: chunk-0051
  count: 85
- chunk_id: chunk-0013
  count: 79
- chunk_id: chunk-0008
  count: 77
- chunk_id: chunk-0017
  count: 75
- chunk_id: chunk-0032
  count: 74
- chunk_id: chunk-0050
  count: 73
- chunk_id: chunk-0014
  count: 70
- chunk_id: chunk-0015
  count: 70
evidence:
- unit_id: 122-10-2-8
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-10-2-8
  line: 3
  source_quote: Tassa pāde namassitvā, sambuddhassa sirīmato;
  target_quote: 顶礼彼正觉，具福者之足；
- unit_id: 122-11-2-8
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-11-2-8
  line: 4
  source_quote: Saddhammañcassa pūjetvā, katvā saṅghassa cañjaliṃ.
  target_quote: 我亦敬正法，合掌向僧团。
- unit_id: 122-31-2-7
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-31-2-7
  line: 17
  source_quote: Pahāyāropayitvāna , tantibhāsaṃ manoramaṃ;
  target_quote: 精简增加后，圣典语悦意。
- unit_id: 122-34-2-9
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-34-2-9
  line: 19
  source_quote: Kevalaṃ taṃ vibhāvetvā, sesaṃ tameva atthato;
  target_quote: 我皆阐明彼，依义释其余。
- unit_id: 122-44-13-65
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-44-13-65
  line: 32
  source_quote: So ekadivasaṃ nhānatitthaṃ nhatvā natvā āgacchanto antarāmagge sampannapattasākhaṃ
    ekaṃ vanappatiṃ disvā‘‘ ayaṃ mahesakkhāya devatāya pariggahito bhavissatī’’ ti
    tassa heṭṭhābhāgaṃ sodhāpetvā pākāraparikkhepaṃ kārāpetvā vālukaṃ okirāpetvā dhajapaṭākaṃ
    ussāpet…
  target_quote: 一天，他在浴场洗完澡回来的路上看到一棵枝繁叶茂的树王，（心想）这树上一定住有大威力的天神。于是他将树下打扫干净，建了围墙并铺上沙子，还竖了一面旗幡。装饰了树王后合掌说：“如果能获得一个儿子或者女儿，我将向您做大敬奉。”许完愿他就离开了。
- unit_id: 122-45-10-17
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-45-10-17
  line: 34
  source_quote: Sā gabbhassa patiṭṭhitabhāvaṃ ñatvā tassa ārocesi.
  target_quote: 妻子知道自己怀上以后就告诉了他，
- unit_id: 122-45-49-59
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-45-49-59
  line: 39
  source_quote: Tassa {cūḷapālo}ti nāmaṃ katvā itarassa {mahāpālo}ti nāmaṃ akāsi.
  target_quote: 就给他取名为**“小护(cūḷapāla)”，另一个则叫“大护”**。
- unit_id: 122-46-2-20
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-2-20
  line: 43
  source_quote: Tasmiṃ samaye satthā pavattitavaradhammacakko anupubbenāgantvā anāthapiṇḍikena
    mahāseṭṭhinā catupaṇṇāsakoṭidhanaṃ vissajjetvā kārite jetavanamahāvihāre viharati
    mahājanaṃ saggamagge ca mokkhamagge ca patiṭṭhāpayamāno.
  target_quote: 那时导师已转起殊胜的法轮，次第到达了由给孤独大富翁(anāthapiṇḍika mahāseṭṭhi)施舍五亿四千万钱财所建造的揭德林大寺，并于居住期间令大众住立于天界之道和解脱之道上。
variant_translations:
- 顶礼彼正觉，具福者之足；
- 我亦敬正法，合掌向僧团。
- 精简增加后，圣典语悦意。
- 我皆阐明彼，依义释其余。
- 一天，他在浴场洗完澡回来的路上看到一棵枝繁叶茂的树王，（心想）这树上一定住有大威力的天神。于是他将树下打扫干净，建了围墙并铺上沙子，还竖了一面旗幡。装饰了树王后合掌说：“如果能获得一个儿子或者女儿，…
- 妻子知道自己怀上以后就告诉了他，
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
version_id: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0
type: sentence_pattern
name: supplemented_syntax
description: 用方括号补出主语、宾语、语境、逻辑关系或术语说明。
grammar_category: supplemented_syntax
source_pattern: implicit source relation + bracketed target supplement
translation_pattern: 时 / 说 / 如 / 不 / 以 / ？
technique: 用方括号补出主语、宾语、语境、逻辑关系或术语说明。
occurrence_count: 1602
chunk_count: 53
top_chunks:
- chunk_id: chunk-0013
  count: 61
- chunk_id: chunk-0006
  count: 51
- chunk_id: chunk-0012
  count: 50
- chunk_id: chunk-0026
  count: 50
- chunk_id: chunk-0018
  count: 48
- chunk_id: chunk-0021
  count: 48
- chunk_id: chunk-0010
  count: 47
- chunk_id: chunk-0009
  count: 46
evidence:
- unit_id: 122-45-65-68
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-45-65-68
  line: 41
  source_quote: Aparabhāge mātāpitaro kālamakaṃsu.
  target_quote: 后来[他们的]父母迎来了死亡，
- unit_id: 122-46-21-55
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-21-55
  line: 44
  source_quote: Tathāgato hi mātipakkhato asītiyā, pitipakkhato asītiyāti dveasītiñātikulasahassehi
    kārite nigrodhamahāvihāre ekameva vassāvāsaṃ vasi, anāthapiṇḍikena kārite jetavanamahāvihāre
    ekūnavīsativassāni, visākhāya sattavīsatikoṭidhanapariccāgena kārite pubbārāme
    cha…
  target_quote: 如来在由他父方八万和母方八万如此共十六万亲族家庭共同建立的榕树大寺只度过了一个雨安居，而在由给孤独[大富翁]所建的揭德林大寺度过了十九个雨安居，在由维沙卡施舍两亿七千万钱财所建造的东园度过了六个雨安居，如此出于这两家[会有]许多功德果报，[佛陀]依于沙瓦提城度过了二十五个雨安居。
- unit_id: 122-46-56-81
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-56-81
  line: 45
  source_quote: Anāthapiṇḍikopi visākhāpi mahāupāsikā nibaddhaṃ divasassa dve vāre
    tathāgatassa upaṭṭhānaṃ gacchanti, gacchantā ca‘‘ daharasāmaṇerā no hatthe olokessantī’’
    ti tucchahatthā na gatapubbā.
  target_quote: 给孤独[大富翁]和维沙卡大近事女总是每天两次为前去侍奉如来，当去的时候想“年轻的比库、沙马内勒们将会看着我们的手”，就从未空手而去。
- unit_id: 122-46-107-116
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-107-116
  line: 48
  source_quote: Annapānabhesajjesu yo yaṃ icchati, tassa taṃ yathicchitameva sampajjati.
  target_quote: 无论哪位[比库]需要食物、饮料、药物中的任何物品，其所需之物都会如所需充分提供。
- unit_id: 122-46-117-124
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-117-124
  line: 49
  source_quote: Tesu anāthapiṇḍikena ekadivasampi satthā pañhaṃ na pucchitapubbo.
  target_quote: 在他们（给孤独大富翁和维沙卡）中，给孤独大富翁[任何]一天都没有问过导师问题。
- unit_id: 122-46-125-152
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-125-152
  line: 50
  source_quote: So kira‘‘ tathāgato buddhasukhumālo khattiyasukhumālo,‘ bahūpakāro
    me, gahapatī’ ti mayhaṃ dhammaṃ desento kilameyyā’’ ti satthari adhimattasinehena
    pañhaṃ na pucchati.
  target_quote: 据说他[出于]：“如来身为佛陀而娇嫩，身为刹帝利而娇嫩，若[想着]‘[这位]家主对我助益良多’而对我说法会疲倦”，由于对导师强烈的敬爱而没有问过问题。
- unit_id: 122-46-153-164
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-153-164
  line: 51
  source_quote: Satthā pana tasmiṃ nisinnamatteyeva‘‘ ayaṃ seṭṭhi maṃ arakkhitabbaṭṭhāne
    rakkhati.
  target_quote: 正当他坐着时，导师则[想]：“这位富翁在不需要保护之处保护我。
- unit_id: 122-48-2-25
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-48-2-25
  line: 58
  source_quote: Buddhā ca nāma dhammaṃ desentā saraṇasīlapabbajjādīnaṃ upanissayaṃ
    oloketvā ajjhāsayavasena dhammaṃ desenti, tasmā taṃ divasaṃ satthā tassa upanissayaṃ
    oloketvā dhammaṃ desento anupubbikathaṃ kathesi.
  target_quote: 而诸佛开示佛法时[都是]观察了[听众的]皈依、持戒、出家等强依止后，根据意乐开示佛法，因此那天导师观察了他（大护）的强依止后在说法时开示了次第论。
variant_translations:
- 后来[他们的]父母迎来了死亡，
- 如来在由他父方八万和母方八万如此共十六万亲族家庭共同建立的榕树大寺只度过了一个雨安居，而在由给孤独[大富翁]所建的揭德林大寺度过了十九个雨安居，在由维沙卡施舍两亿七千万钱财所建造的东园度过了六个雨安…
- 给孤独[大富翁]和维沙卡大近事女总是每天两次为前去侍奉如来，当去的时候想“年轻的比库、沙马内勒们将会看着我们的手”，就从未空手而去。
- 无论哪位[比库]需要食物、饮料、药物中的任何物品，其所需之物都会如所需充分提供。
- 在他们（给孤独大富翁和维沙卡）中，给孤独大富翁[任何]一天都没有问过导师问题。
- 据说他[出于]：“如来身为佛陀而娇嫩，身为刹帝利而娇嫩，若[想着]‘[这位]家主对我助益良多’而对我说法会疲倦”，由于对导师强烈的敬爱而没有问过问题。
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
version_id: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0
type: sentence_pattern
name: long_sentence
description: 把长句拆为分号、句号、方括号补足或换行结构。
grammar_category: long_sentence
source_pattern: long multi-clause sentence
translation_pattern: 说 / 时 / 不 / 如 / ？ / 以
technique: 把长句拆为分号、句号、方括号补足或换行结构。
occurrence_count: 1396
chunk_count: 53
top_chunks:
- chunk_id: chunk-0007
  count: 43
- chunk_id: chunk-0020
  count: 41
- chunk_id: chunk-0017
  count: 38
- chunk_id: chunk-0029
  count: 38
- chunk_id: chunk-0023
  count: 37
- chunk_id: chunk-0026
  count: 37
- chunk_id: chunk-0005
  count: 34
- chunk_id: chunk-0041
  count: 34
evidence:
- unit_id: 122-44-13-65
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-44-13-65
  line: 32
  source_quote: So ekadivasaṃ nhānatitthaṃ nhatvā natvā āgacchanto antarāmagge sampannapattasākhaṃ
    ekaṃ vanappatiṃ disvā‘‘ ayaṃ mahesakkhāya devatāya pariggahito bhavissatī’’ ti
    tassa heṭṭhābhāgaṃ sodhāpetvā pākāraparikkhepaṃ kārāpetvā vālukaṃ okirāpetvā dhajapaṭākaṃ
    ussāpet…
  target_quote: 一天，他在浴场洗完澡回来的路上看到一棵枝繁叶茂的树王，（心想）这树上一定住有大威力的天神。于是他将树下打扫干净，建了围墙并铺上沙子，还竖了一面旗幡。装饰了树王后合掌说：“如果能获得一个儿子或者女儿，我将向您做大敬奉。”许完愿他就离开了。
- unit_id: 122-46-2-20
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-2-20
  line: 43
  source_quote: Tasmiṃ samaye satthā pavattitavaradhammacakko anupubbenāgantvā anāthapiṇḍikena
    mahāseṭṭhinā catupaṇṇāsakoṭidhanaṃ vissajjetvā kārite jetavanamahāvihāre viharati
    mahājanaṃ saggamagge ca mokkhamagge ca patiṭṭhāpayamāno.
  target_quote: 那时导师已转起殊胜的法轮，次第到达了由给孤独大富翁(anāthapiṇḍika mahāseṭṭhi)施舍五亿四千万钱财所建造的揭德林大寺，并于居住期间令大众住立于天界之道和解脱之道上。
- unit_id: 122-46-21-55
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-21-55
  line: 44
  source_quote: Tathāgato hi mātipakkhato asītiyā, pitipakkhato asītiyāti dveasītiñātikulasahassehi
    kārite nigrodhamahāvihāre ekameva vassāvāsaṃ vasi, anāthapiṇḍikena kārite jetavanamahāvihāre
    ekūnavīsativassāni, visākhāya sattavīsatikoṭidhanapariccāgena kārite pubbārāme
    cha…
  target_quote: 如来在由他父方八万和母方八万如此共十六万亲族家庭共同建立的榕树大寺只度过了一个雨安居，而在由给孤独[大富翁]所建的揭德林大寺度过了十九个雨安居，在由维沙卡施舍两亿七千万钱财所建造的东园度过了六个雨安居，如此出于这两家[会有]许多功德果报，[佛陀]依于沙瓦提城度过了二十五个雨安居。
- unit_id: 122-46-56-81
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-56-81
  line: 45
  source_quote: Anāthapiṇḍikopi visākhāpi mahāupāsikā nibaddhaṃ divasassa dve vāre
    tathāgatassa upaṭṭhānaṃ gacchanti, gacchantā ca‘‘ daharasāmaṇerā no hatthe olokessantī’’
    ti tucchahatthā na gatapubbā.
  target_quote: 给孤独[大富翁]和维沙卡大近事女总是每天两次为前去侍奉如来，当去的时候想“年轻的比库、沙马内勒们将会看着我们的手”，就从未空手而去。
- unit_id: 122-46-165-185
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-165-185
  line: 52
  source_quote: Ahañhi kappasatasahassādhikāni cattāri asaṅkhyeyyāni alaṅkatapaṭiyattaṃ
    attano sīsaṃ chinditvā akkhīni uppāṭetvā hadayamaṃsaṃ uppāṭetvā pāṇasamaṃ puttadāraṃ
    pariccajitvā pāramiyo pūrento paresaṃ dhammadesanatthameva pūresiṃ.
  target_quote: 我历经四个不可数又十万大劫，砍断自己华饰的头颅、挖出眼睛、挖出心脏以及施舍珍若生命般的妻儿，而圆满巴拉密的时候，就只是为了对他人开示佛法而圆满的。
- unit_id: 122-47-39-76
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-47-39-76
  line: 57
  source_quote: Athekadivasaṃ mahāpālo ariyasāvake gandhamālādihatthe vihāraṃ gacchante
    disvā‘‘ ayaṃ mahājano kuhiṃ gacchatī’’ ti pucchitvā‘‘ dhammassavanāyā’’ ti sutvā‘‘
    ahampi gamissāmī’’ ti gantvā satthāraṃ vanditvā parisapariyante nisīdi.
  target_quote: 当时有一天，大护（mahāpāla）看到那些圣弟子们手里拿着香和花前去寺院，问道：“这一大群人是去哪里呢？”听到“去听闻佛法”后，就说“我也要去。”去到后礼敬了导师，接着在听众的外围坐下。
- unit_id: 122-48-2-25
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-48-2-25
  line: 58
  source_quote: Buddhā ca nāma dhammaṃ desentā saraṇasīlapabbajjādīnaṃ upanissayaṃ
    oloketvā ajjhāsayavasena dhammaṃ desenti, tasmā taṃ divasaṃ satthā tassa upanissayaṃ
    oloketvā dhammaṃ desento anupubbikathaṃ kathesi.
  target_quote: 而诸佛开示佛法时[都是]观察了[听众的]皈依、持戒、出家等强依止后，根据意乐开示佛法，因此那天导师观察了他（大护）的强依止后在说法时开示了次第论。
- unit_id: 122-48-26-43
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-48-26-43
  line: 59
  source_quote: Seyyathidaṃ– dānakathaṃ, sīlakathaṃ, saggakathaṃ, kāmānaṃ ādīnavaṃ,
    okāraṃ saṃkilesaṃ, nekkhamme ānisaṃsaṃ pakāsesi.
  target_quote: 即：布施论，持戒论，生天论，诸欲的过患、卑劣、杂染，阐明了出离的利益。
variant_translations:
- 一天，他在浴场洗完澡回来的路上看到一棵枝繁叶茂的树王，（心想）这树上一定住有大威力的天神。于是他将树下打扫干净，建了围墙并铺上沙子，还竖了一面旗幡。装饰了树王后合掌说：“如果能获得一个儿子或者女儿，…
- 那时导师已转起殊胜的法轮，次第到达了由给孤独大富翁(anāthapiṇḍika mahāseṭṭhi)施舍五亿四千万钱财所建造的揭德林大寺，并于居住期间令大众住立于天界之道和解脱之道上。
- 如来在由他父方八万和母方八万如此共十六万亲族家庭共同建立的榕树大寺只度过了一个雨安居，而在由给孤独[大富翁]所建的揭德林大寺度过了十九个雨安居，在由维沙卡施舍两亿七千万钱财所建造的东园度过了六个雨安…
- 给孤独[大富翁]和维沙卡大近事女总是每天两次为前去侍奉如来，当去的时候想“年轻的比库、沙马内勒们将会看着我们的手”，就从未空手而去。
- 我历经四个不可数又十万大劫，砍断自己华饰的头颅、挖出眼睛、挖出心脏以及施舍珍若生命般的妻儿，而圆满巴拉密的时候，就只是为了对他人开示佛法而圆满的。
- 当时有一天，大护（mahāpāla）看到那些圣弟子们手里拿着香和花前去寺院，问道：“这一大群人是去哪里呢？”听到“去听闻佛法”后，就说“我也要去。”去到后礼敬了导师，接着在听众的外围坐下。
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
version_id: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0
type: sentence_pattern
name: negation
description: 把否定结构译为不、没有、不能、无等。
grammar_category: negation
source_pattern: na / no / natthi / mā + predicate
translation_pattern: 不 / 说 / 时 / 如 / 无 / ？
technique: 把否定结构译为不、没有、不能、无等。
occurrence_count: 1302
chunk_count: 54
top_chunks:
- chunk_id: chunk-0004
  count: 43
- chunk_id: chunk-0037
  count: 38
- chunk_id: chunk-0005
  count: 36
- chunk_id: chunk-0038
  count: 36
- chunk_id: chunk-0031
  count: 35
- chunk_id: chunk-0044
  count: 34
- chunk_id: chunk-0018
  count: 33
- chunk_id: chunk-0036
  count: 33
evidence:
- unit_id: 122-22-2-8
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-22-2-8
  line: 11
  source_quote: Na sādhayati sesānaṃ, sattānaṃ hitasampadaṃ;
  target_quote: 未令余有情，获利益成就；
- unit_id: 122-32-2-9
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-32-2-9
  line: 18
  source_quote: Gāthānaṃ byañjanapadaṃ, yaṃ tattha na vibhāvitaṃ.
  target_quote: 此中未阐明，偈颂之文辞。
- unit_id: 122-45-2-9
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-45-2-9
  line: 33
  source_quote: Athassa na cirasseva bhariyāya kucchiyaṃ gabbho patiṭṭhāsi.
  target_quote: 不久之后他妻子就怀孕了。
- unit_id: 122-46-56-81
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-56-81
  line: 45
  source_quote: Anāthapiṇḍikopi visākhāpi mahāupāsikā nibaddhaṃ divasassa dve vāre
    tathāgatassa upaṭṭhānaṃ gacchanti, gacchantā ca‘‘ daharasāmaṇerā no hatthe olokessantī’’
    ti tucchahatthā na gatapubbā.
  target_quote: 给孤独[大富翁]和维沙卡大近事女总是每天两次为前去侍奉如来，当去的时候想“年轻的比库、沙马内勒们将会看着我们的手”，就从未空手而去。
- unit_id: 122-46-117-124
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-117-124
  line: 49
  source_quote: Tesu anāthapiṇḍikena ekadivasampi satthā pañhaṃ na pucchitapubbo.
  target_quote: 在他们（给孤独大富翁和维沙卡）中，给孤独大富翁[任何]一天都没有问过导师问题。
- unit_id: 122-46-125-152
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-125-152
  line: 50
  source_quote: So kira‘‘ tathāgato buddhasukhumālo khattiyasukhumālo,‘ bahūpakāro
    me, gahapatī’ ti mayhaṃ dhammaṃ desento kilameyyā’’ ti satthari adhimattasinehena
    pañhaṃ na pucchati.
  target_quote: 据说他[出于]：“如来身为佛陀而娇嫩，身为刹帝利而娇嫩，若[想着]‘[这位]家主对我助益良多’而对我说法会疲倦”，由于对导师强烈的敬爱而没有问过问题。
- unit_id: 122-48-50-76
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-48-50-76
  line: 61
  source_quote: ‘‘ paralokaṃ gacchantaṃ puttadhītaro vā bhātaro vā bhogā vā nānugacchanti,
    sarīrampi attanā saddhiṃ na gacchati, kiṃ me gharāvāsena pabbajissāmī’’ ti.
  target_quote: “儿女、兄弟、财产都不会跟着去往来世者而去，连身体也不会同自己一起去，住在家里对我又有何益？我要出家！”
- unit_id: 122-48-182-218
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-48-182-218
  line: 69
  source_quote: ‘‘ Kiṃ kathesi bhātika, tvaṃ me mātari matāya mātā viya, pitari mate
    pitā viya laddho, gehe te mahāvibhavo, sakkā gehaṃ ajjhāvasanteheva puññāni kātuṃ
    , mā evaṃ karitthā’’ ti.
  target_quote: “你在说什么呢，哥哥？母亲去世时有您就像有了母亲，父亲死时有您就像有了父亲。你的家里有很多财产，住在家里时你也可以做福德啊，不要这样做。”
variant_translations:
- 未令余有情，获利益成就；
- 此中未阐明，偈颂之文辞。
- 不久之后他妻子就怀孕了。
- 给孤独[大富翁]和维沙卡大近事女总是每天两次为前去侍奉如来，当去的时候想“年轻的比库、沙马内勒们将会看着我们的手”，就从未空手而去。
- 在他们（给孤独大富翁和维沙卡）中，给孤独大富翁[任何]一天都没有问过导师问题。
- 据说他[出于]：“如来身为佛陀而娇嫩，身为刹帝利而娇嫩，若[想着]‘[这位]家主对我助益良多’而对我说法会疲倦”，由于对导师强烈的敬爱而没有问过问题。
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
version_id: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0
type: sentence_pattern
name: question_or_problem
description: 把问句或设问译为何、为什么、若问等解释性结构。
grammar_category: question_or_problem
source_pattern: interrogative + explanatory answer
translation_pattern: ？ / 说 / 时 / 如 / 不 / 当
technique: 把问句或设问译为何、为什么、若问等解释性结构。
occurrence_count: 696
chunk_count: 52
top_chunks:
- chunk_id: chunk-0026
  count: 28
- chunk_id: chunk-0032
  count: 27
- chunk_id: chunk-0027
  count: 25
- chunk_id: chunk-0023
  count: 23
- chunk_id: chunk-0051
  count: 22
- chunk_id: chunk-0029
  count: 20
- chunk_id: chunk-0034
  count: 19
- chunk_id: chunk-0014
  count: 18
evidence:
- unit_id: 122-43-2-6
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-43-2-6
  line: 27
  source_quote: Ayaṃ dhammadesanā kattha bhāsitāti?
  target_quote: 这佛法开示是在何处说的呢？
- unit_id: 122-48-50-76
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-48-50-76
  line: 61
  source_quote: ‘‘ paralokaṃ gacchantaṃ puttadhītaro vā bhātaro vā bhogā vā nānugacchanti,
    sarīrampi attanā saddhiṃ na gacchati, kiṃ me gharāvāsena pabbajissāmī’’ ti.
  target_quote: “儿女、兄弟、财产都不会跟着去往来世者而去，连身体也不会同自己一起去，住在家里对我又有何益？我要出家！”
- unit_id: 122-48-161-171
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-48-161-171
  line: 67
  source_quote: ‘‘ Tumhe pana kiṃ karissathā’’ ti āha.
  target_quote: “那您要做什么呢？” （弟弟）问。
- unit_id: 122-48-182-218
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-48-182-218
  line: 69
  source_quote: ‘‘ Kiṃ kathesi bhātika, tvaṃ me mātari matāya mātā viya, pitari mate
    pitā viya laddho, gehe te mahāvibhavo, sakkā gehaṃ ajjhāvasanteheva puññāni kātuṃ
    , mā evaṃ karitthā’’ ti.
  target_quote: “你在说什么呢，哥哥？母亲去世时有您就像有了母亲，父亲死时有您就像有了父亲。你的家里有很多财产，住在家里时你也可以做福德啊，不要这样做。”
- unit_id: 122-48-269-299
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-48-269-299
  line: 73
  source_quote: ‘‘ Tāta, mahallakassa hi attano hatthapādāpi anassavā honti, na attano
    vase vattanti, kimaṅgaṃ pana ñātakā, svāhaṃ tava kathaṃ na karomi, samaṇapaṭipattiṃyeva
    pūressāmi’’.
  target_quote: “弟弟啊，老人自己的手脚都会不听使唤，不受自己控制，更何况是亲戚们呢？我不会照你说的做，我就是要圆满沙门的行道。”
- unit_id: 122-50-2-11
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-50-2-11
  line: 75
  source_quote: Yassa so vihatatthāmo, kathaṃ dhammaṃ carissati’’.
  target_quote: 气力已衰竭，彼何堪修法？”
- unit_id: 122-53-78-92
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-53-78-92
  line: 91
  source_quote: ‘‘ Kiṃ panetaṃ, āvuso, patirūpaṃ, nanu appamattehi bhavitabbaṃ’’?
  target_quote: “贤友们，这怎么合适呢？难道不是应当成为不放逸者吗？
- unit_id: 122-53-129-139
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-53-129-139
  line: 94
  source_quote: ‘‘ Kiṃ tumhe pana, bhante’’ ti?
  target_quote: “尊者，那您将怎样（度过）呢？”
variant_translations:
- 这佛法开示是在何处说的呢？
- “儿女、兄弟、财产都不会跟着去往来世者而去，连身体也不会同自己一起去，住在家里对我又有何益？我要出家！”
- “那您要做什么呢？” （弟弟）问。
- “你在说什么呢，哥哥？母亲去世时有您就像有了母亲，父亲死时有您就像有了父亲。你的家里有很多财产，住在家里时你也可以做福德啊，不要这样做。”
- “弟弟啊，老人自己的手脚都会不听使唤，不受自己控制，更何况是亲戚们呢？我不会照你说的做，我就是要圆满沙门的行道。”
- 气力已衰竭，彼何堪修法？”
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.88
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-newline-decomposition-syntax-585a7090

```yaml
id: open-syntax-newline-decomposition-syntax-585a7090
version_id: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0
type: sentence_pattern
name: decomposition
description: 用换行拆解并列、长句、偈颂或注释层次。
grammar_category: decomposition
source_pattern: complex source + target line breaks
translation_pattern: 说 / 时 / 以 / 不 / 在此 / 无
technique: 用换行拆解并列、长句、偈颂或注释层次。
occurrence_count: 595
chunk_count: 43
top_chunks:
- chunk_id: chunk-0037
  count: 41
- chunk_id: chunk-0043
  count: 41
- chunk_id: chunk-0039
  count: 40
- chunk_id: chunk-0035
  count: 36
- chunk_id: chunk-0038
  count: 36
- chunk_id: chunk-0046
  count: 32
- chunk_id: chunk-0042
  count: 31
- chunk_id: chunk-0034
  count: 30
evidence:
- unit_id: 122-95-129-156
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-95-129-156
  line: 297
  source_quote: Sā vejjenāgantvā‘‘ kīdisaṃ, bhadde’’ ti puṭṭhā‘‘ pubbe me akkhīni
    thokaṃ rujjiṃsu, idāni pana atirekataraṃ rujjantī’’ ti āha.
  target_quote: '医生前来问她：“贤妹，怎么样了？”

    她答道：“以前我的眼睛只是略微疼痛，现在却非常疼痛了。”'
- unit_id: 122-204-55-67
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-204-55-67
  line: 460
  source_quote: So satthu adhivāsanaṃ viditvā vegenāgantvā sake nivesane paṇītaṃ khādanīyaṃ
    bhojanīyañca paṭiyādāpesi.
  target_quote: '知道导师同意之后，他迅速返回，令人在自己家

    里准备了胜妙的主食和副食。'
- unit_id: 122-233-178-219
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-233-178-219
  line: 582
  source_quote: Nāradopi‘‘ uṭṭhehi, ācariya, khamāmi te’’ ti vatvā,‘‘ mahārāja, nāyaṃ
    yathāmanena khamāpeti, nagarassa avidūre eko saro atthi, tattha naṃ sīse mattikāpiṇḍaṃ
    katvā galappamāṇe udake ṭhapāpehī’’ ti āha.
  target_quote: '那勒德也说：“起来吧，老师！我原谅您。”

    那勒德接着对国王说：“大王，他不是心甘情愿请求原谅的。在城市不远处有个湖，在那里请将土块放在他的头上，让其站在深及颈部的水中。”'
- unit_id: 122-242-13-16
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-242-13-16
  line: 600
  source_quote: Dubbacopi subbacoyeva jātoti.
  target_quote: "难教者也变成了易教者。\n\x0F"
- unit_id: 122-246-201-264
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-246-201-264
  line: 616
  source_quote: Yaṃnūnāhaṃ sayameva ekaṃ kumārikaṃ āneyyan’’ ti cintetvā ekaṃ kulaṃ
    gantvā tassatthāya kumārikaṃ vāretvā‘‘ kiṃ nāmetaṃ, amma, vadesī’’ ti tehi paṭikkhittā‘‘
    ahaṃ vañjhā, aputtakaṃ nāma kulaṃ vinassati, tumhākaṃ pana dhītā puttaṃ vā dhītaraṃ
    vā labhitvā kuṭumb…
  target_quote: '我何不自己带个女孩来呢？” 她便去到一户人家为丈夫求取闺女。“姑娘，你说的这是什么话？”被[女孩的亲属们]反对后，

    [女人]恳求道：“我不能生育，绝后的家庭将会消亡，而你们的女儿得了儿子或女儿后，将成为富人的正室。请将她交给我丈夫吧！”令其同意后，将她带回来安置在丈夫家中。'
- unit_id: 122-254-2-31
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-254-2-31
  line: 663
  source_quote: Tattha na hi {verenā}ti yathā hi kheḷasiṅghāṇikādīhi asucīhi makkhitaṃ
    ṭhānaṃ teheva asucīhi dhovantā suddhaṃ niggandhaṃ kātuṃ na sakkonti, atha kho
    taṃ ṭhānaṃ bhiyyosomattāya asuddhatarañceva duggandhatarañca hoti;
  target_quote: '在此，“ 皆非怨[止怨](na hi verena)

    ”：正如被唾液、鼻涕等不净物涂抹之处，用那些不净物清洗，是不可能变得洁净、无味的，实际上该处只会更加肮脏、恶臭。'
- unit_id: 122-254-63-82
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-254-63-82
  line: 666
  source_quote: Averena ca {sammantī}ti yathā pana tāni kheḷādīni asucīni vippasannena
    udakena dhoviyamānāni nassanti, taṃ ṭhānaṃ suddhaṃ hoti sugandhaṃ;
  target_quote: '“ 无怨方息怨(averena ca sammanti)

    ” ：再者，正如那些唾液等不净物被洁净的水清洗时便会消失，该处也变得干净、清香；'
- unit_id: 122-254-95-104
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-254-95-104
  line: 668
  source_quote: Esa dhammo {sanantano}ti esa averena verūpasamanasaṅkhāto porāṇako
    dhammo;
  target_quote: '“ 此为古习法(esa dhammo sanantano)

    ”：这所谓的以无怨息怨乃是古人的传统之法;'
variant_translations:
- 医生前来问她：“贤妹，怎么样了？” 她答道：“以前我的眼睛只是略微疼痛，现在却非常疼痛了。”
- 知道导师同意之后，他迅速返回，令人在自己家 里准备了胜妙的主食和副食。
- 那勒德也说：“起来吧，老师！我原谅您。” 那勒德接着对国王说：“大王，他不是心甘情愿请求原谅的。在城市不远处有个湖，在那里请将土块放在他的头上，让其站在深及颈部的水中。”
- "难教者也变成了易教者。 \x0F"
- 我何不自己带个女孩来呢？” 她便去到一户人家为丈夫求取闺女。“姑娘，你说的这是什么话？”被[女孩的亲属们]反对后， [女人]恳求道：“我不能生育，绝后的家庭将会消亡，而你们的女儿得了儿子或女儿后，将…
- 在此，“ 皆非怨[止怨](na hi verena) ”：正如被唾液、鼻涕等不净物涂抹之处，用那些不净物清洗，是不可能变得洁净、无味的，实际上该处只会更加肮脏、恶臭。
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
version_id: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0
type: sentence_pattern
name: locative_topic
description: 把处所或论题入口译为在此、此中、其中、这里。
grammar_category: locative_topic
source_pattern: ettha / tattha / idha
translation_pattern: 在此 / 说 / 不 / 时 / 以 / 如
technique: 把处所或论题入口译为在此、此中、其中、这里。
occurrence_count: 411
chunk_count: 53
top_chunks:
- chunk_id: chunk-0005
  count: 17
- chunk_id: chunk-0047
  count: 16
- chunk_id: chunk-0048
  count: 14
- chunk_id: chunk-0012
  count: 13
- chunk_id: chunk-0021
  count: 12
- chunk_id: chunk-0022
  count: 12
- chunk_id: chunk-0035
  count: 12
- chunk_id: chunk-0042
  count: 12
evidence:
- unit_id: 122-32-2-9
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-32-2-9
  line: 18
  source_quote: Gāthānaṃ byañjanapadaṃ, yaṃ tattha na vibhāvitaṃ.
  target_quote: 此中未阐明，偈颂之文辞。
- unit_id: 122-52-2-26
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-52-2-26
  line: 83
  source_quote: So satthāraṃ vanditvā attanā sahagāmino bhikkhū pariyesanto saṭṭhi
    bhikkhū labhitvā tehi saddhiṃ nikkhamitvā vīsayojanasatamaggaṃ gantvā ekaṃ mahantaṃ
    paccantagāmaṃ patvā tattha saparivāro piṇḍāya pāvisi.
  target_quote: 他礼敬导师后，在寻找与自己同行的比库时，得到了六十位比库，就与他们一起出发了，走了一百二十由旬的路后，到达了一个边远的大村庄。他就和同伴们入村托钵。
- unit_id: 122-52-27-90
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-52-27-90
  line: 84
  source_quote: Manussā vattasampanne bhikkhū disvāva pasannacittā āsanāni paññāpetvā
    nisīdāpetvā paṇītenāhārena parivisitvā,‘‘ bhante, kuhiṃ ayyā gacchantī’’ ti pucchitvā‘‘
    yathāphāsukaṭṭhānaṃ upāsakā’’ ti vutte paṇḍitā manussā‘‘ vassāvāsaṃ senāsanaṃ
    pariyesanti bhadantā’’ …
  target_quote: 人们一看到这群具足行仪的比库就心生净信，他们敷设座位并邀请入座，以胜妙的食物款待后，问道：“尊者，你们要去哪里？”，“近事男们，任何安乐之处。”
    当这样说时，这些贤智之人就知道尊者们在找雨安居的坐卧处。他们说：“诸位尊者，如果圣尊们这三个月能住在这里，我们将能住立于皈依并能获得戒。”
- unit_id: 122-74-35-44
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-74-35-44
  line: 189
  source_quote: ‘‘ Ko nāma tattha vasatī’’ ti?
  target_quote: “是谁住在那里呢？”
- unit_id: 122-76-2-25
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-76-2-25
  line: 205
  source_quote: Sāmaṇero tattha nimittaṃ gahetvā yaṭṭhikoṭiṃ vissajjetvā‘‘ tiṭṭhatha
    tāva, bhante, kiccaṃ me atthī’’ ti tassā santikaṃ gato.
  target_quote: 沙马内勒执取那（声）相，松开拐杖（对长老说）：“尊者，您先等等，我有事要做。”说完就走到女人的跟前。
- unit_id: 122-76-192-210
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-76-192-210
  line: 219
  source_quote: ‘‘ Bhante, amanussupaddavo maggo, tumhe ca andhā apariṇāyakā, kathaṃ
    idha vasissathā’’ ti?
  target_quote: “尊者，路上有非人的危险，您又失去了视力，无人引导要怎么留在这里呢？”
- unit_id: 122-101-2-8
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-101-2-8
  line: 306
  source_quote: Tattha {mano}ti kāmāvacarakusalādibhedaṃ sabbampi catubhūmikacittaṃ.
  target_quote: 在此（偈颂）中，“意”（mano)指欲界善心等类别的一切四地心四个层次的心。
- unit_id: 122-104-31-59
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-104-31-59
  line: 314
  source_quote: ‘‘ Idha pana, bhikkhave, ekacce kulaputtā dhammaṃ pariyāpuṇanti suttaṃ
    geyyan’’ ti( ma. ni.1.239) ayaṃ pariyattidhammo nāma.
  target_quote: 3）“在此（教法中），诸比库，一些良家子学得法：经，应颂……”（《中部》.1.239），这是指教理之法。
variant_translations:
- 此中未阐明，偈颂之文辞。
- 他礼敬导师后，在寻找与自己同行的比库时，得到了六十位比库，就与他们一起出发了，走了一百二十由旬的路后，到达了一个边远的大村庄。他就和同伴们入村托钵。
- 人们一看到这群具足行仪的比库就心生净信，他们敷设座位并邀请入座，以胜妙的食物款待后，问道：“尊者，你们要去哪里？”，“近事男们，任何安乐之处。” 当这样说时，这些贤智之人就知道尊者们在找雨安居的坐卧…
- “是谁住在那里呢？”
- 沙马内勒执取那（声）相，松开拐杖（对长老说）：“尊者，您先等等，我有事要做。”说完就走到女人的跟前。
- “尊者，路上有非人的危险，您又失去了视力，无人引导要怎么留在这里呢？”
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
version_id: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0
type: sentence_pattern
name: simile
description: 把譬喻关系译为如、譬如、犹如、像。
grammar_category: simile
source_pattern: viya / iva / seyyathāpi
translation_pattern: 如 / 说 / 时 / 不 / 以 / 无
technique: 把譬喻关系译为如、譬如、犹如、像。
occurrence_count: 241
chunk_count: 48
top_chunks:
- chunk_id: chunk-0022
  count: 10
- chunk_id: chunk-0030
  count: 10
- chunk_id: chunk-0032
  count: 10
- chunk_id: chunk-0007
  count: 9
- chunk_id: chunk-0033
  count: 9
- chunk_id: chunk-0045
  count: 8
- chunk_id: chunk-0006
  count: 7
- chunk_id: chunk-0010
  count: 7
evidence:
- unit_id: 122-48-182-218
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-48-182-218
  line: 69
  source_quote: ‘‘ Kiṃ kathesi bhātika, tvaṃ me mātari matāya mātā viya, pitari mate
    pitā viya laddho, gehe te mahāvibhavo, sakkā gehaṃ ajjhāvasanteheva puññāni kātuṃ
    , mā evaṃ karitthā’’ ti.
  target_quote: “你在说什么呢，哥哥？母亲去世时有您就像有了母亲，父亲死时有您就像有了父亲。你的家里有很多财产，住在家里时你也可以做福德啊，不要这样做。”
- unit_id: 122-54-13-19
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-54-13-19
  line: 98
  source_quote: Chiddaghaṭato udakadhārā viya akkhīhi assudhārā paggharanti.
  target_quote: 犹如从破水罐漏出水流一般，从他的双眼涌出泪流。
- unit_id: 122-74-211-223
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-74-211-223
  line: 202
  source_quote: Itthisaddo viya hi añño saddo purisānaṃ sakalasarīraṃ pharitvā ṭhātuṃ
    samattho nāma natthi.
  target_quote: 没有其他声音能像女人的声音那样遍满男人的全身而住。
- unit_id: 122-95-211-217
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-95-211-217
  line: 301
  source_quote: Athassā dve akkhīni dīpasikhā viya vijjhāyiṃsu.
  target_quote: 当时，她的双眼就像灯火般熄灭了。
- unit_id: 122-96-12-34
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-96-12-34
  line: 304
  source_quote: Pāpakammañhi nāmetaṃ dhuraṃ vahato balibaddassa padaṃ cakkaṃ viya
    anugacchatīti idaṃ vatthuṃ kathetvā anusandhiṃ ghaṭetvā patiṭṭhāpitamattikaṃ sāsanaṃ
    rājamuddāya lañchanto viya dhammarājā imaṃ gāthamāha–
  target_quote: “此恶业就像（车）轮跟随负重的公牛之足一样（跟随愚人）”，说完这个故事并指出关联后，犹如（国王）用王印压盖已敷上封泥的信笺，法王（佛陀）说出这首偈颂：
- unit_id: 122-107-33-45
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-107-33-45
  line: 334
  source_quote: Cakkaṃva vahato padan ti dhure yuttassa dhuraṃ vahato balibaddassa
    padaṃ cakkaṃ viya.
  target_quote: “如轮随兽足”：就像轮子跟随着套于轭上并拉着轭的公牛之足。
- unit_id: 122-114-76-90
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-114-76-90
  line: 379
  source_quote: So tathāgate cakkhupathaṃ vijahanteyeva pasannamano kālaṃ katvā suttappabuddho
    viya devaloke tiṃsayojanike kanakavimāne nibbatti.
  target_quote: 当如来离开视线时，他心怀净信死去了，如同从梦中醒来一般，投生于天界三十由旬的黄金宫殿中。
- unit_id: 122-149-2-6
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-149-2-6
  line: 411
  source_quote: Candaṃ viya dārako rudaṃ,
  target_quote: 犹如小儿泣求月，
variant_translations:
- “你在说什么呢，哥哥？母亲去世时有您就像有了母亲，父亲死时有您就像有了父亲。你的家里有很多财产，住在家里时你也可以做福德啊，不要这样做。”
- 犹如从破水罐漏出水流一般，从他的双眼涌出泪流。
- 没有其他声音能像女人的声音那样遍满男人的全身而住。
- 当时，她的双眼就像灯火般熄灭了。
- “此恶业就像（车）轮跟随负重的公牛之足一样（跟随愚人）”，说完这个故事并指出关联后，犹如（国王）用王印压盖已敷上封泥的信笺，法王（佛陀）说出这首偈颂：
- “如轮随兽足”：就像轮子跟随着套于轭上并拉着轭的公牛之足。
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.88
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-alternative-series-18071276

```yaml
id: open-syntax-alternative-series-18071276
version_id: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0
type: sentence_pattern
name: alternative_or_variant
description: 把多项替代或并列解释译为或、或者、换行列举。
grammar_category: alternative_or_variant
source_pattern: X vā Y vā
translation_pattern: 或 / 不 / 说 / 时 / 如 / 以
technique: 把多项替代或并列解释译为或、或者、换行列举。
occurrence_count: 233
chunk_count: 51
top_chunks:
- chunk_id: chunk-0004
  count: 9
- chunk_id: chunk-0036
  count: 9
- chunk_id: chunk-0037
  count: 9
- chunk_id: chunk-0051
  count: 9
- chunk_id: chunk-0010
  count: 8
- chunk_id: chunk-0013
  count: 8
- chunk_id: chunk-0035
  count: 8
- chunk_id: chunk-0003
  count: 7
evidence:
- unit_id: 122-41-2-10
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-41-2-10
  line: 25
  source_quote: Manasā ce paduṭṭhena, bhāsati vā karoti vā;
  target_quote: 若以染污意，或语或行动；
- unit_id: 122-44-13-65
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-44-13-65
  line: 32
  source_quote: So ekadivasaṃ nhānatitthaṃ nhatvā natvā āgacchanto antarāmagge sampannapattasākhaṃ
    ekaṃ vanappatiṃ disvā‘‘ ayaṃ mahesakkhāya devatāya pariggahito bhavissatī’’ ti
    tassa heṭṭhābhāgaṃ sodhāpetvā pākāraparikkhepaṃ kārāpetvā vālukaṃ okirāpetvā dhajapaṭākaṃ
    ussāpet…
  target_quote: 一天，他在浴场洗完澡回来的路上看到一棵枝繁叶茂的树王，（心想）这树上一定住有大威力的天神。于是他将树下打扫干净，建了围墙并铺上沙子，还竖了一面旗幡。装饰了树王后合掌说：“如果能获得一个儿子或者女儿，我将向您做大敬奉。”许完愿他就离开了。
- unit_id: 122-48-50-76
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-48-50-76
  line: 61
  source_quote: ‘‘ paralokaṃ gacchantaṃ puttadhītaro vā bhātaro vā bhogā vā nānugacchanti,
    sarīrampi attanā saddhiṃ na gacchati, kiṃ me gharāvāsena pabbajissāmī’’ ti.
  target_quote: “儿女、兄弟、财产都不会跟着去往来世者而去，连身体也不会同自己一起去，住在家里对我又有何益？我要出家！”
- unit_id: 122-51-63-105
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-51-63-105
  line: 80
  source_quote: ‘‘ Attano paññānurūpena ekaṃ vā dve vā nikāye sakalaṃ vā pana tepiṭakaṃ
    buddhavacanaṃ uggaṇhitvā tassa dhāraṇaṃ, kathanaṃ, vācananti idaṃ ganthadhuraṃ
    nāma, sallahukavuttino pana pantasenāsanābhiratassa attabhāve khayavayaṃ paṭṭhapetvā
    sātaccakiriyavasena vip…
  target_quote: “依据自己的智慧学得的一部、两部或整个三藏佛语，对此忆持、宣说、令诵，这称为教理义务。生活简朴并乐于偏远坐卧处[的比库]于自体建立坏灭（想）后，持恒培育观智后证得阿拉汉（果），这称为观禅义务。”
- unit_id: 122-54-406-427
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-54-406-427
  line: 126
  source_quote: Tasmā te cakkhūni nassantu vā bhijjantu vā, buddhasāsanameva dhārehi,
    mā cakkhūnī’’ ti bhūtakāyaṃ ovadanto imā gāthāyo abhāsi–
  target_quote: 因此，就让你的双眼毁掉或者迸裂吧，你只要保持佛陀的教法而不是双眼。”教诫完（依于四大）种而成的身体，他诵出了这些偈颂：
- unit_id: 122-105-19-59
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-105-19-59
  line: 319
  source_quote: Yathā hi bahūsu ekato gāmaghātādīni kammāni karontesu‘‘ ko etesaṃ
    pubbaṅgamo’’ ti vutte yo nesaṃ paccayo hoti, yaṃ nissāya te taṃ kammaṃ karonti,
    so datto vā mitto vā tesaṃ pubbaṅgamoti vuccati, evaṃsampadamidaṃ veditabbaṃ.
  target_quote: 正如当很多人一起造做劫掠村庄等的业时，如果问“谁是他们先行者？”，那么何人是他们的缘，依靠何人他们造了这个业，无论那人是愚人或是朋友，都被称为“他们的先行者”，当了知如是达成的此（譬喻本体——意先行）。
- unit_id: 122-106-81-109
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-106-81-109
  line: 330
  source_quote: Evaṃ manasā ce paduṭṭhena, bhāsati vā karoti vā so bhāsamāno catubbidhaṃ
    vacīduccaritameva bhāsati, karonto tividhaṃ kāyaduccaritameva karoti, abhāsanto
    akaronto tāya abhijjhādīhi paduṭṭhamānasatāya tividhaṃ manoduccaritaṃ pūreti.
  target_quote: 如是，若以染污意，或语或行动，当他说时只说四种语恶行，行动时只做三种身恶行，既不说也不做时，因被贪婪等所染污之意而盈满三种意恶行。
- unit_id: 122-112-150-158
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-112-150-158
  line: 355
  source_quote: Athassa te yaṃ vā taṃ vā rukkhatacādiṃ ācikkhanti.
  target_quote: 当时医生们告诉他模棱两可的树皮等（药）。
variant_translations:
- 若以染污意，或语或行动；
- 一天，他在浴场洗完澡回来的路上看到一棵枝繁叶茂的树王，（心想）这树上一定住有大威力的天神。于是他将树下打扫干净，建了围墙并铺上沙子，还竖了一面旗幡。装饰了树王后合掌说：“如果能获得一个儿子或者女儿，…
- “儿女、兄弟、财产都不会跟着去往来世者而去，连身体也不会同自己一起去，住在家里对我又有何益？我要出家！”
- “依据自己的智慧学得的一部、两部或整个三藏佛语，对此忆持、宣说、令诵，这称为教理义务。生活简朴并乐于偏远坐卧处[的比库]于自体建立坏灭（想）后，持恒培育观智后证得阿拉汉（果），这称为观禅义务。”
- 因此，就让你的双眼毁掉或者迸裂吧，你只要保持佛陀的教法而不是双眼。”教诫完（依于四大）种而成的身体，他诵出了这些偈颂：
- 正如当很多人一起造做劫掠村庄等的业时，如果问“谁是他们先行者？”，那么何人是他们的缘，依靠何人他们造了这个业，无论那人是愚人或是朋友，都被称为“他们的先行者”，当了知如是达成的此（譬喻本体——意先行…
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.88
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-conditional-clause-848b81ac

```yaml
id: open-syntax-conditional-clause-848b81ac
version_id: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0
type: sentence_pattern
name: conditional
description: 把条件从句译为若、如果、当……时等条件关系。
grammar_category: conditional
source_pattern: sace / ce / yadi + clause
translation_pattern: 说 / 不 / 如 / 若 / 时 / 以
technique: 把条件从句译为若、如果、当……时等条件关系。
occurrence_count: 147
chunk_count: 46
top_chunks:
- chunk_id: chunk-0035
  count: 7
- chunk_id: chunk-0005
  count: 6
- chunk_id: chunk-0026
  count: 6
- chunk_id: chunk-0029
  count: 6
- chunk_id: chunk-0004
  count: 5
- chunk_id: chunk-0012
  count: 5
- chunk_id: chunk-0015
  count: 5
- chunk_id: chunk-0019
  count: 5
evidence:
- unit_id: 122-41-2-10
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-41-2-10
  line: 25
  source_quote: Manasā ce paduṭṭhena, bhāsati vā karoti vā;
  target_quote: 若以染污意，或语或行动；
- unit_id: 122-44-13-65
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-44-13-65
  line: 32
  source_quote: So ekadivasaṃ nhānatitthaṃ nhatvā natvā āgacchanto antarāmagge sampannapattasākhaṃ
    ekaṃ vanappatiṃ disvā‘‘ ayaṃ mahesakkhāya devatāya pariggahito bhavissatī’’ ti
    tassa heṭṭhābhāgaṃ sodhāpetvā pākāraparikkhepaṃ kārāpetvā vālukaṃ okirāpetvā dhajapaṭākaṃ
    ussāpet…
  target_quote: 一天，他在浴场洗完澡回来的路上看到一棵枝繁叶茂的树王，（心想）这树上一定住有大威力的天神。于是他将树下打扫干净，建了围墙并铺上沙子，还竖了一面旗幡。装饰了树王后合掌说：“如果能获得一个儿子或者女儿，我将向您做大敬奉。”许完愿他就离开了。
- unit_id: 122-52-27-90
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-52-27-90
  line: 84
  source_quote: Manussā vattasampanne bhikkhū disvāva pasannacittā āsanāni paññāpetvā
    nisīdāpetvā paṇītenāhārena parivisitvā,‘‘ bhante, kuhiṃ ayyā gacchantī’’ ti pucchitvā‘‘
    yathāphāsukaṭṭhānaṃ upāsakā’’ ti vutte paṇḍitā manussā‘‘ vassāvāsaṃ senāsanaṃ
    pariyesanti bhadantā’’ …
  target_quote: 人们一看到这群具足行仪的比库就心生净信，他们敷设座位并邀请入座，以胜妙的食物款待后，问道：“尊者，你们要去哪里？”，“近事男们，任何安乐之处。”
    当这样说时，这些贤智之人就知道尊者们在找雨安居的坐卧处。他们说：“诸位尊者，如果圣尊们这三个月能住在这里，我们将能住立于皈依并能获得戒。”
- unit_id: 122-95-64-82
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-95-64-82
  line: 293
  source_quote: ‘‘ Sace me akkhīni pākatikāni kātuṃ sakkhissasi, ahaṃ te saddhiṃ puttadhītāhi
    dāsī bhavissāmī’’ ti.
  target_quote: “如果我的眼睛能复原，我和我的儿女们将做您的奴仆。”
- unit_id: 122-106-81-109
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-106-81-109
  line: 330
  source_quote: Evaṃ manasā ce paduṭṭhena, bhāsati vā karoti vā so bhāsamāno catubbidhaṃ
    vacīduccaritameva bhāsati, karonto tividhaṃ kāyaduccaritameva karoti, abhāsanto
    akaronto tāya abhijjhādīhi paduṭṭhamānasatāya tividhaṃ manoduccaritaṃ pūreti.
  target_quote: 如是，若以染污意，或语或行动，当他说时只说四种语恶行，行动时只做三种身恶行，既不说也不做时，因被贪婪等所染污之意而盈满三种意恶行。
- unit_id: 122-112-31-53
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-112-31-53
  line: 346
  source_quote: Athassa pilandhanaṃ kāretukāmo‘‘ sace suvaṇṇakāre kāressāmi, bhattavetanaṃ
    dātabbaṃ bhavissatī’’ ti sayameva suvaṇṇaṃ koṭṭetvā maṭṭhāni kuṇḍalāni katvā adāsi.
  target_quote: 当时，他想让人为儿子打造一件首饰，（想）道：“如果让金匠们做，还要提供餐食和薪酬”，他就自己锻打黄金，制成一副光滑的耳环给（儿子）。
- unit_id: 122-112-86-96
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-112-86-96
  line: 350
  source_quote: ‘‘ Bhoti sace vejjaṃ ānessāmi, bhattavetanaṃ dātabbaṃ bhavissati;
  target_quote: “夫人啊，如果我请医生来，就得提供餐食和薪酬，
- unit_id: 122-212-2-10
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-212-2-10
  line: 484
  source_quote: Manasā ce pasannena, bhāsati vā karoti vā;
  target_quote: 若以清净意，或语或行动，
variant_translations:
- 若以染污意，或语或行动；
- 一天，他在浴场洗完澡回来的路上看到一棵枝繁叶茂的树王，（心想）这树上一定住有大威力的天神。于是他将树下打扫干净，建了围墙并铺上沙子，还竖了一面旗幡。装饰了树王后合掌说：“如果能获得一个儿子或者女儿，…
- 人们一看到这群具足行仪的比库就心生净信，他们敷设座位并邀请入座，以胜妙的食物款待后，问道：“尊者，你们要去哪里？”，“近事男们，任何安乐之处。” 当这样说时，这些贤智之人就知道尊者们在找雨安居的坐卧…
- “如果我的眼睛能复原，我和我的儿女们将做您的奴仆。”
- 如是，若以染污意，或语或行动，当他说时只说四种语恶行，行动时只做三种身恶行，既不说也不做时，因被贪婪等所染污之意而盈满三种意恶行。
- 当时，他想让人为儿子打造一件首饰，（想）道：“如果让金匠们做，还要提供餐食和薪酬”，他就自己锻打黄金，制成一副光滑的耳环给（儿子）。
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
version_id: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0
type: sentence_pattern
name: coordination
description: 把多项并列译为和、与、以及，或用顿号/换行列举。
grammar_category: coordination
source_pattern: X ca Y ca
translation_pattern: 和 / 时 / 不 / 以 / 说 / 如
technique: 把多项并列译为和、与、以及，或用顿号/换行列举。
occurrence_count: 132
chunk_count: 50
top_chunks:
- chunk_id: chunk-0024
  count: 8
- chunk_id: chunk-0004
  count: 5
- chunk_id: chunk-0005
  count: 5
- chunk_id: chunk-0020
  count: 5
- chunk_id: chunk-0041
  count: 5
- chunk_id: chunk-0008
  count: 4
- chunk_id: chunk-0018
  count: 4
- chunk_id: chunk-0022
  count: 4
evidence:
- unit_id: 122-46-2-20
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-2-20
  line: 43
  source_quote: Tasmiṃ samaye satthā pavattitavaradhammacakko anupubbenāgantvā anāthapiṇḍikena
    mahāseṭṭhinā catupaṇṇāsakoṭidhanaṃ vissajjetvā kārite jetavanamahāvihāre viharati
    mahājanaṃ saggamagge ca mokkhamagge ca patiṭṭhāpayamāno.
  target_quote: 那时导师已转起殊胜的法轮，次第到达了由给孤独大富翁(anāthapiṇḍika mahāseṭṭhi)施舍五亿四千万钱财所建造的揭德林大寺，并于居住期间令大众住立于天界之道和解脱之道上。
- unit_id: 122-53-116-128
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-53-116-128
  line: 93
  source_quote: Pamattassa ca nāma cattāro apāyā sakagehasadisā, appamattā hothāvuso’’
    ti.
  target_quote: 而且，四恶趣就像放逸者自己的家，成为不放逸者吧，贤友们！”
- unit_id: 122-72-150-202
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-72-150-202
  line: 172
  source_quote: ‘‘ Mā vo, āvuso, evaṃ ruccittha, evaṃ sante mayhaṃ aphāsukaṃ bhavissati,
    mayhaṃ kaniṭṭho pana tumhe disvā pucchissati, athassa mama cakkhūnaṃ parihīnabhāvaṃ
    āroceyyātha, so mayhaṃ santikaṃ kañcideva pahiṇissati, tena saddhiṃ āgacchissāmi,
    tumhe mama vacanena …
  target_quote: “贤友们，你们不要乐于如此（走），这样的话我就会不安乐的。此外，我弟弟看到你们后，将会问起（我），你们就把我视力已经衰弱的情况告诉他，他就会派人来到我这里，我会跟那个（人）一起走，请以我的话礼敬十力（佛陀）和八十大长老。“说完后就送走了他们。
- unit_id: 122-93-2-36
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-93-2-36
  line: 267
  source_quote: Athekadivasaṃ disāvāsino bhikkhū‘‘ satthāraṃ passissāmā’’ ti jetavanaṃ
    āgantvā tathāgataṃ vanditvā asītimahāthere ca, vanditvā vihāracārikaṃ carantā
    cakkhupālattherassa vasanaṭṭhānaṃ patvā‘‘ idampi passissāmā’’ ti sāyaṃ tadabhimukhā
    ahesuṃ.
  target_quote: 当时，有一天，住于他方的一些比库（心想）：“我们要看望导师”，他们来到揭德林，礼敬佛陀和八十大长老后，当在寺院里漫步时，到达了护眼长老的住处，说“我们也看看此处吧”。就在傍晚时来到该处前面。
- unit_id: 122-106-16-54
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-106-16-54
  line: 328
  source_quote: Yathā hi pasannaṃ udakaṃ āgantukehi nīlādīhi upakkiliṭṭhaṃ nīlodakādibhedaṃ
    hoti, na ca navaṃ udakaṃ, nāpi purimaṃ pasannaudakameva, tathā tampi āgantukehi
    abhijjhādīhi dosehi paduṭṭhaṃ hoti, na ca navaṃ cittaṃ, nāpi purimaṃ bhavaṅgacittameva,
    tenāha bhagavā–
  target_quote: 就像清水被外来的青色等染污时，而有青色等种类的水，但（它）既不是新的水，也不是原先的清水；同样的，它（意）虽然被外来的贪婪等过失所染污，但（它）既不是新的心，也不是原先的有分心。因此跋葛瓦说：
- unit_id: 122-233-95-124
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-233-95-124
  line: 577
  source_quote: ‘‘ Tena hi khamāpehī’’ ti vutte‘‘ eso, mahārāja, maṃ jaṭāsu ca gīvāya
    ca akkami, nāhaṃ etaṃ kūṭajaṭilaṃ khamāpemī’’ ti.
  target_quote: “既然如此，你就请求原谅吧！”当如此说时，（戴维拉）说：“大王，他踩了我的发髻和脖子，我不向这狡诈的髻发者请求原谅。”
- unit_id: 122-241-31-73
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-241-31-73
  line: 595
  source_quote: Ye ca tan ti ye keci devatā vā manussā vā gahaṭṭhā vā pabbajitā vā
    taṃ‘‘ akkocchi man’’ tiādivatthukaṃ kodhaṃ sakaṭadhuraṃ viya naddhinā pūtimacchādīni
    viya ca kusādīhi punappunaṃ veṭhetvā upanayhanti, tesaṃ sakiṃ uppannaṃ veraṃ na
    {sammatī}ti vūpasammati.
  target_quote: “若人[怀]此[恨]”（Ye ca taṃ）：若任何天人、人、在家人或出家人，犹如用皮带层层缠绕车轭，又如用香茅草等层层包裹咸鱼等那样，怀有基于“他曾辱骂我”等[而产生]的那怨恨，他们生起一次的怨恨就不能平息、止息。
- unit_id: 122-246-2-17
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-246-2-17
  line: 604
  source_quote: Eko kira kuṭumbikaputto pitari kālakate khette ca ghare ca sabbakammāni
    attanāva karonto mātaraṃ paṭijaggi.
  target_quote: 据说，一个富人的儿子在父亲死后，一边独自处理田间和家里所有事务，一边赡养母亲。
variant_translations:
- 那时导师已转起殊胜的法轮，次第到达了由给孤独大富翁(anāthapiṇḍika mahāseṭṭhi)施舍五亿四千万钱财所建造的揭德林大寺，并于居住期间令大众住立于天界之道和解脱之道上。
- 而且，四恶趣就像放逸者自己的家，成为不放逸者吧，贤友们！”
- “贤友们，你们不要乐于如此（走），这样的话我就会不安乐的。此外，我弟弟看到你们后，将会问起（我），你们就把我视力已经衰弱的情况告诉他，他就会派人来到我这里，我会跟那个（人）一起走，请以我的话礼敬十力…
- 当时，有一天，住于他方的一些比库（心想）：“我们要看望导师”，他们来到揭德林，礼敬佛陀和八十大长老后，当在寺院里漫步时，到达了护眼长老的住处，说“我们也看看此处吧”。就在傍晚时来到该处前面。
- 就像清水被外来的青色等染污时，而有青色等种类的水，但（它）既不是新的水，也不是原先的清水；同样的，它（意）虽然被外来的贪婪等过失所染污，但（它）既不是新的心，也不是原先的有分心。因此跋葛瓦说：
- “既然如此，你就请求原谅吧！”当如此说时，（戴维拉）说：“大王，他踩了我的发髻和脖子，我不向这狡诈的髻发者请求原谅。”
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.85
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-relative-correlative-56a796f6

```yaml
id: open-syntax-relative-correlative-56a796f6
version_id: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0
type: sentence_pattern
name: relative_correlative
description: 把关系从句转成汉语的所、凡、若、此/彼对应关系。
grammar_category: relative_correlative
source_pattern: ya-/yo- relative + ta-/so- correlative
translation_pattern: 说 / 若 / 不 / 以 / 如 / 时
technique: 把关系从句转成汉语的所、凡、若、此/彼对应关系。
occurrence_count: 127
chunk_count: 44
top_chunks:
- chunk_id: chunk-0011
  count: 7
- chunk_id: chunk-0018
  count: 7
- chunk_id: chunk-0004
  count: 6
- chunk_id: chunk-0038
  count: 6
- chunk_id: chunk-0039
  count: 6
- chunk_id: chunk-0024
  count: 5
- chunk_id: chunk-0031
  count: 5
- chunk_id: chunk-0035
  count: 5
evidence:
- unit_id: 122-46-107-116
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-46-107-116
  line: 48
  source_quote: Annapānabhesajjesu yo yaṃ icchati, tassa taṃ yathicchitameva sampajjati.
  target_quote: 无论哪位[比库]需要食物、饮料、药物中的任何物品，其所需之物都会如所需充分提供。
- unit_id: 122-48-136-160
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-48-136-160
  line: 66
  source_quote: ‘‘ tāta, yaṃ mayhaṃ imasmiṃ gehe saviññāṇakampi aviññāṇakampi dhanaṃ
    kiñci atthi, sabbaṃ taṃ tava bhāro, paṭipajjāhi nan’’ ti.
  target_quote: “弟弟啊！在我的这个家中任何有生命或无生命的财产，那一切都是你的责任了，把它承担起来吧！”
- unit_id: 122-50-2-11
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-50-2-11
  line: 75
  source_quote: Yassa so vihatatthāmo, kathaṃ dhammaṃ carissati’’.
  target_quote: 气力已衰竭，彼何堪修法？”
- unit_id: 122-105-19-59
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-105-19-59
  line: 319
  source_quote: Yathā hi bahūsu ekato gāmaghātādīni kammāni karontesu‘‘ ko etesaṃ
    pubbaṅgamo’’ ti vutte yo nesaṃ paccayo hoti, yaṃ nissāya te taṃ kammaṃ karonti,
    so datto vā mitto vā tesaṃ pubbaṅgamoti vuccati, evaṃsampadamidaṃ veditabbaṃ.
  target_quote: 正如当很多人一起造做劫掠村庄等的业时，如果问“谁是他们先行者？”，那么何人是他们的缘，依靠何人他们造了这个业，无论那人是愚人或是朋友，都被称为“他们的先行者”，当了知如是达成的此（譬喻本体——意先行）。
- unit_id: 122-112-150-158
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-112-150-158
  line: 355
  source_quote: Athassa te yaṃ vā taṃ vā rukkhatacādiṃ ācikkhanti.
  target_quote: 当时医生们告诉他模棱两可的树皮等（药）。
- unit_id: 122-214-51-97
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-214-51-97
  line: 491
  source_quote: Yathā hi bahūsu ekato hutvā mahābhikkhusaṅghassa cīvaradānādīni vā
    uḷārapūjādhammassavanādīni vā mālāgandhasakkārakaraṇādīni vā puññāni karontesu‘‘
    ko etesaṃ pubbaṅgamo’’ ti vutte yo tesaṃ paccayo hoti, yaṃ nissāya te tāni puññāni
    karonti, so tisso vā phusso …
  target_quote: 正如当很多人一起，作供养大比库僧团衣等（功德）、作殊胜的敬奉、闻法（的功德），或作用花、香敬奉等功德时，如果问“他们之中谁是先行者？”那么何人是他们的缘，依靠何人他们作了那些功德。无论是帝思（Tissa）或普思（Phussa），他都被称为他们的先行者，当了知如是达成的此[譬喻本体——意先行]。
- unit_id: 122-226-6-34
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-226-6-34
  line: 562
  source_quote: Nārado,‘‘ ācariya, mayhaṃ doso natthīti mama vadantasseva tumhe abhisapatha,
    yassa doso atthi, tassa muddhā phalatu, mā niddosassā’’ ti vatvā–
  target_quote: 那勒德说：“就在我说'老师，我没有过失'时，您发出了诅咒，（那么）谁有过失，就让他的头碎裂吧，而非无过失者。”
- unit_id: 122-233-2-33
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-233-2-33
  line: 573
  source_quote: Nārado sabbaṃ taṃ pavattiṃ ācikkhitvā iminā kāraṇena ahaṃ iminā abhisapito,
    athāhaṃ‘‘ mayhaṃ doso natthi, yassa doso atthi, tasseva upari abhisapo patatū’’
    ti vatvā abhisapiṃ.
  target_quote: 那勒德告知了那一切经过，“我因这个原因而被他诅咒了，我当时说：‘我没有过失，谁有过失，就让诅咒落在他之上“。随后发出了诅咒。
variant_translations:
- 无论哪位[比库]需要食物、饮料、药物中的任何物品，其所需之物都会如所需充分提供。
- “弟弟啊！在我的这个家中任何有生命或无生命的财产，那一切都是你的责任了，把它承担起来吧！”
- 气力已衰竭，彼何堪修法？”
- 正如当很多人一起造做劫掠村庄等的业时，如果问“谁是他们先行者？”，那么何人是他们的缘，依靠何人他们造了这个业，无论那人是愚人或是朋友，都被称为“他们的先行者”，当了知如是达成的此（譬喻本体——意先行…
- 当时医生们告诉他模棱两可的树皮等（药）。
- 正如当很多人一起，作供养大比库僧团衣等（功德）、作殊胜的敬奉、闻法（的功德），或作用花、香敬奉等功德时，如果问“他们之中谁是先行者？”那么何人是他们的缘，依靠何人他们作了那些功德。无论是帝思（Tis…
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.84
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-gerundive-obligation-fcba4188

```yaml
id: open-syntax-gerundive-obligation-fcba4188
version_id: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0
type: sentence_pattern
name: gerundive_or_obligation
description: 把应做、可做、当知、应被理解等义务或可能性显化。
grammar_category: gerundive_or_obligation
source_pattern: -tabba / -anīya forms
translation_pattern: 应 / 不 / 时 / 说 / 如 / ？
technique: 把应做、可做、当知、应被理解等义务或可能性显化。
occurrence_count: 83
chunk_count: 36
top_chunks:
- chunk_id: chunk-0022
  count: 6
- chunk_id: chunk-0003
  count: 5
- chunk_id: chunk-0033
  count: 5
- chunk_id: chunk-0016
  count: 4
- chunk_id: chunk-0002
  count: 3
- chunk_id: chunk-0005
  count: 3
- chunk_id: chunk-0015
  count: 3
- chunk_id: chunk-0018
  count: 3
evidence:
- unit_id: 122-53-78-92
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-53-78-92
  line: 91
  source_quote: ‘‘ Kiṃ panetaṃ, āvuso, patirūpaṃ, nanu appamattehi bhavitabbaṃ’’?
  target_quote: “贤友们，这怎么合适呢？难道不是应当成为不放逸者吗？
- unit_id: 122-53-93-115
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-53-93-115
  line: 92
  source_quote: ‘‘ Mayañhi dharamānakassa buddhassa santikā kammaṭṭhānaṃ gahetvā āgatā,
    buddhā ca nāma na sakkā pamādena ārādhetuṃ, kalyāṇajjhāsayena te vo ārādhetabbā.
  target_quote: 我们从活着的佛陀面前获得业处而来，确实不能透过放逸令诸佛满意，你们必须以良善的意欲来取悦他们。
- unit_id: 122-105-19-59
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-105-19-59
  line: 319
  source_quote: Yathā hi bahūsu ekato gāmaghātādīni kammāni karontesu‘‘ ko etesaṃ
    pubbaṅgamo’’ ti vutte yo nesaṃ paccayo hoti, yaṃ nissāya te taṃ kammaṃ karonti,
    so datto vā mitto vā tesaṃ pubbaṅgamoti vuccati, evaṃsampadamidaṃ veditabbaṃ.
  target_quote: 正如当很多人一起造做劫掠村庄等的业时，如果问“谁是他们先行者？”，那么何人是他们的缘，依靠何人他们造了这个业，无论那人是愚人或是朋友，都被称为“他们的先行者”，当了知如是达成的此（譬喻本体——意先行）。
- unit_id: 122-112-31-53
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-112-31-53
  line: 346
  source_quote: Athassa pilandhanaṃ kāretukāmo‘‘ sace suvaṇṇakāre kāressāmi, bhattavetanaṃ
    dātabbaṃ bhavissatī’’ ti sayameva suvaṇṇaṃ koṭṭetvā maṭṭhāni kuṇḍalāni katvā adāsi.
  target_quote: 当时，他想让人为儿子打造一件首饰，（想）道：“如果让金匠们做，还要提供餐食和薪酬”，他就自己锻打黄金，制成一副光滑的耳环给（儿子）。
- unit_id: 122-112-86-96
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-112-86-96
  line: 350
  source_quote: ‘‘ Bhoti sace vejjaṃ ānessāmi, bhattavetanaṃ dātabbaṃ bhavissati;
  target_quote: “夫人啊，如果我请医生来，就得提供餐食和薪酬，
- unit_id: 122-114-18-63
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-114-18-63
  line: 377
  source_quote: Māṇavo‘‘ kiṃ obhāso nāmeso’’ ti parivattetvā nipannova satthāraṃ disvā,‘‘
    andhabālapitaraṃ nissāya evarūpaṃ buddhaṃ upasaṅkamitvā kāyaveyyāvaṭikaṃ vā kātuṃ
    dānaṃ vā dātuṃ dhammaṃ vā sotuṃ nālatthaṃ, idāni me hatthāpi anadhipateyyā, aññaṃ
    kattabbaṃ natthī’’ ti…
  target_quote: 年轻人想“这是什么光？”于是翻过身，就躺着看到了导师，（心想）“因愚昧父亲之故，我不能亲近这样的佛陀、以身侍奉、供布施或听法，现在我的手都不听使唤了，没有其他能做的了。”心就生起了净信。
- unit_id: 122-204-55-67
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-204-55-67
  line: 460
  source_quote: So satthu adhivāsanaṃ viditvā vegenāgantvā sake nivesane paṇītaṃ khādanīyaṃ
    bhojanīyañca paṭiyādāpesi.
  target_quote: '知道导师同意之后，他迅速返回，令人在自己家

    里准备了胜妙的主食和副食。'
- unit_id: 122-214-51-97
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-214-51-97
  line: 491
  source_quote: Yathā hi bahūsu ekato hutvā mahābhikkhusaṅghassa cīvaradānādīni vā
    uḷārapūjādhammassavanādīni vā mālāgandhasakkārakaraṇādīni vā puññāni karontesu‘‘
    ko etesaṃ pubbaṅgamo’’ ti vutte yo tesaṃ paccayo hoti, yaṃ nissāya te tāni puññāni
    karonti, so tisso vā phusso …
  target_quote: 正如当很多人一起，作供养大比库僧团衣等（功德）、作殊胜的敬奉、闻法（的功德），或作用花、香敬奉等功德时，如果问“他们之中谁是先行者？”那么何人是他们的缘，依靠何人他们作了那些功德。无论是帝思（Tissa）或普思（Phussa），他都被称为他们的先行者，当了知如是达成的此[譬喻本体——意先行]。
variant_translations:
- “贤友们，这怎么合适呢？难道不是应当成为不放逸者吗？
- 我们从活着的佛陀面前获得业处而来，确实不能透过放逸令诸佛满意，你们必须以良善的意欲来取悦他们。
- 正如当很多人一起造做劫掠村庄等的业时，如果问“谁是他们先行者？”，那么何人是他们的缘，依靠何人他们造了这个业，无论那人是愚人或是朋友，都被称为“他们的先行者”，当了知如是达成的此（譬喻本体——意先行…
- 当时，他想让人为儿子打造一件首饰，（想）道：“如果让金匠们做，还要提供餐食和薪酬”，他就自己锻打黄金，制成一副光滑的耳环给（儿子）。
- “夫人啊，如果我请医生来，就得提供餐食和薪酬，
- 年轻人想“这是什么光？”于是翻过身，就躺着看到了导师，（心想）“因愚昧父亲之故，我不能亲近这样的佛陀、以身侍奉、供布施或听法，现在我的手都不听使唤了，没有其他能做的了。”心就生起了净信。
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.77
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-cause-reason-relation-43b7ef06

```yaml
id: open-syntax-cause-reason-relation-43b7ef06
version_id: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0
type: sentence_pattern
name: cause_or_reason
description: 把原因、条件或依据译为因为、由于、以……为缘。
grammar_category: cause_or_reason
source_pattern: kāraṇā / hetu / hetunā / paccayā
translation_pattern: ？ / 说 / 时 / 因为 / 以 / 当
technique: 把原因、条件或依据译为因为、由于、以……为缘。
occurrence_count: 52
chunk_count: 28
top_chunks:
- chunk_id: chunk-0032
  count: 5
- chunk_id: chunk-0023
  count: 4
- chunk_id: chunk-0001
  count: 3
- chunk_id: chunk-0009
  count: 3
- chunk_id: chunk-0021
  count: 3
- chunk_id: chunk-0029
  count: 3
- chunk_id: chunk-0041
  count: 3
- chunk_id: chunk-0005
  count: 2
evidence:
- unit_id: 122-58-2-7
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-58-2-7
  line: 130
  source_quote: Kiṃ kāraṇā pālita tvaṃ pamajjasi.
  target_quote: 大护！汝何故放逸？
- unit_id: 122-62-2-7
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-62-2-7
  line: 134
  source_quote: Kiṃ kāraṇā pālita tvaṃ pamajjasi.
  target_quote: 大护！汝何故放逸？
- unit_id: 122-66-2-10
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-66-2-10
  line: 138
  source_quote: Kiṃ kāraṇā pālita tvaṃ pamajjasī’’ ti.
  target_quote: 大护！汝何故放逸？”
- unit_id: 122-263-28-35
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-263-28-35
  line: 731
  source_quote: ‘‘ Kiṃ kāraṇā’’ ti?
  target_quote: “什么原因呢？”
- unit_id: 122-291-128-136
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-291-128-136
  line: 849
  source_quote: ‘‘ Thero kiṃ kāraṇā’’ ti?
  target_quote: 长老[问]：“什么原因呢？”
- unit_id: 122-351-23-25
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-351-23-25
  line: 1114
  source_quote: Kiṃ kāraṇā?
  target_quote: 什么原因呢？
- unit_id: 122-389-2-22
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-389-2-22
  line: 1339
  source_quote: Tattha asāre {sāramatino}ti cattāro paccayā, dasavatthukā micchādiṭṭhi,
    tassā upanissayabhūtā dhammadesanāti ayaṃ asāro nāma, tasmiṃ sāradiṭṭhinoti attho.
  target_quote: 在此，“糟粕视精要(asāre sāramatino)”：四资具、十事(dasavatthukā)邪见、以及作为那[邪见]强依止的法谈，这叫做糟粕。即“有视那[糟粕]为精要的见解”之义。
- unit_id: 122-400-14-30
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-400-14-30
  line: 1412
  source_quote: Assosuṃ kho bhikkhū,‘‘ āyasmā kira nando bhagavato bhātā mātucchāputto
    accharānaṃ hetu brahmacariyaṃ carati.
  target_quote: 比库们获悉：“据说跋葛瓦的弟弟——姨母之子具寿难德因为天女才修习梵行。
variant_translations:
- 大护！汝何故放逸？
- 大护！汝何故放逸？”
- “什么原因呢？”
- 长老[问]：“什么原因呢？”
- 什么原因呢？
- 在此，“糟粕视精要(asāre sāramatino)”：四资具、十事(dasavatthukā)邪见、以及作为那[邪见]强依止的法谈，这叫做糟粕。即“有视那[糟粕]为精要的见解”之义。
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.72
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-yatha-tatha-correlative-73c1c803

```yaml
id: open-syntax-yatha-tatha-correlative-73c1c803
version_id: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0
type: sentence_pattern
name: correlative_comparison
description: 把如是对应结构译为如……同样/也……。
grammar_category: correlative_comparison
source_pattern: yathā ... tathā ...
translation_pattern: 如 / 同样 / 不 / 时 / 说 / 无
technique: 把如是对应结构译为如……同样/也……。
occurrence_count: 18
chunk_count: 13
top_chunks:
- chunk_id: chunk-0002
  count: 3
- chunk_id: chunk-0003
  count: 2
- chunk_id: chunk-0012
  count: 2
- chunk_id: chunk-0046
  count: 2
- chunk_id: chunk-0004
  count: 1
- chunk_id: chunk-0006
  count: 1
- chunk_id: chunk-0010
  count: 1
- chunk_id: chunk-0011
  count: 1
evidence:
- unit_id: 122-105-103-121
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-105-103-121
  line: 325
  source_quote: Yathā pana dāruādīhi nipphannāni tāni tāni bhaṇḍāni dārumayādīni nāma
    honti, tathā tepi manato nipphannattā manomayā nāma.
  target_quote: 又如因木头等而制成的种种器具被称为“木制等”，同样地，那（三名蕴）也因意而生成，故名“意生成”(manomayā)。
- unit_id: 122-106-16-54
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-106-16-54
  line: 328
  source_quote: Yathā hi pasannaṃ udakaṃ āgantukehi nīlādīhi upakkiliṭṭhaṃ nīlodakādibhedaṃ
    hoti, na ca navaṃ udakaṃ, nāpi purimaṃ pasannaudakameva, tathā tampi āgantukehi
    abhijjhādīhi dosehi paduṭṭhaṃ hoti, na ca navaṃ cittaṃ, nāpi purimaṃ bhavaṅgacittameva,
    tenāha bhagavā–
  target_quote: 就像清水被外来的青色等染污时，而有青色等种类的水，但（它）既不是新的水，也不是原先的清水；同样的，它（意）虽然被外来的贪婪等过失所染污，但（它）既不是新的心，也不是原先的有分心。因此跋葛瓦说：
- unit_id: 122-112-119-132
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-112-119-132
  line: 353
  source_quote: ‘‘ Yathā me dhanacchedo na hoti, tathā karissāmī’’ ti.
  target_quote: “我怎样能不破财，就那样做。”
- unit_id: 122-214-129-142
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-214-129-142
  line: 495
  source_quote: Yathā hi gaṇādīnaṃ adhipati puriso gaṇaseṭṭho seṇiseṭṭhoti vuccati,
    tathā tesampi manova seṭṭho.
  target_quote: 即是说，正如众人等群体中的首领被称为众主、团体之主；同样，唯有它们（三名蕴）的意是主宰。
- unit_id: 122-214-143-158
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-214-143-158
  line: 496
  source_quote: Yathā pana suvaṇṇādīhi nipphāditāni bhaṇḍāni suvaṇṇamayādīni nāma
    honti, tathā etepi manato nipphannattā manomayā nāma.
  target_quote: 又如因金等而制成的种种器具名为“金制等”，同样，那（三名蕴）也因意而生成，故名“意生成”(manomayā)。
- unit_id: 122-256-67-88
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-256-67-88
  line: 679
  source_quote: ‘‘ Bhante, ahaṃ pubbe yathā vā tathā vā jīvikaṃ kappentīpi kucchipūraṃ
    nālatthaṃ, idāni kathaṃ jīvissāmī’’ ti.
  target_quote: “尊者，我以前将就着谋生，也不曾填饱肚子，现在又怎样才能活命呢？”
- unit_id: 122-307-60-90
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-307-60-90
  line: 924
  source_quote: Taṃ {ve}ti evarūpaṃ taṃ puggalaṃ yathā dubbalavāto saṇikaṃ paharanto
    ekagghanaṃ selaṃ cāletuṃ na sakkoti, tathā abbhantare uppajjamānopi dubbalakilesamāro
    nappasahati, khobhetuṃ vā cāletuṃ vā na sakkotīti attho.
  target_quote: “[魔]实[莫胜]彼(taṃ ve)”的含义是：犹如微风徐徐拂过时，无法动摇一块坚厚的岩石[山]，同样地，内心生起的微弱烦恼魔也无法征服、搅扰、动摇那像这样的人。
- unit_id: 122-436-94-116
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-436-94-116
  line: 1522
  source_quote: Maraṇabhayena tajjitassa pana bahinikkhamanaṃ nivāretuṃ asakkonto
    sabbo gehajano yathā antoṭhito bahi vicarituṃ na sakkoti, tathā gehadvārāni thaketvā
    bahigehaṃ parivāretvā rakkhanto acchati.
  target_quote: 无法阻止为死亡的怖畏所威吓者去到外面时，怎样使身处屋内者无法外出，所有家人就那样紧闭屋门，围于屋外而持续守住。
variant_translations:
- 又如因木头等而制成的种种器具被称为“木制等”，同样地，那（三名蕴）也因意而生成，故名“意生成”(manomayā)。
- 就像清水被外来的青色等染污时，而有青色等种类的水，但（它）既不是新的水，也不是原先的清水；同样的，它（意）虽然被外来的贪婪等过失所染污，但（它）既不是新的心，也不是原先的有分心。因此跋葛瓦说：
- “我怎样能不破财，就那样做。”
- 即是说，正如众人等群体中的首领被称为众主、团体之主；同样，唯有它们（三名蕴）的意是主宰。
- 又如因金等而制成的种种器具名为“金制等”，同样，那（三名蕴）也因意而生成，故名“意生成”(manomayā)。
- “尊者，我以前将就着谋生，也不曾填饱肚子，现在又怎样才能活命呢？”
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.64
review_status: machine_generated
discovery_method: open_syntactic_signal
```

## open-syntax-vasena-relation-202efe52

```yaml
id: open-syntax-vasena-relation-202efe52
version_id: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0
type: sentence_pattern
name: relation_by_mode
description: 把方式、依据、范围译为以、依、由于、按照……方式。
grammar_category: relation_by_mode
source_pattern: X-vasena
translation_pattern: 以 / 不 / 通过 / 说 / 如 / 无
technique: 把方式、依据、范围译为以、依、由于、按照……方式。
occurrence_count: 16
chunk_count: 9
top_chunks:
- chunk_id: chunk-0012
  count: 3
- chunk_id: chunk-0039
  count: 3
- chunk_id: chunk-0009
  count: 2
- chunk_id: chunk-0016
  count: 2
- chunk_id: chunk-0043
  count: 2
- chunk_id: chunk-0031
  count: 1
- chunk_id: chunk-0033
  count: 1
- chunk_id: chunk-0041
  count: 1
evidence:
- unit_id: 122-389-46-78
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-389-46-78
  line: 1341
  source_quote: Te sāran ti te pana taṃ micchādiṭṭhiggahaṇaṃ gahetvā ṭhitā kāmavitakkādīnaṃ
    vasena micchāsaṅkappagocarā hutvā sīlasāraṃ, samādhisāraṃ, paññāsāraṃ, vimuttisāraṃ,
    vimuttiñāṇadassanasāraṃ,‘‘ paramatthasāraṃ, nibbānañca nādhigacchan’’ ti.
  target_quote: “彼[不证]精要(te sāra)”：他们执取那被执取的邪见而住，并通过欲寻等而有邪思惟作行境，不能证达戒精要(sīlasāra)、定精要(amādhisāra)、慧精要(paññāsāra)、解脱精要(vimuttisāra)、解脱智见精要(vimuttiñāṇadassanasāra)以及究竟精要(paramatthasāra)的涅槃。
- unit_id: 122-389-102-119
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-389-102-119
  line: 1343
  source_quote: Te sāran ti te paṇḍitā evaṃ sammādassanaṃ gahetvā ṭhitā nekkhammasaṅkappādīnaṃ
    vasena sammāsaṅkappagocarā hutvā taṃ vuttappakāraṃ sāraṃ adhigacchantīti.
  target_quote: “彼[能证精]要(te sāraṃ)”：那些智者取得正见而住，并通过出离思惟等而有正思惟作行境。他们能够证得前述类别的精要。
- unit_id: 122-558-2-18
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-558-2-18
  line: 1911
  source_quote: Iti satthā sīlasampannassa bahussutassa pamādavihārino aniccādivasena
    yonisomanasikāre pamattassa bhikkhuno vasena paṭhamaṃ gāthaṃ kathesi, na dussīlassa.
  target_quote: 如是，第一首偈颂是导师针对已成就戒、多闻，却放逸而住、在以无常等[三相]如理作意方面放逸的比库而说的，并非是对无戒比库。
- unit_id: 122-558-19-28
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-558-19-28
  line: 1912
  source_quote: Dutiyagāthā pana appassutassapi yonisomanasikāre kammaṃ karontassa
    kārakapuggalassa vasena kathitā.
  target_quote: 而第二首偈颂是针对虽然寡闻，却能致力于如理作意的实修者而说的。
- unit_id: 122-559-36-86
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-559-36-86
  line: 1916
  source_quote: So imāya sammāpaṭipattiyā rāgañca dosañca pahāya mohaṃ sammā hetunā
    nayena parijānitabbe dhamme parijānanto tadaṅgavikkhambhanasamucchedapaṭippassaddhinissaraṇavimuttīnaṃ
    vasena suvimuttacitto, anupādiyāno idha vā huraṃ {vā}ti idhalokaparalokapariyāpannā
    vā a…
  target_quote: 他以这种正行道而舍断贪、嗔、痴后，藉由适当之因与方法遍知应遍知之法，通过彼分解脱、镇服解脱、正断解脱、止息解脱、出离解脱而心善解脱。“不执此他世(anupādiyāno
    idha vā huraṃ vā)”：由于不以四种执取而执取属于今生与来世及内在与外在的蕴、处、界，所以成为了大漏尽者，并享有因称为圣道的沙门[法]之力而来的沙门分——沙门果与五种无学法蕴，他就犹如以宝石屋顶而获取了屋顶那样，通过阿拉汉[果]而得达了教法顶峰。
- unit_id: 122-635-82-85
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-635-82-85
  line: 2569
  source_quote: Itaresaṃ dvinnaṃ vasena.
  target_quote: 是因另外[两]人[而说的]。
- unit_id: 122-635-86-94
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-635-86-94
  line: 2570
  source_quote: Buddhā hi āghātaṃ agaṇetvā maggaphalādhigamārahānaṃ vasena dhammaṃ
    desentiyeva.
  target_quote: 事实上，诸佛并不在意[别人的]怨恨，只是因为适合证悟道果者而说法。
- unit_id: 122-2763-46-53
  unit_key: 5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0:122-2763-46-53
  line: 5126
  source_quote: Anantagocaran ti anantārammaṇassa sabbaññutaññāṇassa vasena apariyanta
    gocaraṃ.
  target_quote: '“无边行境”(anantagocaraṃ)

    ：藉由所缘无边的一切知智而有无边行境。'
variant_translations:
- “彼[不证]精要(te sāra)”：他们执取那被执取的邪见而住，并通过欲寻等而有邪思惟作行境，不能证达戒精要(sīlasāra)、定精要(amādhisāra)、慧精要(paññāsāra)、解脱…
- “彼[能证精]要(te sāraṃ)”：那些智者取得正见而住，并通过出离思惟等而有正思惟作行境。他们能够证得前述类别的精要。
- 如是，第一首偈颂是导师针对已成就戒、多闻，却放逸而住、在以无常等[三相]如理作意方面放逸的比库而说的，并非是对无戒比库。
- 而第二首偈颂是针对虽然寡闻，却能致力于如理作意的实修者而说的。
- 他以这种正行道而舍断贪、嗔、痴后，藉由适当之因与方法遍知应遍知之法，通过彼分解脱、镇服解脱、正断解脱、止息解脱、出离解脱而心善解脱。“不执此他世(anupādiyāno
  idha vā huraṃ …
- 是因另外[两]人[而说的]。
conditions:
- 由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。
counter_examples: []
confidence: 0.59
review_status: machine_generated
discovery_method: open_syntactic_signal
```
