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
version_id: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43
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
- open-collocation-paccayo-73560908
- open-collocation-honti-8a2d0644
- open-collocation-vuccati-67761320
- open-collocation-tiadi-98cccd94
- open-collocation-tiadina-d084698e
- open-collocation-ti-ettha-65038982
- open-collocation-bhagava-8b0af50d
- open-collocation-hotiti-d2340631
evidence:
- unit_id: 25-150-24-43
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:25-150-24-43
  line: 56
  source_quote: Tattha yo paccayo paccayuppannadhammassa uppādāya paccayo hoti, yasmiṃ
    asati paccayuppanno dhammo na uppajjati, tassa paccayakiccaṃ jananakiccaṃ nāma.
  target_quote: 在此，某缘作为缘生法生起的缘，没有它缘所生法就不能生起；该缘的功能称为产生的功能。
- unit_id: 25-150-47-74
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:25-150-47-74
  line: 58
  source_quote: Yo paccayo paccayuppannadhammassa ṭhitiyā ca vuḍḍhiyā ca viruḷhiyā
    ca paccayo hoti, yasmiṃ asati paccayuppanno dhammo na tiṭṭhati na vaḍḍhati na
    virūhati, tassa paccayakiccaṃ upatthambhanakiccaṃ nāma.
  target_quote: 某缘作为缘生法保持、扩展、增长的缘，没有它缘生法就不能保持、扩展、增长；该缘的功能称为支持的功能。
- unit_id: 25-150-78-103
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:25-150-78-103
  line: 60
  source_quote: Yo paccayo paccayuppannassa dhammassa pavattiyā paccayo hoti, yena
    vinā paccayuppanno dhammo cirakālaṃ na pavattati, santati gamanaṃ chijjati, tassa
    paccaya kiccaṃ anupālanakiccaṃ nāma.
  target_quote: 某缘作为缘生法运转的缘，没有它缘生法就不能长期运转，相续中断；该缘的功能称为维持的功能。
- unit_id: 64-200-2-11
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:64-200-2-11
  line: 210
  source_quote: Gilānapaccayabhesajjaparikkhāran ti ettha rogassa paṭiayanaṭṭhena
    paccayo, paccanīkagamanaṭṭhenāti attho.
  target_quote: '医疗保健用品(gilānapaccayabhesajjaparikkhāra)

    这里，称为疗paccayo是因为疾病的对治之义，意思是因为扭转之义。'
- unit_id: 64-926-2-57
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:64-926-2-57
  line: 243
  source_quote: Ābhidhammikagodattatthero pana‘‘ purimā purimā kusalā dhammā pacchimānaṃ
    pacchimānaṃ kusalānaṃ dhammānaṃ āsevanapaccayena paccayo’’ ti( paṭṭhā.1.1.12)
    imaṃ suttaṃ vatvā āsevanapaccayena pacchimo pacchimo dhammo balavā h…
  target_quote: '阿毗达摩师（论师）乔达答长老说：“前前诸善法为后后诸

    善法的习行缘 ，依据此种经  中的习行缘来说，则后后诸善法

    的力量更强，所以在第六与第七的速行心也得有安止定的。”然

    而在义疏中却排斥他说：“这是长老一己的意见。”'
- unit_id: 64-927-41-47
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:64-927-41-47
  line: 252
  source_quote: Nirodhassa paccayo nevasaññānāsaññāyatanaṃ dvinnamupari na hoti.
  target_quote: '为灭尽定之缘的非有想非无想处是不会有

    二剎那心以上的。'
- unit_id: 64-2209-2-17
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:64-2209-2-17
  line: 1282
  source_quote: 357. {Paccayato}ti pathavīdhātu āposaṅgahitā tejoanupālitā vāyovitthambhitā
    tiṇṇaṃ mahābhūtānaṃ patiṭṭhā hutvā paccayo hoti.
  target_quote: '（十一）“以缘”，此地界，——以水摄之，以火保护，以

    风支持，是（水火风）三大种的住处及缘。'
- unit_id: 64-2209-18-28
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:64-2209-18-28
  line: 1283
  source_quote: Āpodhātu pathavīpatiṭṭhitā tejoanupālitā vāyovitthambhitā tiṇṇaṃ mahābhūtānaṃ
    ābandhanaṃ hutvā paccayo hoti.
  target_quote: '水界，——以地而

    住，以火保护，以风支持，是（地火风）三大种的结着及缘。'
confidence: 0.72
review_status: machine_generated
discovery_method: open_synthesis
```

## strategy-open-explanatory-citation

```yaml
id: strategy-open-explanatory-citation
version_id: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43
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
- unit_id: 9-54-73-81
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:9-54-73-81
  line: 2
  source_quote: Yakkha pūjāyaṃ, yakkhīyate pūjīyateti yakkho, kuverādiko.
  target_quote: 被祭祀者表达为祭祀，应被祭祀，应被供奉，因此为 被祭祀者，如：俱吠罗，统治北方的神(kuvera)等。
- unit_id: 9-54-82-88
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:9-54-82-88
  line: 3
  source_quote: Rakkhanti attānaṃ etasmāti rakkhaso, vibhīsaṇādi.
  target_quote: '保护自己所远离的，故为

    罗刹，vībhīsana天神。

    非人(amanussa)'
- unit_id: 9-54-92-124
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:9-54-92-124
  line: 4
  source_quote: Pisitaṃ maṃsaṃ asati bhakkhatīti pisāco, sakuni sakuntiādiko kuverānucaro,
    yadādinā pisitassa pibhāvo, asa ssa ca sācā desabhāvo[ pāṇini6.3.109; moggallānapañcikā1.47].
  target_quote: '吃肉pisita，故为啖肉灵，

    俱吠罗，统治北方的神的追随者，

    pi取pisita(肉)的含义，

    sāca取asa（吃）的含义'
- unit_id: 9-489-10-18
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:9-489-10-18
  line: 6
  source_quote: Tattha vividhaṃ aniccādikaṃ saṅkhāresu passatīti vipassanā, yu.
  target_quote: 那里，“在诸行上看种种无常等”是观。
- unit_id: 9-499-31-58
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:9-499-31-58
  line: 7
  source_quote: Kaṃ sukhaṃ rundhatīti karuṇā, rudhi āvaraṇe, dha ssa ṇo, atha vā karonti
    attānamadhīnametāyāti karuṇā, yu, ā, karuṇā, sā eva kāruññaṃ.
  target_quote: '“阻止（rundhati）某种（ka） 快乐”为 悲悯(karuṇā)

    ，[词根] rudhi

    是关闭屏蔽之义+[把其中的音节] dha

    变为 ṇa

    ；又或“完成（karonti）自己与他人的连接[所要凭借的]”名为悲悯

    ，[词根kara]+yu（到达、产生）+ā（阴性名词）= 悲悯，其（中性变体）即为 kāruñña

    。'
- unit_id: 9-501-41-51
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:9-501-41-51
  line: 9
  source_quote: Mida snehe, mijjati sinehatīti mettā, ta, ā.
  target_quote: '[词根] mida

    为爱[之义]，因此“亲近，喜爱”名为 mettā

    =mida（爱）+ta（产生）+ā（阴性名词）'
- unit_id: 9-501-52-55
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:9-501-52-55
  line: 10
  source_quote: Metti, ti.
  target_quote: Metti=mida+ti
- unit_id: 9-501-56-64
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:9-501-56-64
  line: 11
  source_quote: Atha vā mitte bhavā mettā, metti ca.
  target_quote: '又或，友谊为mettā和metti

    。'
confidence: 0.72
review_status: machine_generated
discovery_method: open_synthesis
```

## strategy-open-decomposition

```yaml
id: strategy-open-decomposition
version_id: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43
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
- open-syntax-newline-decomposition-syntax-585a7090
- open-syntax-long-sentence-decomposition-da6644d0
evidence:
- unit_id: 9-499-31-58
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:9-499-31-58
  line: 7
  source_quote: Kaṃ sukhaṃ rundhatīti karuṇā, rudhi āvaraṇe, dha ssa ṇo, atha vā karonti
    attānamadhīnametāyāti karuṇā, yu, ā, karuṇā, sā eva kāruññaṃ.
  target_quote: '“阻止（rundhati）某种（ka） 快乐”为 悲悯(karuṇā)

    ，[词根] rudhi

    是关闭屏蔽之义+[把其中的音节] dha

    变为 ṇa

    ；又或“完成（karonti）自己与他人的连接[所要凭借的]”名为悲悯

    ，[词根kara]+yu（到达、产生）+ā（阴性名词）= 悲悯，其（中性变体）即为 kāruñña

    。'
- unit_id: 9-501-41-51
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:9-501-41-51
  line: 9
  source_quote: Mida snehe, mijjati sinehatīti mettā, ta, ā.
  target_quote: '[词根] mida

    为爱[之义]，因此“亲近，喜爱”名为 mettā

    =mida（爱）+ta（产生）+ā（阴性名词）'
- unit_id: 16-2439-71-90
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:16-2439-71-90
  line: 24
  source_quote: Tathā hi yakkhopi sattopi devopi sakkopi khīṇāsavopi yakkhoyeva nāma,
    mahānubhāvatāya yakkhiyati saraṇagatehi janehi nānāpaccayehi nānābalīhi ca pūjiyatīti
    yakkho.
  target_quote: 同样地，被祭祀者、有情、神(deva)、萨卡天帝、漏尽者皆名为被祭祀者，应被大功德者祭祀祭奠，[展开来说]应被去到庇护所的人们种种因素、种种能力来祭祀祭奠，[此即]被祭祀者。
- unit_id: 16-3253-17-28
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:16-3253-17-28
  line: 30
  source_quote: Kaṃ vuccati sukhaṃ, taṃ rundhati vibādhati kāruṇikaṃ na sukhāpetītipi
    karuṇā.
  target_quote: '凡某种[法]被称为乐，即阻止、妨碍该[法]而不让心怀悲悯者快乐，故亦名为 悲悯

    。'
- unit_id: 23-1037-86-93
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:23-1037-86-93
  line: 45
  source_quote: Natthi attanā gahitaṃ kiñci ārammaṇaṃnāma assāti anārammaṇaṃ.
  target_quote: 对于那[色]来说，的确没有哪个所缘被自身所包含，故为无所缘(anārammaṇa)。
- unit_id: 25-150-2-14
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:25-150-2-14
  line: 53
  source_quote: Ettha vadeyya, dve itthindriyapurisindriyadhammā indriyabhūtā samānāpi
    kasmā indriyapaccaye visuṃ na gahitāti.
  target_quote: 在此，[有人]或许会说：“女性根(itthindriya)和男性根(purisindriya)二法同样作为根(indriya)，在根缘(indriyapaccaya)中却为何单独分开而不被包括[在缘法之内]？”
- unit_id: 25-150-15-17
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:25-150-15-17
  line: 54
  source_quote: Paccayakiccassa abhāvato.
  target_quote: ”[因为它们]没有缘的功能。
- unit_id: 25-150-108-128
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:25-150-108-128
  line: 62
  source_quote: Ete pana dve indriyadhammā tesu tīsu paccaya kiccesu ekakiccaṃpi nasādhenti,
    tasmā ete dve dhammā indriya paccaye visuṃ na gahitāti.
  target_quote: 在此，二根法并没有满足这三种paccayakicca中的任何一种功能，所以，二法在根缘中单独分开而不被包括[在缘法之内]。
confidence: 0.72
review_status: machine_generated
discovery_method: open_synthesis
```

## strategy-open-relation-explicitation

```yaml
id: strategy-open-relation-explicitation
version_id: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43
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
- open-syntax-coordinated-series-9a122f4e
- open-syntax-alternative-series-18071276
- open-syntax-relative-correlative-56a796f6
- open-syntax-conditional-clause-848b81ac
- open-syntax-cause-reason-relation-43b7ef06
- open-syntax-vasena-relation-202efe52
- open-syntax-yatha-tatha-correlative-73c1c803
evidence:
- unit_id: 16-2440-2-11
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:16-2440-2-11
  line: 25
  source_quote: Satte deve ca sakke ca, khīṇāsave ca rakkhase;
  target_quote: 有情、神、萨卡天帝、漏尽者、罗刹，
- unit_id: 25-80-5-20
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:25-80-5-20
  line: 52
  source_quote: Sabbepi atītānāgata paccuppannā ajjhattabahiddhābhūtā cittacetasikarūpadhammā
    ca nibbānañca paññatti ca sabbesaṃ paccuppannānaṃ cittacetasikānaṃ dhammānaṃ yathārahaṃ
    pakatūpanissayo.
  target_quote: 一切过去、未来、现在、作为内在、外在的心、心所(cetasika)、色法、涅槃(nibbāna)和概念，依情况而为一切当下的心、心所法的自性强依止。
- unit_id: 25-150-47-74
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:25-150-47-74
  line: 58
  source_quote: Yo paccayo paccayuppannadhammassa ṭhitiyā ca vuḍḍhiyā ca viruḷhiyā
    ca paccayo hoti, yasmiṃ asati paccayuppanno dhammo na tiṭṭhati na vaḍḍhati na
    virūhati, tassa paccayakiccaṃ upatthambhanakiccaṃ nāma.
  target_quote: 某缘作为缘生法保持、扩展、增长的缘，没有它缘生法就不能保持、扩展、增长；该缘的功能称为支持的功能。
- unit_id: 25-151-60-91
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:25-151-60-91
  line: 70
  source_quote: Na ca itthindriyarūpaṃ te pañcakkhandhadhamme janeti, na ca upatthambhati,
    nāpi anupāleti, atha kho te dhammā attano attano paccayehi uppajjamānā evañcevañca
    uppajjantūti āṇaṃ ṭhapentaṃ viya tesu attano anubhāvaṃ pavatteti.
  target_quote: 女根色并没有产生那些五蕴法，没有支持[它们]，也没有维持[它们]，然而，当那些法依各自的缘生起时，[性根]犹如发出命令“应如此这般地生起”一样，而对它们行使自己的控制力。
- unit_id: 64-147-60-90
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:64-147-60-90
  line: 105
  source_quote: Iti iminā ca ācārena iminā ca gocarena upeto hoti samupeto upagato
    samupagato upapanno sampanno samannāgato, tena vuccati‘‘ ācāragocarasampanno’’
    ti( vibha.511).
  target_quote: 如是具足、善具足、从事、善从事、圆满、善圆满、具备而不离此正行与此行处。因此称为“具足正行与行处”。
- unit_id: 64-148-21-160
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:64-148-21-160
  line: 109
  source_quote: Idhekacco saṅghagatopi acittīkārakato there bhikkhū ghaṭṭayantopi
    tiṭṭhati, ghaṭṭayantopi nisīdati, puratopi tiṭṭhati, puratopi nisīdati, uccepi
    āsane nisīdati, sasīsampi pārupitvā nisīdati, ṭhitakopi bhaṇati, bāhāvikkhepakopi
    bhaṇati, therānaṃ bhikkhūnaṃ anu…
  target_quote: 于此，一些[比库]进入僧团的集会时，不恭敬，排挤上座比库们而站着，排挤[上座比库们]而坐着；站在前面，坐在前面，坐在高座，覆头而坐，站着说话，挥手说话；上座比库们不穿鞋经行时，他却穿鞋经行；[上座比库们]在低处经行，他却在高处；[上座比库们]在地面经行，他却在经行道经行；排挤上座比库们而站着，排挤[上座比库们]而坐着，侵占下座比库们之座；在火房未征询上座比库们便添柴、关门；在河边浴场排挤上座比库们而下水，在[上座比库们]前面下水，排挤上座比库们而沐浴，在[上座比库们]前面沐浴，排挤上座比库们而上来，在[上座比库们…
- unit_id: 64-153-48-60
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:64-153-48-60
  line: 129
  source_quote: Iti iminā ca ācārena iminā ca gocarena upeto… pe… samannāgato.
  target_quote: 如是具足……具备而不离此正行与此行处。
- unit_id: 64-154-26-41
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:64-154-26-41
  line: 133
  source_quote: Ettha ca‘‘ pātimokkhasaṃvarasaṃvuto’’ ti ettāvatā ca puggalādhiṭṭhānāya
    desanāya pātimokkhasaṃvarasīlaṃ dassitaṃ.
  target_quote: 而在这里，就以“防护巴帝摩卡防护”这等文句，通过基于人的开示而阐明了巴帝摩卡防护戒。
confidence: 0.72
review_status: machine_generated
discovery_method: open_synthesis
```

## strategy-open-verbal-relation

```yaml
id: strategy-open-verbal-relation
version_id: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43
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
- unit_id: 23-1363-2-8
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:23-1363-2-8
  line: 48
  source_quote: Puretaraṃ uppajjitvā vattamānabhāvena upakārako dhammo purejātapaccayo.
  target_quote: （比缘所生法）更早生起并通过其存在的状态而起资助(upakāraka)作用的法，即是前生缘(purejātapaccaya)。
- unit_id: 23-1446-374-380
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:23-1446-374-380
  line: 49
  source_quote: Tassa hitasukhaṃ avippakiṇṇaṃ katvā saṅgaṇhatīti attho.
  target_quote: “不破坏其利益快乐而善待”之义。
- unit_id: 64-148-21-160
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:64-148-21-160
  line: 109
  source_quote: Idhekacco saṅghagatopi acittīkārakato there bhikkhū ghaṭṭayantopi
    tiṭṭhati, ghaṭṭayantopi nisīdati, puratopi tiṭṭhati, puratopi nisīdati, uccepi
    āsane nisīdati, sasīsampi pārupitvā nisīdati, ṭhitakopi bhaṇati, bāhāvikkhepakopi
    bhaṇati, therānaṃ bhikkhūnaṃ anu…
  target_quote: 于此，一些[比库]进入僧团的集会时，不恭敬，排挤上座比库们而站着，排挤[上座比库们]而坐着；站在前面，坐在前面，坐在高座，覆头而坐，站着说话，挥手说话；上座比库们不穿鞋经行时，他却穿鞋经行；[上座比库们]在低处经行，他却在高处；[上座比库们]在地面经行，他却在经行道经行；排挤上座比库们而站着，排挤[上座比库们]而坐着，侵占下座比库们之座；在火房未征询上座比库们便添柴、关门；在河边浴场排挤上座比库们而下水，在[上座比库们]前面下水，排挤上座比库们而沐浴，在[上座比库们]前面沐浴，排挤上座比库们而上来，在[上座比库们…
- unit_id: 64-191-2-23
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:64-191-2-23
  line: 136
  source_quote: 18. Yaṃ panetaṃ tadanantaraṃ paccayasannissitasīlaṃ vuttaṃ, tattha
    paṭisaṅkhā {yoniso}ti upāyena pathena paṭisaṅkhāya ñatvā, paccavekkhitvāti attho
    .
  target_quote: '紧接上文（ 活命清净戒 ）在所说的资具依止戒中，如理省思完之后

    的意思是用（适合禅修的）方式、（正确的）方法来省思、知道、省察后。'
- unit_id: 64-191-149-179
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:64-191-149-179
  line: 152
  source_quote: '{Sarīsapā}ti ye keci sarantā gacchanti dīghajātikā sappādayo, tesaṃ
    daṭṭhasamphasso ca phuṭṭhasamphasso cāti duvidho samphasso, sopi cīvaraṃ pārupitvā
    nisinnaṃ na bādhati, tasmā tādisesu ṭhānesu tesaṃ paṭighātatthāya paṭisevati.'
  target_quote: “爬虫(sarīsapa)”，即任何爬行的长虫类如蛇等，它们具有咬触和碰触两种接触，其（两种触）无法折磨披著衣而坐者，因此，在那样的情况下为了防御那（两种触）而受用（衣）。
- unit_id: 64-196-2-11
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:64-196-2-11
  line: 193
  source_quote: ‘ ‘ Cattāro pañca ālope, abhutvā udakaṃ pive;
  target_quote: 少吃四、五口，然后可喝水。
- unit_id: 64-199-27-32
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:64-199-27-32
  line: 199
  source_quote: Taṃ ekato katvā senāsananti vuccati.
  target_quote: 把那（卧处、坐处）合为一个（复合词）后，而称为“坐卧处”。
- unit_id: 64-199-111-134
  unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:64-199-111-134
  line: 209
  source_quote: Ye yattha apariguttiyā ca asappāyarūpadassanādinā ca ābādhaṃ na karonti,
    taṃ senāsanaṃ evaṃ jānitvā paccavekkhitvā paṭisevanto bhikkhu paṭisaṅkhā yoniso
    senāsanaṃ utuparissayavinodanatthaṃ paṭisevatīti veditabbo.
  target_quote: '在这样的地方，（上述两种危险）不会因为没有对外环境防护和看到不适宜的色所缘(rūpārammaṇa)等而（对住在此的人）造成压迫，

    当知比库以该方式确认那坐卧处（已免除了两种危险），然后省思并受用，即（所说的）“如理省思，坐卧处的受用是为了免除季候危险的目的”（这句话的意涵）。'
confidence: 0.72
review_status: machine_generated
discovery_method: open_synthesis
```
