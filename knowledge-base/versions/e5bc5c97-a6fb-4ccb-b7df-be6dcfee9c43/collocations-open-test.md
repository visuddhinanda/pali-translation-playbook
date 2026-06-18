# 开放式固定搭配测试

本文件是 `初译·高级班内部讨论` 版本的开放式固定搭配测试结果，不是正式定稿。测试目标是验证新规则：不在提示词或抽取逻辑中预设 `paccayo`、`vuccati`、`nāma`、`vā` 等少数搭配，而是从 chunk 内部寻找高频、稳定、可复用的 Pali-Chinese 表达模式。

## 测试范围

本轮只测试 3 个 chunk：

| Chunk | Path | Lines | Records |
| --- | --- | ---: | ---: |
| `chunk-0158` | `visuddhimagga > Visuddhimaggo(Dutiyo bhāgo)` | 2441-2623 | 183 |
| `chunk-0048` | `līnatthappakāsanā > (DN)Mahāvaggaṭīkā` | 12114-12277 | 164 |
| `chunk-0129` | `therāpadānapāḷi > Therāpadānapāḷi(Paṭhamo bhāgo)` | 9894-10069 | 176 |

结论：开放式测试明显能发现脚本预设公式之外的搭配，尤其是引文公式、偈颂结尾公式、圣果成就公式、命名公式和注释解释公式。正式重跑时应对 191 个 chunk 全部执行同类开放式发现，然后合并、去重、人工筛选。

## 候选摘要

| ID | Source Pattern | Translation Pattern | Test Count | Status |
| --- | --- | --- | ---: | --- |
| `open-collocation-yathaha-quote` | `Yathāha / Yathā cāha` | 如说 / 又如所说 | 4 | candidate |
| `open-collocation-tenaha-quote` | `Tenāha / Tenevāha ... ti` | 因此说 / 故说 / 正因此说 | 5 | candidate |
| `open-collocation-ti-veditabba` | `... ti veditabbaṃ` | 当知 / 当如此了知 / 应先如此了知 | 4 | candidate |
| `open-collocation-apadana-colophon` | `Itthaṃ sudaṃ āyasmā ... thero imā gāthāyo abhāsitthāti` | 如此/到这里，具寿某长老诵出/说完这些偈颂 | 4 | candidate |
| `open-collocation-attainment-patisambhida` | `Paṭisambhidā catasso, vimokkhāpi ca aṭṭhime` | 四种辨析，以及八解脱 | 4 | candidate |
| `open-collocation-attainment-chalabhinna` | `Chaḷabhiññā sacchikatā, kataṃ buddhassa sāsanaṃ` | 六神通已现证，佛陀教法已实践/奉行 | 4 | candidate |
| `open-collocation-nama-namena` | `X nāma / X nāma nāmena` | 以X命名 / 名为X / 其名为X | 6 | candidate |
| `open-collocation-five-causes-formula` | `moho avijjā, āyūhanā saṅkhārā, nikanti taṇhā, upagamanaṃ upādānaṃ, cetanā bhavo` | 痴为无明，努力为行，欲求为爱/渴爱，黏著为取，思为有 | 2 | candidate |

## open-collocation-yathaha-quote

```yaml
id: open-collocation-yathaha-quote
version_id: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43
type: collocation
source_pattern: Yathāha / Yathā cāha
translation_pattern: 如说 / 又如所说
collocation_type: quotation_formula
occurrence_count_in_test_chunks: 4
evidence:
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:65-1244-10-11
    source_quote: "Yathāha–"
    target_quote: "如说："
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:65-1247-2-4
    source_quote: "Yathā cāha–"
    target_quote: "又如所说："
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:65-1256-49-50
    source_quote: "Yathāha–"
    target_quote: "如说："
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:65-1276-17-18
    source_quote: "Tenāha–"
    target_quote: "故说："
variant_translations:
  - 如说
  - 又如所说
  - 故说
conditions:
  - 引出经论引文或偈颂。
  - 破折号或引号后通常接引用文本。
notes:
  - 第四条 `Tenāha` 与 `Yathāha` 功能相近，但可在正式合并时拆成“引用导入公式”和“因果导入公式”两类。
confidence: 0.72
review_status: machine_generated
```

## open-collocation-tenaha-quote

```yaml
id: open-collocation-tenaha-quote
version_id: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43
type: collocation
source_pattern: Tenāha / Tenevāha ... ti
translation_pattern: 因此说 / 故说 / 正因此说 / 之所以说
collocation_type: explanatory_quote_formula
occurrence_count_in_test_chunks: 5
evidence:
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:186-1014-10-19
    source_quote: "Tenāha‘‘ sujāya asurakaññāya kāraṇā’’ ti."
    target_quote: "因此说：“因为……苏佳属于阿苏罗女子”。"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:186-1019-42-50
    source_quote: "Tenāha‘‘ candanissitakā devā’’ ti."
    target_quote: "因此说：“随侍月神诸天”。"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:186-1027-41-49
    source_quote: "Tenevāha‘‘ nāmabhāgena nāmakoṭṭhāsenā’’ ti."
    target_quote: "因此说：“按名称分类、按名字分组”。"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:186-1297-34-41
    source_quote: "Tenevāha‘‘ tāvadevā’’ ti."
    target_quote: "因此说：“直至还……时”。"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:65-1272-41-78
    source_quote: "Tenāha‘‘ purimakammabhavasmiṃ moho avijjā..."
    target_quote: "故说：“‘有先前的业有时，痴为无明..."
variant_translations:
  - 因此说
  - 故说
  - 正因此说
conditions:
  - 注释书解释前文后，引出原文或权威引文。
  - 常与 `ti` 构成闭合引文。
notes:
  - 这是本版本非常重要的注释书套语，正式全量抽取时应优先统计。
confidence: 0.82
review_status: machine_generated
```

## open-collocation-ti-veditabba

```yaml
id: open-collocation-ti-veditabba
version_id: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43
type: collocation
source_pattern: ... ti veditabbaṃ
translation_pattern: 当知 / 当如此了知 / 应先如此了知
collocation_type: interpretive_instruction
occurrence_count_in_test_chunks: 4
evidence:
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:65-1254-26-33
    source_quote: "Evaṃ tāvettha sokādīhi avijjā siddhā hotīti veditabbā."
    target_quote: "于这[缘起教说]中，应先如此了知“无明因愁等而成就”。"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:65-1256-90-95
    source_quote: "Evamidaṃ bhavacakkaṃ {aviditādī}ti veditabbaṃ."
    target_quote: "当如此了知“此有轮不知始等”。"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:65-1257-59-63
    source_quote: "Iti kārakavedakarahitan ti veditabbaṃ."
    target_quote: "是故当知[此有轮]“无有作者与受者”。"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:65-1258-45-50
    source_quote: "Tasmā dvādasavidhasuññatāsuñña metaṃ bhavacakkanti veditabbaṃ."
    target_quote: "因此当知此有轮以十二[支]空而空无。"
variant_translations:
  - 当知
  - 当如此了知
  - 应先如此了知
conditions:
  - 注释者总结前文解释并要求读者按某种方式理解。
notes:
  - 可归入“解释性指令公式”，与 `daṭṭhabbaṃ` 可能属于同一大类。
confidence: 0.84
review_status: machine_generated
```

## open-collocation-apadana-colophon

```yaml
id: open-collocation-apadana-colophon
version_id: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43
type: collocation
source_pattern: Itthaṃ sudaṃ āyasmā ... thero imā gāthāyo abhāsitthāti
translation_pattern: 如此/到这里，具寿某长老诵出/说完这些偈颂
collocation_type: colophon_formula
occurrence_count_in_test_chunks: 4
evidence:
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:143-2322-2-10
    source_quote: "Itthaṃ sudaṃ āyasmā rāhulo thero imā gāthāyo abhāsitthāti."
    target_quote: "到这里，具寿罗睺罗长老已将该偈颂说完了。"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:143-2359-2-12
    source_quote: "Itthaṃ sudaṃ āyasmā upaseno vaṅgantaputto thero imā gāthāyo abhāsitthāti."
    target_quote: "如是说，尊者 伍巴赛那长老，瓦甘塔之子，据称已经诵出了这些偈颂。"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:143-2408-2-10
    source_quote: "Itthaṃ sudaṃ āyasmā raṭṭhapālo thero imā gāthāyo abhāsitthāti."
    target_quote: "如此，具寿护国长老诵出了这些偈颂。"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:143-2447-2-10
    source_quote: "Itthaṃ sudaṃ āyasmā sopāko thero imā gāthāyo abhāsitthāti."
    target_quote: "如此，这位具寿（尊者）Sopāka长老确实宣说了这些偈颂。"
variant_translations:
  - 到这里，具寿某长老已将该偈颂说完了
  - 如是说，尊者某长老已经诵出了这些偈颂
  - 如此，具寿某长老诵出了这些偈颂
conditions:
  - 《长老譬喻》类文本的章节或偈颂结尾公式。
notes:
  - 该候选说明不同 path 会产生完全不同于注释书的固定搭配，必须按 path/chunk 开放发现。
confidence: 0.9
review_status: machine_generated
```

## open-collocation-attainment-patisambhida

```yaml
id: open-collocation-attainment-patisambhida
version_id: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43
type: collocation
source_pattern: Paṭisambhidā catasso, vimokkhāpi ca aṭṭhime
translation_pattern: 四种辨析，以及八解脱
collocation_type: attainment_formula
occurrence_count_in_test_chunks: 4
evidence:
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:143-2320-2-11
    source_quote: "Paṭisambhidā catasso, vimokkhāpi ca aṭṭhime;"
    target_quote: "「无论是四种辨析，亦或这八种解脱；"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:143-2357-2-10
    source_quote: "Paṭisambhidā catasso, vimokkhāpi ca aṭṭhime;"
    target_quote: "四种辨析(paṭisambhida)智，这八种解脱。"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:143-2406-2-10
    source_quote: "Paṭisambhidā catasso, vimokkhāpi ca aṭṭhime;"
    target_quote: "具足四辨析，以及八解脱；"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:143-2445-2-11
    source_quote: "Paṭisambhidā catasso, vimokkhāpi ca aṭṭhime;"
    target_quote: "「有四种辨析（通智），以及这八种解脱（解脱）。」"
variant_translations:
  - 四种辨析
  - 四辨析
  - 四种辨析智
conditions:
  - 圣者成就或譬喻偈颂中的功德公式。
notes:
  - 本条重点不是单词术语，而是整句功德公式的稳定重复。
confidence: 0.88
review_status: machine_generated
```

## open-collocation-attainment-chalabhinna

```yaml
id: open-collocation-attainment-chalabhinna
version_id: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43
type: collocation
source_pattern: Chaḷabhiññā sacchikatā, kataṃ buddhassa sāsanaṃ
translation_pattern: 六神通已现证，佛陀教法已实践/奉行
collocation_type: attainment_formula
occurrence_count_in_test_chunks: 4
evidence:
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:143-2321-2-10
    source_quote: "Chaḷabhiññā sacchikatā, kataṃ buddhassa sāsanaṃ."
    target_quote: "及六神通已现证，佛陀教法[已实践]。"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:143-2358-2-10
    source_quote: "Chaḷabhiññā sacchikatā, kataṃ buddhassa sāsanaṃ."
    target_quote: "六种神通已现证，佛陀之教法已被奉行。"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:143-2407-2-10
    source_quote: "Chaḷabhiññā sacchikatā, kataṃ buddhassa sāsanaṃ."
    target_quote: "已达六神通，佛陀教法成。”"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:143-2446-2-10
    source_quote: "Chaḷabhiññā sacchikatā, kataṃ buddhassa sāsanaṃ."
    target_quote: "六种神通已被实现，佛陀的教法已被实践。"
variant_translations:
  - 六神通已现证
  - 六种神通已现证
  - 已达六神通
  - 佛陀教法已实践
  - 佛陀之教法已被奉行
conditions:
  - 常与 `Paṭisambhidā catasso...` 成对出现。
notes:
  - 正式合并时可与上一条组成“长老譬喻成就公式”复合条目。
confidence: 0.9
review_status: machine_generated
```

## open-collocation-nama-namena

```yaml
id: open-collocation-nama-namena
version_id: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43
type: collocation
source_pattern: X nāma / X nāma nāmena
translation_pattern: 以X命名 / 名为X / 其名为X
collocation_type: naming_formula
occurrence_count_in_test_chunks: 6
evidence:
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:143-2303-2-9
    source_quote: "Gotamo nāma gottena, satthā loke bhavissati."
    target_quote: "以最牛氏来命名，将成为世间的导师。」"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:143-2312-2-10
    source_quote: "Rāhulo nāma nāmena, arahā so bhavissati’."
    target_quote: "以罗睺罗来命名，他将成为阿拉汉。」"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:143-2395-2-8
    source_quote: "Raṭṭhapāloti nāmena, hessati satthu sāvako."
    target_quote: "其名为护国，世尊之弟子。"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:143-2413-2-9
    source_quote: "Siddhattho nāma bhagavā, āgacchi mama santikaṃ."
    target_quote: "名为Siddhattha（悉达多）的Bhagavā（世尊），来到了我的身边。"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:143-2512-2-12
    source_quote: "Himavantassāvidūre, nisabho nāma pabbato;"
    target_quote: "在喜马拉雅山脉附近，有一座名为尼萨婆的山；"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:143-2515-2-10
    source_quote: "Kosiyo nāma nāmena, jaṭilo uggatāpano;"
    target_quote: "名为拘翼的人，髻发者习惯显眼；"
variant_translations:
  - 以X来命名
  - 其名为X
  - 名为X
conditions:
  - 专名、族姓、山名、人物名等命名语境。
notes:
  - 与旧 `nāma` 定义公式不同，此处重点是叙事偈颂中的命名模式。
confidence: 0.82
review_status: machine_generated
```

## open-collocation-five-causes-formula

```yaml
id: open-collocation-five-causes-formula
version_id: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43
type: collocation
source_pattern: moho avijjā, āyūhanā saṅkhārā, nikanti taṇhā, upagamanaṃ upādānaṃ, cetanā bhavo
translation_pattern: 痴为无明，努力为行，欲求为爱/渴爱，黏著为取，思为有
collocation_type: doctrinal_mapping_formula
occurrence_count_in_test_chunks: 2
evidence:
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:65-1272-41-78
    source_quote: "moho avijjā, āyūhanā saṅkhārā, nikanti taṇhā, upagamanaṃ upādānaṃ, cetanā bhavo"
    target_quote: "痴为无明，努力为行，欲求为渴爱，黏著为取，思为有"
  - unit_key: e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:65-1275-40-81
    source_quote: "moho avijjā, āyūhanā saṅkhārā, nikanti taṇhā, upagamanaṃ upādānaṃ, cetanā bhavo"
    target_quote: "痴是无明，努力是行，欲求是爱，黏著是取，思是有"
variant_translations:
  - X为Y
  - X是Y
conditions:
  - 缘起分析中把五个概念映射到五个缘起支。
notes:
  - 虽然测试 chunk 中只有 2 条，但整句稳定度高，值得全量搜索。
confidence: 0.76
review_status: machine_generated
```

## 测试结论

- 开放式抽取能发现预设公式之外的搭配，尤其是 path 特有公式。
- `therāpadānapāḷi` chunk 中出现大量偈颂结尾、成就公式和命名公式；这些不会被 `paccayo / vuccati / nāma / vā` 定向扫描充分捕获。
- `līnatthappakāsanā` chunk 中 `Tenāha / Tenevāha` 类型非常突出，适合归入注释书引文或解释公式。
- `visuddhimagga` chunk 中 `... ti veditabbaṃ` 和缘起支映射公式突出，适合归入解释性指令和教理映射搭配。
- 正式重跑应逐 chunk 输出候选，再按 `source_pattern`、`translation_pattern`、`collocation_type` 聚类合并。
